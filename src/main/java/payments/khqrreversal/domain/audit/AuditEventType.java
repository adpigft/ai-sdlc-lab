package payments.khqrreversal.domain.audit;

public enum AuditEventType {
    REVERSAL_REQUESTED,
    REVERSAL_REJECTED,
    AUTHORIZATION_FAILURE,
    DUPLICATE_REVERSAL_ATTEMPT,
    IDEMPOTENCY_CONFLICT
}
