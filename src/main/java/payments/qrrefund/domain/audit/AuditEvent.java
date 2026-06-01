package payments.qrrefund.domain.audit;

import java.time.Instant;
import payments.qrrefund.domain.model.Refund;

public record AuditEvent(
        AuditEventType eventType,
        String originalPaymentId,
        String refundId,
        String initiator,
        String userRole,
        String reasonCode,
        Instant timestamp,
        String approvalUser,
        String correlationId,
        String outcomeCode) {

    public static AuditEvent refundRequested(Refund refund) {
        return new AuditEvent(
                AuditEventType.REFUND_REQUESTED,
                refund.originalPaymentId(),
                refund.refundId(),
                refund.requestedBy(),
                refund.requestedByRole(),
                refund.reasonCode().value(),
                refund.createdAt(),
                null,
                refund.correlationId(),
                "REQUESTED");
    }

    public static AuditEvent rejection(
            AuditEventType eventType,
            String originalPaymentId,
            String refundId,
            String initiator,
            String userRole,
            String reasonCode,
            String correlationId,
            String outcomeCode) {
        return new AuditEvent(
                eventType,
                originalPaymentId,
                refundId,
                initiator,
                userRole,
                reasonCode,
                Instant.now(),
                null,
                correlationId,
                outcomeCode);
    }
}
