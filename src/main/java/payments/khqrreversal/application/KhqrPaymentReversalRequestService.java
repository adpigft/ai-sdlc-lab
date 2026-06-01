package payments.khqrreversal.application;

import java.time.Clock;
import java.util.Objects;
import payments.khqrreversal.application.command.CreateKhqrPaymentReversalCommand;
import payments.khqrreversal.application.port.AuditOutboxPort;
import payments.khqrreversal.application.port.IdempotencyStorePort;
import payments.khqrreversal.application.port.OperationsEntitlementPort;
import payments.khqrreversal.application.port.OriginalPaymentLookupPort;
import payments.khqrreversal.application.port.ReversalIdGenerator;
import payments.khqrreversal.application.port.ReversalRepositoryPort;
import payments.khqrreversal.application.port.ReversalUnitOfWorkPort;
import payments.khqrreversal.domain.audit.AuditEvent;
import payments.khqrreversal.domain.audit.AuditEventType;
import payments.khqrreversal.domain.error.ReversalException;
import payments.khqrreversal.domain.error.ReversalRejectionCode;
import payments.khqrreversal.domain.idempotency.IdempotencyHasher;
import payments.khqrreversal.domain.idempotency.IdempotencyRecord;
import payments.khqrreversal.domain.model.ActorSummary;
import payments.khqrreversal.domain.model.OriginalPaymentSnapshot;
import payments.khqrreversal.domain.model.PaymentReversal;
import payments.khqrreversal.domain.model.ReversalWorkflowStatus;
import payments.khqrreversal.domain.value.PaymentStatus;
import payments.khqrreversal.domain.value.ReversalReasonCode;
import payments.khqrreversal.domain.value.SettlementState;

public final class KhqrPaymentReversalRequestService {
    private static final String OPERATION_TYPE = "KHQR_PAYMENT_REVERSAL_REQUEST";

    private final OriginalPaymentLookupPort originalPaymentLookupPort;
    private final ReversalRepositoryPort reversalRepositoryPort;
    private final IdempotencyStorePort idempotencyStorePort;
    private final AuditOutboxPort auditOutboxPort;
    private final ReversalIdGenerator reversalIdGenerator;
    private final ReversalUnitOfWorkPort unitOfWorkPort;
    private final IdempotencyHasher idempotencyHasher;
    private final OperationsEntitlementPort operationsEntitlementPort;
    private final Clock clock;

    public KhqrPaymentReversalRequestService(
            OriginalPaymentLookupPort originalPaymentLookupPort,
            ReversalRepositoryPort reversalRepositoryPort,
            IdempotencyStorePort idempotencyStorePort,
            AuditOutboxPort auditOutboxPort,
            ReversalIdGenerator reversalIdGenerator,
            ReversalUnitOfWorkPort unitOfWorkPort,
            IdempotencyHasher idempotencyHasher,
            OperationsEntitlementPort operationsEntitlementPort,
            Clock clock) {
        this.originalPaymentLookupPort = Objects.requireNonNull(originalPaymentLookupPort);
        this.reversalRepositoryPort = Objects.requireNonNull(reversalRepositoryPort);
        this.idempotencyStorePort = Objects.requireNonNull(idempotencyStorePort);
        this.auditOutboxPort = Objects.requireNonNull(auditOutboxPort);
        this.reversalIdGenerator = Objects.requireNonNull(reversalIdGenerator);
        this.unitOfWorkPort = Objects.requireNonNull(unitOfWorkPort);
        this.idempotencyHasher = Objects.requireNonNull(idempotencyHasher);
        this.operationsEntitlementPort = Objects.requireNonNull(operationsEntitlementPort);
        this.clock = Objects.requireNonNull(clock);
    }

    public ReversalRequestResult createReversalRequest(CreateKhqrPaymentReversalCommand command) {
        return unitOfWorkPort.required(() -> createReversalRequestInUnitOfWork(command));
    }

