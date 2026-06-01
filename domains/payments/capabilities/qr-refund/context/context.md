# QR Refund Architecture Context

## Metadata

| Field | Value |
| --- | --- |
| Context ID | CTX-QRREF-001 |
| Intent ID | INT-QRREF-001 |
| Spec ID | SPEC-QRREF-001 |
| Jira Epic | JIRA-QRREF-001 |
| Confluence Page | CONF-PAY-QRREF-CONTEXT |
| Domain | Payments |
| Capability | QR Refund |
| Status | Architecture context approved for API contract design |
| Source Intent | `domains/payments/capabilities/qr-refund/intent/intent.md` |
| Source Spec | `domains/payments/capabilities/qr-refund/specs/spec.md` |

## Architecture Summary

QR Refund is a payment capability for full refunds of completed KHQR payments. The capability accepts refund initiation from merchant and operations channels, validates eligibility against original KHQR payment data and merchant/operations authorization, prevents duplicate refunds through idempotency and original-payment refund locking, coordinates refund execution with payment processor and ledger/core banking dependencies, records immutable audit events, supports operations exception handling, and provides data for end-of-day reconciliation and reporting.

This context does not define API contracts, acceptance tests, or application code.

## System Boundary

QR Refund owns:

- Refund eligibility orchestration for completed KHQR payments.
- Refund lifecycle state for MVP statuses: `Requested`, `Processing`, `Completed`, `Rejected`, `Failed`.
- Idempotency and duplicate refund prevention for refund initiation.
- Refund audit event production.
- Operations exception queue inputs for failed refunds.
- Refund data required for status tracking, reconciliation, and reporting.

QR Refund does not own:

- Merchant onboarding or merchant master data.
- Customer-initiated refund requests.
- Partial refunds.
- KHQR payment execution.
- Core ledger implementation.
- Payment processor settlement.
- Notification delivery platform.
- Reporting platform implementation.
- Regulatory retention policy definition.

## Actors And Channels

| Actor / Channel | Role | Trust Boundary |
| --- | --- | --- |
| Merchant Application | Merchant refund initiation and merchant refund status visibility. | External authenticated merchant channel |
| Operations Portal | Operations refund creation, override approval, retry, and exception investigation. | Internal privileged user channel |
| QR Refund Capability | Refund orchestration, state, idempotency, audit, and integration coordination. | Payments platform boundary |
| Customer | Original payer receiving refund and notification. | Notification recipient, not refund initiator |
| Finance / Operations Reporting Consumer | Uses refund reporting and reconciliation evidence. | Internal reporting boundary |

## Component Context

| Component | Responsibility | Data Owned |
| --- | --- | --- |
| QR Refund Orchestrator | Coordinates validation, state transitions, processor submission, ledger posting, audit, notifications, and exception routing. | Refund lifecycle state and correlation IDs |
| Refund Eligibility Validator | Checks original payment status, ownership, 30-day window, suspended merchant state, duplicate refund state, reason code, and high-value review requirement. | Validation result only |
| Idempotency Store | Stores idempotency keys, request fingerprints, refund references, and conflict state. | Idempotency records |
| Refund State Store | Stores refund ID, original payment ID, merchant reference, status, timestamps, reason code, refund amount, processor reference, ledger reference, and retry metadata. | Refund records |
| Override Approval Control | Enforces entitlement, reason code, distinct maker/checker approval, and audit for operations overrides. | Override approval records |
| Audit Event Producer | Emits immutable audit events for refund lifecycle and control events. | Audit event payloads |
| Exception Queue Publisher | Publishes failed or stuck refund cases to operations exception handling. | Exception queue event payloads |
| Reconciliation Data Publisher | Makes refund data available for end-of-day reconciliation. | Reconciliation extract/feed payloads |

## Integration Context

