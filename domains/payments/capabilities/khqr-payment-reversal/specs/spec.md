# KHQR Payment Reversal Specification

## Metadata

| Field | Value |
| --- | --- |
| Spec ID | SPEC-KHQRREV-001 |
| Intent ID | INT-KHQRREV-001 |
| Jira Epic | JIRA-KHQRREV-001 |
| Confluence Page | CONF-PAY-KHQRREV-SPEC |
| Domain | Payments |
| Capability | KHQR Payment Reversal |
| MVP Scope | Operations-initiated full reversal of completed, not-finally-settled KHQR payments due to processor, ledger, or system error |
| Status | Draft pending BA / PO approval |
| Source Intent | `domains/payments/capabilities/khqr-payment-reversal/intent/intent.md` |

## Summary

The KHQR Payment Reversal capability enables authorized bank operations users to reverse a completed KHQR payment when a processor, ledger, or system error requires operational correction before final settlement. The MVP supports full amount reversal only, requires maker-checker approval, prevents duplicate reversal execution, requires both processor and ledger reversal outcomes, and preserves audit and reconciliation evidence.

This specification does not define architecture, API contracts, QA test design, implementation slices, or application code.

## Requirement Gaps Carried Forward

These gaps do not block a draft specification, but they must be resolved before downstream architecture, API design, test design, implementation, validation, or release as indicated.

| Gap ID | Gap | Required Resolution |
| --- | --- | --- |
| GAP-KHQRREV-001 | Exact definition of "not yet finally settled" was required before specification approval. | Resolved in this specification by the settlement eligibility rule. |
| GAP-KHQRREV-002 | Settlement cutoff source of truth is not approved. | Architecture and Finance decision before architecture approval. |
| GAP-KHQRREV-003 | Processor-ledger split outcome behavior is not approved. | Architecture, Finance, and Operations decision before implementation. |
| GAP-KHQRREV-004 | Retry rules for `Reversal Pending` and `Reversal Failed` are not approved. | Operations and Architecture decision before test design finalization. |
| GAP-KHQRREV-005 | Reversal reason-code catalog was required before specification approval. | Resolved in this specification by the MVP reversal reason-code catalog. |
| GAP-KHQRREV-006 | Customer or merchant notification scope is not approved. | Product and Compliance decision before test design finalization. |
| GAP-KHQRREV-007 | Reversal completion time and reconciliation success targets are not approved. | Product, Finance, Operations, and QA decision before validation planning. |

## Actors

| Actor | Description |
| --- | --- |
| Operations Maker | Authorized operations user who requests a KHQR payment reversal with reason code and supporting evidence. |
| Operations Checker | Separate authorized operations user who approves or rejects the reversal request. |
| Finance User | Reviews settlement cutoff, ledger correction, and reconciliation impact. |
| Payments Support User | Investigates reversal status and safe operational evidence. |

## Reversal Status Model

| Status | Meaning | Terminal |
| --- | --- | --- |
| Reversal Pending | Reversal request is approved or accepted for execution, but processor and ledger outcomes are not both final. | No |
| Reversed | Processor reversal and ledger reversal are complete and reconciliation evidence is available. | Yes |
| Reversal Failed | Reversal execution failed or reached an unresolved state requiring operations investigation. | Yes |
| Reversal Rejected | Reversal request failed authorization, eligibility, approval, reason-code, duplicate, settlement, or control checks. | Yes |

## Settlement Eligibility Rule

For MVP, a KHQR payment is not yet finally settled only when all of the following are true:

- Original payment status is `Completed`.
- Original payment has not been included in a closed merchant settlement batch.
- Original payment has no final merchant settlement confirmation.
- Original payment has no final settlement ledger posting.
- Settlement cutoff check returns `not_finally_settled` at reversal request time and again immediately before execution.

If any settlement check is unavailable, stale, contradictory, or returns `finally_settled`, the reversal request must be rejected or held from execution and made visible to operations. Architecture must identify the approved settlement cutoff source of truth before implementation.

## MVP Reversal Reason Codes

The following reason codes are approved for MVP reversal request and checker decision flows:

