package payments.qrrefund.domain.idempotency;

import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import payments.qrrefund.domain.error.RefundException;
import payments.qrrefund.domain.error.RefundRejectionCode;

public final class HmacSha256IdempotencyHasher implements IdempotencyHasher {
    private static final String ALGORITHM = "HmacSHA256";
    private static final int MINIMUM_KEY_BYTES = 32;

    private final byte[] key;

    public HmacSha256IdempotencyHasher(byte[] key) {
        if (key == null || key.length < MINIMUM_KEY_BYTES) {
            throw new RefundException(
                    RefundRejectionCode.INVALID_REQUEST,
                    "Idempotency HMAC key must be at least 32 bytes.");
        }
        this.key = Arrays.copyOf(key, key.length);
    }

    @Override
    public String hashKey(String idempotencyKey) {
        return hmac(idempotencyKey);
    }

    @Override
    public String hashPayload(String normalizedPayload) {
        return hmac(normalizedPayload);
    }

    private String hmac(String value) {
        if (value == null) {
            throw new RefundException(
                    RefundRejectionCode.INVALID_REQUEST,
                    "Cannot hash a null idempotency value.");
        }
        try {
            Mac mac = Mac.getInstance(ALGORITHM);
            mac.init(new SecretKeySpec(key, ALGORITHM));
            byte[] digest = mac.doFinal(value.getBytes(StandardCharsets.UTF_8));
            StringBuilder hex = new StringBuilder(digest.length * 2);
            for (byte b : digest) {
                hex.append(String.format("%02x", b));
            }
            return hex.toString();
        } catch (Exception exception) {
            throw new IllegalStateException("HMAC-SHA-256 idempotency hashing failed.", exception);
        }
    }
}