| Integration | Direction | Purpose | Assumption |
| --- | --- | --- | --- |
| Merchant App | Inbound / outbound | Initiate merchant refunds and show merchant-safe refund status. | Merchant authentication exists and can identify merchant entity. |
| Operations Portal | Inbound / outbound | Operations refund creation, override approval, retry, and exception investigation. | Operations entitlement model exists. |
| KHQR Payment Service | Outbound lookup | Retrieve original payment status, merchant ownership, amount, currency, payment date, settlement state, and existing refund linkage. | Completed KHQR payments are searchable by payment ID. |
| Merchant Identity / Authorization | Outbound lookup | Verify merchant user and merchant entity authorization. | Service can prove merchant owns or is entitled to the original payment. |
| Merchant Profile / Status | Outbound lookup | Determine suspended merchant state and other merchant restrictions. | Suspended merchant flag is available at refund decision time. |
| Payment Processor | Outbound command / inbound status | Execute full refund and obtain processor refund reference. | Processor supports full refund for completed KHQR payments. |
| Ledger / Core Banking | Outbound command / inbound status | Post refund accounting entry against original payment reference. | Ledger supports refund postings against original payment reference. |
| Notification Service | Outbound event | Notify customer for completed and failed refunds. | Approved templates/channels are pending product/compliance decision. |
| Audit Store | Outbound event | Persist immutable audit records. | Audit store supports immutability and retention once policy is confirmed. |
| Reconciliation Platform | Outbound extract/feed | End-of-day matching across payment, refund, processor, ledger, and merchant settlement. | Reconciliation platform and mismatch workflow are pending decision. |
| Reporting Platform | Outbound extract/feed | Provide refund history, failed refunds, pending refunds, and daily totals. | Reporting platform is not yet selected. |

## Data Ownership

| Data | Owner | Notes |
| --- | --- | --- |
| Original KHQR payment record | KHQR Payment Service | Source for original status, amount, currency, merchant, date, and settlement state. |
| Refund lifecycle record | QR Refund Capability | Source for refund status and refund audit correlation. |
| Refund idempotency record | QR Refund Capability | Must prevent duplicate refunds and conflicting duplicate keys. |
| Merchant status and authorization | Merchant services | Source for merchant ownership and suspension checks. |
| Operations entitlement | Operations identity / entitlement service | Source for operations action and override rights. |
| Processor refund reference | Payment Processor | Captured by QR Refund when available. |
| Ledger refund posting reference | Ledger/Core Banking | Captured by QR Refund when available. |
| Audit record | Audit platform | Immutable evidence for all material events. |
| Reconciliation result | Reconciliation platform | Final matching and mismatch evidence. |
| Reporting view | Reporting platform | Consumer-facing reporting, not canonical refund state. |

## Conceptual Flow: Merchant-Initiated Refund

1. Merchant user submits full refund request with original KHQR payment ID, reason code, and idempotency key.
2. QR Refund validates idempotency key and request fingerprint.
3. QR Refund retrieves original KHQR payment details.
4. QR Refund verifies original payment is `Completed`, within 30 calendar days, owned by the requesting merchant, not already refunded, and not blocked by merchant suspension.
5. QR Refund checks whether the refund is above high-value review threshold.
6. If manual review is not required, QR Refund creates refund record and moves status from `Requested` to `Processing`.
7. QR Refund submits refund to processor and ledger/core banking according to architecture decisions.
8. QR Refund records processor and ledger references when available.
9. QR Refund updates status to `Completed` or `Failed`.
10. QR Refund emits audit events, notification events, reconciliation data, and reporting data.
11. Failed refunds are published to the operations exception queue.

## Conceptual Flow: Operations Override

1. Maker creates override request with refund context, reason code, and target control to override.
2. QR Refund verifies maker entitlement.
3. Checker reviews and approves or rejects the override.
4. QR Refund verifies checker entitlement and maker/checker separation.
5. QR Refund records immutable audit event for the override decision.
6. Approved override allows the refund flow to continue only for controls explicitly permitted by policy.

## Explicit Architecture Decisions Required

| Decision ID | Decision Needed | Options To Evaluate | Owner | Required Before |
| --- | --- | --- | --- | --- |
| ADR-QRREF-001 | Accounting treatment and settlement adjustment for refunds after merchant settlement. | Merchant receivable, settlement adjustment, ledger reversal model, processor-led refund settlement. | Payments Architect / Finance Lead | Accepted with conditions; Slice 2 remains blocked until conditions close |
| ADR-QRREF-002 | Refund state ownership and relationship to KHQR payment state. | Separate refund aggregate, extension of payment aggregate, payment-service-owned refund module. | Payments Architect | API design |
| ADR-QRREF-003 | Idempotency and concurrency control boundary. | API gateway, QR Refund service, payment service, ledger lock, database uniqueness. | Payments Architect | API design |
| ADR-QRREF-004 | High-value manual review state model. | Add explicit review state, model as `Requested`, or model through exception/approval queue. | Payments Architect / Risk Lead | API and test design |
| ADR-QRREF-005 | Retry and exception queue design. | Manual-only retry, bounded automatic retry, hybrid retry, retry event queue. | Payments Architect / Operations Lead | Validation design |
| ADR-QRREF-006 | Safe degradation behavior during processor, ledger, notification, and reconciliation outages. | Synchronous failure, durable async processing, pending/stuck processing with operational alerting. | Payments Architect / DevSecOps | Accepted with conditions; Slice 2 remains blocked until conditions close |
| ADR-QRREF-007 | Reconciliation mismatch handling. | Operations queue, finance workflow, manual case management, existing reconciliation platform. | Operations Lead / Finance Lead | Release readiness |
| ADR-QRREF-008 | Reporting data delivery model. | Reporting extract, event stream, database view, reporting platform integration. | Product Owner / Operations Lead | Release readiness |

