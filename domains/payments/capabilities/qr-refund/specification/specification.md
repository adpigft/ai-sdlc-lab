# QR Refund Specification

## Metadata

| Field | Value |
| --- | --- |
| Spec ID | SPEC-QRREF-001 |
| Intent ID | INT-QRREF-001 |
| Jira Epic | JIRA-QRREF-001 |
| Confluence Page | CONF-PAY-QRREF-SPEC |
| Domain | Payments |
| Capability | QR Refund |
| MVP Scope | Full refunds for completed KHQR payments |
| Status | Specification approved for architecture context |
| Source Intent | `domains/payments/capabilities/qr-refund/intent/intent.md` |

## Summary

The QR Refund capability enables merchants and authorized bank operations users to initiate full refunds for completed KHQR payments. The MVP must prevent duplicate refund execution, enforce refund eligibility, support operations override with maker-checker approval, notify customers of successful and failed refunds, provide operational transparency, and support end-of-day reconciliation.

No architecture, API contract, test implementation, or application code is defined by this specification.

## Requirement Gaps Carried Forward

These gaps are not blockers for a draft specification, but they must be resolved before architecture approval, API design, or implementation:

| Gap ID | Gap | Required Resolution |
| --- | --- | --- |
| GAP-QRREF-001 | Settlement adjustment and accounting treatment for post-settlement refunds are not yet defined. | Architecture and finance decision. |
| GAP-QRREF-002 | Regulatory retention requirements for refund evidence are unknown. | Compliance decision. |
| GAP-QRREF-003 | Reconciliation mismatch handling process is unknown. | Operations and finance decision. |
| GAP-QRREF-004 | Reporting platform is unknown. | Product and operations decision. |
| GAP-QRREF-005 | MVP refund volume assumptions are unknown. | Product and architecture decision. |
| GAP-QRREF-006 | Detailed retry limits, retry intervals, and escalation SLAs are not yet defined. | Operations and architecture decision. |
| GAP-QRREF-007 | High-value manual review thresholds are business configuration and not yet defined. | Product and risk configuration decision. |

## Actors

| Actor | Description |
| --- | --- |
| Merchant User | Authenticated merchant application user requesting a full refund for a completed KHQR payment. |
| Bank Operations User | Authorized bank user who can create refunds, approve overrides, and retry failed refunds. |
| Maker | Operations user who requests an override. |
| Checker | Separate authorized operations user who approves or rejects an override. |
| Customer | Original payer receiving the refund and refund notification. Customer-initiated refund requests are out of scope. |
| Finance User | Consumer of refund totals and reconciliation evidence. |

## Refund Status Model

| Status | Meaning | Terminal |
| --- | --- | --- |
| Requested | Refund request has been accepted for eligibility and control evaluation. | No |
| Processing | Refund has passed required checks and is being processed by downstream systems. | No |
| Completed | Refund completed successfully and is available for reconciliation and reporting. | Yes |
| Rejected | Refund request failed business, authorization, control, or approval checks before processing completed. | Yes |
| Failed | Refund processing failed after processing started and requires operational review. | Yes |

## Functional Requirements

