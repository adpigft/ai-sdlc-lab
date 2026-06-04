# QR Refund Intent

## Metadata

| Field | Value |
| --- | --- |
| Intent ID | INT-QRREF-001 |
| Jira Epic | JIRA-QRREF-001 |
| Confluence Page | CONF-PAY-QRREF-INTENT |
| Domain | Payments |
| Capability | QR Refund |
| MVP Scope | Full refunds for completed KHQR payments |
| Owner | Digital Payments Product Owner |
| Status | Intent approved for artifact creation; pending specification approval |
| Created | 2026-06-01 |

## Problem Statement

Merchants and bank operations users need a controlled way to refund completed KHQR payments without relying on manual back-office handling. The bank needs refund processing that is fast, auditable, compliant, traceable to the original payment, resilient to duplicate requests, and visible to operations, finance, and merchants.

## Desired Outcomes

- Improve merchant refund experience.
- Process refunds faster and reduce manual operations effort.
- Reduce refund processing errors.
- Improve operational transparency and tracking.
- Maintain auditability and compliance.
- Support end-of-day reconciliation across original payment, refund transaction, processor, ledger, and merchant settlement records.

## Success Metrics

| Metric | Target |
| --- | --- |
| Manual refund handling reduction | 80% reduction |
| Refund processing time | 95% of refunds processed within 60 seconds |
| Refund processing error reduction | 50% reduction |
| Reconciliation match rate | Above 99% |
| Merchant refund support ticket reduction | 30% reduction |
| Audit completeness | 100% |

## In Scope

- Full refunds for completed KHQR payments.
- Merchant-initiated refunds through the merchant application.
- Bank operations initiated refunds through operations tooling.
- Operations override for authorized users.
- Refund status tracking.
- Customer notification for successful and failed refunds.
- Failed refund routing to an operations exception queue.
- Retry of failed refunds by operations users.
- End-of-day reconciliation.
- Required reports for refund history, failed refunds, pending refunds, and daily refund totals.
- Immutable audit trail for all material refund events.

## Out Of Scope

- Partial refunds.
- Customer-initiated refund requests.
- Non-KHQR QR refunds.
- Refund velocity limits.
- Suspicious merchant screening.
- AML and sanctions screening for refunds, because funds are returned to the original payer.
- Intraday reconciliation.
- Reporting platform implementation.
- Detailed settlement and accounting design.

## Stakeholders

| Role | Responsibility | Approval Reference |
| --- | --- | --- |
| Product Owner | Business scope, refund journey, and MVP approval | JIRA-QRREF-001 |
| Payments Architect | Refund lifecycle, integration, idempotency, and settlement design | JIRA-QRREF-002 |
| QA Lead | Acceptance criteria and validation coverage | JIRA-QRREF-003 |
| Security and Risk Lead | Fraud controls, authorization, audit, and sensitive-data handling | JIRA-QRREF-004 |
| Operations Lead | Exception queue, retry, override, and operational transparency | JIRA-QRREF-005 |
| Finance Lead | Reconciliation, settlement, and reporting needs | JIRA-QRREF-006 |
| Release Manager | Release readiness and change approval | JIRA-QRREF-007 |

## Business Rules

| Rule ID | Rule |
| --- | --- |
| BR-QRREF-001 | A completed KHQR payment can be refunded only once in MVP because only full refunds are supported. |
| BR-QRREF-002 | Refund is allowed only when the original payment status is `Completed`. |
| BR-QRREF-003 | Refund must be requested within 30 calendar days from the original payment date. |
| BR-QRREF-004 | Refunds are allowed after merchant settlement. |
| BR-QRREF-005 | Merchant balance availability is not required for MVP. |
| BR-QRREF-006 | Refunds must be blocked for suspended merchants. |
| BR-QRREF-007 | High-value refunds above configurable thresholds require manual review. Threshold values will be determined during business configuration and are out of scope for intent. |
| BR-QRREF-008 | Refund reason codes are required. |
| BR-QRREF-009 | Refund APIs must be idempotent to prevent duplicate refund execution. |

## Operational Rules

Refund statuses for MVP:

- `Requested`
- `Processing`
- `Completed`
- `Rejected`
- `Failed`

Operational behavior:

- Merchant-initiated refunds should process automatically when all business rules and controls pass.
- Bank operations users can create refunds, approve overrides, and retry failed refunds.
- Failed refunds must be routed to an operations exception queue for investigation and retry.
- Maker-checker approval is required only for operations override actions.
- Customer notifications are required for successful and failed refunds.

