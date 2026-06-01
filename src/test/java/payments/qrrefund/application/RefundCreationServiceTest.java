package payments.qrrefund.application;

import java.math.BigDecimal;
import java.time.Clock;
import java.time.Instant;
import java.time.LocalDate;
import java.time.ZoneOffset;
import java.util.ArrayList;
import java.util.Currency;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import payments.qrrefund.application.RefundCreationService.RefundCreationResult;
import payments.qrrefund.application.command.InitiateMerchantRefundCommand;
import payments.qrrefund.application.port.AuditOutboxPort;
import payments.qrrefund.application.port.IdempotencyStorePort;
import payments.qrrefund.application.port.OriginalPaymentLookupPort;
import payments.qrrefund.application.port.RefundRepositoryPort;
import payments.qrrefund.domain.audit.AuditEvent;
import payments.qrrefund.domain.audit.AuditEventType;
import payments.qrrefund.domain.error.RefundException;
import payments.qrrefund.domain.error.RefundRejectionCode;
import payments.qrrefund.domain.idempotency.IdempotencyRecord;
import payments.qrrefund.domain.idempotency.Sha256IdempotencyHasher;
import payments.qrrefund.domain.model.OriginalPaymentSnapshot;
import payments.qrrefund.domain.model.Refund;
import payments.qrrefund.domain.model.RefundStatus;
import payments.qrrefund.domain.value.PaymentStatus;
import payments.qrrefund.domain.value.SettlementState;

public final class RefundCreationServiceTest {
    private static final Clock CLOCK = Clock.fixed(
            Instant.parse("2026-06-01T02:00:00Z"),
            ZoneOffset.UTC);
    private static final Currency USD = Currency.getInstance("USD");

    public static void main(String[] args) {
        RefundCreationServiceTest test = new RefundCreationServiceTest();
        test.createsMerchantRefundForCompletedKhqrPayment();
        test.rejectsNonCompletedOriginalPayment();
        test.rejectsRefundOutsideThirtyDayWindow();
        test.allowsRefundAfterMerchantSettlement();
        test.rejectsSuspendedMerchant();
        test.rejectsDuplicateOriginalPaymentRefund();
        test.replaysSameIdempotencyKeyAndPayload();
        test.rejectsSameIdempotencyKeyWithConflictingPayload();
        test.storesHashedIdempotencyKeyOnly();
        test.auditFailurePreventsRefundStateCreation();
        test.rejectsMissingIdempotencyKey();
        test.rejectsInvalidReasonCode();
        System.out.println("RefundCreationServiceTest passed");
    }

    void createsMerchantRefundForCompletedKhqrPayment() {
        TestFixture fixture = TestFixture.withPayment(completedPayment("pay_synth_20260601"));

        RefundCreationResult result = fixture.service.createMerchantRefund(command(
                "pay_synth_20260601",
                "MERCH-001",
                "CUSTOMER_RETURN",
                "idem-qrref-001"));

        assertFalse(result.replayed(), "new refund should not be replayed");
        assertEquals(RefundStatus.REQUESTED, result.status(), "refund status");
        assertEquals("pay_synth_20260601", result.refund().originalPaymentId(), "original payment link");
        assertEquals(new BigDecimal("125.50"), result.refund().amount(), "full refund amount");
        assertEquals(USD, result.refund().currency(), "currency");
        assertEquals(0L, result.refund().version(), "initial aggregate version");
        assertEquals(1, fixture.refunds.records.size(), "created refund count");
        assertTrue(fixture.audit.contains(AuditEventType.REFUND_REQUESTED), "request audit event");
    }

    void rejectsNonCompletedOriginalPayment() {
        TestFixture fixture = TestFixture.withPayment(payment(
                "pay_non_completed",
                "MERCH-001",
                PaymentStatus.PROCESSING,
                LocalDate.of(2026, 5, 25),
                SettlementState.NOT_SETTLED,
                false,
                false));

        RefundException exception = expectRefundException(() -> fixture.service.createMerchantRefund(command(
                "pay_non_completed",
                "MERCH-001",
                "CUSTOMER_RETURN",
                "idem-qrref-002")));

        assertEquals(RefundRejectionCode.PAYMENT_NOT_COMPLETED, exception.code(), "rejection code");
        assertEquals(0, fixture.refunds.records.size(), "no refund created");
        assertTrue(fixture.audit.hasOutcome(RefundRejectionCode.PAYMENT_NOT_COMPLETED.name()), "rejection audit");
    }

