# Traceability Matrix

This matrix links KHQR business intent to Jira, Confluence, requirements, API contract, acceptance tests, validation evidence, release evidence, and feedback. It should be updated whenever a material artifact changes.

## Status Legend

- `Draft`: artifact exists but is not approved.
- `Ready`: reviewed and approved for the next lifecycle stage.
- `Validated`: test or review evidence exists.
- `Released`: included in a release with approval evidence.
- `Blocked`: missing mandatory evidence or approval.

## Capability: KHQR Payment

Traceability ID: TRACE-KHQR-001

| Intent | Jira | Confluence | Requirement | Requirements | API | Acceptance Scenario | Validation | Release | Feedback | Status | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| INT-KHQR-001 | JIRA-KHQR-010 | CONF-PAY-KHQR-SPEC | FR-KHQR-001 Validate QR payload before payment creation | `domains/payments/capabilities/payment-initiation/features/khqr-payment/requirements/requirements.md` | `POST /khqr/payments` | Reject malformed KHQR payload before payment creation | VAL-KHQR-001 / TEST-KHQR-001 | REL-KHQR-001 | FB-KHQR-003 | Draft | Product Owner |
| INT-KHQR-001 | JIRA-KHQR-011 | CONF-PAY-KHQR-SPEC | FR-KHQR-002 Display confirmation details | `domains/payments/capabilities/payment-initiation/features/khqr-payment/requirements/requirements.md` | `POST /khqr/payments` | Display confirmation details before payment submission | VAL-KHQR-001 / TEST-KHQR-002 | REL-KHQR-001 | FB-KHQR-004 | Draft | Product Owner |
| INT-KHQR-001 | JIRA-KHQR-012 | CONF-PAY-KHQR-SPEC | FR-KHQR-003 Verify funding account authorization | `domains/payments/capabilities/payment-initiation/features/khqr-payment/requirements/requirements.md` | `POST /khqr/payments` | Reject payment from an unauthorized funding account | VAL-KHQR-001 / TEST-KHQR-003 | REL-KHQR-001 | FB-KHQR-005 | Draft | Security and Risk Lead |
| INT-KHQR-001 | JIRA-KHQR-013 | CONF-PAY-KHQR-SPEC | FR-KHQR-004 Enforce transaction and customer limits | `domains/payments/capabilities/payment-initiation/features/khqr-payment/requirements/requirements.md` | `POST /khqr/payments` | Reject payment that breaches transaction limit | VAL-KHQR-001 / TEST-KHQR-004 | REL-KHQR-001 | FB-KHQR-006 | Draft | Product Owner |
| INT-KHQR-001 | JIRA-KHQR-014 | CONF-PAY-KHQR-SPEC | FR-KHQR-005 Require idempotency key | `domains/payments/capabilities/payment-initiation/features/khqr-payment/requirements/requirements.md` | `POST /khqr/payments` | Require idempotency key for initiation | VAL-KHQR-001 / TEST-KHQR-005 | REL-KHQR-001 | FB-KHQR-001 | Draft | Payments Architect |
| INT-KHQR-001 | JIRA-KHQR-015 | CONF-PAY-KHQR-SPEC | FR-KHQR-006 Prevent duplicate execution for same key and payload | `domains/payments/capabilities/payment-initiation/features/khqr-payment/requirements/requirements.md` | `POST /khqr/payments` | Return original payment for duplicate request with same idempotency key | VAL-KHQR-001 / TEST-KHQR-006 | REL-KHQR-001 | FB-KHQR-001 | Draft | Payments Architect |
| INT-KHQR-001 | JIRA-KHQR-016 | CONF-PAY-KHQR-SPEC | FR-KHQR-007 Reject duplicate key with conflicting payload | `domains/payments/capabilities/payment-initiation/features/khqr-payment/requirements/requirements.md` | `POST /khqr/payments` | Reject duplicate idempotency key with conflicting payload | VAL-KHQR-001 / TEST-KHQR-007 | REL-KHQR-001 | FB-KHQR-001 | Draft | Payments Architect |
| INT-KHQR-001 | JIRA-KHQR-017 | CONF-PAY-KHQR-CONTROLS | FR-KHQR-008 Submit eligible instructions to fraud and sanctions screening | `domains/payments/capabilities/payment-initiation/features/khqr-payment/requirements/requirements.md` | `POST /khqr/payments` | Hold payment when fraud screening requires review | VAL-KHQR-001 / TEST-KHQR-008 | REL-KHQR-001 | FB-KHQR-007 | Draft | Security and Risk Lead |
| INT-KHQR-001 | JIRA-KHQR-018 | CONF-PAY-KHQR-SPEC | FR-KHQR-009 Support asynchronous pending status | `domains/payments/capabilities/payment-initiation/features/khqr-payment/requirements/requirements.md` | `POST /khqr/payments`, `GET /khqr/payments/{paymentId}` | Return pending status when processor outcome is delayed | VAL-KHQR-001 / TEST-KHQR-009 | REL-KHQR-001 | FB-KHQR-008 | Draft | Payments Architect |
| INT-KHQR-001 | JIRA-KHQR-019 | CONF-PAY-KHQR-SPEC | FR-KHQR-010 Provide customer-owned payment status inquiry | `domains/payments/capabilities/payment-initiation/features/khqr-payment/requirements/requirements.md` | `GET /khqr/payments/{paymentId}` | Customer retrieves own status; customer cannot retrieve another customer's status | VAL-KHQR-001 / TEST-KHQR-010 | REL-KHQR-001 | FB-KHQR-009 | Draft | Product Owner |
| INT-KHQR-001 | JIRA-KHQR-020 | CONF-PAY-KHQR-SPEC | FR-KHQR-011 Emit customer notifications for final outcomes where configured | `domains/payments/capabilities/payment-initiation/features/khqr-payment/requirements/requirements.md` | Event or notification integration pending | Planned notification validation | VAL-KHQR-001 / TEST-KHQR-011 | REL-KHQR-001 | FB-KHQR-010 | Draft | Product Owner |
| INT-KHQR-001 | JIRA-KHQR-021 | CONF-PAY-KHQR-CONTROLS | FR-KHQR-012 Create audit events for material state changes | `domains/payments/capabilities/payment-initiation/features/khqr-payment/requirements/requirements.md` | `POST /khqr/payments`, `GET /khqr/payments/{paymentId}` | Audit all terminal payment outcomes | VAL-KHQR-001 / TEST-KHQR-012 | REL-KHQR-001 | FB-KHQR-011 | Draft | Operations Lead |
| INT-KHQR-001 | JIRA-KHQR-030 | CONF-PAY-KHQR-SPEC | NFR-KHQR-001 Meet approved initiation latency target | `domains/payments/capabilities/payment-initiation/features/khqr-payment/requirements/requirements.md` | `POST /khqr/payments` | Performance test pending | VAL-KHQR-001 | REL-KHQR-001 | FB-KHQR-012 | Blocked | Payments Architect |
| INT-KHQR-001 | JIRA-KHQR-031 | CONF-PAY-KHQR-RUNBOOK | NFR-KHQR-002 Provide observability | `domains/payments/capabilities/payment-initiation/features/khqr-payment/requirements/requirements.md` | All operations | Operational readiness validation pending | VAL-KHQR-001 / OPS-KHQR-001 | REL-KHQR-001 | FB-KHQR-013 | Draft | DevSecOps Lead |
| INT-KHQR-001 | JIRA-KHQR-032 | CONF-PAY-KHQR-CONTROLS | NFR-KHQR-003 Protect sensitive data | `domains/payments/capabilities/payment-initiation/features/khqr-payment/requirements/requirements.md` | All operations | Security validation pending | VAL-KHQR-001 / SEC-KHQR-001 | REL-KHQR-001 | FB-KHQR-014 | Draft | Security and Risk Lead |
| INT-KHQR-001 | JIRA-KHQR-033 | CONF-PAY-KHQR-SPEC | NFR-KHQR-004 Resilient to retries and network loss | `domains/payments/capabilities/payment-initiation/features/khqr-payment/requirements/requirements.md` | `POST /khqr/payments` | Duplicate and pending scenarios | VAL-KHQR-001 | REL-KHQR-001 | FB-KHQR-001 | Draft | Payments Architect |
| INT-KHQR-001 | JIRA-KHQR-034 | CONF-PAY-KHQR-RUNBOOK | NFR-KHQR-005 Support reconciliation | `domains/payments/capabilities/payment-initiation/features/khqr-payment/requirements/requirements.md` | All operations | Operations validation pending | VAL-KHQR-001 / OPS-KHQR-002 | REL-KHQR-001 | FB-KHQR-015 | Draft | Operations Lead |
| INT-KHQR-001 | JIRA-KHQR-035 | CONF-PAY-KHQR-VALIDATION | NFR-KHQR-006 Require GitHub Actions and SonarCloud gates before release | `domains/payments/capabilities/payment-initiation/features/khqr-payment/requirements/requirements.md` | N/A | CI evidence pending | VAL-KHQR-001 / GHA-KHQR-001 / SONAR-KHQR-001 | REL-KHQR-001 | FB-KHQR-002 | Blocked | DevSecOps Lead |