| Req ID | Jira | Requirement | Priority | Acceptance Criteria |
| --- | --- | --- | --- | --- |
| FR-QRREF-001 | JIRA-QRREF-020 | The system shall allow a merchant user to request a full refund for a completed KHQR payment. | Must | Given an authenticated authorized merchant user and a completed KHQR payment owned by the merchant, when the merchant requests a full refund within the refund window, then the refund request is accepted for processing. |
| FR-QRREF-002 | JIRA-QRREF-021 | The system shall allow an authorized bank operations user to create a full refund for a completed KHQR payment. | Must | Given an authorized operations user and eligible completed KHQR payment, when the user creates a refund with a valid reason code, then the refund request is accepted for processing. |
| FR-QRREF-003 | JIRA-QRREF-022 | The system shall reject refunds for original payments that are not in `Completed` status. | Must | Given an original payment in any status other than `Completed`, when a refund is requested, then the refund is rejected and no refund transaction is created. |
| FR-QRREF-004 | JIRA-QRREF-023 | The system shall enforce one full refund per original KHQR payment in MVP. | Must | Given an original payment that already has a completed, processing, or requested full refund, when another refund is requested, then the request is rejected as duplicate or already refunded. |
| FR-QRREF-005 | JIRA-QRREF-024 | The system shall enforce a 30 calendar day refund window from the original payment date. | Must | Given a completed KHQR payment older than 30 calendar days, when a refund is requested without an approved operations override, then the refund is rejected. |
| FR-QRREF-006 | JIRA-QRREF-025 | The system shall allow refunds after merchant settlement. | Must | Given an eligible completed KHQR payment that has already settled to the merchant, when a refund is requested, then settlement state alone does not block refund eligibility. |
| FR-QRREF-007 | JIRA-QRREF-026 | The system shall block refunds for suspended merchants. | Must | Given a suspended merchant, when a refund is requested by the merchant, then the refund is rejected unless an authorized operations override is approved where policy permits. |
| FR-QRREF-008 | JIRA-QRREF-027 | The system shall require a refund reason code for every refund request. | Must | Given a refund request without a valid reason code, when submitted, then the request is rejected. |
| FR-QRREF-009 | JIRA-QRREF-028 | The system shall require idempotency for refund initiation. | Must | Given duplicate refund submissions with the same idempotency key and same payload, when submitted, then only one refund is created and the original refund reference/status is returned. |
| FR-QRREF-010 | JIRA-QRREF-029 | The system shall reject duplicate idempotency keys with conflicting refund payloads. | Must | Given a previous refund request for an idempotency key, when a different payload is submitted with the same key, then the request is rejected with a duplicate conflict. |
| FR-QRREF-011 | JIRA-QRREF-030 | The system shall route high-value refunds above configurable thresholds to manual review. | Must | Given a refund above the configured high-value threshold, when requested, then the refund does not proceed automatically and is held for manual review. |
| FR-QRREF-012 | JIRA-QRREF-031 | The system shall support operations override only for authorized users with entitlement, reason code, maker-checker approval, and immutable audit trail. | Must | Given an override request, when entitlement, reason code, maker-checker approval, or audit capture is missing, then the override is rejected. |
| FR-QRREF-013 | JIRA-QRREF-032 | The system shall route failed refunds to an operations exception queue. | Must | Given a refund processing failure, when failure is detected, then the refund status becomes `Failed` and the refund appears in the exception queue with investigation details safe for operations use. |
| FR-QRREF-014 | JIRA-QRREF-033 | The system shall allow authorized operations users to retry failed refunds. | Must | Given a failed refund eligible for retry, when an authorized operations user retries with a reason code, then retry is attempted and audited. |
| FR-QRREF-015 | JIRA-QRREF-034 | The system shall notify customers of successful and failed refunds. | Must | Given a refund reaches `Completed` or `Failed`, when notification service is available, then a customer-safe notification is sent without exposing sensitive operational details. |
| FR-QRREF-016 | JIRA-QRREF-035 | The system shall provide refund status tracking for merchants and operations users. | Must | Given an authorized merchant or operations user, when they request refund status for an allowed refund, then current refund status and safe summary details are returned. |
| FR-QRREF-017 | JIRA-QRREF-036 | The system shall generate refund references separate from original payment references. | Must | Given a refund is accepted, when the refund record is created, then a unique refund ID and downstream refund reference are captured when available. |
| FR-QRREF-018 | JIRA-QRREF-037 | The system shall support end-of-day reconciliation across original payment, refund transaction, payment processor, ledger, and merchant settlement. | Must | Given end-of-day reconciliation runs, when refund records are matched, then matched and mismatched records are identifiable for operations and finance. |
| FR-QRREF-019 | JIRA-QRREF-038 | The system shall provide refund reporting data for refund history, failed refunds, pending refunds, and daily refund totals. | Must | Given an authorized report consumer, when reporting data is requested through the approved reporting channel, then required refund report data is available subject to access controls. |
| FR-QRREF-020 | JIRA-QRREF-039 | The system shall audit all material refund events. | Must | Given any request, approval, rejection, retry, completion, failure, or override event, when it occurs, then an immutable audit record is captured with required fields and masked sensitive customer data. |

