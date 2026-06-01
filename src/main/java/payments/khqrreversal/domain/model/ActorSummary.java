package payments.khqrreversal.domain.model;

import payments.khqrreversal.domain.error.ReversalException;
import payments.khqrreversal.domain.error.ReversalRejectionCode;

public record ActorSummary(String actorId, String role) {
    public ActorSummary {
        if (actorId == null || actorId.isBlank()) {
            throw new ReversalException(
                    ReversalRejectionCode.INVALID_REQUEST,
                    "Actor ID is required.");
        }
        if (role == null || role.isBlank()) {
            throw new ReversalException(
                    ReversalRejectionCode.INVALID_REQUEST,
                    "Actor role is required.");
        }
    }
}
