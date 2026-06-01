package payments.qrrefund.domain.audit;

public enum AuditEventType {
    REFUND_REQUESTED,
    REFUND_REJECTED,
    DUPLICATE_REFUND_ATTEMPT,
    IDEMPOTENCY_CONFLICT
}
