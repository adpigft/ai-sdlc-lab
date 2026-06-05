# OpenAPI Generation Standard

## Purpose

Define contract-first REST API standards for Java 21 Spring Boot 3.x services and generated clients.

## Contract-First Rule

OpenAPI v3 contracts must be created and reviewed before implementation begins. Generated server interfaces, DTOs, and clients must be treated as governed artifacts and reviewed with the same care as handwritten code.

## Contract Location

Service repositories should store contracts under:

```text
openapi/
└── api-spec.yaml
```

Feature-level AI SDLC artifacts may store approved contracts under:

```text
domains/<domain>/capabilities/<capability>/features/<feature>/contracts/openapi.yaml
```

## Java Generation

- Use OpenAPI Generator for Spring Boot 3.x compatible Java generation.
- Generate interfaces and DTOs during build.
- Keep generated code separate from handwritten application code.
- Implement generated interfaces in the transport layer.
- Map generated DTOs to application commands and queries before entering business logic.
- Do not expose domain objects directly as API models.

## API Design Rules

- Use stable resource names and explicit API versions.
- Use nouns for resources and command sub-resources only when business action semantics require them.
- Use standard HTTP status codes consistently.
- Validate request bodies, path parameters, query parameters, headers, and authentication context.
- Avoid ambiguous strings for money, timestamps, identifiers, statuses, and enums.
- Define required fields, formats, constraints, examples, and safe descriptions.
- Define pagination contracts for list endpoints.
- Define backward-compatible evolution rules for all fields.

## Headers

| Header | Requirement |
| --- | --- |
| `X-Correlation-ID` | Mandatory for inbound and outbound requests. Generate if missing at the gateway or transport boundary. |
| `traceparent` / `tracestate` | Propagate W3C trace context across HTTP and event boundaries. |
| `X-Idempotency-Key` | Mandatory for write endpoints that mutate banking state or coordinate external providers. |

Idempotency keys for state-mutating operations must be retained for at least 24 hours unless a stricter domain standard applies. Duplicate requests must return the original outcome where the request identity and payload match.

## Error Model

Every API failure must return a standard safe error body:

```json
{
  "name": "RESOURCE_NOT_FOUND",
  "message": "Requested resource was not found.",
  "errorId": "b18ca721-a5de-4d04-a728-b985cb5f70f6"
}
```

| Condition | Status |
| --- | --- |
| Malformed input or validation failure | 400 |
| Missing or invalid authentication | 401 |
| Authenticated actor lacks permission | 403 |
| Resource not found | 404 |
| Business rule rejection | 422 |
| External dependency failure | 502 or approved safe service error |
| Unexpected internal failure | 500 |

## Security

- Use OAuth2 and OIDC with Spring Security.
- Mobile apps must use Authorization Code Flow with PKCE.
- Service-to-service integrations must use client credentials with mTLS, signed assertions, or approved workload identity.
- Validate JWT signature, issuer, audience, expiration, not-before, and clock skew.
- Map scopes and claims to Spring Security authorities.
- Do not expose sensitive card, customer, token, fraud, or processor details in responses.

## Resilience

- Protect external HTTP clients with circuit breakers, timeouts, retries, and rate limits where appropriate.
- Use Resilience4j or an approved platform equivalent for synchronous external calls.
- Record timeout and retry behavior in design and tests.
- Avoid retrying non-idempotent provider calls unless an idempotency or reconciliation model is approved.

## Review Gate

An OpenAPI contract is ready for implementation only after product, architecture, API owner, security, QA, and impacted consumers have reviewed the relevant operations and traceability links.

