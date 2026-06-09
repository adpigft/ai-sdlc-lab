# Requirements Template

## Metadata

| Field | Value |
| --- | --- |
| Requirements ID | REQ-YYYY-NNN |
| Intent ID | INT-YYYY-NNN |
| Jira Epic | PAY-000 |
| Capability |  |
| Status | Draft / In Review / Approved |
| Owner |  |

## Summary

Briefly describe the capability and the customer value.

## Functional Requirements

| Req ID | Requirement | Priority | Acceptance Criteria | Jira |
| --- | --- | --- | --- | --- |
| FR-001 | Customer can submit a KHQR payment with a valid QR payload and selected funding account. | Must | Given a valid customer, account, and QR payload, when the customer confirms, then the system creates one payment request and returns a trackable status. | PAY-000 |

## Non-Functional Requirements

| Req ID | Requirement | Measure | Jira |
| --- | --- | --- | --- |
| NFR-001 | Payment initiation response is timely. | 95th percentile under target agreed by architecture. | PAY-000 |

## Business Rules

| Rule ID | Rule | Source | Test Reference |
| --- | --- | --- | --- |
| BR-001 | A repeated request with the same idempotency key must not create a second payment. | Product and architecture review |  |

## Payment States

Define allowed states and transitions.

| State | Meaning | Customer Message | Operational Handling |
| --- | --- | --- | --- |
| pending | Processor or ledger outcome is not final. | Payment is being processed. | Monitor and reconcile. |

## API And Contract Notes

- OpenAPI file:
- Authentication:
- Authorization:
- Idempotency:
- Error model:

## Observability

- Metrics:
- Logs:
- Traces:
- Audit events:
- Dashboards:

## Open Questions

| Question | Owner | Due Date | Status |
| --- | --- | --- | --- |
|  |  |  |  |

## Review Gate

Use `framework/07-templates/review-gate-template.md` and link the approval evidence here.
