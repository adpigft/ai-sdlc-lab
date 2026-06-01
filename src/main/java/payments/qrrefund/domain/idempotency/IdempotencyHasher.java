package payments.qrrefund.domain.idempotency;

public interface IdempotencyHasher {
    String hashKey(String idempotencyKey);

    String hashPayload(String normalizedPayload);
}
