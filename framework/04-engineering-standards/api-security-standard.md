# API Security Standard

## Purpose

Define security standards for REST, GraphQL, mobile, and service-to-service APIs. This standard complements `openapi-generation-standard.md` by focusing on authentication, authorization, token validation, GraphQL controls, and abuse resistance.

## Authentication

| Actor Type | Required Flow |
| --- | --- |
| Mobile app user | OAuth2 Authorization Code Flow with PKCE. |
| Operations user | Enterprise OIDC flow approved for operations channels. |
| Service-to-service client | OAuth2 Client Credentials with mTLS, signed client assertions, or approved workload identity. |
| External partner | Approved partner identity model with contract, rate limit, monitoring, and revocation controls. |

Implicit grant and password credential flow are prohibited for new digital banking capabilities.

## JWT Validation

Services that process JWTs must validate:

- signature using identity-provider JWKS
- issuer
- audience
- expiration
- not-before
- accepted clock skew
- token type where provided
- required scopes, roles, groups, or claims

Claims used for audit, such as subject, client ID, channel, and actor type, must be copied into the request security context and safe diagnostic context.

## Authorization

- Enforce authorization at the transport boundary and again at application use-case boundaries where business ownership checks are required.
- Map OAuth scopes, roles, groups, or entitlement claims to Spring Security authorities.
- Prevent customer actors from accessing resources they do not own.
- Prevent operations users from accessing capabilities without explicit entitlement.
- Use method-level authorization for sensitive use cases where practical.
- Record unauthorized attempts in audit evidence for material banking actions.

Java example:

```java
@PreAuthorize("hasAuthority('SCOPE_cards:replacement:write')")
public ReplacementResponse submitReplacement(ReplacementCommand command) {
    return replacementService.submit(command);
}
```

## GraphQL Standards

GraphQL APIs require explicit approval because flexible query shape increases security and performance risk.

GraphQL schemas must:

- be type-first and version controlled
- use thin resolvers that delegate business behavior to application services
- enforce field-level authorization for sensitive fields
- use cursor-based pagination for lists
- set a maximum page size of 100 unless a stricter limit is approved
- prevent N+1 access patterns through batching and data loading
- reject introspection in production unless explicitly approved for a controlled endpoint
- enforce query depth and complexity limits

Recommended limits:

| Control | Default Limit |
| --- | --- |
| Query depth | 7 |
| Complexity score | 250 |
| List page size | 100 |

GraphQL resolvers must not bypass domain services, authorization policies, audit controls, or data masking.

## REST Abuse Controls

- Require idempotency keys for state-mutating banking commands.
- Apply rate limits by client, user, tenant, channel, or IP according to risk.
- Use circuit breakers and timeouts for downstream dependencies.
- Reject oversized requests.
- Validate content type.
- Validate path, query, body, and header fields.
- Return actor-safe error messages.

## Sensitive Data Controls

- Do not expose full PAN, CVV, secrets, tokens, raw credentials, private fraud signals, or sensitive profile data in API responses.
- Mask sensitive values in logs, traces, events, validation evidence, and support tooling.
- Use stable tokenized or surrogate identifiers where possible.
- Classify fields in API and GraphQL schemas when they carry sensitive data.

## Review Checklist

- Authentication flow matches actor type.
- JWT validation rules are explicit.
- Authorization checks cover actor, resource ownership, channel, and operation.
- GraphQL depth, complexity, pagination, batching, and field security controls are defined where GraphQL is used.
- Rate limits, idempotency, circuit breakers, and safe errors are documented.
- Sensitive data is masked or excluded.

