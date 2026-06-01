package payments.khqrreversal.domain.audit;

import java.time.Instant;
import java.util.Objects;
import payments.khqrreversal.domain.model.PaymentReversal;

public record AuditEvent(
        AuditEventType eventType,
        String reversalId,
        String originalPaymentId,
        String actorId,
        String actorRole,
        String reasonCode,
        String outcomeCode,
        String correlationId,
        Instant timestamp) {

    public AuditEvent {
        Objects.requireNonNull(eventType, "eventType");
        if (originalPaymentId == null || originalPaymentId.isBlank()) {
            throw new IllegalArgumentException("originalPaymentId is required.");
        }
        if (actorId == null || actorId.isBlank()) {
            throw new IllegalArgumentException("actorId is required.");
        }
        if (actorRole == null || actorRole.isBlank()) {
            throw new IllegalArgumentException("actorRole is required.");
        }
        if (correlationId == null || correlationId.isBlank()) {
            throw new IllegalArgumentException("correlationId is required.");
        }
        Objects.requireNonNull(timestamp, "timestamp");
    }

    public static AuditEvent reversalRequested(PaymentReversal reversal) {
        return new AuditEvent(
                AuditEventType.REVERSAL_REQUESTED,
                reversal.reversalId(),
                reversal.originalPaymentId(),
                reversal.maker().actorId(),
                reversal.maker().role(),
                reversal.reasonCode().name(),
                "requested",
                reversal.correlationId(),
                reversal.createdAt());
    }

    public static AuditEvent rejection(
            AuditEventType eventType,
            String originalPaymentId,
            String actorId,
            String actorRole,
            String reasonCode,
            String correlationId,
            String outcomeCode,
            Instant timestamp) {
        return new AuditEvent(
                eventType,
                null,
                originalPaymentId,
                actorId,
                actorRole,
                reasonCode,
                outcomeCode,
                correlationId,
                timestamp);
    }
}
