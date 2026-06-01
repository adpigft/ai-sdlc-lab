package payments.khqrreversal.domain.error;

public final class ReversalException extends RuntimeException {
    private final ReversalRejectionCode code;

    public ReversalException(ReversalRejectionCode code, String message) {
        super(message);
        this.code = code;
    }

    public ReversalRejectionCode code() {
        return code;
    }
}
