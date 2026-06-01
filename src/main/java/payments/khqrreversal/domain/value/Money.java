package payments.khqrreversal.domain.value;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Currency;
import payments.khqrreversal.domain.error.ReversalException;
import payments.khqrreversal.domain.error.ReversalRejectionCode;

public record Money(BigDecimal value, Currency currency) {
    public Money {
        if (value == null || value.signum() <= 0) {
            throw new ReversalException(
                    ReversalRejectionCode.INVALID_REQUEST,
                    "Money value must be positive.");
        }
        if (currency == null) {
            throw new ReversalException(
                    ReversalRejectionCode.INVALID_REQUEST,
                    "Currency is required.");
        }
        value = value.setScale(2, RoundingMode.UNNECESSARY);
    }

    public String normalizedValue() {
        return value.toPlainString();
    }
}
