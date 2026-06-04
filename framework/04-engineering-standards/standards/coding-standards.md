# Coding Standards

## Scope

These standards are reserved for future application code. This baseline repository does not contain application implementation.

## General Requirements

- Code must be readable, maintainable, tested, and traceable to Jira and requirement IDs.
- Generated code must be reviewed as carefully as human-written code.
- Prefer simple domain language over clever abstractions.
- Keep payment state transitions explicit and auditable.
- Avoid hidden side effects around money movement, ledger updates, notifications, and retries.

## Banking Payments Requirements

- Validate all external inputs at system boundaries.
- Treat money, currency, limits, status, timestamps, and customer identifiers as domain values with clear constraints.
- Make idempotency, retries, and duplicate handling visible in code and tests.
- Avoid logging sensitive data. Mask or tokenize customer and payment identifiers where needed.
- Emit audit events for payment initiation, authorization, status changes, reversals, and administrative actions.

## Pull Request Expectations

- Link Jira issues and requirement IDs.
- Include test evidence and SonarCloud status.
- Explain risk, rollback, and monitoring impact.
- Identify any generated code and prompt assumptions that influenced the change.

## Not Yet Active

Application code must not be added until the intent, specification, review, traceability, and build gates have been completed for the target capability.