## Human Approval Gates

| Gate | Jira Placeholder | Artifact | Required Approver | Status |
| --- | --- | --- | --- | --- |
| Intent approval | JIRA-KHQR-001 | `intent/intent.md` | Product Owner | Pending |
| Architecture feasibility approval | JIRA-KHQR-002 | `design/design.md` | Payments Architect | Pending |
| QA acceptance review | JIRA-KHQR-003 | `tests/acceptance.feature` | QA Lead | Pending |
| Security and risk approval | JIRA-KHQR-004 | `design/design.md`, `requirements/requirements.md` | Security and Risk Lead | Pending |
| Operations readiness input | JIRA-KHQR-005 | `design/design.md`, `release/release-notes.md` | Operations Lead | Pending |
| Release approval | JIRA-KHQR-006 | `release/release-notes.md` | Release Manager | Pending |
| Requirements approval | JIRA-KHQR-050 | `requirements/requirements.md` | Product Owner | Pending |
| Validation sign-off | JIRA-KHQR-080 | `validation/validation-report.md` | QA Lead | Pending |
| Change approval | CHG-KHQR-001 | `release/release-notes.md` | Release Manager | Pending |

## Required Checks Before Build

- Every `Must` requirement has a Jira reference.
- Every requirement has acceptance criteria or a documented review control.
- Every API operation maps to at least one requirement.
- Every human gate has an approval reference.
- Every unresolved risk has an owner and target decision date.
- Open questions in the intent, context, and requirements have owners.

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

