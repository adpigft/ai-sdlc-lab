# KHQR Payment Reversal Intent

## Metadata

| Field | Value |
| --- | --- |
| Intent ID | INT-KHQRREV-001 |
| Jira Epic | JIRA-KHQRREV-001 |
| Confluence Page | CONF-PAY-KHQRREV-INTENT |
| Domain | Payments |
| Capability | KHQR Payment Reversal |
| MVP Scope | Operations-initiated full reversal of completed, not-finally-settled KHQR payments due to processor, ledger, or system error |
| Owner | Digital Payments Product Owner |
| Status | Intent approved for artifact creation; pending specification approval |
| Created | 2026-06-01 |

## Problem Statement

Bank operations users need a controlled way to reverse completed KHQR payments when a processor, ledger, or system error requires an operational correction before final settlement. The bank needs reversal processing that is auditable, maker-checker controlled, resilient to duplicate execution, traceable to the original payment, and reconciled across processor, ledger, and settlement records.

## Desired Outcomes

- Operations can reverse eligible KHQR payments without using the merchant refund flow.
- Processor and ledger reversal actions remain consistent and traceable.
- Duplicate reversals are prevented during retries, resubmissions, or concurrent operations.
- Reversal outcomes are visible to operations and finance.
- Reconciliation can prove the original payment, reversal, processor activity, ledger postings, and settlement position.
- Audit evidence exists for every material reversal event and approval decision.

## Success Metrics

| Metric | Target |
| --- | --- |
| Reversal completion time | Target to be approved during specification or architecture review |
| Reconciliation success rate | Target to be approved by Finance and Operations |
| Duplicate reversal prevention | 100% duplicate reversal prevention for approved command paths |
| Audit completeness | 100% of material reversal events and approval decisions audited |

## In Scope

- Full amount reversal only.
- Completed KHQR payments only.
- Payments that are not yet finally settled.
- Operations-initiated reversals only.
- Reversal due to processor, ledger, or system error.
- Processor reversal and ledger reversal are both required for MVP.
- Maker-checker approval before reversal execution.
- Reversal status tracking for operations users.
- Reconciliation evidence across original payment, reversal, processor, ledger, and settlement references.
- Immutable audit trail for request, approval, rejection, processing, completion, failure, and retry where retry is approved.

## Out Of Scope

- Merchant-initiated refunds.
- Customer-initiated reversals.
- Customer dispute or chargeback case management.
- Partial reversals.
- Reversals after final settlement.
- Business goodwill refunds or merchant service adjustments.
- Non-KHQR payment reversals.
- Application code implementation.

## Capability Boundary

KHQR Payment Reversal is distinct from QR Refund.

| Capability | Boundary |
| --- | --- |
| QR Refund | Merchant or business initiated return of funds for completed KHQR payments. |
| KHQR Payment Reversal | Bank or system operational correction for completed KHQR payments affected by processor, ledger, or system error before final settlement. |

## Actors

| Actor | Description |
| --- | --- |
| Operations Maker | Authorized operations user who requests a payment reversal with reason code and supporting evidence. |
| Operations Checker | Separate authorized operations user who approves or rejects the reversal request. |
| Finance User | Reviews settlement and reconciliation impact. |
| Payments Support User | Investigates reversal status and operational evidence. |

## Business Rules

| Rule ID | Rule |
| --- | --- |
| BR-KHQRREV-001 | A reversal can be initiated only by an authorized operations user. |
| BR-KHQRREV-002 | A reversal requires maker-checker approval before execution. |
| BR-KHQRREV-003 | Maker and checker must be separate users. |
| BR-KHQRREV-004 | A reversal is allowed only for a completed KHQR payment. |
| BR-KHQRREV-005 | A reversal is allowed only before final settlement. |
| BR-KHQRREV-006 | MVP supports full amount reversal only. |
| BR-KHQRREV-007 | Processor reversal and ledger reversal are both required for a completed reversal. |
| BR-KHQRREV-008 | A reversal reason code is required. |
| BR-KHQRREV-009 | Reversal commands must be idempotent to prevent duplicate reversal execution. |
| BR-KHQRREV-010 | Reversal must preserve original payment, processor, ledger, settlement, and correlation references for reconciliation. |

## Reversal Statuses

| Status | Meaning |
| --- | --- |
| Reversal Pending | Reversal has been approved or accepted for execution, but processor and ledger outcomes are not complete. |
| Reversed | Processor and ledger reversal have completed and reconciliation evidence is available. |
| Reversal Failed | Reversal execution failed or reached an unresolved state requiring operations investigation. |
| Reversal Rejected | Reversal request failed eligibility, authorization, approval, reason-code, duplicate, or settlement checks. |

## Operational Controls

