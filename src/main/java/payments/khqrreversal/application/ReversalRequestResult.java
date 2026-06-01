package payments.khqrreversal.application;

import payments.khqrreversal.domain.model.PaymentReversal;

public record ReversalRequestResult(PaymentReversal reversal, boolean replayed) {
    public static ReversalRequestResult created(PaymentReversal reversal) {
        return new ReversalRequestResult(reversal, false);
    }

    public static ReversalRequestResult replayed(PaymentReversal reversal) {
        return new ReversalRequestResult(reversal, true);
    }
}
