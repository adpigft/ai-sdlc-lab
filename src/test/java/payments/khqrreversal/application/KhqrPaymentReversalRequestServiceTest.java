package payments.khqrreversal.application;

import java.math.BigDecimal;
import java.nio.charset.StandardCharsets;
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
import payments.khqrreversal.domain.idempotency.HmacSha256IdempotencyHasher;
import payments.khqrreversal.domain.idempotency.IdempotencyRecord;
import payments.khqrreversal.domain.model.OriginalPaymentSnapshot;
import payments.khqrreversal.domain.model.PaymentReversal;
import payments.khqrreversal.domain.model.ReversalWorkflowStatus;
import payments.khqrreversal.domain.value.Money;
import payments.khqrreversal.domain.value.PaymentStatus;
import payments.khqrreversal.domain.value.ReversalReasonCode;
import payments.khqrreversal.domain.value.SettlementState;

public final class KhqrPaymentReversalRequestServiceTest {
    private static final Clock CLOCK = Clock.fixed(
            Instant.parse("2026-06-02T03:00:00Z"),
            ZoneOffset.UTC);
    private static final Currency USD = Currency.getInstance("USD");
    private static final byte[] HMAC_KEY =
            "synthetic-khqr-reversal-hmac-key-32b".getBytes(StandardCharsets.UTF_8);

    public static void main(String[] args) {
        KhqrPaymentReversalRequestServiceTest test = new KhqrPaymentReversalRequestServiceTest();
        test.createsReversalRequestForEligibleCompletedPayment();
        test.rejectsUnauthorizedMaker();
        test.rejectsNonCompletedOriginalPayment();
        test.rejectsIneligibleSettlementState();
        test.rejectsPartialAmount();
        test.rejectsMissingIdempotencyKey();
        test.rejectsInvalidReasonCode();
        test.replaysSameIdempotencyKeyAndPayload();
        test.rejectsSameIdempotencyKeyWithConflictingPayload();
        test.rejectsDuplicateActiveReversalForSameOriginalPayment();
        test.auditFailurePreventsStateCreation();
        test.storesHashedIdempotencyKeyOnly();
        test.usesKeyedHmacForIdempotencyHashing();
        System.out.println("KhqrPaymentReversalRequestServiceTest passed");
    }

    void createsReversalRequestForEligibleCompletedPayment() {
        TestFixture fixture = TestFixture.withPayment(completedPayment("pay_khqrrev_20260601"));

        ReversalRequestResult result = fixture.service.createReversalRequest(command(
                "pay_khqrrev_20260601",
                "100.00",
                "PROCESSOR_STATUS_CORRECTION",
                "evidence-khqrrev-001",
                "idem-khqrrev-001"));

        assertFalse(result.replayed(), "new request should not be replayed");
        assertEquals(ReversalWorkflowStatus.AWAITING_APPROVAL, result.reversal().workflowStatus(), "workflow status");
        assertEquals("pay_khqrrev_20260601", result.reversal().originalPaymentId(), "original payment link");
        assertEquals(new BigDecimal("100.00"), result.reversal().amount().value(), "full amount");
        assertEquals(USD, result.reversal().amount().currency(), "currency");
        assertEquals(0L, result.reversal().version(), "version");
        assertTrue(fixture.audit.contains(AuditEventType.REVERSAL_REQUESTED), "request audit");
        assertEquals(1, fixture.reversals.records.size(), "created reversal count");
    }

    void rejectsUnauthorizedMaker() {
        TestFixture fixture = TestFixture.withPayment(completedPayment("pay_khqrrev_20260601"));
        fixture.entitlements.allowMaker = false;

        ReversalException exception = expectReversalException(() -> fixture.service.createReversalRequest(command(
                "pay_khqrrev_20260601",
                "100.00",
                "PROCESSOR_STATUS_CORRECTION",
                "evidence-khqrrev-002",
                "idem-khqrrev-002")));

        assertEquals(ReversalRejectionCode.UNAUTHORIZED_MAKER, exception.code(), "rejection code");
        assertEquals(0, fixture.reversals.records.size(), "no reversal created");
        assertTrue(fixture.audit.hasOutcome(ReversalRejectionCode.UNAUTHORIZED_MAKER.name()), "authorization audit");
    }