- Intent: `domains/payments/capabilities/payment-refund/features/qr-refund/intent/intent.md`
- Requirements: `domains/payments/capabilities/payment-refund/features/qr-refund/requirements/requirements.md`
- Architecture context: `domains/payments/capabilities/payment-refund/features/qr-refund/design/design.md`
- API contract: `domains/payments/capabilities/payment-refund/features/qr-refund/contracts/openapi.yaml`
- Acceptance tests: `domains/payments/capabilities/payment-refund/features/qr-refund/tests/acceptance.feature`

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
| ADR-QRREF-001 Accounting treatment and settlement adjustment | QR Refund Orchestrator, Ledger/Core Banking, Reconciliation Data Publisher | FR-QRREF-006, FR-QRREF-018, NFR-QRREF-008 | Accepted with conditions; Slice 2 blocked until settlement-adjustment conditions close |
| ADR-QRREF-002 Refund state ownership and payment-state relationship | QR Refund Orchestrator, Refund State Store, KHQR Payment Service | FR-QRREF-003, FR-QRREF-004, FR-QRREF-016 | Required before API finalization / implementation |
| ADR-QRREF-003 Idempotency and concurrency boundary | Idempotency Store, Refund State Store, QR Refund Orchestrator | FR-QRREF-004, FR-QRREF-009, FR-QRREF-010, NFR-QRREF-005 | Accepted with conditions; Slice 2 blocked until processor/ledger conditions close |
| ADR-QRREF-004 High-value manual review state model | Refund Eligibility Validator, Override Approval Control, Refund State Store | FR-QRREF-011, FR-QRREF-012 | Required before test finalization |
| ADR-QRREF-005 Retry and exception queue design | Exception Queue Publisher, QR Refund Orchestrator, Refund State Store | FR-QRREF-013, FR-QRREF-014, NFR-QRREF-008 | Required before validation design |
| ADR-QRREF-006 Safe degradation behavior | QR Refund Orchestrator, Payment Processor integration, Ledger/Core Banking integration, Notification Service integration, Audit Event Producer | NFR-QRREF-008 | Accepted with conditions; Slice 2 blocked until timeout and unresolved-state conditions close |
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

### Implementation Slice Traceability

