package payments.qrrefund.application.port;

import java.util.Optional;
import payments.qrrefund.domain.model.OriginalPaymentSnapshot;

public interface OriginalPaymentLookupPort {
    Optional<OriginalPaymentSnapshot> findByPaymentId(String originalPaymentId);
}
