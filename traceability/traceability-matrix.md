# Traceability Matrix

This matrix links business intent to Jira, specification, tests, validation, release evidence, and feedback. It should be updated whenever a material artifact changes.

## Status Legend

- `Draft`: artifact exists but is not approved.
- `Ready`: reviewed and approved for the next lifecycle stage.
- `Validated`: test or review evidence exists.
- `Released`: included in a release with approval evidence.
- `Blocked`: missing mandatory evidence or approval.

## Capability: KHQR Payment

| Intent | Jira | Requirement | Spec | API | Test | Validation | Release | Feedback | Status | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| INT-KHQR-001 | PAY-EPIC-001 | FR-001 Customer initiates KHQR payment from mobile banking | `domains/payments/capabilities/khqr-payment/specs/spec.md` | `domains/payments/capabilities/khqr-payment/contracts/openapi.yaml` | `domains/payments/capabilities/khqr-payment/tests/acceptance.feature` | `domains/payments/capabilities/khqr-payment/validation/validation-report.md` | `domains/payments/capabilities/khqr-payment/release/release-notes.md` | `feedback/feedback-log.md` | Draft | Product owner |
| INT-KHQR-001 | PAY-EPIC-001 | BR-001 Duplicate submissions must not create duplicate payments | `domains/payments/capabilities/khqr-payment/specs/spec.md` | `domains/payments/capabilities/khqr-payment/contracts/openapi.yaml` | `domains/payments/capabilities/khqr-payment/tests/acceptance.feature` | `domains/payments/capabilities/khqr-payment/validation/validation-report.md` | `domains/payments/capabilities/khqr-payment/release/release-notes.md` | `feedback/feedback-log.md` | Draft | Architect |
| INT-KHQR-001 | PAY-EPIC-001 | NFR-001 Payment flow must be observable and auditable | `domains/payments/capabilities/khqr-payment/specs/spec.md` | `domains/payments/capabilities/khqr-payment/contracts/openapi.yaml` | `domains/payments/capabilities/khqr-payment/tests/acceptance.feature` | `domains/payments/capabilities/khqr-payment/validation/validation-report.md` | `domains/payments/capabilities/khqr-payment/release/release-notes.md` | `feedback/feedback-log.md` | Draft | DevSecOps |

## Required Checks Before Build

- Every `Must` requirement has a Jira reference.
- Every requirement has acceptance criteria or a documented review control.
- Every API operation maps to at least one requirement.
- Every human gate has an approval reference.
- Every unresolved risk has an owner and target decision date.

## Required Checks Before Release

- GitHub Actions evidence is linked.
- SonarCloud quality gate is linked.
- Validation report covers all mandatory requirements.
- Release notes list unresolved defects and accepted risks.
- Feedback capture path is ready for post-release observations.
