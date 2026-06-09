# KHQR Payment Intent

## Metadata

| Field | Value |
| --- | --- |
| Intent ID | INT-KHQR-001 |
| Jira Epic | JIRA-KHQR-001 |
| Confluence Page | CONF-PAY-KHQR-INTENT |
| Domain | Payments |
| Capability | KHQR payment initiation |
| Owner | Digital Payments Product Owner |
| Status | Draft pending human approval |
| Created | 2026-06-01 |

## Problem Statement

Retail mobile banking customers need to pay KHQR merchants by scanning a QR code and confirming the payment in the bank's mobile channel. The bank needs a controlled payment flow that prevents duplicate execution, applies customer and transaction limits, protects sensitive data, supports fraud and sanctions checks, and provides auditable status for operations and reconciliation.

## Desired Outcomes

- Customers can initiate a KHQR merchant payment from a valid QR payload.
- The system prevents duplicate payment execution during retries, network loss, or customer resubmission.
- Customers receive a clear payment status without exposing internal processor details.
- Operations can reconcile initiated, pending, completed, failed, and rejected payments.
- Risk, fraud, audit, and support teams receive sufficient evidence for investigation.

## In Scope

- Mobile banking KHQR merchant payment initiation.
- QR payload validation before payment submission.
- Customer confirmation and funding account selection.
- Idempotency for payment initiation.
- Payment status inquiry.
- Customer-facing pending, completed, rejected, failed, and expired states.
- Audit, reconciliation, observability, and support evidence.

## Out Of Scope

- Merchant onboarding.
- Cross-border QR payments.
- Scheduled KHQR payments.
- Payment reversal or refund execution.
- Dispute case management.
- Application code implementation.

## Primary Stakeholders

| Role | Responsibility | Approval Reference |
| --- | --- | --- |
| Product Owner | Business scope and customer journey approval | JIRA-KHQR-001 |
| Payments Architect | Integration, state model, idempotency, and resilience review | JIRA-KHQR-002 |
| QA Lead | Acceptance criteria and validation coverage review | JIRA-KHQR-003 |
| Security and Risk Lead | Fraud, data protection, and control review | JIRA-KHQR-004 |
| Operations Lead | Support, monitoring, reconciliation, and runbook review | JIRA-KHQR-005 |
| Release Manager | Release readiness and change approval | JIRA-KHQR-006 |

## Banking Assumptions

- Customer authentication and session controls are provided by the mobile banking platform.
- Funding account eligibility is determined by core banking account services.
- QR parsing follows the approved KHQR payload requirements used by the bank.
- Fraud and sanctions screening may hold or reject payments before execution.
- Payment processor status can be asynchronous and may temporarily remain pending.
- All sample data in SDLC artifacts must be synthetic or masked.

## Risks

| Risk ID | Risk | Impact | Mitigation | Owner |
| --- | --- | --- | --- | --- |
| R-KHQR-001 | Duplicate submission creates duplicate merchant payment. | Customer financial loss and operational remediation. | Mandatory idempotency key and duplicate payload controls. | Payments Architect |
| R-KHQR-002 | QR payload is tampered with before payment confirmation. | Payment to wrong merchant or amount. | Validate QR payload, display confirmation details, and bind confirmed payload to payment request. | Security and Risk Lead |
| R-KHQR-003 | Processor timeout is shown as failure while payment later completes. | Customer confusion and double payment attempt. | Use explicit pending state and status inquiry. | Product Owner |
| R-KHQR-004 | Sensitive customer or payment data leaks to logs. | Privacy, compliance, and reputational impact. | Mask logs and validate observability requirements. | DevSecOps Lead |

## Human Approval Gate

The intent is not approved until all required stakeholders record a decision in Jira.

| Gate | Jira Placeholder | Required Approver | Status |
| --- | --- | --- | --- |
| Product intent approval | JIRA-KHQR-001 | Product Owner | Pending |
| Architecture feasibility approval | JIRA-KHQR-002 | Payments Architect | Pending |
| Security and risk approval | JIRA-KHQR-004 | Security and Risk Lead | Pending |
| Operations readiness input | JIRA-KHQR-005 | Operations Lead | Pending |
