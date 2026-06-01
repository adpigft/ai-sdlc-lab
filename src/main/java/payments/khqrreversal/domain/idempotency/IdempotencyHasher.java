package payments.khqrreversal.domain.idempotency;

public interface IdempotencyHasher {
    String hashKey(String rawKey);

    String hashPayload(String normalizedPayload);
}