    void rejectsNonCompletedOriginalPayment() {
        TestFixture fixture = TestFixture.withPayment(payment(
                "pay_khqrrev_non_completed",
                PaymentStatus.PENDING,
                SettlementState.NOT_FINALLY_SETTLED));

        ReversalException exception = expectReversalException(() -> fixture.service.createReversalRequest(command(
                "pay_khqrrev_non_completed",
                "100.00",
                "SYSTEM_PROCESSING_ERROR",
                "evidence-khqrrev-003",
                "idem-khqrrev-003")));

        assertEquals(ReversalRejectionCode.PAYMENT_NOT_COMPLETED, exception.code(), "rejection code");
        assertEquals(0, fixture.reversals.records.size(), "no reversal created");
    }

    void rejectsIneligibleSettlementState() {
        TestFixture fixture = TestFixture.withPayment(payment(
                "pay_khqrrev_settled",
                PaymentStatus.COMPLETED,
                SettlementState.FINALLY_SETTLED));

        ReversalException exception = expectReversalException(() -> fixture.service.createReversalRequest(command(
                "pay_khqrrev_settled",
                "100.00",
                "LEDGER_POSTING_ERROR",
                "evidence-khqrrev-004",
                "idem-khqrrev-004")));

        assertEquals(ReversalRejectionCode.SETTLEMENT_CUTOFF_NOT_ELIGIBLE, exception.code(), "rejection code");
        assertEquals(0, fixture.reversals.records.size(), "no reversal created");
        assertTrue(fixture.audit.hasOutcome(ReversalRejectionCode.SETTLEMENT_CUTOFF_NOT_ELIGIBLE.name()),
                "settlement cutoff audit");
    }

    void rejectsPartialAmount() {
        TestFixture fixture = TestFixture.withPayment(completedPayment("pay_khqrrev_20260601"));

        ReversalException exception = expectReversalException(() -> fixture.service.createReversalRequest(command(
                "pay_khqrrev_20260601",
                "40.00",
                "RECONCILIATION_BREAK_CORRECTION",
                "evidence-khqrrev-005",
                "idem-khqrrev-005")));

        assertEquals(ReversalRejectionCode.PARTIAL_AMOUNT_NOT_SUPPORTED, exception.code(), "rejection code");
        assertEquals(0, fixture.reversals.records.size(), "no reversal created");
    }

    void rejectsMissingIdempotencyKey() {
        TestFixture fixture = TestFixture.withPayment(completedPayment("pay_khqrrev_20260601"));

        ReversalException exception = expectReversalException(() -> fixture.service.createReversalRequest(new CreateKhqrPaymentReversalCommand(
                "pay_khqrrev_20260601",
                new Money(new BigDecimal("100.00"), USD),
                "PROCESSOR_DUPLICATE_EXECUTION",
                "evidence-khqrrev-006",
                "ops-maker-001",
                "operations_maker",
                "corr-khqrrev-006",
                "",
                null)));

        assertEquals(ReversalRejectionCode.MISSING_IDEMPOTENCY_KEY, exception.code(), "rejection code");
        assertEquals(0, fixture.reversals.records.size(), "no reversal created");
    }

    void rejectsInvalidReasonCode() {
        TestFixture fixture = TestFixture.withPayment(completedPayment("pay_khqrrev_20260601"));

        ReversalException exception = expectReversalException(() -> fixture.service.createReversalRequest(command(
                "pay_khqrrev_20260601",
                "100.00",
                "CUSTOMER_RETURN",
                "evidence-khqrrev-007",
                "idem-khqrrev-007")));

        assertEquals(ReversalRejectionCode.INVALID_REASON_CODE, exception.code(), "rejection code");
        assertEquals(0, fixture.reversals.records.size(), "no reversal created");
        assertTrue(fixture.audit.hasOutcome(ReversalRejectionCode.INVALID_REASON_CODE.name()), "reason audit");
    }

