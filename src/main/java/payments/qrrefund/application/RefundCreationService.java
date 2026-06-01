package payments.qrrefund.application;

import java.time.Clock;
import java.time.LocalDate;
import java.util.Objects;
import payments.qrrefund.application.command.InitiateMerchantRefundCommand;
import payments.qrrefund.application.port.AuditOutboxPort;
import payments.qrrefund.application.port.IdempotencyStorePort;
import payments.qrrefund.application.port.OriginalPaymentLookupPort;
import payments.qrrefund.application.port.RefundIdGenerator;
import payments.qrrefund.application.port.RefundRepositoryPort;
import payments.qrrefund.domain.audit.AuditEvent;
import payments.qrrefund.domain.audit.AuditEventType;
import payments.qrrefund.domain.error.RefundException;
import payments.qrrefund.domain.error.RefundRejectionCode;
import payments.qrrefund.domain.idempotency.IdempotencyHasher;
import payments.qrrefund.domain.idempotency.IdempotencyRecord;
import payments.qrrefund.domain.model.OriginalPaymentSnapshot;
import payments.qrrefund.domain.model.Refund;
import payments.qrrefund.domain.model.RefundStatus;
import payments.qrrefund.domain.value.PaymentStatus;
import payments.qrrefund.domain.value.ReasonCode;

public final class RefundCreationService {
    private static final String OPERATION_TYPE = "MERCHANT_REFUND_CREATE";

    private final OriginalPaymentLookupPort originalPaymentLookupPort;
    private final RefundRepositoryPort refundRepositoryPort;
    private final IdempotencyStorePort idempotencyStorePort;
    private final AuditOutboxPort auditOutboxPort;
    private final RefundIdGenerator refundIdGenerator;
    private final IdempotencyHasher idempotencyHasher;
    private final Clock clock;

    public RefundCreationService(
            OriginalPaymentLookupPort originalPaymentLookupPort,
            RefundRepositoryPort refundRepositoryPort,
            IdempotencyStorePort idempotencyStorePort,
            AuditOutboxPort auditOutboxPort,
            RefundIdGenerator refundIdGenerator,
            IdempotencyHasher idempotencyHasher,
            Clock clock) {
        this.originalPaymentLookupPort = Objects.requireNonNull(originalPaymentLookupPort);
        this.refundRepositoryPort = Objects.requireNonNull(refundRepositoryPort);
        this.idempotencyStorePort = Objects.requireNonNull(idempotencyStorePort);
        this.auditOutboxPort = Objects.requireNonNull(auditOutboxPort);
        this.refundIdGenerator = Objects.requireNonNull(refundIdGenerator);
        this.idempotencyHasher = Objects.requireNonNull(idempotencyHasher);
        this.clock = Objects.requireNonNull(clock);
    }

    public RefundCreationResult createMerchantRefund(InitiateMerchantRefundCommand command) {
        validateCommandWithAudit(command);
        ReasonCode reasonCode = reasonCodeWithAudit(command);

        String idempotencyKeyHash = idempotencyHasher.hashKey(command.idempotencyKey());
        String payloadHash = idempotencyHasher.hashPayload(command.normalizedPayload());

        IdempotencyRecord existing = idempotencyStorePort.find(OPERATION_TYPE, idempotencyKeyHash);
        if (existing != null) {
            if (!existing.matches(command.merchantId(), command.originalPaymentId(), payloadHash)) {
                auditOutboxPort.append(AuditEvent.rejection(
                        AuditEventType.IDEMPOTENCY_CONFLICT,
                        command.originalPaymentId(),
                        null,
                        command.actorId(),
                        command.actorRole(),
                        command.reasonCode(),
                        command.correlationId(),
                        RefundRejectionCode.IDEMPOTENCY_CONFLICT.name()));
                throw new RefundException(
                        RefundRejectionCode.IDEMPOTENCY_CONFLICT,
                        "Idempotency key was already used with a different refund payload.");
            }
            Refund existingRefund = refundRepositoryPort.findByRefundId(existing.refundId());
            if (existingRefund == null) {
                throw new RefundException(
                        RefundRejectionCode.IDEMPOTENCY_STATE_NOT_FOUND,
                        "Idempotency replay result is unavailable.");
            }
            return RefundCreationResult.replayed(existingRefund);
        }

        OriginalPaymentSnapshot originalPayment = originalPaymentLookupPort
                .findByPaymentId(command.originalPaymentId())
                .orElseThrow(() -> rejectAndReturn(
                        command,
                        RefundRejectionCode.ORIGINAL_PAYMENT_NOT_FOUND,
                        "Original KHQR payment was not found."));

        validateEligibility(command, originalPayment);

        if (refundRepositoryPort.existsByOriginalPaymentId(command.originalPaymentId())) {
            auditOutboxPort.append(AuditEvent.rejection(
                    AuditEventType.DUPLICATE_REFUND_ATTEMPT,
                    command.originalPaymentId(),
                    null,
                    command.actorId(),
                    command.actorRole(),
                    command.reasonCode(),
                    command.correlationId(),
                    RefundRejectionCode.DUPLICATE_REFUND.name()));
            throw new RefundException(
                    RefundRejectionCode.DUPLICATE_REFUND,
                    "Original KHQR payment already has a refund.");
        }

        String refundId = refundIdGenerator.nextRefundId();
        Refund refund = Refund.requested(
                refundId,
                originalPayment.originalPaymentId(),
                originalPayment.merchantId(),
                originalPayment.amount(),
                originalPayment.currency(),
                reasonCode,
                command.actorId(),
                command.actorRole(),
                command.channel(),
                command.correlationId(),
                clock.instant());

        IdempotencyRecord idempotencyRecord = IdempotencyRecord.completed(
                OPERATION_TYPE,
                idempotencyKeyHash,
                command.merchantId(),
                command.originalPaymentId(),
                payloadHash,
                refundId,
                clock.instant());

        auditOutboxPort.append(AuditEvent.refundRequested(refund));
        idempotencyStorePort.save(idempotencyRecord);
        refundRepositoryPort.saveNew(refund);

        return RefundCreationResult.created(refund);
    }

