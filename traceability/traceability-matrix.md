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

## Capability: QR Refund

Traceability ID: TRACE-QRREF-001

Source artifacts:

- Intent: `domains/payments/capabilities/qr-refund/intent/intent.md`
- Specification: `domains/payments/capabilities/qr-refund/specs/spec.md`
- Architecture context: `domains/payments/capabilities/qr-refund/context/context.md`
- API contract: `domains/payments/capabilities/qr-refund/contracts/openapi.yaml`
- Acceptance tests: `domains/payments/capabilities/qr-refund/tests/acceptance.feature`

### Intent To Functional Requirements

| Intent | Jira | Outcome / Scope | Functional Requirements | Status | Owner |
| --- | --- | --- | --- | --- | --- |
| INT-QRREF-001 | JIRA-QRREF-001 | Full refunds for completed KHQR payments | FR-QRREF-001, FR-QRREF-002, FR-QRREF-003, FR-QRREF-004 | Ready | Product Owner |
| INT-QRREF-001 | JIRA-QRREF-001 | Merchant and operations initiation | FR-QRREF-001, FR-QRREF-002, FR-QRREF-012, FR-QRREF-014 | Ready | Product Owner / Operations Lead |
| INT-QRREF-001 | JIRA-QRREF-001 | Duplicate refund prevention | FR-QRREF-004, FR-QRREF-009, FR-QRREF-010 | Ready | Payments Architect |
| INT-QRREF-001 | JIRA-QRREF-001 | 30-day refund window | FR-QRREF-005, FR-QRREF-012 | Ready | Product Owner |
| INT-QRREF-001 | JIRA-QRREF-001 | Suspended merchant blocking | FR-QRREF-007, FR-QRREF-012 | Ready with open override-policy question | Security and Risk Lead |
| INT-QRREF-001 | JIRA-QRREF-001 | High-value manual review | FR-QRREF-011 | Ready with configuration open | Product Owner / Risk Lead |
| INT-QRREF-001 | JIRA-QRREF-001 | Customer notification | FR-QRREF-015 | Ready with notification-template open | Product Owner |
| INT-QRREF-001 | JIRA-QRREF-001 | Status tracking, reporting, audit, reconciliation | FR-QRREF-016, FR-QRREF-017, FR-QRREF-018, FR-QRREF-019, FR-QRREF-020 | Ready with reporting/reconciliation open | Operations Lead / Finance Lead |

### Functional Requirements To APIs And Acceptance Tests