- Operations users require reversal entitlement.
- Reversal request requires reason code and correlation ID.
- Maker-checker approval is required before execution.
- Maker cannot approve their own reversal request.
- Duplicate reversal attempts must be rejected or return the prior reversal result when idempotency rules allow.
- Failed or pending reversals must be visible to operations with safe investigation details.
- Reversal actions must not rely on merchant refund permissions.

## Audit Requirements

Audit all material events:

- Reversal request.
- Maker submission.
- Checker approval.
- Checker rejection.
- Eligibility rejection.
- Processor reversal attempt and outcome.
- Ledger reversal attempt and outcome.
- Reversal completion.
- Reversal failure.
- Duplicate reversal attempt.
- Retry attempt if retry is later approved.

Audit records must capture:

- Original payment ID.
- Reversal ID.
- Initiator.
- Approver where applicable.
- User role.
- Reason code.
- Timestamp.
- Processor reference where available.
- Ledger reference where available.
- Settlement reference where available.
- Correlation ID.

Sensitive customer, merchant, processor, and ledger data must be masked where not explicitly authorized.

## Reconciliation Requirements

The reversal capability must support reconciliation across:

- Original KHQR payment.
- Reversal transaction.
- Payment processor activity.
- Ledger or core banking postings.
- Settlement state.
- Operations approval evidence.

Reconciliation must identify matched, mismatched, pending, and failed reversal outcomes.

## Assumptions

- Customer authentication is not in scope because reversals are operations initiated.
- Merchant refund behavior remains owned by QR Refund.
- The KHQR Payment capability remains the source for original payment status and ownership data.
- Final settlement status can be determined by an approved settlement source of truth.
- Processor and ledger integrations support reversal or equivalent correction operations for eligible payments.
- All examples and evidence in SDLC artifacts use synthetic or masked data.

## Risks

| Risk ID | Risk | Impact | Mitigation | Owner |
| --- | --- | --- | --- | --- |
| R-KHQRREV-001 | Duplicate reversal execution. | Financial loss, reconciliation breaks, customer or merchant impact. | Mandatory idempotency, original-payment reversal uniqueness, and audit evidence. | Payments Architect |
| R-KHQRREV-002 | Reversal attempted after final settlement. | Incorrect settlement or finance adjustment. | Settlement cutoff validation before approval and execution. | Finance Lead |
| R-KHQRREV-003 | Processor reversal succeeds but ledger reversal fails, or the reverse. | Inconsistent financial state. | Safe degradation, pending/failed state handling, exception queue, reconciliation evidence. | Payments Architect / Operations Lead |
| R-KHQRREV-004 | Maker-checker controls are bypassed. | Unauthorized operational correction. | Separate entitlements, maker-checker separation, and immutable audit trail. | Security and Risk Lead |
| R-KHQRREV-005 | Reversal is confused with refund. | Incorrect product behavior, reporting, and support handling. | Explicit capability boundary and separate Jira/Git traceability. | Product Owner |

## Open Questions

| Question | Owner | Required Before |
| --- | --- | --- |
| What is the exact definition of "not yet finally settled"? | Finance Lead / Payments Architect | Resolved in `SPEC-KHQRREV-001` settlement eligibility rule |
| Which system is the settlement cutoff source of truth? | Finance Lead / Payments Architect | Architecture approval |
| What should happen when processor reversal succeeds but ledger reversal fails, or ledger reversal succeeds but processor reversal fails? | Payments Architect / Finance Lead / Operations Lead | Architecture approval |
| Are retries allowed for `Reversal Pending` or `Reversal Failed`, and what limits apply? | Operations Lead / Payments Architect | Specification approval |
| What reversal reason codes are required for MVP? | Product Owner / Operations Lead | Resolved in `SPEC-KHQRREV-001` MVP reason-code catalog |
| Are customer or merchant notifications in scope for MVP reversal outcomes? | Product Owner / Compliance Lead | Specification approval |
| What completion-time and reconciliation-rate targets apply? | Product Owner / Finance Lead / QA Lead | Specification approval |

## Human Approval Gate

The intent is approved for artifact creation based on explicit user approval in chat on 2026-06-01. Specification work requires the next PO / BA approval gate.

| Gate | Jira Placeholder | Required Approver | Status |
| --- | --- | --- | --- |
| Product intent approval | JIRA-KHQRREV-001 | Product Owner / BA | Approved |
| Architecture feasibility input | JIRA-KHQRREV-002 | Payments Architect | Pending |
| Operations readiness input | JIRA-KHQRREV-003 | Operations Lead | Pending |
| Finance settlement input | JIRA-KHQRREV-004 | Finance Lead | Pending |
| Security and risk input | JIRA-KHQRREV-005 | Security and Risk Lead | Pending |
| QA intent review | JIRA-KHQRREV-006 | QA Lead | Pending |

## Next Step

After PO / BA approval to proceed, use `$specification` to create the KHQR Payment Reversal specification. When workflow-state is adopted, prepare `workflow-state.yaml` to move from `intent_review` to `specification_review`.
