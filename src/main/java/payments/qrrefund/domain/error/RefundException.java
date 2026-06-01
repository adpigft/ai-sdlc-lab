package payments.qrrefund.domain.error;

public final class RefundException extends RuntimeException {
    private final RefundRejectionCode code;

    public RefundException(RefundRejectionCode code, String message) {
        super(message);
        this.code = code;
    }

    public RefundRejectionCode code() {
        return code;
    }
}
