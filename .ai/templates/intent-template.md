# Intent Template

## Metadata

| Field | Value |
| --- | --- |
| Intent ID | INT-YYYY-NNN |
| Jira Epic | PAY-000 |
| Capability | Example: KHQR payment initiation |
| Domain | Payments |
| Owner | Product owner name |
| Created | YYYY-MM-DD |
| Status | Draft / In Review / Approved / Rejected |

## Problem Statement

Describe the customer or operational problem in plain banking language.

Example: Retail customers need to pay KHQR merchants from the mobile banking app without manually copying merchant details or risking duplicate payment submission.

## Desired Outcome

State measurable outcomes.

- Customer payment completion rate:
- Payment exception rate:
- Support contact reduction:
- Settlement or status confirmation target:

## Scope

### In Scope

- Customer journey:
- Payment rail or processor:
- Channels:
- Currencies:
- Limits:

### Out Of Scope

- Deferred features:
- Unsupported channels:
- Unsupported payment states:

## Stakeholders

| Role | Name or Team | Responsibility |
| --- | --- | --- |
| Product owner |  | Scope and business approval |
| Architect |  | Architecture approval |
| QA lead |  | Validation approach |
| Security or risk |  | Risk and control review |
| Operations |  | Support and reconciliation |

## Assumptions

- 

## Risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Duplicate payment execution | Customer harm and financial loss |  | Require idempotency and reconciliation controls |

## Human Gate

| Approval | Jira Reference | Approver | Date | Decision |
| --- | --- | --- | --- | --- |
| Product intent approval |  |  |  |  |
