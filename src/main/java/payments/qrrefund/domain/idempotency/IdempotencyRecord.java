package payments.qrrefund.domain.idempotency;

import java.time.Instant;
import payments.qrrefund.domain.error.RefundException;
import payments.qrrefund.domain.error.RefundRejectionCode;

public record IdempotencyRecord(
        String operationType,
        String idempotencyKeyHash,
        String merchantId,
        String originalPaymentId,
        String requestPayloadHash,
        String refundId,
        String status,
        Instant createdAt) {

    public IdempotencyRecord {
        require(operationType, "operationType");
        require(idempotencyKeyHash, "idempotencyKeyHash");
        require(merchantId, "merchantId");
        require(originalPaymentId, "originalPaymentId");
        require(requestPayloadHash, "requestPayloadHash");
        require(refundId, "refundId");
        require(status, "status");
        if (createdAt == null) {
            throw new RefundException(RefundRejectionCode.INVALID_REQUEST, "createdAt is required.");
        }
    }

    public static IdempotencyRecord completed(
            String operationType,
            String idempotencyKeyHash,
            String merchantId,
            String originalPaymentId,
            String requestPayloadHash,
            String refundId,
            Instant createdAt) {
        return new IdempotencyRecord(
                operationType,
                idempotencyKeyHash,
                merchantId,
                originalPaymentId,
                requestPayloadHash,
                refundId,
                "COMPLETED",
                createdAt);
    }

    public boolean matches(String merchantId, String originalPaymentId, String requestPayloadHash) {
        return this.merchantId.equals(merchantId)
                && this.originalPaymentId.equals(originalPaymentId)
                && this.requestPayloadHash.equals(requestPayloadHash);
    }

    private static void require(String value, String field) {
        if (value == null || value.isBlank()) {
            throw new RefundException(
                    RefundRejectionCode.INVALID_REQUEST,
                    "Missing idempotency field: " + field + ".");
        }
    }
}
