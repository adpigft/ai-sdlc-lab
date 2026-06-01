package payments.khqrreversal.application.command;

import java.util.Objects;
import payments.khqrreversal.domain.error.ReversalException;
import payments.khqrreversal.domain.error.ReversalRejectionCode;
import payments.khqrreversal.domain.value.Money;

public record CreateKhqrPaymentReversalCommand(
        String originalPaymentId,
        Money amount,
        String reasonCode,
        String evidenceReference,
        String makerId,
        String makerRole,
        String correlationId,
        String idempotencyKey,
        String reasonNotes) {

    public CreateKhqrPaymentReversalCommand {
        require(originalPaymentId, "originalPaymentId");
        Objects.requireNonNull(amount, "amount");
        require(evidenceReference, "evidenceReference");
        require(makerId, "makerId");
        require(makerRole, "makerRole");
        require(correlationId, "correlationId");
        if (idempotencyKey == null || idempotencyKey.isBlank()) {
            throw new ReversalException(
                    ReversalRejectionCode.MISSING_IDEMPOTENCY_KEY,
                    "Idempotency key is required.");
        }
    }

    public String normalizedPayload() {
        return String.join("|",
                originalPaymentId.trim(),
                amount.normalizedValue(),
                amount.currency().getCurrencyCode(),
                reasonCode == null ? "" : reasonCode.trim(),
                evidenceReference.trim(),
                makerId.trim(),
                makerRole.trim(),
                reasonNotes == null ? "" : reasonNotes.trim());
    }

    private static void require(String value, String field) {
        if (value == null || value.isBlank()) {
            throw new ReversalException(
                    ReversalRejectionCode.INVALID_REQUEST,
                    "Missing field: " + field + ".");
        }
    }
}