| Slice | Status | Requirements | APIs / Interfaces | Acceptance / Test Coverage |
| --- | --- | --- | --- | --- |
| Slice 1 - Refund Creation Foundation | Can start now | FR-QRREF-001, FR-QRREF-003, FR-QRREF-004, FR-QRREF-005, FR-QRREF-006, FR-QRREF-007, FR-QRREF-008, FR-QRREF-009, FR-QRREF-010, FR-QRREF-016, FR-QRREF-020, NFR-QRREF-005, NFR-QRREF-006, NFR-QRREF-007 | `POST /qr-refunds`, `GET /qr-refunds/{refundId}`, original payment lookup port, HMAC idempotency hasher, refund creation unit-of-work port, refund repository uniqueness/versioning contract | Successful merchant full refund; non-completed rejection; duplicate prevention; idempotency replay/conflict/missing key; keyed HMAC idempotency hashing; concurrent same-payment submissions; 30-day window rejection; post-settlement eligibility; merchant balance non-blocking; suspended merchant rejection; missing/invalid reason code; merchant status inquiry; audit event creation; audit fail-closed behavior. |
| Slice 2 - Processor and Ledger Integration | Blocked pending ADR/config approval | FR-QRREF-014, FR-QRREF-017, NFR-QRREF-008 | Processor refund port; ledger refund posting port; `POST /qr-refunds`; `POST /operations/qr-refunds`; `POST /operations/qr-refunds/{refundId}/retry` | Processor timeout; ledger timeout; downstream reference capture; integration and failure-mode tests. |
| Slice 3 - Operations Refund and Override | Blocked pending override policy approval | FR-QRREF-002, FR-QRREF-008, FR-QRREF-012, FR-QRREF-020, NFR-QRREF-006, NFR-QRREF-007 | `POST /operations/qr-refunds`; `POST /operations/qr-refunds/{refundId}/overrides`; `POST /operations/qr-refunds/{refundId}/overrides/{overrideId}/decision` | Successful operations full refund creation; entitlement rejection; override request; non-approved override rejection; maker-checker approval; same-user rejection; audit event creation. |
| Slice 4 - Retry and Exception Handling | Starts after Slice 2 | FR-QRREF-013, FR-QRREF-014, FR-QRREF-020, NFR-QRREF-003, NFR-QRREF-008 | `POST /operations/qr-refunds/{refundId}/retry`; failed refund exception queue interface | Retry failed refund from operations exception queue; processor timeout operations visibility; ledger timeout operations visibility; retry audit events. |
| Slice 5 - Reconciliation | Blocked pending reconciliation design | FR-QRREF-018, NFR-QRREF-008 | Reconciliation feed/extract, not currently in OpenAPI | End-of-day reconciliation matched records; end-of-day mismatch for investigation; reconciliation feed failure validation. |
| Slice 6 - Reporting | Future phase / projection seam only | FR-QRREF-019 | Reporting event/interface placeholder only; no reporting API in MVP | Future reporting validation after `ADR-QRREF-008`; no MVP acceptance execution beyond projection seam review. |

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
| Resolved hardening gap | NFR-QRREF-005 / NFR-QRREF-006 / NFR-QRREF-007 | Slice 1 validation found plain SHA-256 idempotency hashing, missing unit-of-work contract, and implicit duplicate-prevention persistence contract. | Slice 1 source now uses keyed HMAC-SHA-256, explicit refund creation unit-of-work port contract, and repository/idempotency/audit port contracts for atomicity, unique original-payment constraint, locking, and optimistic versioning. |
| Partial API coverage | FR-QRREF-013 | Retry flow references exception queue, but API has no exception queue list/read operation. | Decide whether exception queue is outside API contract or add operation. |
| Partial API coverage | FR-QRREF-015 | Notification behavior covered by scenario but no event contract. | Document notification event as out-of-contract or add event schema. |
| Partial API coverage | FR-QRREF-018 | Reconciliation scenarios exist, but no reconciliation feed/extract contract. | Document feed as out-of-contract or add contract. |
| Partial API coverage | FR-QRREF-020 | Audit scenario exists, but OpenAPI only exposes `AuditSummary`; no full audit event contract. | Add audit event schema or mark audit integration as internal/out-of-contract. |
| Conditional approval | ADR-QRREF-001 | Accounting and settlement treatment accepted with conditions, but finance posting rules and completion criteria remain open. | Keep Slice 2 blocked until conditions are closed. |
| Conditional approval | ADR-QRREF-003 | Cross-system idempotency and concurrency accepted with conditions, but processor/ledger client reference and inquiry rules remain open. | Keep Slice 2 blocked until conditions are closed. |
| Conditional approval | ADR-QRREF-006 | Processor and ledger failure behavior accepted with conditions, but timeout mapping and unresolved-state rules remain open. | Keep Slice 2 blocked until conditions are closed. |
| Open design gap | ADR-QRREF-004 | High-value review state model unresolved. | Resolve before final API/test baseline. |
| Open compliance gap | JIRA-QRREF-008 | Retention policy unresolved. | Resolve before implementation if persistence design depends on retention controls; otherwise resolve before release readiness. |

### Traceability Approval Gates

| Gate | Jira Placeholder | Required Approver | Status |
| --- | --- | --- | --- |
| Traceability review | JIRA-QRREF-070 | BA / Architect / QA Lead | Pending |
| API coverage review | JIRA-QRREF-071 | API Architect | Pending |
| Test coverage review | JIRA-QRREF-072 | QA Lead | Pending |
| Security coverage review | JIRA-QRREF-073 | Security Architect | Pending |

## Capability: KHQR Payment Reversal

Traceability ID: TRACE-KHQRREV-001

Source artifacts:

- Intent: `domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/intent/intent.md`
- Requirements: `domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/requirements/requirements.md`
- Architecture context: `domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/design/design.md`
- API contract: `domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/contracts/openapi.yaml`
- Acceptance tests: `domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/tests/acceptance.feature`
- Implementation plan: `domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/implementation/implementation-plan.md`
- Validation report: `domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/validation/validation-report.md`
- Workflow state: `domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/workflow-state.yaml`

### Intent To Functional Requirements