| Reason Code | Meaning | Allowed For |
| --- | --- | --- |
| `PROCESSOR_DUPLICATE_EXECUTION` | Processor created or confirmed duplicate payment execution requiring correction. | Request, approval, rejection |
| `PROCESSOR_STATUS_CORRECTION` | Processor status was corrected after the payment was marked completed incorrectly. | Request, approval, rejection |
| `LEDGER_POSTING_ERROR` | Ledger or core banking posting is incorrect and requires reversal before final settlement. | Request, approval, rejection |
| `SYSTEM_PROCESSING_ERROR` | Bank system error created an incorrect completed payment state or downstream instruction. | Request, approval, rejection |
| `RECONCILIATION_BREAK_CORRECTION` | Operations or finance identified a reconciliation break requiring pre-settlement reversal. | Request, approval, rejection |
| `CHECKER_REJECTED_INSUFFICIENT_EVIDENCE` | Checker rejects because evidence does not support reversal. | Rejection only |
| `CHECKER_REJECTED_NOT_ELIGIBLE` | Checker rejects because eligibility, settlement, or control criteria are not met. | Rejection only |

Free-text reason notes may be captured for operations evidence, but they do not replace the required reason code.

## Functional Requirements

| Req ID | Jira | Requirement | Priority | Acceptance Criteria |
| --- | --- | --- | --- | --- |
| FR-KHQRREV-001 | JIRA-KHQRREV-020 | The system shall allow an authorized operations maker to request a full reversal for an eligible completed KHQR payment. | Must | Given an authorized operations maker and an eligible completed KHQR payment that is not finally settled, when the maker requests a full reversal with a valid reason code and correlation ID, then a reversal request is created for checker approval. |
| FR-KHQRREV-002 | JIRA-KHQRREV-021 | The system shall reject reversal requests from users without operations reversal entitlement. | Must | Given a user without reversal entitlement, when the user requests a reversal, then the request is rejected and no reversal request is created. |
| FR-KHQRREV-003 | JIRA-KHQRREV-022 | The system shall require maker-checker approval before reversal execution. | Must | Given a reversal request, when checker approval is missing, then processor and ledger reversal execution does not start. |
| FR-KHQRREV-004 | JIRA-KHQRREV-023 | The system shall enforce maker-checker separation. | Must | Given a maker submitted the reversal request, when the same user attempts to approve it as checker, then the approval is rejected and the reversal remains unexecuted. |
| FR-KHQRREV-005 | JIRA-KHQRREV-024 | The system shall allow an authorized operations checker to approve or reject a reversal request. | Must | Given an authorized checker who is not the maker, when the checker approves the request, then the reversal is accepted for execution; when the checker rejects it, then the reversal is marked `Reversal Rejected`. |
| FR-KHQRREV-006 | JIRA-KHQRREV-025 | The system shall allow reversal only for original KHQR payments in `Completed` status. | Must | Given an original KHQR payment in any status other than `Completed`, when a reversal is requested, then the request is rejected and no reversal execution occurs. |
| FR-KHQRREV-007 | JIRA-KHQRREV-026 | The system shall allow reversal only before final settlement. | Must | Given a completed KHQR payment that fails any MVP settlement eligibility check, when a reversal is requested or about to execute, then the request is rejected or held from execution and no reversal execution occurs. |
| FR-KHQRREV-008 | JIRA-KHQRREV-027 | The system shall support full amount reversal only for MVP. | Must | Given a reversal request for less than the full original payment amount, when submitted, then the request is rejected. |
| FR-KHQRREV-009 | JIRA-KHQRREV-028 | The system shall require an approved MVP reversal reason code for every reversal request and checker decision. | Must | Given a reversal request or checker decision without one of the approved MVP reason codes, when submitted, then it is rejected and no reversal execution occurs. |
| FR-KHQRREV-010 | JIRA-KHQRREV-029 | The system shall require idempotency for reversal request and reversal execution commands. | Must | Given a reversal command without an idempotency key, when submitted, then the command is rejected. |
| FR-KHQRREV-011 | JIRA-KHQRREV-030 | The system shall prevent duplicate reversal execution for the same original payment. | Must | Given an original KHQR payment with an existing pending or completed reversal, when another reversal is requested, then no second reversal execution is created. |
| FR-KHQRREV-012 | JIRA-KHQRREV-031 | The system shall return the prior reversal result for repeated requests with the same idempotency key and same request fingerprint. | Must | Given a repeated reversal command with the same idempotency key and same payload, when submitted, then the system returns the existing reversal reference and current status. |
| FR-KHQRREV-013 | JIRA-KHQRREV-032 | The system shall reject conflicting reuse of an idempotency key. | Must | Given an idempotency key previously used with a different request fingerprint, when submitted again, then the command is rejected with a duplicate-conflict outcome. |
| FR-KHQRREV-014 | JIRA-KHQRREV-033 | The system shall execute both processor reversal and ledger reversal for an approved reversal. | Must | Given a checker-approved reversal, when execution starts, then processor and ledger reversal actions are attempted according to the approved architecture and both outcomes are recorded. |
| FR-KHQRREV-015 | JIRA-KHQRREV-034 | The system shall mark a reversal as `Reversed` only when processor reversal and ledger reversal are both complete. | Must | Given processor and ledger reversal both complete successfully, when reconciliation references are available, then the reversal status becomes `Reversed`. |
| FR-KHQRREV-016 | JIRA-KHQRREV-035 | The system shall mark a reversal as `Reversal Pending` when processor or ledger outcome is not final. | Must | Given an approved reversal where at least one required downstream outcome is delayed or unknown, when status is requested, then the reversal is shown as `Reversal Pending` with safe operational details. |
| FR-KHQRREV-017 | JIRA-KHQRREV-036 | The system shall mark a reversal as `Reversal Failed` when reversal execution fails or reaches an unresolved state requiring investigation. | Must | Given processor or ledger reversal failure that cannot complete automatically, when failure is detected, then the reversal is marked `Reversal Failed` and made visible to operations. |
| FR-KHQRREV-018 | JIRA-KHQRREV-037 | The system shall provide reversal status tracking for authorized operations users. | Must | Given an authorized operations user, when they request reversal status, then the system returns current reversal status and safe operational summary details. |
| FR-KHQRREV-019 | JIRA-KHQRREV-038 | The system shall preserve original payment, reversal, processor, ledger, settlement, and correlation references. | Must | Given a reversal request or outcome, when the reversal record is stored or updated, then all available references required for reconciliation are retained. |
| FR-KHQRREV-020 | JIRA-KHQRREV-039 | The system shall create immutable audit evidence for material reversal events. | Must | Given reversal request, approval, rejection, execution, completion, failure, duplicate attempt, or retry, when the event occurs, then an immutable audit record is captured with required masked fields. |
| FR-KHQRREV-021 | JIRA-KHQRREV-040 | The system shall distinguish reversal from refund in records, audit, reporting, and operations views. | Must | Given a reversal record is created or viewed, when it is displayed or exported, then it is identified as a bank/system operational correction and not as a merchant/business refund. |
| FR-KHQRREV-022 | JIRA-KHQRREV-041 | The system shall support reconciliation of reversed, pending, failed, and rejected reversal outcomes. | Must | Given reconciliation runs, when reversal records are matched, then matched, mismatched, pending, failed, and rejected reversal outcomes are identifiable for operations and finance. |
| FR-KHQRREV-023 | JIRA-KHQRREV-042 | The system shall support approved retry handling for failed or pending reversals only after retry rules are approved. | Should | Given retry rules are approved, when an authorized operations user retries an eligible reversal with reason code and idempotency key, then the retry is audited and duplicate-safe. |
| FR-KHQRREV-024 | JIRA-KHQRREV-043 | The system shall support customer or merchant notification only if notification scope is approved for MVP. | Should | Given notification scope is approved, when reversal reaches a notifiable outcome, then notification is sent using approved customer-safe or merchant-safe content. |