    void replaysSameIdempotencyKeyAndPayload() {
        TestFixture fixture = TestFixture.withPayment(completedPayment("pay_khqrrev_20260601"));
        CreateKhqrPaymentReversalCommand command = command(
                "pay_khqrrev_20260601",
                "100.00",
                "PROCESSOR_STATUS_CORRECTION",
                "evidence-khqrrev-008",
                "idem-khqrrev-008");

        ReversalRequestResult first = fixture.service.createReversalRequest(command);
        ReversalRequestResult second = fixture.service.createReversalRequest(command);

        assertFalse(first.replayed(), "first request");
        assertTrue(second.replayed(), "second request should replay");
        assertEquals(first.reversal().reversalId(), second.reversal().reversalId(), "same reversal id");
        assertEquals(1, fixture.reversals.records.size(), "only one reversal");
    }

    void rejectsSameIdempotencyKeyWithConflictingPayload() {
        TestFixture fixture = TestFixture.withPayment(completedPayment("pay_khqrrev_20260601"));

        fixture.service.createReversalRequest(command(
                "pay_khqrrev_20260601",
                "100.00",
                "PROCESSOR_STATUS_CORRECTION",
                "evidence-khqrrev-009",
                "idem-khqrrev-009"));

        ReversalException exception = expectReversalException(() -> fixture.service.createReversalRequest(command(
                "pay_khqrrev_20260602",
                "100.00",
                "PROCESSOR_STATUS_CORRECTION",
                "evidence-khqrrev-009",
                "idem-khqrrev-009")));

        assertEquals(ReversalRejectionCode.IDEMPOTENCY_CONFLICT, exception.code(), "rejection code");
        assertEquals(1, fixture.reversals.records.size(), "no second reversal");
        assertTrue(fixture.audit.contains(AuditEventType.IDEMPOTENCY_CONFLICT), "conflict audit");
    }

    void rejectsDuplicateActiveReversalForSameOriginalPayment() {
        TestFixture fixture = TestFixture.withPayment(completedPayment("pay_khqrrev_20260601"));
        fixture.reversals.saveNew(existingReversal("rev-existing-001", "pay_khqrrev_20260601"));

        ReversalException exception = expectReversalException(() -> fixture.service.createReversalRequest(command(
                "pay_khqrrev_20260601",
                "100.00",
                "PROCESSOR_STATUS_CORRECTION",
                "evidence-khqrrev-010",
                "idem-khqrrev-010")));

        assertEquals(ReversalRejectionCode.DUPLICATE_REVERSAL, exception.code(), "rejection code");
        assertEquals(1, fixture.reversals.records.size(), "no second reversal");
        assertTrue(fixture.audit.contains(AuditEventType.DUPLICATE_REVERSAL_ATTEMPT), "duplicate audit");
    }

    void auditFailurePreventsStateCreation() {
        TestFixture fixture = TestFixture.withPayment(completedPayment("pay_khqrrev_20260601"));
        fixture.audit.failOnAppend = true;

        IllegalStateException exception = expectIllegalState(() -> fixture.service.createReversalRequest(command(
                "pay_khqrrev_20260601",
                "100.00",
                "PROCESSOR_STATUS_CORRECTION",
                "evidence-khqrrev-011",
                "idem-khqrrev-011")));

        assertEquals("Audit outbox unavailable.", exception.getMessage(), "audit failure message");
        assertEquals(0, fixture.reversals.records.size(), "no reversal state when audit fails");
        assertEquals(0, fixture.idempotency.records.size(), "no idempotency state when audit fails");
    }

    void storesHashedIdempotencyKeyOnly() {
        TestFixture fixture = TestFixture.withPayment(completedPayment("pay_khqrrev_20260601"));

        fixture.service.createReversalRequest(command(
                "pay_khqrrev_20260601",
                "100.00",
                "SYSTEM_PROCESSING_ERROR",
                "evidence-khqrrev-012",
                "raw-idempotency-key"));

        IdempotencyRecord record = fixture.idempotency.records.values().iterator().next();
        assertNotEquals("raw-idempotency-key", record.idempotencyKeyHash(), "raw idempotency key must not be stored");
        assertEquals(64, record.idempotencyKeyHash().length(), "sha-256 hmac hex length");
        assertEquals("ops-maker-001:operations_maker", record.actorScope(), "actor scope");
    }

    void usesKeyedHmacForIdempotencyHashing() {
        HmacSha256IdempotencyHasher first = new HmacSha256IdempotencyHasher(HMAC_KEY);
        HmacSha256IdempotencyHasher second = new HmacSha256IdempotencyHasher(
                "different-khqr-reversal-hmac-key-32b".getBytes(StandardCharsets.UTF_8));

        String firstHash = first.hashKey("idem-khqrrev-hmac");
        String secondHash = second.hashKey("idem-khqrrev-hmac");

        assertEquals(64, firstHash.length(), "hmac sha-256 hex length");
        assertNotEquals(firstHash, secondHash, "same raw key must not imply same hash");
    }