| Intent | Jira | Outcome / Scope | Functional Requirements | Status | Owner |
| --- | --- | --- | --- | --- | --- |
| INT-KHQRREV-001 | JIRA-KHQRREV-001 | Operations-only full reversal before final settlement | FR-KHQRREV-001, FR-KHQRREV-006, FR-KHQRREV-007, FR-KHQRREV-008 | Ready | Product Owner / Operations Lead |
| INT-KHQRREV-001 | JIRA-KHQRREV-001 | Maker-checker control | FR-KHQRREV-003, FR-KHQRREV-004, FR-KHQRREV-005 | Ready | Operations Lead / Security and Risk Lead |
| INT-KHQRREV-001 | JIRA-KHQRREV-001 | Duplicate reversal prevention and idempotency | FR-KHQRREV-010, FR-KHQRREV-011, FR-KHQRREV-012, FR-KHQRREV-013 | Ready | Payments Architect |
| INT-KHQRREV-001 | JIRA-KHQRREV-001 | Processor and ledger reversal execution | FR-KHQRREV-014, FR-KHQRREV-015, FR-KHQRREV-016, FR-KHQRREV-017 | Ready | Payments Architect / Finance Lead |
| INT-KHQRREV-001 | JIRA-KHQRREV-001 | Status, audit, reconciliation, and reversal/refund separation | FR-KHQRREV-018, FR-KHQRREV-019, FR-KHQRREV-020, FR-KHQRREV-021, FR-KHQRREV-022 | Ready | Operations Lead / Finance Lead |
| INT-KHQRREV-001 | JIRA-KHQRREV-001 | Deferred retry and notification scope | FR-KHQRREV-023, FR-KHQRREV-024 | Ready as MVP exclusions | Product Owner / Compliance Lead |

### Functional Requirements To APIs And Acceptance Tests

| Requirement | Jira | API Operations / Interfaces | Acceptance Scenarios | Coverage | Notes |
| --- | --- | --- | --- | --- | --- |
| FR-KHQRREV-001 Operations maker request | JIRA-KHQRREV-020 | `POST /operations/khqr-payment-reversals` | Operations maker creates reversal request for eligible completed payment | Covered | Request creates an internal awaiting-approval workflow state, not downstream execution. |
| FR-KHQRREV-002 Entitlement rejection | JIRA-KHQRREV-021 | `POST /operations/khqr-payment-reversals` | Reject reversal request without operations reversal entitlement | Covered | API returns actor-safe `403`. |
| FR-KHQRREV-003 Approval required before execution | JIRA-KHQRREV-022 | `POST /operations/khqr-payment-reversals/{reversalId}/decision` | Processor and ledger execution does not start before checker approval | Covered | No downstream commands before checker approval. |
| FR-KHQRREV-004 Maker-checker separation | JIRA-KHQRREV-023 | `POST /operations/khqr-payment-reversals/{reversalId}/decision` | Reject maker self-approval | Covered | API returns actor-safe `403` or conflict per implementation standard. |
| FR-KHQRREV-005 Checker approve/reject | JIRA-KHQRREV-024 | `POST /operations/khqr-payment-reversals/{reversalId}/decision` | Checker rejects reversal request; Checker approval starts controlled reversal execution | Covered | Approval and rejection reason-code constraints are represented in OpenAPI. |
| FR-KHQRREV-006 Completed payment only | JIRA-KHQRREV-025 | `POST /operations/khqr-payment-reversals`; KHQR Payment Service lookup port | Reject reversal when original payment is not completed | Covered | Scenario outline covers non-completed states. |
| FR-KHQRREV-007 Before final settlement only | JIRA-KHQRREV-026 | `POST /operations/khqr-payment-reversals`; `POST /operations/khqr-payment-reversals/{reversalId}/decision`; Merchant Settlement Service cutoff port | Reject request-time ineligible cutoff; Re-check settlement cutoff immediately before execution | Covered | OpenAPI has safe structured settlement-cutoff error details. |
| FR-KHQRREV-008 Full amount only | JIRA-KHQRREV-027 | `POST /operations/khqr-payment-reversals` | Reject partial reversal request in MVP | Covered | API request requires amount; implementation must compare to original payment amount. |
| FR-KHQRREV-009 Reason code required | JIRA-KHQRREV-028 | Command APIs | Reject missing/invalid request reason code; Reject checker decision with missing/invalid decision reason code | Covered | Approval and rejection reason-code enums are separated. |
| FR-KHQRREV-010 Idempotency required | JIRA-KHQRREV-029 | Command APIs with `Idempotency-Key` | Reject reversal command without idempotency key | Covered | OpenAPI requires idempotency key on command operations. |
| FR-KHQRREV-011 Duplicate prevention | JIRA-KHQRREV-030 | `POST /operations/khqr-payment-reversals`; idempotency and reversal uniqueness store | Prevent duplicate reversal for same original payment; Concurrent reversal submissions do not create duplicate execution | Covered | Implementation must enforce unique active reversal per original payment. |
| FR-KHQRREV-012 Idempotency replay | JIRA-KHQRREV-031 | Command APIs with `Idempotency-Key` | Same idempotency key and same payload returns existing reversal | Covered | API returns `200` for replay. |
| FR-KHQRREV-013 Idempotency conflict | JIRA-KHQRREV-032 | Command APIs with `409 Conflict` | Same idempotency key and different payload is rejected | Covered | Error category `idempotency` available in structured details. |
| FR-KHQRREV-014 Processor and ledger execution | JIRA-KHQRREV-033 | Processor reversal port; ledger reversal port | Checker approval starts controlled reversal execution; Processor and ledger success marks reversal reversed | Covered | Ports are out-of-process interfaces, not public OpenAPI operations. |
| FR-KHQRREV-015 Reversed only after both complete | JIRA-KHQRREV-034 | Processor reversal port; ledger reversal port; status API | Processor and ledger success marks reversal reversed | Covered | Response status uses approved business outcome values. |
| FR-KHQRREV-016 Pending for non-final outcomes | JIRA-KHQRREV-035 | Processor and ledger ports; `GET /operations/khqr-payment-reversals/{reversalId}` | Processor success and ledger unknown remains pending; Ledger success and processor unknown remains pending; Pending threshold handling | Covered | Operations detail includes pending age and next action. |
| FR-KHQRREV-017 Failed execution | JIRA-KHQRREV-036 | Processor and ledger ports; exception queue port; status API | Terminal processor or ledger failure marks reversal failed; Pending threshold handling | Covered | No automatic compensation without approved retry policy. |
| FR-KHQRREV-018 Status tracking | JIRA-KHQRREV-037 | `GET /operations/khqr-payment-reversals/{reversalId}` | Authorized operations user views reversal status; Reject reversal status view without entitlement | Covered | Sensitive fields must be masked unless authorized. |
| FR-KHQRREV-019 Reference preservation | JIRA-KHQRREV-038 | Reversal state store; reconciliation projection | Preserve references needed for reconciliation | Covered | API status exposes safe references; full reconciliation record is internal/projection. |
| FR-KHQRREV-020 Audit evidence | JIRA-KHQRREV-039 | Audit outbox / Audit Store port | Audit material reversal events; Do not complete material state change when audit persistence fails | Covered | Audit integration is internal/out-of-contract; status exposes `AuditSummary`. |
| FR-KHQRREV-021 Reversal is not refund | JIRA-KHQRREV-040 | Reversal state store; reporting/reconciliation projections | Reversal is not reported as refund | Covered | Boundary enforced by separate capability and API paths. |
| FR-KHQRREV-022 Reconciliation outcomes | JIRA-KHQRREV-041 | Reconciliation projection / extract | Reconciliation identifies reversal outcomes | Covered | Feed/extract contract is an internal projection, not public OpenAPI. |
| FR-KHQRREV-023 Retry after approved policy only | JIRA-KHQRREV-042 | Future retry command; currently disabled | Retry is disabled until retry policy is approved | Covered as MVP exclusion | No retry API in approved MVP contract. |
| FR-KHQRREV-024 Notifications if approved only | JIRA-KHQRREV-043 | Future notification event integration | Notifications are not required for MVP until scope is approved | Covered as MVP exclusion | No notification event contract for MVP. |