## Non-Functional Requirements

| NFR ID | Jira | Requirement | Measure |
| --- | --- | --- | --- |
| NFR-KHQRREV-001 | JIRA-KHQRREV-050 | Reversal completion shall meet the approved operations target. | Target pending approval under `GAP-KHQRREV-007`. |
| NFR-KHQRREV-002 | JIRA-KHQRREV-051 | Reversal command processing shall be idempotent and concurrency-safe. | Duplicate and concurrent reversal submissions must not create duplicate reversal execution. |
| NFR-KHQRREV-003 | JIRA-KHQRREV-052 | Reversal records shall support reconciliation. | Original payment ID, reversal ID, processor reference, ledger reference, settlement reference, amount, currency, status, timestamps, actor, approval, and correlation ID are available where applicable. |
| NFR-KHQRREV-004 | JIRA-KHQRREV-053 | Reversal audit completeness shall be enforced. | 100% of material reversal events and approval decisions have immutable audit evidence. |
| NFR-KHQRREV-005 | JIRA-KHQRREV-054 | Sensitive data shall be protected. | Customer, account, merchant, processor, and ledger identifiers are masked in logs, reports, operations views, notifications, and test evidence unless explicitly authorized. |
| NFR-KHQRREV-006 | JIRA-KHQRREV-055 | Processor and ledger uncertainty shall degrade safely. | Unknown or partial downstream outcomes do not create duplicate execution, untraceable state, or hidden financial inconsistency. |
| NFR-KHQRREV-007 | JIRA-KHQRREV-056 | Reversal workflow shall be observable. | Metrics, logs, traces, and alerts exist for request, approval, rejection, execution, pending, failed, reversed, duplicate, and settlement-cutoff outcomes. |
| NFR-KHQRREV-008 | JIRA-KHQRREV-057 | Operations status visibility shall be available for pending and failed reversals. | Pending and failed reversals are visible with safe details, owner, age, reason, and next action. |
| NFR-KHQRREV-009 | JIRA-KHQRREV-058 | Delivery pipeline evidence shall be required before release once application code exists. | GitHub Actions, relevant tests, security checks, and quality gates are linked in validation evidence. |