    private ReversalRequestResult createReversalRequestInUnitOfWork(CreateKhqrPaymentReversalCommand command) {
        validateCommand(command);
        ReversalReasonCode reasonCode = reasonCodeWithAudit(command);

        if (!"operations_maker".equals(command.makerRole())
                || !operationsEntitlementPort.hasReversalMakerEntitlement(command.makerId())) {
            throw rejectAndReturn(command,
                    ReversalRejectionCode.UNAUTHORIZED_MAKER,
                    AuditEventType.AUTHORIZATION_FAILURE,
                    "Operations maker entitlement is required.");
        }

        String idempotencyKeyHash = idempotencyHasher.hashKey(command.idempotencyKey());
        String payloadHash = idempotencyHasher.hashPayload(command.normalizedPayload());

        IdempotencyRecord existing = idempotencyStorePort.find(OPERATION_TYPE, idempotencyKeyHash);
        if (existing != null) {
            if (!existing.matches(actorScope(command), command.originalPaymentId(), payloadHash)) {
                auditOutboxPort.append(AuditEvent.rejection(
                        AuditEventType.IDEMPOTENCY_CONFLICT,
                        command.originalPaymentId(),
                        command.makerId(),
                        command.makerRole(),
                        command.reasonCode(),
                        command.correlationId(),
                        ReversalRejectionCode.IDEMPOTENCY_CONFLICT.name(),
                        clock.instant()));
                throw new ReversalException(
                        ReversalRejectionCode.IDEMPOTENCY_CONFLICT,
                        "Idempotency key was already used with a different reversal payload.");
            }
            PaymentReversal existingReversal = reversalRepositoryPort.findByReversalId(existing.reversalId());
            if (existingReversal == null) {
                throw new ReversalException(
                        ReversalRejectionCode.IDEMPOTENCY_STATE_NOT_FOUND,
                        "Idempotency replay result is unavailable.");
            }
            return ReversalRequestResult.replayed(existingReversal);
        }

        OriginalPaymentSnapshot originalPayment = originalPaymentLookupPort
                .findByPaymentId(command.originalPaymentId())
                .orElseThrow(() -> rejectAndReturn(
                        command,
                        ReversalRejectionCode.ORIGINAL_PAYMENT_NOT_FOUND,
                        AuditEventType.REVERSAL_REJECTED,
                        "Original KHQR payment was not found."));

        validateEligibility(command, originalPayment, reasonCode);

        if (reversalRepositoryPort.existsByOriginalPaymentId(command.originalPaymentId())) {
            auditOutboxPort.append(AuditEvent.rejection(
                    AuditEventType.DUPLICATE_REVERSAL_ATTEMPT,
                    command.originalPaymentId(),
                    command.makerId(),
                    command.makerRole(),
                    command.reasonCode(),
                    command.correlationId(),
                    ReversalRejectionCode.DUPLICATE_REVERSAL.name(),
                    clock.instant()));
            throw new ReversalException(
                    ReversalRejectionCode.DUPLICATE_REVERSAL,
                    "Original KHQR payment already has an active reversal.");
        }

        String reversalId = reversalIdGenerator.nextReversalId();
        PaymentReversal reversal = PaymentReversal.awaitingApproval(
                reversalId,
                originalPayment.originalPaymentId(),
                command.amount(),
                reasonCode,
                new ActorSummary(command.makerId(), command.makerRole()),
                command.evidenceReference(),
                command.reasonNotes(),
                command.correlationId(),
                clock.instant());

        IdempotencyRecord idempotencyRecord = IdempotencyRecord.completed(
                OPERATION_TYPE,
                idempotencyKeyHash,
                actorScope(command),
                command.originalPaymentId(),
                payloadHash,
                reversalId,
                clock.instant());

        auditOutboxPort.append(AuditEvent.reversalRequested(reversal));
        idempotencyStorePort.save(idempotencyRecord);
        reversalRepositoryPort.saveNew(reversal);
        return ReversalRequestResult.created(reversal);
    }

    private void validateCommand(CreateKhqrPaymentReversalCommand command) {
        try {
            Objects.requireNonNull(command, "command");
        } catch (NullPointerException exception) {
            throw new ReversalException(
                    ReversalRejectionCode.INVALID_REQUEST,
                    "Reversal command is required.");
        }
    }

    private ReversalReasonCode reasonCodeWithAudit(CreateKhqrPaymentReversalCommand command) {
        try {
            return ReversalReasonCode.of(command.reasonCode());
        } catch (ReversalException exception) {
            auditOutboxPort.append(AuditEvent.rejection(
                    AuditEventType.REVERSAL_REJECTED,
                    command.originalPaymentId(),
                    command.makerId(),
                    command.makerRole(),
                    command.reasonCode(),
                    command.correlationId(),
                    exception.code().name(),
                    clock.instant()));
            throw exception;
        }
    }

    private void validateEligibility(
            CreateKhqrPaymentReversalCommand command,
            OriginalPaymentSnapshot originalPayment,
            ReversalReasonCode reasonCode) {
        if (originalPayment.paymentStatus() != PaymentStatus.COMPLETED) {
            throw rejectAndReturn(
                    command,
                    ReversalRejectionCode.PAYMENT_NOT_COMPLETED,
                    AuditEventType.REVERSAL_REJECTED,
                    "Original KHQR payment is not completed.");
        }
        if (originalPayment.settlementState() != SettlementState.NOT_FINALLY_SETTLED) {
            throw rejectAndReturn(
                    command,
                    ReversalRejectionCode.SETTLEMENT_CUTOFF_NOT_ELIGIBLE,
                    AuditEventType.REVERSAL_REJECTED,
                    "Original KHQR payment is not eligible for pre-settlement reversal.");
        }
        if (!command.amount().currency().equals(originalPayment.amount().currency())
                || command.amount().value().compareTo(originalPayment.amount().value()) != 0) {
            throw rejectAndReturn(
                    command,
                    ReversalRejectionCode.PARTIAL_AMOUNT_NOT_SUPPORTED,
                    AuditEventType.REVERSAL_REJECTED,
                    "KHQR reversal supports full amount only.");
        }
    }

    private ReversalException rejectAndReturn(
            CreateKhqrPaymentReversalCommand command,
            ReversalRejectionCode code,
            AuditEventType eventType,
            String safeMessage) {
        auditOutboxPort.append(AuditEvent.rejection(
                eventType,
                command.originalPaymentId(),
                command.makerId(),
                command.makerRole(),
                command.reasonCode(),
                command.correlationId(),
                code.name(),
                clock.instant()));
        return new ReversalException(code, safeMessage);
    }

    private static String actorScope(CreateKhqrPaymentReversalCommand command) {
        return command.makerId() + ":" + command.makerRole();
    }
}
