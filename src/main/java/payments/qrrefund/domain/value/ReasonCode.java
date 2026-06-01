package payments.qrrefund.domain.value;

import payments.qrrefund.domain.error.RefundException;
import payments.qrrefund.domain.error.RefundRejectionCode;

public record ReasonCode(String value) {
    private static final String PATTERN = "[A-Z][A-Z0-9_]{2,63}";

    public ReasonCode {
        if (value == null || !value.matches(PATTERN)) {
            throw new RefundException(
                    RefundRejectionCode.INVALID_REASON_CODE,
                    "Reason code must be uppercase and 3 to 64 characters.");
        }
    }

    public static ReasonCode of(String value) {
        return new ReasonCode(value == null ? null : value.trim());
    }
}
