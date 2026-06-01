# Traceability Matrix

This matrix links KHQR business intent to Jira, Confluence, specification, API contract, acceptance tests, validation evidence, release evidence, and feedback. It should be updated whenever a material artifact changes.

## Status Legend

- `Draft`: artifact exists but is not approved.
- `Ready`: reviewed and approved for the next lifecycle stage.
- `Validated`: test or review evidence exists.
- `Released`: included in a release with approval evidence.
- `Blocked`: missing mandatory evidence or approval.

## Capability: KHQR Payment

Traceability ID: TRACE-KHQR-001

| Intent | Jira | Confluence | Requirement | Spec | API | Acceptance Scenario | Validation | Release | Feedback | Status | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| INT-KHQR-001 | JIRA-KHQR-010 | CONF-PAY-KHQR-SPEC | FR-KHQR-001 Validate QR payload before payment creation | `domains/payments/capabilities/khqr-payment/specs/spec.md` | `POST /khqr/payments` | Reject malformed KHQR payload before payment creation | VAL-KHQR-001 / TEST-KHQR-001 | REL-KHQR-001 | FB-KHQR-003 | Draft | Product Owner |
| INT-KHQR-001 | JIRA-KHQR-011 | CONF-PAY-KHQR-SPEC | FR-KHQR-002 Display confirmation details | `domains/payments/capabilities/khqr-payment/specs/spec.md` | `POST /khqr/payments` | Display confirmation details before payment submission | VAL-KHQR-001 / TEST-KHQR-002 | REL-KHQR-001 | FB-KHQR-004 | Draft | Product Owner |
| INT-KHQR-001 | JIRA-KHQR-012 | CONF-PAY-KHQR-SPEC | FR-KHQR-003 Verify funding account authorization | `domains/payments/capabilities/khqr-payment/specs/spec.md` | `POST /khqr/payments` | Reject payment from an unauthorized funding account | VAL-KHQR-001 / TEST-KHQR-003 | REL-KHQR-001 | FB-KHQR-005 | Draft | Security and Risk Lead |
| INT-KHQR-001 | JIRA-KHQR-013 | CONF-PAY-KHQR-SPEC | FR-KHQR-004 Enforce transaction and customer limits | `domains/payments/capabilities/khqr-payment/specs/spec.md` | `POST /khqr/payments` | Reject payment that breaches transaction limit | VAL-KHQR-001 / TEST-KHQR-004 | REL-KHQR-001 | FB-KHQR-006 | Draft | Product Owner |
| INT-KHQR-001 | JIRA-KHQR-014 | CONF-PAY-KHQR-SPEC | FR-KHQR-005 Require idempotency key | `domains/payments/capabilities/khqr-payment/specs/spec.md` | `POST /khqr/payments` | Require idempotency key for initiation | VAL-KHQR-001 / TEST-KHQR-005 | REL-KHQR-001 | FB-KHQR-001 | Draft | Payments Architect |
| INT-KHQR-001 | JIRA-KHQR-015 | CONF-PAY-KHQR-SPEC | FR-KHQR-006 Prevent duplicate execution for same key and payload | `domains/payments/capabilities/khqr-payment/specs/spec.md` | `POST /khqr/payments` | Return original payment for duplicate request with same idempotency key | VAL-KHQR-001 / TEST-KHQR-006 | REL-KHQR-001 | FB-KHQR-001 | Draft | Payments Architect |
| INT-KHQR-001 | JIRA-KHQR-016 | CONF-PAY-KHQR-SPEC | FR-KHQR-007 Reject duplicate key with conflicting payload | `domains/payments/capabilities/khqr-payment/specs/spec.md` | `POST /khqr/payments` | Reject duplicate idempotency key with conflicting payload | VAL-KHQR-001 / TEST-KHQR-007 | REL-KHQR-001 | FB-KHQR-001 | Draft | Payments Architect |
| INT-KHQR-001 | JIRA-KHQR-017 | CONF-PAY-KHQR-CONTROLS | FR-KHQR-008 Submit eligible instructions to fraud and sanctions screening | `domains/payments/capabilities/khqr-payment/specs/spec.md` | `POST /khqr/payments` | Hold payment when fraud screening requires review | VAL-KHQR-001 / TEST-KHQR-008 | REL-KHQR-001 | FB-KHQR-007 | Draft | Security and Risk Lead |
| INT-KHQR-001 | JIRA-KHQR-018 | CONF-PAY-KHQR-SPEC | FR-KHQR-009 Support asynchronous pending status | `domains/payments/capabilities/khqr-payment/specs/spec.md` | `POST /khqr/payments`, `GET /khqr/payments/{paymentId}` | Return pending status when processor outcome is delayed | VAL-KHQR-001 / TEST-KHQR-009 | REL-KHQR-001 | FB-KHQR-008 | Draft | Payments Architect |
| INT-KHQR-001 | JIRA-KHQR-019 | CONF-PAY-KHQR-SPEC | FR-KHQR-010 Provide customer-owned payment status inquiry | `domains/payments/capabilities/khqr-payment/specs/spec.md` | `GET /khqr/payments/{paymentId}` | Customer retrieves own status; customer cannot retrieve another customer's status | VAL-KHQR-001 / TEST-KHQR-010 | REL-KHQR-001 | FB-KHQR-009 | Draft | Product Owner |
| INT-KHQR-001 | JIRA-KHQR-020 | CONF-PAY-KHQR-SPEC | FR-KHQR-011 Emit customer notifications for final outcomes where configured | `domains/payments/capabilities/khqr-payment/specs/spec.md` | Event or notification integration pending | Planned notification validation | VAL-KHQR-001 / TEST-KHQR-011 | REL-KHQR-001 | FB-KHQR-010 | Draft | Product Owner |
| INT-KHQR-001 | JIRA-KHQR-021 | CONF-PAY-KHQR-CONTROLS | FR-KHQR-012 Create audit events for material state changes | `domains/payments/capabilities/khqr-payment/specs/spec.md` | `POST /khqr/payments`, `GET /khqr/payments/{paymentId}` | Audit all terminal payment outcomes | VAL-KHQR-001 / TEST-KHQR-012 | REL-KHQR-001 | FB-KHQR-011 | Draft | Operations Lead |
| INT-KHQR-001 | JIRA-KHQR-030 | CONF-PAY-KHQR-SPEC | NFR-KHQR-001 Meet approved initiation latency target | `domains/payments/capabilities/khqr-payment/specs/spec.md` | `POST /khqr/payments` | Performance test pending | VAL-KHQR-001 | REL-KHQR-001 | FB-KHQR-012 | Blocked | Payments Architect |
| INT-KHQR-001 | JIRA-KHQR-031 | CONF-PAY-KHQR-RUNBOOK | NFR-KHQR-002 Provide observability | `domains/payments/capabilities/khqr-payment/specs/spec.md` | All operations | Operational readiness validation pending | VAL-KHQR-001 / OPS-KHQR-001 | REL-KHQR-001 | FB-KHQR-013 | Draft | DevSecOps Lead |
| INT-KHQR-001 | JIRA-KHQR-032 | CONF-PAY-KHQR-CONTROLS | NFR-KHQR-003 Protect sensitive data | `domains/payments/capabilities/khqr-payment/specs/spec.md` | All operations | Security validation pending | VAL-KHQR-001 / SEC-KHQR-001 | REL-KHQR-001 | FB-KHQR-014 | Draft | Security and Risk Lead |
| INT-KHQR-001 | JIRA-KHQR-033 | CONF-PAY-KHQR-SPEC | NFR-KHQR-004 Resilient to retries and network loss | `domains/payments/capabilities/khqr-payment/specs/spec.md` | `POST /khqr/payments` | Duplicate and pending scenarios | VAL-KHQR-001 | REL-KHQR-001 | FB-KHQR-001 | Draft | Payments Architect |
| INT-KHQR-001 | JIRA-KHQR-034 | CONF-PAY-KHQR-RUNBOOK | NFR-KHQR-005 Support reconciliation | `domains/payments/capabilities/khqr-payment/specs/spec.md` | All operations | Operations validation pending | VAL-KHQR-001 / OPS-KHQR-002 | REL-KHQR-001 | FB-KHQR-015 | Draft | Operations Lead |
| INT-KHQR-001 | JIRA-KHQR-035 | CONF-PAY-KHQR-VALIDATION | NFR-KHQR-006 Require GitHub Actions and SonarCloud gates before release | `domains/payments/capabilities/khqr-payment/specs/spec.md` | N/A | CI evidence pending | VAL-KHQR-001 / GHA-KHQR-001 / SONAR-KHQR-001 | REL-KHQR-001 | FB-KHQR-002 | Blocked | DevSecOps Lead |

