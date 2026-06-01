# API Standards

## Scope

These standards apply to APIs for banking and digital payments capabilities, including future KHQR payment endpoints.

## Contract Requirements

- Use OpenAPI for REST contracts.
- Include version, owners, contact, authentication scheme, idempotency behavior, error model, and examples.
- Define request and response schemas with explicit required fields, formats, constraints, and descriptions.
- Avoid ambiguous `string` fields for money, dates, identifiers, and status values.
- Use decimal-safe amount representation, such as string with fixed scale or integer minor units, as defined by the domain.

## Payment Behavior

- Payment initiation endpoints must support an idempotency key.
- Payment status must distinguish `accepted`, `pending`, `completed`, `failed`, `rejected`, `expired`, and `cancelled` where applicable.
- Timeouts must not imply payment failure unless confirmed by the payment processor or ledger.
- Error responses must be stable enough for client handling and safe enough for customer display.

## Security

- Do not expose account numbers, national IDs, tokens, secrets, or internal fraud signals in API responses.
- Use authenticated and authorized endpoints for customer payment actions.
- Include correlation IDs for audit and support without leaking sensitive values.
- Document rate limits and abuse controls.

## Review Gate

An API contract is ready for implementation only after product, architecture, security, and QA have reviewed it and the traceability matrix links contract operations to requirements.