## Non-Functional Requirements

| NFR ID | Jira | Requirement | Measure |
| --- | --- | --- | --- |
| NFR-QRREF-001 | JIRA-QRREF-040 | Successful refund processing shall be timely. | 95% of successful refunds processed within 60 seconds. |
| NFR-QRREF-002 | JIRA-QRREF-041 | Refund initiation and status capability shall meet availability target. | 99.9% availability target. |
| NFR-QRREF-003 | JIRA-QRREF-042 | Refunds shall not remain non-terminal beyond the maximum pending duration without operations visibility. | Maximum pending duration: 24 hours. |
| NFR-QRREF-004 | JIRA-QRREF-043 | Refund capability shall be observable. | Metrics, logs, traces, and alerts exist for initiation, rejection, processing, failure, retry, completion, overrides, high-value review, and reconciliation breaks. |
| NFR-QRREF-005 | JIRA-QRREF-044 | Refund initiation shall be idempotent and concurrency-safe. | Duplicate requests and concurrent submissions must not create duplicate refunds. |
| NFR-QRREF-006 | JIRA-QRREF-045 | Refund audit completeness shall be enforced. | 100% of material refund events have immutable audit records. |
| NFR-QRREF-007 | JIRA-QRREF-046 | Sensitive customer and account data shall be protected. | Customer, account, merchant, and payment identifiers are masked in logs, reports, notifications, and operations views unless explicitly authorized. |
| NFR-QRREF-008 | JIRA-QRREF-047 | Refund processing shall degrade safely during downstream outages. | Processor, ledger, notification, or reconciliation dependency failure must not create duplicate refunds or untraceable states. |
| NFR-QRREF-009 | JIRA-QRREF-048 | Refund records shall support regulatory and audit retention once retention requirements are confirmed. | Retention policy pending compliance decision in JIRA-QRREF-008. |

## Business Rules

| Rule ID | Source | Rule | Requirement Links |
| --- | --- | --- | --- |
| BR-QRREF-001 | Intent | A completed KHQR payment can be refunded only once in MVP. | FR-QRREF-003, FR-QRREF-004 |
| BR-QRREF-002 | Intent | Refund is allowed only when original payment status is `Completed`. | FR-QRREF-003 |
| BR-QRREF-003 | Intent | Refund must be requested within 30 calendar days from original payment date unless an authorized override is approved. | FR-QRREF-005, FR-QRREF-012 |
| BR-QRREF-004 | Intent | Refunds are allowed after merchant settlement. | FR-QRREF-006 |
| BR-QRREF-005 | Intent | Merchant balance availability is not required for MVP. | FR-QRREF-006 |
| BR-QRREF-006 | Intent | Refunds must be blocked for suspended merchants unless policy allows authorized operations override. | FR-QRREF-007, FR-QRREF-012 |
| BR-QRREF-007 | Intent | High-value refunds above configured thresholds require manual review. Threshold values are configuration and out of intent scope. | FR-QRREF-011 |
| BR-QRREF-008 | Intent | Refund reason codes are required. | FR-QRREF-008, FR-QRREF-012 |
| BR-QRREF-009 | Intent | Refund APIs must be idempotent. | FR-QRREF-009, FR-QRREF-010 |

## Acceptance Criteria Summary

