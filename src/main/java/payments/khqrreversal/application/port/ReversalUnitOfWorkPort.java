package payments.khqrreversal.application.port;

import java.util.function.Supplier;

public interface ReversalUnitOfWorkPort {
    <T> T required(Supplier<T> work);
}