    void rejectsRefundOutsideThirtyDayWindow() {
        TestFixture fixture = TestFixture.withPayment(payment(
                "pay_old_001",
                "MERCH-001",
                PaymentStatus.COMPLETED,
                LocalDate.of(2026, 4, 30),
                SettlementState.NOT_SETTLED,
                false,
                false));

        RefundException exception = expectRefundException(() -> fixture.service.createMerchantRefund(command(
                "pay_old_001",
                "MERCH-001",
                "CUSTOMER_RETURN",
                "idem-qrref-003")));

        assertEquals(RefundRejectionCode.REFUND_WINDOW_EXPIRED, exception.code(), "rejection code");
        assertEquals(0, fixture.refunds.records.size(), "no refund created");
    }

    void allowsRefundAfterMerchantSettlement() {
        TestFixture fixture = TestFixture.withPayment(payment(
                "pay_settled_001",
                "MERCH-001",
                PaymentStatus.COMPLETED,
                LocalDate.of(2026, 5, 20),
                SettlementState.SETTLED,
                false,
                false));

        RefundCreationResult result = fixture.service.createMerchantRefund(command(
                "pay_settled_001",
                "MERCH-001",
                "CUSTOMER_RETURN",
                "idem-qrref-004"));

        assertEquals(RefundStatus.REQUESTED, result.status(), "settled payment refund status");
    }

    void rejectsSuspendedMerchant() {
        TestFixture fixture = TestFixture.withPayment(payment(
                "pay_synth_20260601",
                "MERCH-001",
                PaymentStatus.COMPLETED,
                LocalDate.of(2026, 5, 20),
                SettlementState.NOT_SETTLED,
                false,
                true));

        RefundException exception = expectRefundException(() -> fixture.service.createMerchantRefund(command(
                "pay_synth_20260601",
                "MERCH-001",
                "CUSTOMER_RETURN",
                "idem-qrref-005")));

        assertEquals(RefundRejectionCode.MERCHANT_SUSPENDED, exception.code(), "rejection code");
    }

    void rejectsDuplicateOriginalPaymentRefund() {
        TestFixture fixture = TestFixture.withPayment(completedPayment("pay_synth_20260601"));
        fixture.refunds.saveNew(existingRefund("rfnd_existing_001", "pay_synth_20260601"));

        RefundException exception = expectRefundException(() -> fixture.service.createMerchantRefund(command(
                "pay_synth_20260601",
                "MERCH-001",
                "CUSTOMER_RETURN",
                "idem-qrref-006")));

        assertEquals(RefundRejectionCode.DUPLICATE_REFUND, exception.code(), "rejection code");
        assertEquals(1, fixture.refunds.records.size(), "no second refund");
        assertTrue(fixture.audit.contains(AuditEventType.DUPLICATE_REFUND_ATTEMPT), "duplicate audit");
    }

    void replaysSameIdempotencyKeyAndPayload() {
        TestFixture fixture = TestFixture.withPayment(completedPayment("pay_synth_20260601"));
        InitiateMerchantRefundCommand command = command(
                "pay_synth_20260601",
                "MERCH-001",
                "CUSTOMER_RETURN",
                "idem-qrref-007");

        RefundCreationResult first = fixture.service.createMerchantRefund(command);
        RefundCreationResult second = fixture.service.createMerchantRefund(command);

        assertFalse(first.replayed(), "first request");
        assertTrue(second.replayed(), "second request should replay");
        assertEquals(first.refund().refundId(), second.refund().refundId(), "same refund id");
        assertEquals(1, fixture.refunds.records.size(), "only one refund");
    }

    void rejectsSameIdempotencyKeyWithConflictingPayload() {
        TestFixture fixture = TestFixture.withPayment(completedPayment("pay_synth_20260601"));
        fixture.payments.records.put("pay_synth_20260602", completedPayment("pay_synth_20260602"));

        fixture.service.createMerchantRefund(command(
                "pay_synth_20260601",
                "MERCH-001",
                "CUSTOMER_RETURN",
                "idem-qrref-008"));

        RefundException exception = expectRefundException(() -> fixture.service.createMerchantRefund(command(
                "pay_synth_20260602",
                "MERCH-001",
                "CUSTOMER_RETURN",
                "idem-qrref-008")));

        assertEquals(RefundRejectionCode.IDEMPOTENCY_CONFLICT, exception.code(), "rejection code");
        assertEquals(1, fixture.refunds.records.size(), "no second refund");
        assertTrue(fixture.audit.contains(AuditEventType.IDEMPOTENCY_CONFLICT), "conflict audit");
    }