## Operations Override

Bank operations override is permitted only for authorized users with:

- Appropriate entitlement.
- Reason code.
- Maker-checker approval.
- Immutable audit trail.

## Fraud And Compliance Controls

- High-value refunds above configurable thresholds require manual review.
- Refund velocity limits are out of scope for MVP.
- Suspicious merchant screening is out of scope for MVP.
- Refunds must be blocked for suspended merchants.
- AML and sanctions screening are out of scope for MVP because funds are returned to the original payer.
- Regulatory retention requirements are open pending compliance confirmation.

## Audit Requirements

Audit all key events:

- Request.
- Approval.
- Rejection.
- Retry.
- Completion.
- Failure.
- Override.

Audit records must capture:

- Original payment ID.
- Refund ID.
- Initiator.
- User role.
- Reason code.
- Timestamp.
- Approval user.
- Correlation ID.

Sensitive customer information must be masked. Audit records must be immutable.

## Reconciliation Requirements

The refund capability must support end-of-day reconciliation across:

- Original payment.
- Refund transaction.
- Payment processor.
- Ledger.
- Merchant settlement.

A separate refund reference is required. Intraday reconciliation is future scope.

## Reporting Requirements

Required reports:

- Refund history.
- Failed refunds.
- Pending refunds.
- Daily refund totals.

Report consumers:

- Merchants.
- Operations.
- Finance.

## Non-Functional Requirements

| NFR ID | Requirement | Target |
| --- | --- | --- |
| NFR-QRREF-001 | Successful refund processing time | 95% within 60 seconds |
| NFR-QRREF-002 | Availability | 99.9% |
| NFR-QRREF-003 | Maximum pending duration | 24 hours |
| NFR-QRREF-004 | Observability | Metrics, logs, traces, and alerts |
| NFR-QRREF-005 | Idempotency | Duplicate refund requests must not create duplicate refunds |
| NFR-QRREF-006 | Audit completeness | 100% |

## Dependencies

- Merchant App.
- KHQR Payment Service.
- Operations Portal.
- Ledger/Core Banking.
- Payment Processor.
- Notification Service.
- Merchant identity and authorization service.
- Operations entitlement model.
- Existing KHQR payment status model, if suitable for reuse.

## Assumptions

- Original KHQR payments are searchable by payment ID.
- Payment processor supports full refunds.
- Ledger supports refund postings against original payment reference.
- Merchant authentication is already implemented.
- Merchant identity and authorization services exist.
- Operations entitlement model exists.

## Architecture Decisions Required

| Decision ID | Decision Needed | Owner | Status |
| --- | --- | --- | --- |
| ADR-QRREF-001 | Accounting treatment and settlement adjustment mechanism for refunds after merchant settlement. | Payments Architect / Finance Lead | Required during architecture and detailed design |
| ADR-QRREF-002 | Whether the existing KHQR payment status model is sufficient for refund lifecycle reuse. | Payments Architect | Required during architecture |
| ADR-QRREF-003 | Detailed retry and exception queue design for failed refunds. | Payments Architect / Operations Lead | Required during architecture |

## Open Questions

| Question | Owner | Jira Placeholder | Status |
| --- | --- | --- | --- |
| What are the regulatory retention requirements for refund evidence? | Compliance Lead | JIRA-QRREF-008 | Open |
| What is the mismatch handling process for reconciliation breaks? | Operations Lead / Finance Lead | JIRA-QRREF-009 | Open |
| Which reporting platform will provide refund history, failed refunds, pending refunds, and daily refund totals? | Product Owner / Operations Lead | JIRA-QRREF-010 | Open |
| What are the MVP refund volume assumptions? | Product Owner | JIRA-QRREF-011 | Open |

## Human Approval

| Gate | Jira Placeholder | Required Approver | Status |
| --- | --- | --- | --- |
| Intent approval | JIRA-QRREF-001 | Product Owner / BA | Approved by user chat confirmation on 2026-06-01 |
| Architecture discovery approval | JIRA-QRREF-002 | Payments Architect | Pending |
| Risk and compliance input | JIRA-QRREF-004 | Security and Risk Lead / Compliance Lead | Pending |
| Operations input | JIRA-QRREF-005 | Operations Lead | Pending |
| Finance input | JIRA-QRREF-006 | Finance Lead | Pending |

## Next Step

Proceed to specification only after human approval to continue from intent to `$specification`.
