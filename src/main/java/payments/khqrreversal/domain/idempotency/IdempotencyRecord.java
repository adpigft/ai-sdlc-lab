package payments.khqrreversal.domain.idempotency;

import java.time.Instant;
import java.util.Objects;

public record IdempotencyRecord(
        String operationType,
        String idempotencyKeyHash,
        String actorScope,
        String originalPaymentId,
        String requestPayloadHash,
        String reversalId,
        Instant createdAt) {

    public IdempotencyRecord {
        require(operationType, "operationType");
        require(idempotencyKeyHash, "idempotencyKeyHash");
        require(actorScope, "actorScope");
        require(originalPaymentId, "originalPaymentId");
        require(requestPayloadHash, "requestPayloadHash");
        require(reversalId, "reversalId");
        Objects.requireNonNull(createdAt, "createdAt");
    }

    public static IdempotencyRecord completed(
            String operationType,
            String idempotencyKeyHash,
            String actorScope,
            String originalPaymentId,
            String requestPayloadHash,
            String reversalId,
            Instant createdAt) {
        return new IdempotencyRecord(
                operationType,
                idempotencyKeyHash,
                actorScope,
                originalPaymentId,
                requestPayloadHash,
                reversalId,
                createdAt);
    }

    public boolean matches(String actorScope, String originalPaymentId, String requestPayloadHash) {
        return this.actorScope.equals(actorScope)
                && this.originalPaymentId.equals(originalPaymentId)
                && this.requestPayloadHash.equals(requestPayloadHash);
    }

    private static void require(String value, String field) {
        if (value == null || value.isBlank()) {
            throw new IllegalArgumentException(field + " is required.");
        }
    }
}