    void storesHashedIdempotencyKeyOnly() {
        TestFixture fixture = TestFixture.withPayment(completedPayment("pay_synth_20260601"));

        fixture.service.createMerchantRefund(command(
                "pay_synth_20260601",
                "MERCH-001",
                "CUSTOMER_RETURN",
                "raw-idempotency-key"));

        IdempotencyRecord record = fixture.idempotency.records.values().iterator().next();
        assertNotEquals("raw-idempotency-key", record.idempotencyKeyHash(), "raw key must not be stored");
        assertEquals(64, record.idempotencyKeyHash().length(), "sha-256 hex length");
        assertEquals("MERCH-001", record.merchantId(), "merchant binding");
        assertEquals("pay_synth_20260601", record.originalPaymentId(), "payment binding");
        assertNotEquals(command(
                "pay_synth_20260601",
                "MERCH-001",
                "CUSTOMER_RETURN",
                "raw-idempotency-key").normalizedPayload(), record.requestPayloadHash(), "payload hash only");
    }

    void auditFailurePreventsRefundStateCreation() {
        TestFixture fixture = TestFixture.withPayment(completedPayment("pay_synth_20260601"));
        fixture.audit.failOnAppend = true;

        IllegalStateException exception = expectIllegalState(() -> fixture.service.createMerchantRefund(command(
                "pay_synth_20260601",
                "MERCH-001",
                "CUSTOMER_RETURN",
                "idem-qrref-audit-fail")));

        assertEquals("Audit outbox unavailable.", exception.getMessage(), "audit failure message");
        assertEquals(0, fixture.refunds.records.size(), "no refund state when audit fails");
        assertEquals(0, fixture.idempotency.records.size(), "no idempotency result when audit fails");
    }

    void rejectsMissingIdempotencyKey() {
        TestFixture fixture = TestFixture.withPayment(completedPayment("pay_synth_20260601"));

        RefundException exception = expectRefundException(() -> fixture.service.createMerchantRefund(command(
                "pay_synth_20260601",
                "MERCH-001",
                "CUSTOMER_RETURN",
                "")));

        assertEquals(RefundRejectionCode.INVALID_REQUEST, exception.code(), "rejection code");
        assertTrue(fixture.audit.hasOutcome(RefundRejectionCode.INVALID_REQUEST.name()), "missing idempotency audit");
    }

    void rejectsInvalidReasonCode() {
        TestFixture fixture = TestFixture.withPayment(completedPayment("pay_synth_20260601"));

        RefundException exception = expectRefundException(() -> fixture.service.createMerchantRefund(command(
                "pay_synth_20260601",
                "MERCH-001",
                "lowercase",
                "idem-qrref-009")));

        assertEquals(RefundRejectionCode.INVALID_REASON_CODE, exception.code(), "rejection code");
        assertEquals(0, fixture.refunds.records.size(), "no refund created");
        assertTrue(fixture.audit.hasOutcome(RefundRejectionCode.INVALID_REASON_CODE.name()), "reason code audit");
    }

    private static InitiateMerchantRefundCommand command(
            String originalPaymentId,
            String merchantId,
            String reasonCode,
            String idempotencyKey) {
        return new InitiateMerchantRefundCommand(
                originalPaymentId,
                merchantId,
                reasonCode,
                "merchant-user-001",
                "merchant_refund_user",
                "merchant_app",
                "corr-qrref-test-001",
                idempotencyKey);
    }

    private static OriginalPaymentSnapshot completedPayment(String originalPaymentId) {
        return payment(
                originalPaymentId,
                "MERCH-001",
                PaymentStatus.COMPLETED,
                LocalDate.of(2026, 5, 20),
                SettlementState.NOT_SETTLED,
                false,
                false);
    }

    private static OriginalPaymentSnapshot payment(
            String originalPaymentId,
            String merchantId,
            PaymentStatus status,
            LocalDate paymentDate,
            SettlementState settlementState,
            boolean alreadyRefunded,
            boolean merchantSuspended) {
        return new OriginalPaymentSnapshot(
                originalPaymentId,
                merchantId,
                new BigDecimal("125.50"),
                USD,
                status,
                paymentDate,
                settlementState,
                alreadyRefunded,
                merchantSuspended);
    }

    private static Refund existingRefund(String refundId, String originalPaymentId) {
        return Refund.requested(
                refundId,
                originalPaymentId,
                "MERCH-001",
                new BigDecimal("125.50"),
                USD,
                payments.qrrefund.domain.value.ReasonCode.of("CUSTOMER_RETURN"),
                "merchant-user-001",
                "merchant_refund_user",
                "merchant_app",
                "corr-existing",
                CLOCK.instant());
    }