### NFRs To Validation Requirements

| NFR | Jira | Validation Requirement | Acceptance / Evidence Placeholder | Status |
| --- | --- | --- | --- | --- |
| NFR-KHQRREV-001 Completion time | JIRA-KHQRREV-050 | Validate reversal completion time once Product, Finance, Operations, and QA approve target. | Reversal completion time target requires approved threshold before validation | Blocked by target approval |
| NFR-KHQRREV-002 Idempotency and concurrency | JIRA-KHQRREV-051 | Validate duplicate and concurrent reversal submissions cannot create duplicate execution. | Duplicate prevention, idempotency replay/conflict, concurrent submissions | Covered by acceptance design |
| NFR-KHQRREV-003 Reconciliation support | JIRA-KHQRREV-052 | Validate required original payment, reversal, processor, ledger, settlement, amount, status, actor, approval, and correlation references. | Preserve references; reconciliation identifies outcomes | Covered by acceptance design |
| NFR-KHQRREV-004 Audit completeness | JIRA-KHQRREV-053 | Validate 100% material reversal events and approval decisions have immutable audit evidence. | Audit material events; audit fail-closed scenario | Covered by acceptance design |
| NFR-KHQRREV-005 Sensitive data protection | JIRA-KHQRREV-054 | Validate masking in logs, views, audit, reporting, notifications, and test evidence. | Status masking; reversal command evidence protects sensitive data | Covered by acceptance design; security validation pending |
| NFR-KHQRREV-006 Safe degradation | JIRA-KHQRREV-055 | Validate unknown or partial processor/ledger outcomes remain traceable and do not duplicate execution. | Processor/ledger split outcomes; operational observability | Covered by acceptance design |
| NFR-KHQRREV-007 Observability | JIRA-KHQRREV-056 | Validate metrics, logs, traces, alerts, and queue visibility for lifecycle outcomes. | Operational observability exists for reversal lifecycle | Pending validation evidence |
| NFR-KHQRREV-008 Operations visibility | JIRA-KHQRREV-057 | Validate pending and failed reversals expose safe owner, age, reason, and next action. | Pending threshold handling; authorized status view | Covered by acceptance design |
| NFR-KHQRREV-009 Pipeline evidence | JIRA-KHQRREV-058 | Validate GitHub Actions, relevant tests, security checks, and quality gates once CI exists. | Future validation report / CI evidence | Blocked until CI/GitHub Actions evidence exists |

