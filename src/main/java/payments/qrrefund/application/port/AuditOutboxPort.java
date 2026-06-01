package payments.qrrefund.application.port;

import payments.qrrefund.domain.audit.AuditEvent;

public interface AuditOutboxPort {
    void append(AuditEvent event);
}
