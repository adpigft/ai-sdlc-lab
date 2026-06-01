package payments.khqrreversal.application.port;

import payments.khqrreversal.domain.audit.AuditEvent;

public interface AuditOutboxPort {
    void append(AuditEvent event);
}