### Architecture Decisions To Components

| Architecture Decision | Component(s) Affected | Related Requirements | Status |
| --- | --- | --- | --- |
| ADR-KHQRREV-001 Merchant Settlement Service cutoff source | Settlement Cutoff Adapter, Reversal Eligibility Validator, Operations API errors | FR-KHQRREV-007, FR-KHQRREV-020 | Accepted; API and tests cover unavailable, stale, contradictory, and finally-settled outcomes. |
| ADR-KHQRREV-002 Separate reversal aggregate | Reversal State Store, Reporting, Reconciliation, QR Refund boundary | FR-KHQRREV-021, FR-KHQRREV-022 | Accepted; implementation must keep reversal separate from refund. |
| ADR-KHQRREV-003 Idempotency and reversal uniqueness owned by reversal capability | Reversal Idempotency Store, Reversal State Store, Reversal Orchestrator | FR-KHQRREV-010, FR-KHQRREV-011, FR-KHQRREV-012, FR-KHQRREV-013, NFR-KHQRREV-002 | Accepted; Slice 1 must prove duplicate prevention. |
| ADR-KHQRREV-004 Processor-ledger split outcomes visible and traceable | Processor Adapter, Ledger Adapter, Exception Queue, Reversal State Store | FR-KHQRREV-014, FR-KHQRREV-015, FR-KHQRREV-016, FR-KHQRREV-017, NFR-KHQRREV-006 | Accepted; no automatic compensation without approved policy. |
| ADR-KHQRREV-005 Retry excluded from MVP | Future Retry Service, Operations API, Audit | FR-KHQRREV-023 | Accepted as MVP exclusion; no retry API in MVP contract. |
| ADR-KHQRREV-006 Notifications out of MVP | Notification integration, Product/Compliance scope | FR-KHQRREV-024 | Accepted as MVP exclusion; no notification evidence required for MVP. |

### API Coverage

| API Operation | Requirement Coverage | Acceptance Coverage | Status |
| --- | --- | --- | --- |
| `POST /operations/khqr-payment-reversals` | FR-KHQRREV-001, FR-KHQRREV-002, FR-KHQRREV-006, FR-KHQRREV-007, FR-KHQRREV-008, FR-KHQRREV-009, FR-KHQRREV-010, FR-KHQRREV-011, FR-KHQRREV-012, FR-KHQRREV-013, FR-KHQRREV-020 | Maker request, entitlement rejection, payment status rejection, settlement cutoff rejection, partial amount rejection, reason-code rejection, idempotency replay/conflict/missing key, duplicate prevention, audit | Covered |
| `GET /operations/khqr-payment-reversals/{reversalId}` | FR-KHQRREV-016, FR-KHQRREV-017, FR-KHQRREV-018, FR-KHQRREV-019, NFR-KHQRREV-005, NFR-KHQRREV-008 | Authorized status view, forbidden status view, pending/failed operations visibility, reference preservation | Covered |
| `POST /operations/khqr-payment-reversals/{reversalId}/decision` | FR-KHQRREV-003, FR-KHQRREV-004, FR-KHQRREV-005, FR-KHQRREV-007, FR-KHQRREV-009, FR-KHQRREV-014, FR-KHQRREV-020 | No execution before approval, maker self-approval rejection, checker approval/rejection, pre-execution settlement cutoff, decision reason-code rejection, audit | Covered |

### Implementation Slice Traceability