| Requirement | Jira | API Operations | Acceptance Scenarios | Coverage | Notes |
| --- | --- | --- | --- | --- | --- |
| FR-QRREF-001 Merchant full refund | JIRA-QRREF-020 | `POST /qr-refunds` | Successful merchant full refund | Covered | Merchant ownership covered in scenario and API description. |
| FR-QRREF-002 Operations full refund | JIRA-QRREF-021 | `POST /operations/qr-refunds` | Successful operations full refund creation; Reject operations full refund creation without entitlement | Covered | Covers operations create happy path and entitlement rejection. |
| FR-QRREF-003 Completed-payment-only rule | JIRA-QRREF-022 | `POST /qr-refunds`, `POST /operations/qr-refunds` | Reject refund when original payment is not completed | Covered | Scenario outline covers non-completed statuses. |
| FR-QRREF-004 One full refund per payment | JIRA-QRREF-023 | `POST /qr-refunds`, `POST /operations/qr-refunds` | Prevent duplicate refund for the same original payment | Covered | Also supported by idempotency scenarios. |
| FR-QRREF-005 30-day refund window | JIRA-QRREF-024 | `POST /qr-refunds`, `POST /operations/qr-refunds`, `POST /operations/qr-refunds/{refundId}/overrides` | Reject refund outside the 30-day refund window; Operations override is requested with required controls; Maker-checker approval allows permitted override to continue | Covered | Override eligibility still open. |
| FR-QRREF-006 Refund after merchant settlement | JIRA-QRREF-025 | `POST /qr-refunds`, `POST /operations/qr-refunds` | Allow refund after merchant settlement; Merchant balance availability is not required for MVP refund eligibility | Covered | Acceptance coverage confirms settlement state and merchant balance availability do not block MVP eligibility. |
| FR-QRREF-007 Suspended merchant block | JIRA-QRREF-026 | `POST /qr-refunds`, `POST /operations/qr-refunds/{refundId}/overrides` | Reject refund for suspended merchant | Covered | Override policy remains open. |
| FR-QRREF-008 Reason code required | JIRA-QRREF-027 | `POST /qr-refunds`, `POST /operations/qr-refunds`, override/retry commands | Successful merchant full refund; Successful operations full refund creation; Reject refund request with missing or invalid reason code | Covered | Positive and negative reason-code coverage exists. |
| FR-QRREF-009 Idempotency required | JIRA-QRREF-028 | All command APIs with `Idempotency-Key` | Successful merchant full refund; Return existing refund for duplicate request with same idempotency key and payload; Reject refund initiation without idempotency key | Covered | Missing-key and duplicate-key behavior covered. |
| FR-QRREF-010 Idempotency conflict | JIRA-QRREF-029 | All command APIs with `409 Conflict` | Reject duplicate idempotency key with conflicting payload | Covered | Stable error codes still pending. |
| FR-QRREF-011 High-value manual review | JIRA-QRREF-030 | `POST /qr-refunds`, `POST /operations/qr-refunds`, review metadata in `Refund` | Route high-value refund to manual review | Covered with open design | Final review state model remains architecture decision. |
| FR-QRREF-012 Operations override | JIRA-QRREF-031 | `POST /operations/qr-refunds/{refundId}/overrides`, `POST /operations/qr-refunds/{refundId}/overrides/{overrideId}/decision` | Operations override is requested with required controls; Reject override for a control not approved for override; Maker-checker approval allows permitted override to continue; Reject override approval when maker and checker are the same user | Covered | Final overrideable control list still requires product, risk, and operations approval. |
| FR-QRREF-013 Failed refund exception queue | JIRA-QRREF-032 | `POST /operations/qr-refunds/{refundId}/retry`, status `failed` | Retry failed refund from operations exception queue | Partial | API lacks queue list/read operation. |
| FR-QRREF-014 Retry failed refund | JIRA-QRREF-033 | `POST /operations/qr-refunds/{refundId}/retry` | Retry failed refund from operations exception queue | Covered | Retry limits/intervals open. |
| FR-QRREF-015 Customer notification | JIRA-QRREF-034 | Notification event integration not in OpenAPI | Failed notification handling does not change authoritative refund outcome | Partial | API does not define notification event contract. |
| FR-QRREF-016 Refund status tracking | JIRA-QRREF-035 | `GET /qr-refunds/{refundId}` | Merchant retrieves refund status for own refund; Merchant cannot retrieve another merchant's refund status | Covered | Operations status scenario not explicit. |
| FR-QRREF-017 Separate refund references | JIRA-QRREF-036 | `Refund.refundId`, `Refund.processorRefundReference`, `Refund.ledgerReference` | Successful merchant full refund; End-of-day reconciliation scenarios | Partial | Processor/ledger references nullable in API. |
| FR-QRREF-018 End-of-day reconciliation | JIRA-QRREF-037 | Reconciliation feed/extract not in OpenAPI | End-of-day reconciliation identifies matched refund records; End-of-day reconciliation identifies mismatch for investigation | Partial | API contract does not define reconciliation feed. |
| FR-QRREF-019 Reporting data | JIRA-QRREF-038 | Reporting feed/list API not defined | Coverage gap | Gap | No acceptance scenario or API operation for report data. |
| FR-QRREF-020 Audit events | JIRA-QRREF-039 | `AuditSummary` in responses; audit integration not in OpenAPI | Audit event is created for material refund event | Covered with API gap | Audit event contract not fully defined in OpenAPI. |

### Business Rules To Acceptance Tests