## Human Approval Gates

| Gate | Jira Placeholder | Artifact | Required Approver | Status |
| --- | --- | --- | --- | --- |
| Intent approval | JIRA-KHQR-001 | `intent/intent.md` | Product Owner | Pending |
| Architecture feasibility approval | JIRA-KHQR-002 | `context/context.md` | Payments Architect | Pending |
| QA acceptance review | JIRA-KHQR-003 | `tests/acceptance.feature` | QA Lead | Pending |
| Security and risk approval | JIRA-KHQR-004 | `context/context.md`, `specs/spec.md` | Security and Risk Lead | Pending |
| Operations readiness input | JIRA-KHQR-005 | `context/context.md`, `release/release-notes.md` | Operations Lead | Pending |
| Release approval | JIRA-KHQR-006 | `release/release-notes.md` | Release Manager | Pending |
| Specification approval | JIRA-KHQR-050 | `specs/spec.md` | Product Owner | Pending |
| Validation sign-off | JIRA-KHQR-080 | `validation/validation-report.md` | QA Lead | Pending |
| Change approval | CHG-KHQR-001 | `release/release-notes.md` | Release Manager | Pending |

## Required Checks Before Build

- Every `Must` requirement has a Jira reference.
- Every requirement has acceptance criteria or a documented review control.
- Every API operation maps to at least one requirement.
- Every human gate has an approval reference.
- Every unresolved risk has an owner and target decision date.
- Open questions in the intent, context, and spec have owners.

## Required Checks Before Release

- GitHub Actions evidence is linked.
- SonarCloud quality gate is linked.
- Validation report covers all mandatory requirements.
- Release notes list unresolved defects and accepted risks.
- Confluence placeholders are replaced with actual page links.
- Feedback capture path is ready for post-release observations.
