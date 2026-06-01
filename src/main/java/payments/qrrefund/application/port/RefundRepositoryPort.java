package payments.qrrefund.application.port;

import payments.qrrefund.domain.model.Refund;

public interface RefundRepositoryPort {
    boolean existsByOriginalPaymentId(String originalPaymentId);

    Refund findByRefundId(String refundId);

    /*
     * Implementations must enforce a unique originalPaymentId constraint for
     * full refunds and optimistic locking, row versioning, or an equivalent
     * aggregate-version check for refund writes.
     */
    void saveNew(Refund refund);
}
