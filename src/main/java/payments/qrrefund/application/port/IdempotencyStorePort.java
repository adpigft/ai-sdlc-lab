package payments.qrrefund.application.port;

import payments.qrrefund.domain.idempotency.IdempotencyRecord;

public interface IdempotencyStorePort {
    IdempotencyRecord find(String operationType, String idempotencyKeyHash);

    void save(IdempotencyRecord record);
}
