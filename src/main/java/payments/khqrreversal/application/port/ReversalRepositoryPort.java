package payments.khqrreversal.application.port;

import payments.khqrreversal.domain.model.PaymentReversal;

public interface ReversalRepositoryPort {
    boolean existsByOriginalPaymentId(String originalPaymentId);

    PaymentReversal findByReversalId(String reversalId);

    void saveNew(PaymentReversal reversal);
}
