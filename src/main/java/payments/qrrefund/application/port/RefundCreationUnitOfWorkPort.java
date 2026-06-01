package payments.qrrefund.application.port;

import java.util.function.Supplier;

public interface RefundCreationUnitOfWorkPort {
    /*
     * Implementations must execute the supplied Slice 1 refund creation work in
     * one atomic unit with refund state, idempotency record, and audit outbox.
     */
    <T> T required(Supplier<T> work);
}