| Business Rule | Requirement Links | Acceptance Scenarios | Coverage |
| --- | --- | --- | --- |
| BR-QRREF-001 One full refund per completed KHQR payment | FR-QRREF-003, FR-QRREF-004 | Prevent duplicate refund for the same original payment; Reject refund when original payment is not completed | Covered |
| BR-QRREF-002 Original payment must be `Completed` | FR-QRREF-003 | Reject refund when original payment is not completed | Covered |
| BR-QRREF-003 30 calendar day refund window unless authorized override applies | FR-QRREF-005, FR-QRREF-012 | Reject refund outside the 30-day refund window; Operations override is requested with required controls; Maker-checker approval allows permitted override to continue | Covered |
| BR-QRREF-004 Refunds allowed after merchant settlement | FR-QRREF-006 | Allow refund after merchant settlement | Covered |
| BR-QRREF-005 Merchant balance availability not required for MVP | FR-QRREF-006 | Merchant balance availability is not required for MVP refund eligibility | Covered |
| BR-QRREF-006 Suspended merchants blocked unless policy allows authorized operations override | FR-QRREF-007, FR-QRREF-012 | Reject refund for suspended merchant; Operations override scenarios | Covered with policy open |
| BR-QRREF-007 High-value refunds require manual review | FR-QRREF-011 | Route high-value refund to manual review | Covered with configuration open |
| BR-QRREF-008 Refund reason codes required | FR-QRREF-008, FR-QRREF-012 | Successful merchant full refund; Successful operations full refund creation; Reject refund request with missing or invalid reason code; Operations override is requested with required controls; Retry failed refund from operations exception queue | Covered |
| BR-QRREF-009 Refund APIs must be idempotent | FR-QRREF-009, FR-QRREF-010 | Return existing refund for duplicate request with same idempotency key and payload; Reject duplicate idempotency key with conflicting payload | Covered |

### NFRs To Validation Requirements

| NFR | Jira | Validation Requirement | Acceptance / Evidence Placeholder | Status |
| --- | --- | --- | --- | --- |
| NFR-QRREF-001 Processing time | JIRA-QRREF-040 | Validate 95% successful refunds complete within 60 seconds under approved MVP volume. | VAL-QRREF-PERF-001 | Blocked by MVP volume assumption |
| NFR-QRREF-002 Availability | JIRA-QRREF-041 | Validate design and operational readiness for 99.9% refund initiation/status availability. | VAL-QRREF-OPS-001 | Pending |
| NFR-QRREF-003 Maximum non-terminal duration | JIRA-QRREF-042 | Validate refunds in `requested` or `processing` beyond 24 hours become operations-visible and alerted. | Processor timeout; Ledger timeout | Covered by scenarios |
| NFR-QRREF-004 Observability | JIRA-QRREF-043 | Validate metrics/logs/traces/alerts for refund initiation, rejection, failure, retry, override, high-value review, notification failure, and reconciliation mismatch. | VAL-QRREF-OBS-001 | Pending detailed validation |
| NFR-QRREF-005 Idempotency/concurrency | JIRA-QRREF-044 | Validate duplicate requests and concurrent same-payment submissions cannot create duplicate refunds. | Duplicate refund, idempotency, missing idempotency key, and concurrent same-payment scenarios | Covered by acceptance design |
| NFR-QRREF-006 Audit completeness | JIRA-QRREF-045 | Validate 100% material refund events have immutable audit records. | Audit event scenario outline | Covered by acceptance design |
| NFR-QRREF-007 Sensitive-data protection | JIRA-QRREF-046 | Validate masking in logs, reports, notifications, operations views, and merchant responses. | Status inquiry and notification scenarios | Partial; security validation needed |
| NFR-QRREF-008 Safe degradation | JIRA-QRREF-047 | Validate processor, ledger, notification, audit, and reconciliation failures do not create duplicate or untraceable refund states. | Processor timeout; Ledger timeout; Failed notification handling; Audit failure prevents unaudited material refund state change | Partial; reconciliation feed failure test still needed |
| NFR-QRREF-009 Retention | JIRA-QRREF-048 | Validate refund/audit records meet approved retention policy. | VAL-QRREF-COMP-001 | Blocked by retention open question |