## Decisions Accepted With Conditions

| Decision ID | Conditions | Status |
| --- | --- | --- |
| ADR-QRREF-001 | Finance must confirm settlement adjustment rules, receivable fallback conditions, and ledger account mappings. | Accepted with conditions |
| ADR-QRREF-003 | Payments Architecture must confirm processor and ledger client reference formats, inquiry support, and downstream attempt retention. | Accepted with conditions |
| ADR-QRREF-006 | Payments Architecture, DevSecOps, and Operations must confirm processor/ledger status mapping, timeout thresholds, and unresolved-state visibility. | Accepted with conditions |

## Integration Assumptions

| Assumption ID | Assumption | Validation Owner | Risk If False |
| --- | --- | --- | --- |
| ASM-QRREF-001 | Original KHQR payments are searchable by payment ID and include merchant, amount, currency, status, date, and settlement state. | Payments Architect | Refund eligibility cannot be reliably determined. |
| ASM-QRREF-002 | Merchant identity service can verify the merchant user belongs to the merchant that received the original payment. | Security and Risk Lead | Unauthorized merchant refund risk. |
| ASM-QRREF-003 | Operations entitlement model supports create, override maker, override checker, and retry permissions. | Operations Lead | Override and retry controls cannot be enforced. |
| ASM-QRREF-004 | Payment processor supports full refunds for completed KHQR payments and provides a separate refund reference. | Payments Architect | Refund execution and reconciliation may fail. |
| ASM-QRREF-005 | Ledger/core banking supports refund posting against original payment references. | Finance Lead | Accounting design may require manual or alternate process. |
| ASM-QRREF-006 | Notification service supports customer-safe completed and failed refund notifications. | Product Owner | Customer notification requirement may be delayed. |
| ASM-QRREF-007 | Audit platform supports immutable event capture and later retention policy configuration. | Compliance Lead | Audit completeness target may not be achievable. |
| ASM-QRREF-008 | Reconciliation and reporting platforms can consume refund data feeds or extracts. | Operations Lead / Finance Lead | Operational transparency and finance reporting may be incomplete. |

## Key Risks

| Risk ID | Risk | Impact | Mitigation / Decision |
| --- | --- | --- | --- |
| R-QRREF-001 | Duplicate refund execution from retries or concurrent submissions. | Customer/accounting loss and reconciliation breaks. | Idempotency store, original-payment refund lock, unique refund constraint, audit. |
| R-QRREF-002 | Unauthorized merchant refunds another merchant's payment. | Financial loss and privacy breach. | Merchant ownership validation and authorization checks. |
| R-QRREF-003 | Operations override abuse or error. | Unauthorized refund or control bypass. | Entitlement, maker-checker, reason code, immutable audit, privileged-user monitoring. |
| R-QRREF-004 | Post-settlement accounting not resolved. | Ledger, settlement, and finance breaks. | ADR-QRREF-001 before implementation. |
| R-QRREF-005 | Processor or ledger timeout creates unclear refund outcome. | Duplicate retry, stuck processing, poor customer/merchant experience. | Durable state, safe retry design, exception queue, reconciliation. |
| R-QRREF-006 | Regulatory retention remains undefined. | Compliance gap. | Compliance decision before release. |
| R-QRREF-007 | Reconciliation mismatch workflow unresolved. | Operations and finance unable to close breaks. | ADR-QRREF-007 before release readiness. |
| R-QRREF-008 | High-value review model not represented in status model. | Ambiguous API/test behavior. | ADR-QRREF-004 before API design. |
| R-QRREF-009 | Velocity and suspicious merchant screening out of scope. | Fraud patterns may be missed in MVP. | Compensating monitoring reports for high-value refunds, overrides, failed refunds, and refund totals. |

## Security And Control Context

- Merchant users must be authenticated by merchant application controls.
- Merchant refund requests must be authorized against the original payment merchant.
- Operations users must have explicit entitlements for create, retry, override-maker, and override-checker actions.
- Maker and checker must be different users.
- Refund request payloads must be bound to idempotency key fingerprints.
- Sensitive customer, account, and payment details must be masked in logs, operations views, reports, notifications, and audit views unless explicitly authorized.
- Refund state changes, authorization failures, duplicate attempts, idempotency conflicts, override requests, override approvals/rejections, retries, processor outcomes, ledger outcomes, and reconciliation mismatches should be auditable.
- AML and sanctions screening remain out of scope for MVP based on return-to-original-payer assumption, but compliance approval is required.