## Business Rules

| Rule ID | Source | Rule | Requirement Links |
| --- | --- | --- | --- |
| BR-KHQRREV-001 | Intent | A reversal can be initiated only by an authorized operations user. | FR-KHQRREV-001, FR-KHQRREV-002 |
| BR-KHQRREV-002 | Intent | A reversal requires maker-checker approval before execution. | FR-KHQRREV-003, FR-KHQRREV-005 |
| BR-KHQRREV-003 | Intent | Maker and checker must be separate users. | FR-KHQRREV-004 |
| BR-KHQRREV-004 | Intent | A reversal is allowed only for a completed KHQR payment. | FR-KHQRREV-006 |
| BR-KHQRREV-005 | Intent | A reversal is allowed only when all MVP settlement eligibility checks prove the payment is not yet finally settled. | FR-KHQRREV-007 |
| BR-KHQRREV-006 | Intent | MVP supports full amount reversal only. | FR-KHQRREV-008 |
| BR-KHQRREV-007 | Intent | Processor reversal and ledger reversal are both required for a completed reversal. | FR-KHQRREV-014, FR-KHQRREV-015 |
| BR-KHQRREV-008 | Intent | An approved MVP reversal reason code is required for every reversal request and checker decision. | FR-KHQRREV-009 |
| BR-KHQRREV-009 | Intent | Reversal commands must be idempotent. | FR-KHQRREV-010, FR-KHQRREV-011, FR-KHQRREV-012, FR-KHQRREV-013 |
| BR-KHQRREV-010 | Intent | Reversal must preserve references for reconciliation. | FR-KHQRREV-019, FR-KHQRREV-022 |
| BR-KHQRREV-011 | Specification | Reversal is not refund and must be identified separately. | FR-KHQRREV-021 |
| BR-KHQRREV-012 | Specification | Retry behavior is unavailable until retry rules are approved. | FR-KHQRREV-023 |
| BR-KHQRREV-013 | Specification | Notifications are unavailable until notification scope is approved. | FR-KHQRREV-024 |

## Acceptance Criteria Summary