### Architecture Decisions To Components

| Architecture Decision | Component(s) Affected | Related Requirements | Status |
| --- | --- | --- | --- |
| ADR-QRREF-001 Accounting treatment and settlement adjustment | QR Refund Orchestrator, Ledger/Core Banking, Reconciliation Data Publisher | FR-QRREF-006, FR-QRREF-018, NFR-QRREF-008 | Required before implementation |
| ADR-QRREF-002 Refund state ownership and payment-state relationship | QR Refund Orchestrator, Refund State Store, KHQR Payment Service | FR-QRREF-003, FR-QRREF-004, FR-QRREF-016 | Required before API finalization / implementation |
| ADR-QRREF-003 Idempotency and concurrency boundary | Idempotency Store, Refund State Store, QR Refund Orchestrator | FR-QRREF-004, FR-QRREF-009, FR-QRREF-010, NFR-QRREF-005 | Required before implementation |
| ADR-QRREF-004 High-value manual review state model | Refund Eligibility Validator, Override Approval Control, Refund State Store | FR-QRREF-011, FR-QRREF-012 | Required before test finalization |
| ADR-QRREF-005 Retry and exception queue design | Exception Queue Publisher, QR Refund Orchestrator, Refund State Store | FR-QRREF-013, FR-QRREF-014, NFR-QRREF-008 | Required before validation design |
| ADR-QRREF-006 Safe degradation behavior | QR Refund Orchestrator, Payment Processor integration, Ledger/Core Banking integration, Notification Service integration, Audit Event Producer | NFR-QRREF-008 | Required before implementation |
| ADR-QRREF-007 Reconciliation mismatch handling | Reconciliation Data Publisher, Reconciliation Platform, Operations Portal | FR-QRREF-018 | Required before release readiness |
| ADR-QRREF-008 Reporting data delivery model | Reconciliation Data Publisher, Reporting Platform, Refund State Store | FR-QRREF-019 | Required before release readiness |

### Open Questions To Architecture Decisions Required

| Open Question | Jira | Linked Decision / Artifact | Impact | Status |
| --- | --- | --- | --- | --- |
| Regulatory retention period for refund evidence and audit records | JIRA-QRREF-008 | NFR-QRREF-009; Compliance architecture input | Blocks final retention validation | Open |
| Reconciliation mismatch handling workflow | JIRA-QRREF-009 | ADR-QRREF-007 | Blocks final reconciliation flow and tests | Open |
| Reporting platform or extract mechanism | JIRA-QRREF-010 | ADR-QRREF-008 | Blocks report API/feed design and tests | Open |
| MVP refund volume assumptions | JIRA-QRREF-011 | NFR-QRREF-001; capacity validation | Blocks performance validation | Open |
| Customer notification templates and channels | JIRA-QRREF-012 | Notification Service integration | Blocks final notification acceptance criteria | Open |
| High-value thresholds and review queues | JIRA-QRREF-013 | ADR-QRREF-004 | Blocks final manual review configuration | Open |
| Rejected refund notifications | JIRA-QRREF-014 | FR-QRREF-015 | Clarifies notification scope | Open |
| Overrideable vs non-overrideable controls | JIRA-QRREF-015 | ADR-QRREF-004; OverrideControl enum | Blocks final override policy | Open |

### API Coverage

