package payments.khqrreversal.domain.model;

import java.util.Objects;
import payments.khqrreversal.domain.error.ReversalException;
import payments.khqrreversal.domain.error.ReversalRejectionCode;
import payments.khqrreversal.domain.value.Money;
import payments.khqrreversal.domain.value.PaymentStatus;
import payments.khqrreversal.domain.value.SettlementState;

public record OriginalPaymentSnapshot(
        String originalPaymentId,
        Money amount,
        PaymentStatus paymentStatus,
        SettlementState settlementState) {

    public OriginalPaymentSnapshot {
        if (originalPaymentId == null || originalPaymentId.isBlank()) {
            throw new ReversalException(
                    ReversalRejectionCode.INVALID_REQUEST,
                    "Original payment ID is required.");
        }
        Objects.requireNonNull(amount, "amount");
        Objects.requireNonNull(paymentStatus, "paymentStatus");
        Objects.requireNonNull(settlementState, "settlementState");
    }
}