    private void validateEligibility(
            InitiateMerchantRefundCommand command,
            OriginalPaymentSnapshot originalPayment) {
        if (!command.merchantId().equals(originalPayment.merchantId())) {
            throw rejectAndReturn(command, RefundRejectionCode.MERCHANT_NOT_AUTHORIZED,
                    "Merchant is not authorized for the original payment.");
        }
        if (originalPayment.paymentStatus() != PaymentStatus.COMPLETED) {
            throw rejectAndReturn(command, RefundRejectionCode.PAYMENT_NOT_COMPLETED,
                    "Original KHQR payment is not completed.");
        }
        LocalDate lastRefundDate = originalPayment.paymentDate().plusDays(30);
        if (LocalDate.now(clock).isAfter(lastRefundDate)) {
            throw rejectAndReturn(command, RefundRejectionCode.REFUND_WINDOW_EXPIRED,
                    "Refund window has expired.");
        }
        if (originalPayment.alreadyRefunded()) {
            throw rejectAndReturn(command, RefundRejectionCode.DUPLICATE_REFUND,
                    "Original KHQR payment already has a refund.");
        }
        if (originalPayment.merchantSuspended()) {
            throw rejectAndReturn(command, RefundRejectionCode.MERCHANT_SUSPENDED,
                    "Merchant is suspended.");
        }
    }

    private void validateCommandWithAudit(InitiateMerchantRefundCommand command) {
        try {
            command.validate();
        } catch (RefundException exception) {
            auditOutboxPort.append(AuditEvent.rejection(
                    AuditEventType.REFUND_REJECTED,
                    command.originalPaymentId(),
                    null,
                    command.actorId(),
                    command.actorRole(),
                    command.reasonCode(),
                    command.correlationId(),
                    exception.code().name()));
            throw exception;
        }
    }

    private ReasonCode reasonCodeWithAudit(InitiateMerchantRefundCommand command) {
        try {
            return ReasonCode.of(command.reasonCode());
        } catch (RefundException exception) {
            auditOutboxPort.append(AuditEvent.rejection(
                    AuditEventType.REFUND_REJECTED,
                    command.originalPaymentId(),
                    null,
                    command.actorId(),
                    command.actorRole(),
                    command.reasonCode(),
                    command.correlationId(),
                    exception.code().name()));
            throw exception;
        }
    }

    private RefundException rejectAndReturn(
            InitiateMerchantRefundCommand command,
            RefundRejectionCode code,
            String safeMessage) {
        auditOutboxPort.append(AuditEvent.rejection(
                AuditEventType.REFUND_REJECTED,
                command.originalPaymentId(),
                null,
                command.actorId(),
                command.actorRole(),
                command.reasonCode(),
                command.correlationId(),
                code.name()));
        return new RefundException(code, safeMessage);
    }

    public record RefundCreationResult(Refund refund, boolean replayed) {
        public static RefundCreationResult created(Refund refund) {
            return new RefundCreationResult(refund, false);
        }

        public static RefundCreationResult replayed(Refund refund) {
            return new RefundCreationResult(refund, true);
        }

        public RefundStatus status() {
            return refund.status();
        }
    }
}
