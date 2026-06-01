package payments.khqrreversal.application.port;

import payments.khqrreversal.domain.idempotency.IdempotencyRecord;

public interface IdempotencyStorePort {
    IdempotencyRecord find(String operationType, String idempotencyKeyHash);

    void save(IdempotencyRecord record);
}