| AC ID | Requirement | Acceptance Criteria |
| --- | --- | --- |
| AC-KHQRREV-001 | FR-KHQRREV-001 | Operations maker can request full reversal for an eligible completed, not-finally-settled KHQR payment. |
| AC-KHQRREV-002 | FR-KHQRREV-002 | User without reversal entitlement cannot create a reversal request. |
| AC-KHQRREV-003 | FR-KHQRREV-003 | Processor and ledger reversal execution cannot start before checker approval. |
| AC-KHQRREV-004 | FR-KHQRREV-004 | Maker cannot approve their own reversal request. |
| AC-KHQRREV-005 | FR-KHQRREV-005 | Checker can approve or reject reversal request and status reflects the decision. |
| AC-KHQRREV-006 | FR-KHQRREV-006 | Non-completed original payments are rejected for reversal. |
| AC-KHQRREV-007 | FR-KHQRREV-007 | Finally settled payments are rejected for reversal. |
| AC-KHQRREV-008 | FR-KHQRREV-008 | Partial reversal request is rejected in MVP. |
| AC-KHQRREV-009 | FR-KHQRREV-009 | Missing or invalid reversal reason code is rejected. |
| AC-KHQRREV-010 | FR-KHQRREV-010 | Missing idempotency key is rejected for reversal commands. |
| AC-KHQRREV-011 | FR-KHQRREV-011 | Existing pending or completed reversal prevents second reversal execution. |
| AC-KHQRREV-012 | FR-KHQRREV-012 | Same idempotency key and same payload returns existing reversal reference and status. |
| AC-KHQRREV-013 | FR-KHQRREV-013 | Same idempotency key and conflicting payload is rejected. |
| AC-KHQRREV-014 | FR-KHQRREV-014 | Approved reversal attempts both processor and ledger reversal actions. |
| AC-KHQRREV-015 | FR-KHQRREV-015 | Reversal becomes `Reversed` only after processor and ledger reversal both complete. |
| AC-KHQRREV-016 | FR-KHQRREV-016 | Unknown or delayed downstream outcome is visible as `Reversal Pending`. |
| AC-KHQRREV-017 | FR-KHQRREV-017 | Failed or unresolved reversal is visible as `Reversal Failed` for operations investigation. |
| AC-KHQRREV-018 | FR-KHQRREV-018 | Authorized operations users can view reversal status and safe details. |
| AC-KHQRREV-019 | FR-KHQRREV-019 | Required reconciliation references are preserved on reversal records. |
| AC-KHQRREV-020 | FR-KHQRREV-020 | Audit event is created for every material reversal event. |
| AC-KHQRREV-021 | FR-KHQRREV-021 | Reversal records and views are not reported as refunds. |
| AC-KHQRREV-022 | FR-KHQRREV-022 | Reconciliation identifies matched, mismatched, pending, failed, and rejected reversal outcomes. |

## Edge Cases And Negative Scenarios

| Scenario ID | Scenario | Expected Outcome |
| --- | --- | --- |
| EDGE-KHQRREV-001 | Reversal requested for payment in `Pending`, `Failed`, `Rejected`, or `Expired` state. | Request is rejected; no reversal execution occurs. |
| EDGE-KHQRREV-002 | Reversal requested after final settlement or when settlement status is unavailable, stale, or contradictory. | Request is rejected or held from execution with settlement-cutoff reason and operations visibility. |
| EDGE-KHQRREV-003 | Reversal requested for partial amount. | Request is rejected because MVP supports full amount only. |
| EDGE-KHQRREV-004 | Maker attempts to approve own reversal. | Approval is rejected; reversal remains unexecuted. |
| EDGE-KHQRREV-005 | Duplicate reversal request with same idempotency key and same payload. | Existing reversal reference and status are returned. |
| EDGE-KHQRREV-006 | Duplicate reversal request with same idempotency key and different payload. | Request is rejected with duplicate-conflict outcome. |
| EDGE-KHQRREV-007 | Two makers submit reversal for same payment concurrently. | Only one reversal request or execution path is created; the other is rejected or mapped to the existing reversal according to idempotency rules. |
| EDGE-KHQRREV-008 | Processor reversal completes but ledger reversal outcome is unknown. | Reversal remains `Reversal Pending` or `Reversal Failed` according to approved architecture; operations visibility is required. |
| EDGE-KHQRREV-009 | Ledger reversal completes but processor reversal outcome is unknown. | Reversal remains `Reversal Pending` or `Reversal Failed` according to approved architecture; operations visibility is required. |
| EDGE-KHQRREV-010 | Audit persistence fails for a material reversal state change. | State change must not complete without durable audit evidence or approved durable buffering. |
| EDGE-KHQRREV-011 | Operations user without status-view entitlement requests reversal status. | Request is rejected as forbidden. |
| EDGE-KHQRREV-012 | Reversal is exported to reporting or reconciliation. | Record is identified as reversal, not refund. |

## Data Needs

| Data | Purpose |
| --- | --- |
| Original payment ID | Link reversal to completed KHQR payment. |
| Reversal ID | Unique reversal reference for status, audit, and reconciliation. |
| Original payment status | Confirm `Completed` eligibility. |
| Settlement status and cutoff | Confirm not-finally-settled eligibility. |
| Amount and currency | Enforce full amount reversal. |
| Operations maker identity and entitlement | Prove authorized request. |
| Operations checker identity and entitlement | Prove authorized approval or rejection. |
| Reason code | Explain business or operational cause. |
| Idempotency key and request fingerprint | Prevent duplicate command execution. |
| Processor reference and reversal reference | Reconcile processor reversal. |
| Ledger reference and reversal reference | Reconcile ledger correction. |
| Settlement reference | Reconcile cutoff and downstream settlement impact. |
| Correlation ID | Trace request across APIs, services, logs, audit, and support evidence. |
| Audit event IDs | Prove immutable evidence for material events. |

