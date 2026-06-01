package payments.khqrreversal.domain.value;

import java.util.Set;
import payments.khqrreversal.domain.error.ReversalException;
import payments.khqrreversal.domain.error.ReversalRejectionCode;

public enum ReversalReasonCode {
    PROCESSOR_DUPLICATE_EXECUTION,
    PROCESSOR_STATUS_CORRECTION,
    LEDGER_POSTING_ERROR,
    SYSTEM_PROCESSING_ERROR,
    RECONCILIATION_BREAK_CORRECTION;

    private static final Set<String> REQUEST_CODES = Set.of(
            PROCESSOR_DUPLICATE_EXECUTION.name(),
            PROCESSOR_STATUS_CORRECTION.name(),
            LEDGER_POSTING_ERROR.name(),
            SYSTEM_PROCESSING_ERROR.name(),
            RECONCILIATION_BREAK_CORRECTION.name());

    public static ReversalReasonCode of(String value) {
        if (value == null || value.isBlank() || !REQUEST_CODES.contains(value)) {
            throw new ReversalException(
                    ReversalRejectionCode.INVALID_REASON_CODE,
                    "Invalid KHQR reversal reason code.");
        }
        return ReversalReasonCode.valueOf(value);
    }
}
