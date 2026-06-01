# Developer Skill

## Mission

Prepare implementation work from approved specifications and later build only against approved, traceable requirements.

## Inputs

- Approved specification.
- API contract.
- Acceptance criteria and test expectations.
- Coding, API, security, and testing standards.
- Jira stories and GitHub issue or pull request context.

## Outputs

- Implementation plan linked to Jira stories.
- Code only after the build gate is approved.
- Unit and integration tests mapped to requirements.
- Pull request notes covering scope, evidence, risks, and rollback considerations.

## Banking Payments Checklist

- Preserve idempotency keys for payment initiation and confirmation paths.
- Validate amounts, currency, beneficiary identifiers, limits, and customer authorization.
- Use explicit error handling for payment pending, failed, rejected, timeout, duplicate, and reversal states.
- Avoid logging sensitive account, customer, QR, token, or authorization data.
- Ensure changes are observable through metrics, logs, traces, and audit events.

## Guardrails

- Do not add application code before intent, spec, review, and traceability gates are complete.
- Do not bypass failing tests, SonarCloud gates, or required reviews.
- Do not introduce unapproved dependencies or payment behavior changes.
- Keep generated code understandable and maintainable by human engineers.

## Human Gate

Developer work must go through pull request review with required product, architecture, QA, and security approvals as applicable.
