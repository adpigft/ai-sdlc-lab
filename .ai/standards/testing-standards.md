# Testing Standards

## Scope

These standards guide acceptance, unit, integration, contract, security, performance, and operational testing for banking payment capabilities.

## Test Layers

- Acceptance tests validate customer-visible behavior and business rules.
- Unit tests validate domain rules and edge cases.
- Integration tests validate system boundaries, processors, ledgers, fraud services, and notification services.
- Contract tests validate API compatibility.
- Security tests validate authorization, input handling, replay resistance, and sensitive-data protection.
- Operational tests validate logging, metrics, traces, alerts, rollback, and reconciliation.

## Payment Coverage

- Happy path payment initiation and completion.
- Invalid or expired QR payload.
- Insufficient funds or limit breach.
- Duplicate submission with same idempotency key.
- Duplicate submission with conflicting payload.
- Processor timeout with later successful completion.
- Fraud hold or sanctions rejection.
- Customer cancellation where supported.
- Reconciliation mismatch and manual review path.

## Evidence Rules

- Every mandatory requirement must link to at least one test or explicit review control.
- Test results must be recorded in validation reports.
- Defects must link to Jira and affected requirement IDs.
- Release notes must state unresolved defects and accepted risks.

## Automation Expectations

GitHub Actions should eventually run tests, coverage, linting, static analysis, contract validation, and traceability checks on pull requests and protected branches.
