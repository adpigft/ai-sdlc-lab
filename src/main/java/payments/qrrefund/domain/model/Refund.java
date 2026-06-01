package payments.qrrefund.domain.model;

import java.math.BigDecimal;
import java.time.Instant;
import java.util.Currency;
import payments.qrrefund.domain.error.RefundException;
import payments.qrrefund.domain.error.RefundRejectionCode;
import payments.qrrefund.domain.value.ReasonCode;

public record Refund(
        String refundId,
        String originalPaymentId,
        String merchantId,
        BigDecimal amount,
        Currency currency,
        RefundStatus status,
        ReasonCode reasonCode,
        String requestedBy,
        String requestedByRole,
        String channel,
        String correlationId,
        Instant createdAt,
        Instant updatedAt,
        long version) {

    public Refund {
        require(refundId, "refundId");
        require(originalPaymentId, "originalPaymentId");
        require(merchantId, "merchantId");
        if (amount == null || amount.signum() <= 0) {
            throw new RefundException(RefundRejectionCode.INVALID_REQUEST, "Refund amount must be positive.");
        }
        if (currency == null) {
            throw new RefundException(RefundRejectionCode.INVALID_REQUEST, "Currency is required.");
        }
        if (status == null) {
            throw new RefundException(RefundRejectionCode.INVALID_REQUEST, "Refund status is required.");
        }
        if (reasonCode == null) {
            throw new RefundException(RefundRejectionCode.INVALID_REQUEST, "Reason code is required.");
        }
        require(requestedBy, "requestedBy");
        require(requestedByRole, "requestedByRole");
        require(channel, "channel");
        require(correlationId, "correlationId");
        if (createdAt == null || updatedAt == null) {
            throw new RefundException(RefundRejectionCode.INVALID_REQUEST, "Refund timestamps are required.");
        }
        if (version < 0) {
            throw new RefundException(RefundRejectionCode.INVALID_REQUEST, "Refund version cannot be negative.");
        }
    }

    public static Refund requested(
            String refundId,
            String originalPaymentId,
            String merchantId,
            BigDecimal amount,
            Currency currency,
            ReasonCode reasonCode,
            String requestedBy,
            String requestedByRole,
            String channel,
            String correlationId,
            Instant now) {
        return new Refund(
                refundId,
                originalPaymentId,
                merchantId,
                amount,
                currency,
                RefundStatus.REQUESTED,
                reasonCode,
                requestedBy,
                requestedByRole,
                channel,
                correlationId,
                now,
                now,
                0);
    }

    private static void require(String value, String field) {
        if (value == null || value.isBlank()) {
            throw new RefundException(RefundRejectionCode.INVALID_REQUEST, "Missing field: " + field + ".");
        }
    }
}