| Slice | Status | Requirements | APIs / Interfaces | Acceptance / Test Coverage |
| --- | --- | --- | --- | --- |
| Slice 1 - Reversal Request Foundation | Blocked pending implementation start approval, first slice approval, and target stack/CI expectations | FR-KHQRREV-001, FR-KHQRREV-002, FR-KHQRREV-006, FR-KHQRREV-008, FR-KHQRREV-009, FR-KHQRREV-010, FR-KHQRREV-011, FR-KHQRREV-012, FR-KHQRREV-013, FR-KHQRREV-020, NFR-KHQRREV-002, NFR-KHQRREV-004, NFR-KHQRREV-005 | `POST /operations/khqr-payment-reversals`; maker entitlement port; payment snapshot port; idempotency store; reversal state store; audit outbox | Maker request, entitlement rejection, non-completed rejection, partial amount rejection, request reason-code rejection, missing idempotency, replay/conflict, duplicate prevention, concurrent submissions, audit, sensitive data masking. |
| Slice 2 - Maker-Checker Decision | Blocked pending Slice 1 | FR-KHQRREV-003, FR-KHQRREV-004, FR-KHQRREV-005, FR-KHQRREV-009, FR-KHQRREV-020 | `POST /operations/khqr-payment-reversals/{reversalId}/decision`; checker entitlement port; audit outbox | No execution before approval, maker self-approval rejection, checker approval/rejection, decision reason-code rejection. |
| Slice 3 - Settlement Eligibility | Blocked pending Slice 1 and Slice 2 | FR-KHQRREV-007, FR-KHQRREV-020 | Merchant Settlement Service cutoff port; structured API error details | Request-time settlement cutoff rejection; pre-execution settlement cutoff re-check. |
| Slice 4 - Processor And Ledger Execution | Blocked pending Slices 1-3 | FR-KHQRREV-014, FR-KHQRREV-015, FR-KHQRREV-016, FR-KHQRREV-017, NFR-KHQRREV-006, NFR-KHQRREV-008 | Processor reversal port; ledger reversal port; exception queue port; status API | Both success -> reversed, split unknown outcomes -> pending, terminal failures -> failed, pending thresholds. |
| Slice 5 - Status, Audit, Reconciliation, Observability | Blocked pending Slices 1-4 | FR-KHQRREV-018, FR-KHQRREV-019, FR-KHQRREV-020, FR-KHQRREV-021, FR-KHQRREV-022, NFR-KHQRREV-003, NFR-KHQRREV-004, NFR-KHQRREV-005, NFR-KHQRREV-007, NFR-KHQRREV-008 | `GET /operations/khqr-payment-reversals/{reversalId}`; audit outbox; reconciliation projection; metrics/logs/traces/alerts | Status view, forbidden status, reference preservation, audit material events, reversal-not-refund, reconciliation outcomes, operational observability. |
| Slice 6 - MVP Exclusions And Release Guards | Blocked pending Product/Compliance/QA validation target decisions | FR-KHQRREV-023, FR-KHQRREV-024, NFR-KHQRREV-001, NFR-KHQRREV-009 | No MVP retry API; no MVP notification event; validation hooks | Retry disabled; notifications not required; completion target conditional; pipeline evidence once code exists. |

### Orphans And Coverage Gaps

| Type | Item | Finding | Recommended Resolution |
| --- | --- | --- | --- |
| No orphan requirement | FR-KHQRREV-001 through FR-KHQRREV-024 | All functional requirements map to API operations, internal interfaces, acceptance scenarios, or explicit MVP exclusions. | Keep mappings current as artifacts change. |
| No orphan API | Approved OpenAPI operations | All three operations map to approved requirements and acceptance scenarios. | Keep API coverage under architecture review if endpoints change. |
| MVP exclusion | FR-KHQRREV-023 Retry | Requirement is `Should`; retry is excluded from MVP until policy approval. | Keep disabled behavior covered; create change request if retry enters MVP. |
| MVP exclusion | FR-KHQRREV-024 Notifications | Requirement is `Should`; notifications are excluded from MVP until Product/Compliance approval. | Keep release readiness from requiring notification evidence. |
| Validation blocker | NFR-KHQRREV-001 | Completion-time target is not approved. | Product, Finance, Operations, and QA approve target before validation planning. |
| Release blocker | NFR-KHQRREV-009 | Pipeline evidence cannot exist until source code exists. | Populate validation report after implementation and CI setup. |
| Implementation readiness blocker | Target stack / CI expectations | Implementation language, test runner, and CI expectations are not approved. | Developer Lead and DevSecOps approve before source-code work. |

### Traceability Approval Gates

| Gate | Jira Placeholder | Required Approver | Status |
| --- | --- | --- | --- |
| Traceability review | JIRA-KHQRREV-080 | BA / Architect / QA Lead | Approved |
| API coverage review | JIRA-KHQRREV-081 | Solution Architect | Approved via JIRA-KHQRREV-062-API |
| Test coverage review | JIRA-KHQRREV-082 | QA Lead | Pending |
| Security coverage review | JIRA-KHQRREV-083 | Security Architect | Pending |

## Capability: Card Lifecycle Management

Traceability ID: TRACE-CARDREP-DEMO-001

| Intent | Jira | Confluence | Requirement | Spec | Acceptance Scenario | Status | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- |
| INT-CARDREP-001 | SCRUM-1 | 688129 | FR-CARDREP-001 through FR-CARDREP-026 | `domains/cards/capabilities/card-lifecycle-management/features/card-replacement/requirements/requirements.md` | `domains/cards/capabilities/card-lifecycle-management/features/card-replacement/requirements/requirements.md` | Draft | Cards Squad |
