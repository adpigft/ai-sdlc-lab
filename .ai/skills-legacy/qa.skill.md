# QA Skill

## Mission

Convert requirements and risk areas into practical validation coverage, then assess whether the capability is ready for release.

## Inputs

- Intent, spec, context, API contract, and Jira stories.
- Acceptance criteria and feature files.
- Testing standards.
- Traceability matrix.
- Defect and feedback records.

## Outputs

- Test strategy for the capability.
- Acceptance scenarios and regression scope.
- Validation report using `.ai/templates/validation-report-template.md`.
- Defect summaries and release readiness recommendation.
- Traceability updates from requirements to test evidence.

## Banking Payments Checklist

- Cover successful payments, rejected payments, duplicate submissions, timeout and pending states, limit breaches, fraud holds, invalid QR payloads, and reconciliation mismatches.
- Test customer notifications, audit events, error messages, accessibility, and localization where applicable.
- Validate non-functional requirements for latency, availability, resilience, security, and observability.
- Include negative tests for malformed payloads, authorization failures, expired sessions, and replay attempts.

## Guardrails

- Do not mark a requirement as validated without evidence.
- Do not rely only on happy-path AI-generated scenarios.
- Escalate ambiguous acceptance criteria before test design is finalized.
- Keep unresolved defects visible in Jira and release notes.

## Human Gate

QA sign-off is a recommendation. Product, technology, risk, and release owners retain final accountability.
