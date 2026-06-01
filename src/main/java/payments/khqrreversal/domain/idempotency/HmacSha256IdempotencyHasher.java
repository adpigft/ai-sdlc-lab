package payments.khqrreversal.domain.idempotency;

import java.nio.charset.StandardCharsets;
import java.security.GeneralSecurityException;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

public final class HmacSha256IdempotencyHasher implements IdempotencyHasher {
    private final byte[] key;

    public HmacSha256IdempotencyHasher(byte[] key) {
        this.key = key.clone();
    }

    @Override
    public String hashKey(String rawKey) {
        return hash(rawKey);
    }

    @Override
    public String hashPayload(String normalizedPayload) {
        return hash(normalizedPayload);
    }

    private String hash(String value) {
        try {
            Mac mac = Mac.getInstance("HmacSHA256");
            mac.init(new SecretKeySpec(key, "HmacSHA256"));
            byte[] digest = mac.doFinal(value.getBytes(StandardCharsets.UTF_8));
            return toHex(digest);
        } catch (GeneralSecurityException exception) {
            throw new IllegalStateException("Unable to hash idempotency data.", exception);
        }
    }

    private static String toHex(byte[] bytes) {
        StringBuilder builder = new StringBuilder(bytes.length * 2);
        for (byte value : bytes) {
            builder.append(Character.forDigit((value >>> 4) & 0xF, 16));
            builder.append(Character.forDigit(value & 0xF, 16));
        }
        return builder.toString();
    }
}
