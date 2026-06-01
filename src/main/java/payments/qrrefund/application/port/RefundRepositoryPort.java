package payments.qrrefund.application.port;

import payments.qrrefund.domain.model.Refund;

public interface RefundRepositoryPort {
    boolean existsByOriginalPaymentId(String originalPaymentId);

    Refund findByRefundId(String refundId);

    void saveNew(Refund refund);
}
