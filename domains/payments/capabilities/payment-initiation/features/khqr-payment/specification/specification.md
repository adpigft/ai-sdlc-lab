# KHQR Payment Specification

## Metadata

| Field | Value |
| --- | --- |
| Spec ID | SPEC-KHQR-001 |
| Intent ID | INT-KHQR-001 |
| Jira Epic | JIRA-KHQR-001 |
| Confluence Page | CONF-PAY-KHQR-SPEC |
| Capability | KHQR payment initiation |
| Status | Draft pending review |
| Owner | Digital Payments Product Owner |

## Summary

The KHQR payment capability allows an authenticated mobile banking customer to scan a KHQR merchant QR code, review payment details, select an eligible funding account, confirm the payment, and receive a trackable payment status. The design must prevent duplicate execution, protect sensitive data, support asynchronous processor outcomes, and provide operational evidence for reconciliation and support.

## Functional Requirements

| Req ID | Jira | Requirement | Priority | Acceptance Criteria |
| --- | --- | --- | --- | --- |
| FR-KHQR-001 | JIRA-KHQR-010 | The system shall validate a submitted KHQR QR payload before creating a payment instruction. | Must | Invalid, expired, unsupported, or malformed QR payloads are rejected before payment creation. |
| FR-KHQR-002 | JIRA-KHQR-011 | The system shall display merchant, amount, currency, and funding account confirmation details before customer submission. | Must | Customer can confirm only after required payment details are available and bound to the request. |
| FR-KHQR-003 | JIRA-KHQR-012 | The system shall verify that the customer is authorized to debit the selected funding account. | Must | Unauthorized or ineligible accounts are rejected with no payment instruction created. |
| FR-KHQR-004 | JIRA-KHQR-013 | The system shall enforce configured transaction, daily, channel, and customer risk limits. | Must | Limit breaches are rejected and auditable. |
| FR-KHQR-005 | JIRA-KHQR-014 | The system shall require an idempotency key for payment initiation. | Must | Missing idempotency key is rejected. |
| FR-KHQR-006 | JIRA-KHQR-015 | The system shall prevent duplicate execution for repeated requests with the same idempotency key and same payload. | Must | Repeated request returns original payment reference and current status. |
| FR-KHQR-007 | JIRA-KHQR-016 | The system shall reject repeated requests with the same idempotency key and a conflicting payload. | Must | Conflicting duplicate receives a deterministic duplicate-conflict error. |
| FR-KHQR-008 | JIRA-KHQR-017 | The system shall submit eligible payment instructions to fraud and sanctions screening when required. | Must | Held or rejected decisions prevent processor submission until resolved. |
| FR-KHQR-009 | JIRA-KHQR-018 | The system shall support asynchronous pending status when processor outcome is not final. | Must | Timeout or delayed processor response returns a pending status, not a false failure. |
| FR-KHQR-010 | JIRA-KHQR-019 | The system shall provide payment status inquiry by payment reference for the authenticated customer. | Must | Customer can retrieve only their own payment status. |
| FR-KHQR-011 | JIRA-KHQR-020 | The system shall emit customer notifications for completed, rejected, failed, or expired payment outcomes where configured. | Should | Notification is sent without exposing sensitive internal details. |
| FR-KHQR-012 | JIRA-KHQR-021 | The system shall create audit events for initiation, screening, processor submission, status changes, and duplicate requests. | Must | Audit events include correlation IDs and masked sensitive values. |

## Non-Functional Requirements

| Req ID | Jira | Requirement | Measure |
| --- | --- | --- | --- |
| NFR-KHQR-001 | JIRA-KHQR-030 | Payment initiation API shall respond within agreed mobile banking latency targets under normal load. | Target to be approved in JIRA-KHQR-030. |
| NFR-KHQR-002 | JIRA-KHQR-031 | The payment flow shall be observable. | Metrics, logs, traces, alerts, and audit events exist for all critical states. |
| NFR-KHQR-003 | JIRA-KHQR-032 | Sensitive data shall be protected in logs, traces, test evidence, and analytics. | No full account numbers, credentials, raw secrets, or unmasked sensitive QR data. |
| NFR-KHQR-004 | JIRA-KHQR-033 | The API shall be resilient to retries and network loss. | Duplicate and pending behavior validated by tests. |
| NFR-KHQR-005 | JIRA-KHQR-034 | The capability shall support reconciliation. | Payment reference, processor reference, status, timestamps, and correlation ID available to operations. |
| NFR-KHQR-006 | JIRA-KHQR-035 | The delivery pipeline shall require GitHub Actions and SonarCloud gates before release once application code exists. | Passing evidence linked in validation report. |

## Business Rules

| Rule ID | Jira | Rule | Validation |
| --- | --- | --- | --- |
| BR-KHQR-001 | JIRA-KHQR-040 | A payment may not be created without a valid QR payload, customer identity, funding account, amount, currency, and idempotency key. | Acceptance and API contract tests. |
| BR-KHQR-002 | JIRA-KHQR-041 | A pending payment must remain queryable until a terminal status is reached or the configured expiry window passes. | Acceptance scenario. |
| BR-KHQR-003 | JIRA-KHQR-042 | A risk or sanctions rejection must not disclose internal scoring or rule details to the customer. | Security review and acceptance scenario. |
| BR-KHQR-004 | JIRA-KHQR-043 | Customer-visible payment status must be consistent with operational status mapping. | QA and operations review. |
| BR-KHQR-005 | JIRA-KHQR-044 | Manual operational correction requires a separate approved process and is not part of this feature. | Release notes and operations review. |

## API Summary

- `POST /khqr/payments`: initiate a KHQR payment.
- `GET /khqr/payments/{paymentId}`: retrieve status for an authenticated customer's payment.
- Contract file: `domains/payments/capabilities/payment-initiation/features/khqr-payment/contracts/openapi.yaml`.

## Human Approval Gates

| Gate | Jira Placeholder | Required Approver | Status |
| --- | --- | --- | --- |
| Product specification approval | JIRA-KHQR-050 | Product Owner | Pending |
| Architecture approval | JIRA-KHQR-051 | Payments Architect | Pending |
| QA testability approval | JIRA-KHQR-052 | QA Lead | Pending |
| Security and risk approval | JIRA-KHQR-053 | Security and Risk Lead | Pending |
| Operations readiness approval | JIRA-KHQR-054 | Operations Lead | Pending |

## Open Questions

| Question | Owner | Jira | Status |
| --- | --- | --- | --- |
| Confirm first-release per-transaction and daily KHQR limits. | Product Owner | JIRA-KHQR-013 | Open |
| Confirm processor timeout and retry policy. | Payments Architect | JIRA-KHQR-018 | Open |
| Confirm masking rules for QR payload fields. | Security and Risk Lead | JIRA-KHQR-032 | Open |