| API Operation | Requirement Coverage | Acceptance Coverage | Status |
| --- | --- | --- | --- |
| `POST /qr-refunds` | FR-QRREF-001, FR-QRREF-003, FR-QRREF-004, FR-QRREF-005, FR-QRREF-007, FR-QRREF-008, FR-QRREF-009, FR-QRREF-010, FR-QRREF-011, FR-QRREF-020 | Merchant success, non-completed rejection, duplicate prevention, idempotency, 30-day window, suspended merchant, high-value review, audit | Covered |
| `GET /qr-refunds/{refundId}` | FR-QRREF-016, NFR-QRREF-007 | Merchant retrieves own refund; Merchant cannot retrieve another merchant's refund | Covered |
| `POST /operations/qr-refunds` | FR-QRREF-002, FR-QRREF-008, FR-QRREF-009, FR-QRREF-010, FR-QRREF-020 | Successful operations full refund creation; Reject operations full refund creation without entitlement | Covered |
| `POST /operations/qr-refunds/{refundId}/overrides` | FR-QRREF-012, FR-QRREF-020 | Operations override is requested with required controls | Covered |
| `POST /operations/qr-refunds/{refundId}/overrides/{overrideId}/decision` | FR-QRREF-012, FR-QRREF-020 | Maker-checker approval allows permitted override; Reject override approval when maker/checker same user | Covered |
| `POST /operations/qr-refunds/{refundId}/retry` | FR-QRREF-014, FR-QRREF-020, NFR-QRREF-008 | Retry failed refund from operations exception queue | Covered |

### Orphans And Coverage Gaps

| Type | Item | Finding | Recommended Resolution |
| --- | --- | --- | --- |
| Resolved coverage gap | FR-QRREF-006 | Requirement now has acceptance coverage for post-settlement eligibility and merchant balance not being an MVP blocker. | No further test correction required before implementation. |
| Orphan requirement | FR-QRREF-019 | Requirement has no API/feed contract and no acceptance scenario. | Define reporting as API, extract/feed, or explicit out-of-contract integration; add scenario. |
| Resolved coverage gap | `POST /operations/qr-refunds` | Operation now has acceptance coverage for operations-created refund and entitlement rejection. | No further test correction required before implementation. |
| Resolved coverage gap | FR-QRREF-008 | Requirement now has negative acceptance coverage for missing and invalid reason codes. | No further test correction required before implementation. |
| Resolved coverage gap | FR-QRREF-009 | Requirement now has missing idempotency key acceptance coverage. | No further test correction required before implementation. |
| Resolved coverage gap | NFR-QRREF-005 | Concurrent same-payment refund race is now covered by acceptance design. | Implementation must prove the concurrency control. |
| Resolved coverage gap | FR-QRREF-012 | Non-approved override control rejection is now covered by acceptance design. | Final overrideable control list still requires product, risk, and operations approval. |
| Resolved coverage gap | FR-QRREF-020 / NFR-QRREF-008 | Audit failure behavior is now covered at acceptance level. | Implementation plan selects durable transactional audit outbox as the MVP reliability pattern; full audit event contract remains internal/out-of-contract unless separately approved. |
| Partial API coverage | FR-QRREF-013 | Retry flow references exception queue, but API has no exception queue list/read operation. | Decide whether exception queue is outside API contract or add operation. |
| Partial API coverage | FR-QRREF-015 | Notification behavior covered by scenario but no event contract. | Document notification event as out-of-contract or add event schema. |
| Partial API coverage | FR-QRREF-018 | Reconciliation scenarios exist, but no reconciliation feed/extract contract. | Document feed as out-of-contract or add contract. |
| Partial API coverage | FR-QRREF-020 | Audit scenario exists, but OpenAPI only exposes `AuditSummary`; no full audit event contract. | Add audit event schema or mark audit integration as internal/out-of-contract. |
| Open design gap | ADR-QRREF-001 | Accounting/settlement adjustment unresolved. | Resolve before implementation. |
| Open design gap | ADR-QRREF-003 | Idempotency and concurrency boundary unresolved. | Resolve before implementation. |
| Open design gap | ADR-QRREF-004 | High-value review state model unresolved. | Resolve before final API/test baseline. |
| Open compliance gap | JIRA-QRREF-008 | Retention policy unresolved. | Resolve before implementation if persistence design depends on retention controls; otherwise resolve before release readiness. |

### Traceability Approval Gates

| Gate | Jira Placeholder | Required Approver | Status |
| --- | --- | --- | --- |
| Traceability review | JIRA-QRREF-070 | BA / Architect / QA Lead | Pending |
| API coverage review | JIRA-QRREF-071 | API Architect | Pending |
| Test coverage review | JIRA-QRREF-072 | QA Lead | Pending |
| Security coverage review | JIRA-QRREF-073 | Security Architect | Pending |