| AC ID | Requirement | Acceptance Criteria |
| --- | --- | --- |
| AC-QRREF-001 | FR-QRREF-001 | Merchant can submit a full refund for an owned completed KHQR payment within 30 days. |
| AC-QRREF-002 | FR-QRREF-002 | Operations user can create a refund only with proper entitlement and valid reason code. |
| AC-QRREF-003 | FR-QRREF-003 | Refund is rejected when original payment is not `Completed`. |
| AC-QRREF-004 | FR-QRREF-004 | Second refund attempt for same original payment is rejected or returns existing refund depending on idempotency context. |
| AC-QRREF-005 | FR-QRREF-005 | Refund outside 30-day window is rejected unless an approved operations override applies. |
| AC-QRREF-006 | FR-QRREF-007 | Suspended merchant refund attempt is blocked unless authorized override policy permits. |
| AC-QRREF-007 | FR-QRREF-009 | Duplicate request with same idempotency key and payload returns existing refund reference/status. |
| AC-QRREF-008 | FR-QRREF-010 | Duplicate request with same idempotency key and conflicting payload is rejected. |
| AC-QRREF-009 | FR-QRREF-011 | High-value refund is routed to manual review and does not automatically process. |
| AC-QRREF-010 | FR-QRREF-012 | Override cannot proceed without entitlement, reason code, maker-checker approval, and audit record. |
| AC-QRREF-011 | FR-QRREF-013 | Failed refund appears in operations exception queue. |
| AC-QRREF-012 | FR-QRREF-014 | Authorized operations retry is audited and updates refund processing status. |
| AC-QRREF-013 | FR-QRREF-015 | Customer-safe notification is sent for completed and failed refunds. |
| AC-QRREF-014 | FR-QRREF-018 | End-of-day reconciliation can identify matched and mismatched refund records. |
| AC-QRREF-015 | FR-QRREF-020 | Audit record is created for request, approval, rejection, retry, completion, failure, and override events. |

## Edge Cases And Negative Scenarios

| Scenario ID | Scenario | Expected Outcome |
| --- | --- | --- |
| EDGE-QRREF-001 | Original payment ID not found. | Refund is rejected with safe error and audited. |
| EDGE-QRREF-002 | Original payment belongs to different merchant. | Merchant request is rejected as unauthorized and audited. |
| EDGE-QRREF-003 | Original payment is not completed. | Refund is rejected. |
| EDGE-QRREF-004 | Original payment is older than 30 calendar days. | Refund is rejected unless approved operations override applies. |
| EDGE-QRREF-005 | Original payment already has a refund. | Duplicate refund is prevented. |
| EDGE-QRREF-006 | Merchant is suspended. | Merchant refund is blocked. |
| EDGE-QRREF-007 | Reason code missing or invalid. | Refund is rejected. |
| EDGE-QRREF-008 | Idempotency key missing. | Refund initiation is rejected. |
| EDGE-QRREF-009 | Same idempotency key with conflicting payload. | Refund is rejected as duplicate conflict. |
| EDGE-QRREF-010 | Processor timeout during refund. | Refund remains traceable, does not duplicate, and becomes visible to operations if unresolved. |
| EDGE-QRREF-011 | Notification service unavailable. | Refund processing outcome remains authoritative; notification failure is observable and recoverable. |
| EDGE-QRREF-012 | Maker and checker are the same user. | Override approval is rejected. |
| EDGE-QRREF-013 | Reconciliation mismatch is detected. | Mismatch is visible to operations and finance pending defined handling process. |

## Reporting Requirements

| Report | Consumers | Required Data |
| --- | --- | --- |
| Refund history | Merchants, Operations | Refund ID, original payment ID, status, reason code, timestamps, safe merchant/customer summary. |
| Failed refunds | Operations | Refund ID, original payment ID, failure category, retry eligibility, correlation ID, timestamp. |
| Pending refunds | Operations, Finance | Refund ID, age, current status, dependency state where available, correlation ID. |
| Daily refund totals | Finance, Operations | Count, amount totals, status totals, merchant totals, processor/ledger match status. |

## Audit Data Requirements

| Field | Required | Notes |
| --- | --- | --- |
| Original payment ID | Yes | Must link refund to source payment. |
| Refund ID | Yes | Bank refund identifier. |
| Processor refund reference | Yes when available | Separate downstream refund reference. |
| Initiator | Yes | Merchant user, operations user, or system actor. |
| User role | Yes | Role at time of action. |
| Reason code | Yes | Required for all refund requests and overrides. |
| Timestamp | Yes | Event timestamp. |
| Approval user | Required for approvals and overrides | Maker-checker evidence. |
| Correlation ID | Yes | Cross-system traceability. |
| Event type | Yes | Request, approval, rejection, retry, completion, failure, override. |
| Masked sensitive identifiers | Yes | No unmasked sensitive customer data in general audit views. |