## API And Contract Notes

- API contract is not created by this specification.
- Operations reversal endpoints are likely required, but endpoint design belongs to the architecture/API stage.
- Authentication must use bank-approved operations identity.
- Authorization must distinguish maker, checker, status-view, retry, and investigation entitlements where applicable.
- Idempotency is mandatory for reversal command APIs.
- Error responses must be deterministic, actor-safe, and must not expose sensitive processor, ledger, customer, merchant, or risk details.

## Observability

The capability must support metrics, logs, traces, alerts, and audit evidence for:

- Reversal request created.
- Checker approval and rejection.
- Eligibility rejection.
- Settlement-cutoff rejection.
- Duplicate reversal attempt.
- Idempotency replay and conflict.
- Processor reversal attempt and outcome.
- Ledger reversal attempt and outcome.
- Reversal pending age.
- Reversal failed count and age.
- Reversal completed.
- Reconciliation match and mismatch.

## Jira Story Guidance

Create Jira Stories only after specification approval. Suggested Story candidates:

| Story | Scope |
| --- | --- |
| Operations Reversal Request And Approval | Maker request, checker approval/rejection, entitlement, reason code, status transitions before execution. |
| Reversal Eligibility And Duplicate Prevention | Completed-payment check, settlement cutoff, full amount only, idempotency, duplicate original-payment reversal prevention. |
| Processor And Ledger Reversal Execution | Processor reversal, ledger reversal, pending/failed/reversed outcomes, split outcome handling after architecture approval. |
| Reversal Status And Operations Visibility | Status inquiry, pending/failed operational visibility, safe details, investigation support. |
| Audit And Reconciliation Evidence | Audit event coverage, reference preservation, reconciliation mapping, reversal-not-refund distinction. |

## Open Questions

| Question | Owner | Jira | Required Before | Status |
| --- | --- | --- | --- | --- |
| What is the exact definition of "not yet finally settled"? | Finance Lead / Payments Architect | JIRA-KHQRREV-004 | Specification approval | Resolved in settlement eligibility rule |
| Which system is the settlement cutoff source of truth? | Finance Lead / Payments Architect | JIRA-KHQRREV-004 | Architecture approval | Open |
| What should happen when processor reversal succeeds but ledger reversal fails, or ledger reversal succeeds but processor reversal fails? | Payments Architect / Finance Lead / Operations Lead | JIRA-KHQRREV-033 | Architecture approval | Open |
| Are retries allowed for `Reversal Pending` or `Reversal Failed`, and what limits apply? | Operations Lead / Payments Architect | JIRA-KHQRREV-042 | Test design finalization | Open |
| What reversal reason codes are required for MVP? | Product Owner / Operations Lead | JIRA-KHQRREV-028 | Specification approval | Resolved in MVP reversal reason-code catalog |
| Are customer or merchant notifications in scope for MVP reversal outcomes? | Product Owner / Compliance Lead | JIRA-KHQRREV-043 | Test design finalization | Open |
| What completion-time and reconciliation-rate targets apply? | Product Owner / Finance Lead / QA Lead | JIRA-KHQRREV-050 | Validation planning | Open |

## Human Approval Gates

| Gate | Jira Placeholder | Required Approver | Status |
| --- | --- | --- | --- |
| Product specification approval | JIRA-KHQRREV-060 | Product Owner | Pending |
| BA specification approval | JIRA-KHQRREV-061 | Business Analyst | Pending |
| Architecture feasibility review | JIRA-KHQRREV-062 | Payments Architect | Pending |
| QA testability review | JIRA-KHQRREV-063 | QA Lead | Pending |
| Security and risk review | JIRA-KHQRREV-064 | Security and Risk Lead | Pending |
| Operations readiness review | JIRA-KHQRREV-065 | Operations Lead | Pending |
| Finance settlement review | JIRA-KHQRREV-066 | Finance Lead | Pending |

## Next Step

BA / PO approval is required before architecture, API design, test design, Jira Story creation, implementation planning, or source code work begins. After specification approval, use `$architecture` and `$test-design`; create Jira Stories from approved business capability slices rather than one Story per requirement.
