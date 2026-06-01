package payments.qrrefund.domain.model;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.Currency;
import payments.qrrefund.domain.error.RefundException;
import payments.qrrefund.domain.error.RefundRejectionCode;
import payments.qrrefund.domain.value.PaymentStatus;
import payments.qrrefund.domain.value.SettlementState;

public record OriginalPaymentSnapshot(
        String originalPaymentId,
        String merchantId,
        BigDecimal amount,
        Currency currency,
        PaymentStatus paymentStatus,
        LocalDate paymentDate,
        SettlementState settlementState,
        boolean alreadyRefunded,
        boolean merchantSuspended) {

    public OriginalPaymentSnapshot {
        require(originalPaymentId, "originalPaymentId");
        require(merchantId, "merchantId");
        if (amount == null || amount.signum() <= 0) {
            throw new RefundException(RefundRejectionCode.INVALID_REQUEST, "Payment amount must be positive.");
        }
        if (currency == null) {
            throw new RefundException(RefundRejectionCode.INVALID_REQUEST, "Currency is required.");
        }
        if (paymentStatus == null) {
            throw new RefundException(RefundRejectionCode.INVALID_REQUEST, "Payment status is required.");
        }
        if (paymentDate == null) {
            throw new RefundException(RefundRejectionCode.INVALID_REQUEST, "Payment date is required.");
        }
        if (settlementState == null) {
            throw new RefundException(RefundRejectionCode.INVALID_REQUEST, "Settlement state is required.");
        }
    }

    private static void require(String value, String field) {
        if (value == null || value.isBlank()) {
            throw new RefundException(RefundRejectionCode.INVALID_REQUEST, "Missing field: " + field + ".");
        }
    }
}
