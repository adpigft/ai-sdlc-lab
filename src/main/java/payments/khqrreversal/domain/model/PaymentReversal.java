package payments.khqrreversal.domain.model;

import java.time.Instant;
import java.util.Objects;
import payments.khqrreversal.domain.error.ReversalException;
import payments.khqrreversal.domain.error.ReversalRejectionCode;
import payments.khqrreversal.domain.value.Money;
import payments.khqrreversal.domain.value.ReversalReasonCode;

public record PaymentReversal(
        String reversalId,
        String originalPaymentId,
        Money amount,
        ReversalWorkflowStatus workflowStatus,
        ReversalReasonCode reasonCode,
        ActorSummary maker,
        ActorSummary checker,
        String evidenceReference,
        String reasonNotes,
        String correlationId,
        Instant createdAt,
        long version) {

    public PaymentReversal {
        if (reversalId == null || reversalId.isBlank()) {
            throw new ReversalException(
                    ReversalRejectionCode.INVALID_REQUEST,
                    "Reversal ID is required.");
        }
        if (originalPaymentId == null || originalPaymentId.isBlank()) {
            throw new ReversalException(
                    ReversalRejectionCode.INVALID_REQUEST,
                    "Original payment ID is required.");
        }
        Objects.requireNonNull(amount, "amount");
        Objects.requireNonNull(workflowStatus, "workflowStatus");
        Objects.requireNonNull(reasonCode, "reasonCode");
        Objects.requireNonNull(maker, "maker");
        if (evidenceReference == null || evidenceReference.isBlank()) {
            throw new ReversalException(
                    ReversalRejectionCode.INVALID_REQUEST,
                    "Evidence reference is required.");
        }
        if (correlationId == null || correlationId.isBlank()) {
            throw new ReversalException(
                    ReversalRejectionCode.INVALID_REQUEST,
                    "Correlation ID is required.");
        }
        Objects.requireNonNull(createdAt, "createdAt");
        if (version < 0) {
            throw new ReversalException(
                    ReversalRejectionCode.INVALID_REQUEST,
                    "Version cannot be negative.");
        }
    }

    public static PaymentReversal awaitingApproval(
            String reversalId,
            String originalPaymentId,
            Money amount,
            ReversalReasonCode reasonCode,
            ActorSummary maker,
            String evidenceReference,
            String reasonNotes,
            String correlationId,
            Instant createdAt) {
        return new PaymentReversal(
                reversalId,
                originalPaymentId,
                amount,
                ReversalWorkflowStatus.AWAITING_APPROVAL,
                reasonCode,
                maker,
                null,
                evidenceReference,
                reasonNotes,
                correlationId,
                createdAt,
                0);
    }
}