    private static RefundException expectRefundException(Runnable runnable) {
        try {
            runnable.run();
        } catch (RefundException exception) {
            return exception;
        }
        throw new AssertionError("Expected RefundException.");
    }

    private static IllegalStateException expectIllegalState(Runnable runnable) {
        try {
            runnable.run();
        } catch (IllegalStateException exception) {
            return exception;
        }
        throw new AssertionError("Expected IllegalStateException.");
    }

    private static void assertEquals(Object expected, Object actual, String label) {
        if (!expected.equals(actual)) {
            throw new AssertionError(label + " expected <" + expected + "> but was <" + actual + ">.");
        }
    }

    private static void assertNotEquals(Object unexpected, Object actual, String label) {
        if (unexpected.equals(actual)) {
            throw new AssertionError(label + " should not equal <" + actual + ">.");
        }
    }

    private static void assertTrue(boolean value, String label) {
        if (!value) {
            throw new AssertionError(label + " expected true.");
        }
    }

    private static void assertFalse(boolean value, String label) {
        if (value) {
            throw new AssertionError(label + " expected false.");
        }
    }

    private static final class TestFixture {
        final FakeOriginalPaymentLookup payments;
        final FakeRefundRepository refunds = new FakeRefundRepository();
        final FakeIdempotencyStore idempotency = new FakeIdempotencyStore();
        final FakeAuditOutbox audit = new FakeAuditOutbox();
        final RefundCreationService service;

        private TestFixture(FakeOriginalPaymentLookup payments) {
            this.payments = payments;
            this.service = new RefundCreationService(
                    payments,
                    refunds,
                    idempotency,
                    audit,
                    new SequentialRefundIdGenerator(),
                    new Sha256IdempotencyHasher(),
                    CLOCK);
        }

        static TestFixture withPayment(OriginalPaymentSnapshot payment) {
            FakeOriginalPaymentLookup lookup = new FakeOriginalPaymentLookup();
            lookup.records.put(payment.originalPaymentId(), payment);
            return new TestFixture(lookup);
        }
    }

    private static final class FakeOriginalPaymentLookup implements OriginalPaymentLookupPort {
        final Map<String, OriginalPaymentSnapshot> records = new HashMap<>();

        @Override
        public Optional<OriginalPaymentSnapshot> findByPaymentId(String originalPaymentId) {
            return Optional.ofNullable(records.get(originalPaymentId));
        }
    }

    private static final class FakeRefundRepository implements RefundRepositoryPort {
        final Map<String, Refund> records = new HashMap<>();

        @Override
        public boolean existsByOriginalPaymentId(String originalPaymentId) {
            return records.values().stream()
                    .anyMatch(refund -> refund.originalPaymentId().equals(originalPaymentId));
        }

        @Override
        public Refund findByRefundId(String refundId) {
            return records.get(refundId);
        }

        @Override
        public void saveNew(Refund refund) {
            if (existsByOriginalPaymentId(refund.originalPaymentId())) {
                throw new RefundException(
                        RefundRejectionCode.DUPLICATE_REFUND,
                        "Original payment already has a refund.");
            }
            records.put(refund.refundId(), refund);
        }
    }

    private static final class FakeIdempotencyStore implements IdempotencyStorePort {
        final Map<String, IdempotencyRecord> records = new HashMap<>();

        @Override
        public IdempotencyRecord find(String operationType, String idempotencyKeyHash) {
            return records.get(key(operationType, idempotencyKeyHash));
        }

        @Override
        public void save(IdempotencyRecord record) {
            records.put(key(record.operationType(), record.idempotencyKeyHash()), record);
        }

        private static String key(String operationType, String idempotencyKeyHash) {
            return operationType + ":" + idempotencyKeyHash;
        }
    }

    private static final class FakeAuditOutbox implements AuditOutboxPort {
        final List<AuditEvent> events = new ArrayList<>();
        boolean failOnAppend;

        @Override
        public void append(AuditEvent event) {
            if (failOnAppend) {
                throw new IllegalStateException("Audit outbox unavailable.");
            }
            events.add(event);
        }

        boolean contains(AuditEventType eventType) {
            return events.stream().anyMatch(event -> event.eventType() == eventType);
        }

        boolean hasOutcome(String outcomeCode) {
            return events.stream().anyMatch(event -> outcomeCode.equals(event.outcomeCode()));
        }
    }

    private static final class SequentialRefundIdGenerator
            implements payments.qrrefund.application.port.RefundIdGenerator {
        private int sequence = 1;

        @Override
        public String nextRefundId() {
            return "rfnd_test_" + sequence++;
        }
    }
}
