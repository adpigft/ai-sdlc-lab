package payments.qrrefund.application.command;

import payments.qrrefund.domain.error.RefundException;
import payments.qrrefund.domain.error.RefundRejectionCode;

public record InitiateMerchantRefundCommand(
        String originalPaymentId,
        String merchantId,
        String reasonCode,
        String actorId,
        String actorRole,
        String channel,
        String correlationId,
        String idempotencyKey) {

    public void validate() {
        require(originalPaymentId, "originalPaymentId");
        require(merchantId, "merchantId");
        require(reasonCode, "reasonCode");
        require(actorId, "actorId");
        require(actorRole, "actorRole");
        require(channel, "channel");
        require(correlationId, "correlationId");
        require(idempotencyKey, "idempotencyKey");
    }

    public String normalizedPayload() {
        return String.join("|",
                "MERCHANT_REFUND_CREATE",
                trim(originalPaymentId),
                trim(merchantId),
                trim(reasonCode),
                trim(actorId),
                trim(actorRole),
                trim(channel));
    }

    private static void require(String value, String field) {
        if (value == null || value.isBlank()) {
            throw new RefundException(
                    RefundRejectionCode.INVALID_REQUEST,
                    "Missing required field: " + field + ".");
        }
    }

    private static String trim(String value) {
        return value == null ? "" : value.trim();
    }
}
