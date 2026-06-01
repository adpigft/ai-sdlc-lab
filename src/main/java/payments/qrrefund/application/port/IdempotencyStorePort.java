package payments.qrrefund.application.port;

import payments.qrrefund.domain.idempotency.IdempotencyRecord;

public interface IdempotencyStorePort {
    /*
     * Implementations must lock or serialize by operationType and
     * idempotencyKeyHash within the refund creation unit of work.
     */
    IdempotencyRecord find(String operationType, String idempotencyKeyHash);

    void save(IdempotencyRecord record);
}