## Observability Context

Required metrics and alerts should include:

- Refund initiation count and success rate.
- Refund rejection count by reason.
- Refund failure count by dependency.
- Duplicate refund attempt count.
- Idempotency conflict count.
- High-value manual review count.
- Override request and approval count.
- Retry count and retry outcome.
- Refunds in `Requested` or `Processing` beyond threshold.
- Notification failures.
- Reconciliation mismatch count.
- End-of-day reconciliation completion status.

## Failure Handling Context

| Failure | Expected Handling |
| --- | --- |
| Original payment lookup unavailable | Reject or defer safely without creating duplicate refund; emit operational signal. |
| Merchant authorization unavailable | Reject or defer safely; do not process refund without authorization evidence. |
| Processor timeout | Preserve refund state, avoid duplicate retry, route unresolved cases to exception queue. |
| Ledger posting failure | Preserve refund state and references, route to exception queue, reconcile outcome before retry. |
| Notification failure | Refund outcome remains authoritative; notification failure is observable and recoverable. |
| Audit event failure | Refund processing must not produce unaudited material state changes; architecture must define fail-closed or durable audit buffering. |
| Reconciliation feed failure | Refund records remain available for replay/re-extract; operations alert required. |

## Data Classification

| Data | Classification | Handling |
| --- | --- | --- |
| Customer identifier | Confidential | Mask in logs, reports, and operations views unless explicitly authorized. |
| Merchant identifier | Confidential | Display only to authorized merchant/operations users. |
| Original payment ID | Confidential | Required for traceability; protect in external views. |
| Refund ID | Confidential | Required for status, support, and reconciliation. |
| Amount and currency | Confidential | Display to authorized users; protect in analytics/logging. |
| Reason code | Internal / Confidential | Visible to authorized merchant and operations users based on policy. |
| Processor refund reference | Confidential | Internal support and reconciliation use. |
| Ledger reference | Restricted | Finance, operations, and reconciliation use only. |
| Audit events | Restricted | Immutable, access controlled, retention pending compliance decision. |

## Context Open Questions

| Question | Owner | Source | Status |
| --- | --- | --- | --- |
| Which settlement adjustment and ledger posting rules are approved for Slice 2? | Finance Lead | ADR-QRREF-001 | Open as condition closure |
| What processor and ledger status mapping applies to timeouts and unknown outcomes? | Payments Architect / Finance Lead | ADR-QRREF-006 | Open as condition closure |
| What processor and ledger client reference formats are required for idempotency? | Payments Architect | ADR-QRREF-003 | Open as condition closure |
| What regulatory retention period applies to refund evidence and audit records? | Compliance Lead | JIRA-QRREF-008 | Open |
| What is the approved reconciliation mismatch handling workflow? | Operations Lead / Finance Lead | JIRA-QRREF-009 | Open |
| Which reporting platform or extract mechanism will provide refund reports? | Product Owner / Operations Lead | JIRA-QRREF-010 | Open |
| What are MVP refund volume assumptions for sizing and NFR validation? | Product Owner | JIRA-QRREF-011 | Open |
| What customer notification templates and channels are approved? | Product Owner / Compliance Lead | JIRA-QRREF-012 | Open |
| What high-value thresholds and review queues are configured for MVP? | Product Owner / Risk Lead | JIRA-QRREF-013 | Open |
| Are rejected refund notifications required? | Product Owner | JIRA-QRREF-014 | Open |
| Which controls are eligible for operations override and which must never be overridden? | Product Owner / Risk Lead / Operations Lead | JIRA-QRREF-015 | Open |

## Human Approval

| Gate | Jira Placeholder | Required Approver | Status |
| --- | --- | --- | --- |
| Architecture context approval | JIRA-QRREF-060 | Payments Architect | Approved by user chat confirmation on 2026-06-01 |
| Finance architecture input | JIRA-QRREF-061 | Finance Lead | Pending |
| Operations architecture input | JIRA-QRREF-062 | Operations Lead | Pending |
| Security and risk architecture input | JIRA-QRREF-063 | Security and Risk Lead | Pending |
| Compliance architecture input | JIRA-QRREF-064 | Compliance Lead | Pending |

## Next Step

Proceed to API contract design only after architecture context approval. Do not create API contracts, tests, or application code from this context without human approval.
