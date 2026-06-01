package payments.khqrreversal.application.port;

import java.util.Optional;
import payments.khqrreversal.domain.model.OriginalPaymentSnapshot;

public interface OriginalPaymentLookupPort {
    Optional<OriginalPaymentSnapshot> findByPaymentId(String originalPaymentId);
}
