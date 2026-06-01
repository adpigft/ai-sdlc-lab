package payments.qrrefund.application.port;

import payments.qrrefund.domain.audit.AuditEvent;

public interface AuditOutboxPort {
    /*
     * Implementations must append this event in the same atomic unit of work as
     * the associated material refund state and idempotency writes.
     */
    void append(AuditEvent event);
}