## Dependencies

| Dependency | Purpose | Status |
| --- | --- | --- |
| Merchant App | Merchant refund initiation and status visibility. | Assumed available |
| KHQR Payment Service | Original payment lookup and eligibility data. | Assumed available |
| Operations Portal | Operations creation, override, retry, and exception queue. | Assumed available |
| Ledger/Core Banking | Refund posting and accounting records. | Assumed available; design required |
| Payment Processor | Full refund execution and processor refund reference. | Assumed available |
| Notification Service | Customer notification for completed and failed refunds. | Assumed available |
| Merchant identity and authorization service | Merchant authentication and ownership checks. | Assumed available |
| Operations entitlement model | Operations permissions and maker-checker support. | Assumed available |

## Architecture Decisions Required

| Decision ID | Decision Needed | Owner | Status |
| --- | --- | --- | --- |
| ADR-QRREF-001 | Accounting treatment and settlement adjustment mechanism for refunds after merchant settlement. | Payments Architect / Finance Lead | Required before implementation |
| ADR-QRREF-002 | Whether existing KHQR payment status model is sufficient for refund lifecycle reuse. | Payments Architect | Required before API design |
| ADR-QRREF-003 | Detailed retry limits, retry intervals, and exception queue design for failed refunds. | Payments Architect / Operations Lead | Required before validation design |
| ADR-QRREF-004 | Safe degradation behavior during processor, ledger, notification, and reconciliation dependency failures. | Payments Architect / Operations Lead | Required before implementation |

## Open Questions

| Question | Owner | Jira Placeholder | Impact |
| --- | --- | --- | --- |
| What are the regulatory retention requirements for refund evidence? | Compliance Lead | JIRA-QRREF-008 | Blocks final retention and archival requirements. |
| What is the mismatch handling process for reconciliation breaks? | Operations Lead / Finance Lead | JIRA-QRREF-009 | Blocks final reconciliation operations design. |
| Which reporting platform will provide refund history, failed refunds, pending refunds, and daily refund totals? | Product Owner / Operations Lead | JIRA-QRREF-010 | Blocks reporting implementation approach. |
| What are the MVP refund volume assumptions? | Product Owner | JIRA-QRREF-011 | Blocks capacity and performance validation design. |
| What customer notification templates and channels are approved for completed and failed refunds? | Product Owner / Compliance Lead | JIRA-QRREF-012 | Blocks final customer communication requirements. |
| What high-value refund thresholds and review queues are configured for MVP? | Product Owner / Risk Lead | JIRA-QRREF-013 | Blocks final manual review configuration. |
| Are refund rejection notifications required, or only completed and failed refund notifications? | Product Owner | JIRA-QRREF-014 | Clarifies customer communication scope. |

## Out Of Scope Confirmation

- Partial refunds.
- Customer-initiated refund requests.
- Non-KHQR QR refunds.
- Refund velocity limits.
- Suspicious merchant screening.
- AML and sanctions screening for refunds.
- Intraday reconciliation.
- Reporting platform implementation.
- Detailed settlement and accounting implementation.
- Architecture design, API contract, acceptance test file, and application code.

## Human Approval

| Gate | Jira Placeholder | Required Approver | Status |
| --- | --- | --- | --- |
| Specification approval | JIRA-QRREF-050 | Product Owner / BA | Approved by user chat confirmation on 2026-06-01 |
| QA testability review | JIRA-QRREF-051 | QA Lead | Pending |
| Architecture readiness review | JIRA-QRREF-052 | Payments Architect | Pending |
| Risk and compliance review | JIRA-QRREF-053 | Security and Risk Lead / Compliance Lead | Pending |
| Operations and finance review | JIRA-QRREF-054 | Operations Lead / Finance Lead | Pending |

## Next Step

Proceed to architecture context only after this specification is reviewed and approved. Do not create architecture, API contracts, tests, or application code from this draft without human approval.