    private static CreateKhqrPaymentReversalCommand command(
            String originalPaymentId,
            String amountValue,
            String reasonCode,
            String evidenceReference,
            String idempotencyKey) {
        return new CreateKhqrPaymentReversalCommand(
                originalPaymentId,
                new Money(new BigDecimal(amountValue), USD),
                reasonCode,
                evidenceReference,
                "ops-maker-001",
                "operations_maker",
                "corr-khqrrev-test-001",
                idempotencyKey,
                null);
    }

    private static OriginalPaymentSnapshot completedPayment(String originalPaymentId) {
        return payment(originalPaymentId, PaymentStatus.COMPLETED, SettlementState.NOT_FINALLY_SETTLED);
    }

    private static OriginalPaymentSnapshot payment(
            String originalPaymentId,
            PaymentStatus paymentStatus,
            SettlementState settlementState) {
        return new OriginalPaymentSnapshot(
                originalPaymentId,
                new Money(new BigDecimal("100.00"), USD),
                paymentStatus,
                settlementState);
    }

    private static PaymentReversal existingReversal(String reversalId, String originalPaymentId) {
        return PaymentReversal.awaitingApproval(
                reversalId,
                originalPaymentId,
                new Money(new BigDecimal("100.00"), USD),
                ReversalReasonCode.PROCESSOR_STATUS_CORRECTION,
                new payments.khqrreversal.domain.model.ActorSummary("ops-maker-001", "operations_maker"),
                "evidence-existing-001",
                null,
                "corr-existing-001",
                CLOCK.instant());
    }

    private static ReversalException expectReversalException(Runnable runnable) {
        try {
            runnable.run();
        } catch (ReversalException exception) {
            return exception;
        }
        throw new AssertionError("Expected ReversalException.");
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
        final FakeReversalRepository reversals = new FakeReversalRepository();
        final FakeIdempotencyStore idempotency = new FakeIdempotencyStore();
        final FakeAuditOutbox audit = new FakeAuditOutbox();
        final FakeEntitlements entitlements = new FakeEntitlements();
        final KhqrPaymentReversalRequestService service;

        private TestFixture(FakeOriginalPaymentLookup payments) {
            this.payments = payments;
            this.service = new KhqrPaymentReversalRequestService(
                    payments,
                    reversals,
                    idempotency,
                    audit,
                    new SequentialReversalIdGenerator(),
                    new ImmediateUnitOfWork(),
                    new HmacSha256IdempotencyHasher(HMAC_KEY),
                    entitlements,
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

    private static final class ImmediateUnitOfWork implements ReversalUnitOfWorkPort {
        @Override
        public <T> T required(java.util.function.Supplier<T> work) {
            return work.get();
        }
    }

    private static final class FakeReversalRepository implements ReversalRepositoryPort {
        final Map<String, PaymentReversal> records = new HashMap<>();

        @Override
        public boolean existsByOriginalPaymentId(String originalPaymentId) {
            return records.values().stream()
                    .anyMatch(reversal -> reversal.originalPaymentId().equals(originalPaymentId));
        }

        @Override
        public PaymentReversal findByReversalId(String reversalId) {
            return records.get(reversalId);
        }

        @Override
        public void saveNew(PaymentReversal reversal) {
            if (existsByOriginalPaymentId(reversal.originalPaymentId())) {
                throw new ReversalException(
                        ReversalRejectionCode.DUPLICATE_REVERSAL,
                        "Original payment already has a reversal.");
            }
            records.put(reversal.reversalId(), reversal);
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

    private static final class FakeEntitlements implements OperationsEntitlementPort {
        boolean allowMaker = true;

        @Override
        public boolean hasReversalMakerEntitlement(String actorId) {
            return allowMaker;
        }
    }

    private static final class SequentialReversalIdGenerator implements ReversalIdGenerator {
        private int sequence = 1;

        @Override
        public String nextReversalId() {
            return "rev-khqr_" + sequence++;
        }
    }
}
