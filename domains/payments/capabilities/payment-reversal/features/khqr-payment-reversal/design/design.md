# KHQR Payment Reversal Architecture Context

## Metadata

| Field | Value |
| --- | --- |
| Context ID | CTX-KHQRREV-001 |
| Intent ID | INT-KHQRREV-001 |
| Spec ID | SPEC-KHQRREV-001 |
| Jira Epic | JIRA-KHQRREV-001 |
| Confluence Page | CONF-PAY-KHQRREV-CONTEXT |
| Domain | Payments |
| Capability | KHQR Payment Reversal |
| Status | Architecture approved for test design |
| Source Intent | `domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/intent/intent.md` |
| Source Spec | `domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/specification/specification.md` |

## Architecture Summary

KHQR Payment Reversal is an operations-only correction capability for completed KHQR payments that must be reversed before final settlement due to processor, ledger, or system error. The capability owns reversal request orchestration, maker-checker control, reversal lifecycle state, idempotency and duplicate prevention, operational visibility, audit event production, and reconciliation evidence.

This context does not define application code, QA test design, or release evidence. The approved OpenAPI contract is maintained separately under `contracts/openapi.yaml`.

## System Boundary

KHQR Payment Reversal owns:

- Operations reversal request and checker decision workflow.
- Reversal lifecycle state: `Reversal Pending`, `Reversed`, `Reversal Failed`, `Reversal Rejected`.
- Idempotency and duplicate reversal prevention for reversal commands.
- Settlement eligibility orchestration using an approved settlement cutoff source.
- Processor and ledger reversal coordination.
- Reversal audit event production.
- Reversal operational visibility for pending, failed, rejected, and completed outcomes.
- Reversal reconciliation evidence.

KHQR Payment Reversal does not own:

- Customer-initiated payments.
- Merchant refunds.
- Customer disputes or chargebacks.
- Processor implementation.
- Ledger or core banking implementation.
- Settlement platform implementation.
- Audit platform implementation.
- Notification service implementation.
- Reporting platform implementation.

## Actors And Channels

| Actor / Channel | Role | Trust Boundary |
| --- | --- | --- |
| Operations Portal | Maker request, checker approval/rejection, status inquiry, failed/pending investigation. | Internal privileged user channel |
| Operations Maker | Initiates reversal request with reason code, evidence, idempotency key, and correlation ID. | Privileged human actor |
| Operations Checker | Approves or rejects request; must be distinct from maker. | Privileged human actor |
| Finance User | Reviews settlement and reconciliation evidence. | Internal finance boundary |
| KHQR Payment Reversal Capability | Orchestrates controls, state, idempotency, downstream reversal, audit, and reconciliation evidence. | Payments platform boundary |

## Component Context

| Component | Responsibility | Data Owned |
| --- | --- | --- |
| Reversal Orchestrator | Coordinates request validation, maker-checker decision, settlement eligibility, processor/ledger reversal, state transitions, audit, and reconciliation evidence. | Reversal lifecycle state and correlation IDs |
| Reversal Eligibility Validator | Checks original payment status, settlement eligibility, full amount, reason code, duplicate reversal state, and operation entitlement. | Eligibility result only |
| Maker-Checker Control | Enforces maker/checker separation, checker entitlement, decision reason, and audit evidence. | Approval records |
| Reversal Idempotency Store | Stores idempotency keys, request fingerprints, operation scope, reversal reference, and conflict state. | Idempotency records |
| Reversal State Store | Stores reversal ID, original payment ID, amount, currency, status, reason code, maker, checker, processor/ledger references, settlement reference, timestamps, and retry metadata. | Reversal records |
| Settlement Cutoff Adapter | Queries approved settlement source to determine `not_finally_settled` or `finally_settled`. | No canonical data; adapter result only |
| Processor Reversal Adapter | Sends processor reversal command and retrieves/records processor outcome/reference. | Processor reversal references |
| Ledger Reversal Adapter | Sends ledger reversal command and retrieves/records ledger outcome/reference. | Ledger reversal references |
| Audit Event Producer | Emits immutable audit events for all material reversal and control events. | Audit event payloads |
| Exception Queue Publisher | Publishes pending, failed, or split-outcome reversal cases for operations investigation. | Exception queue event payloads |
| Reconciliation Data Publisher | Publishes reversal records and references for matching across payment, reversal, processor, ledger, and settlement. | Reconciliation extract/feed payloads |

## Integration Context

| Integration | Direction | Purpose | Architecture Position |
| --- | --- | --- | --- |
| Operations Portal | Inbound / outbound | Request reversal, approve/reject, view status, investigate pending/failed reversals. | Required for MVP. |
| Operations Identity / Entitlement | Outbound lookup | Validate maker, checker, status-view, and future retry entitlements. | Required for MVP. |
| KHQR Payment Service | Outbound lookup | Retrieve original payment status, amount, currency, customer/merchant references, processor/ledger references, and payment identity. | Required for MVP. |
| Settlement Platform / Merchant Settlement Service | Outbound lookup | Source of truth for settlement cutoff and final settlement status. | Required for architecture approval. |
| Payment Processor | Outbound command / inbound status | Execute or confirm processor-side reversal. | Required for MVP execution. |
| Ledger / Core Banking | Outbound command / inbound status | Execute or confirm ledger-side reversal. | Required for MVP execution. |
| Audit Store | Outbound event | Persist immutable audit records. | Required for MVP. |
| Exception Queue / Operations Case Queue | Outbound event | Surface pending, failed, split-outcome, and investigation-needed reversals. | Required for MVP. |
| Reconciliation Platform | Outbound extract/feed | Match original payment, reversal, processor, ledger, and settlement records. | Required for release readiness. |
| Notification Service | Outbound event | Notify customer or merchant only if scope is approved. | Not in MVP until Product/Compliance approval. |

## Data Ownership

| Data | Owner | Notes |
| --- | --- | --- |
| Original KHQR payment record | KHQR Payment Service | Source for original payment status, amount, currency, payment ID, processor reference, ledger reference, and merchant/customer references. |
| Final settlement status | Settlement Platform / Merchant Settlement Service | Source of truth for `not_finally_settled` or `finally_settled`. |
| Reversal lifecycle record | KHQR Payment Reversal Capability | Source for reversal status and operational view. |
| Reversal idempotency record | KHQR Payment Reversal Capability | Must prevent duplicate reversal commands and conflicting duplicate keys. |
| Maker-checker approval record | KHQR Payment Reversal Capability | Source for reversal control evidence. |
| Operations entitlements | Operations identity / entitlement service | Source for maker, checker, status-view, and future retry permissions. |
| Processor reversal reference | Payment Processor | Captured by reversal capability when available. |
| Ledger reversal reference | Ledger / Core Banking | Captured by reversal capability when available. |
| Audit event | Audit Store | Immutable evidence for material events. |
| Reconciliation result | Reconciliation Platform | Matching and mismatch evidence; not canonical reversal state. |

## Proposed Architecture Decisions

| Decision ID | Decision | Status | Rationale | Downstream Impact |
| --- | --- | --- | --- | --- |
| ADR-KHQRREV-001 | Use Merchant Settlement Service cutoff status interface as settlement cutoff source of truth. | Accepted by architecture approval | Settlement status must be external to reversal state and authoritative for final settlement. Reversal rejects or holds execution when this source is unavailable, stale beyond 60 seconds, contradictory, or `finally_settled`. | API and tests must include settlement unavailable, stale, contradictory, and finally-settled scenarios. |
| ADR-KHQRREV-002 | Reversal owns a separate reversal aggregate from KHQR payment and QR Refund. | Accepted by architecture approval | Reversal is a bank/system correction, not a merchant refund or customer payment state. Separate ownership prevents refund/reversal reporting ambiguity. | Traceability and reporting must identify reversal separately from refund. |
| ADR-KHQRREV-003 | Idempotency and original-payment reversal uniqueness are enforced inside KHQR Payment Reversal. | Accepted by architecture approval | API gateway idempotency alone cannot guarantee one reversal per original payment or protect processor/ledger coordination. | Implementation must include idempotency store, request fingerprint, and unique active reversal per original payment. |
| ADR-KHQRREV-004 | Processor-ledger split outcomes remain locally traceable and operations-visible; no automatic compensating command is attempted without approved retry policy. | Accepted by architecture approval | Processor and ledger outcomes can diverge. Automatic compensation can worsen financial inconsistency without operation-specific policy. | Test design must cover processor-success/ledger-unknown, ledger-success/processor-unknown, processor-failure, ledger-failure, and both-success. |
| ADR-KHQRREV-005 | Retry is excluded from MVP execution until retry policy is approved. | Accepted by architecture approval | Specification allows retry only after rules are approved. Keeping retry out of first architecture baseline avoids uncontrolled repeated money movement. | Test design should verify retry is rejected or disabled until policy approval. |
| ADR-KHQRREV-006 | Notifications are out of MVP until Product/Compliance approve scope and templates. | Accepted by architecture approval | Reversal is operations correction and may require careful customer/merchant communication. | Test design should not require notification evidence before scope approval. |

## Conceptual Flow: Reversal Request And Approval

1. Operations maker submits reversal request with original payment ID, reason code, idempotency key, evidence reference, and correlation ID.
2. Reversal Orchestrator validates maker entitlement.
3. Reversal Idempotency Store checks idempotency key and request fingerprint.
4. Reversal Eligibility Validator retrieves original KHQR payment details.
5. Eligibility Validator checks payment is `Completed`, full amount only, not already reversed or pending reversal, and reason code is approved.
6. Settlement Cutoff Adapter checks the approved settlement source.
7. If settlement status is `finally_settled`, unavailable, stale beyond 60 seconds, or contradictory, request is rejected or held from execution according to architecture approval conditions and operations visibility rules.
8. Reversal Orchestrator creates reversal request and maker-checker approval record.
9. Checker approves or rejects request.
10. Maker-Checker Control enforces checker entitlement and maker/checker separation.
11. Rejection moves status to `Reversal Rejected` and emits audit/reconciliation evidence.
12. Approval moves reversal to execution only after settlement eligibility is checked again immediately before execution.

## Conceptual Flow: Processor And Ledger Execution

1. Approved reversal enters `Reversal Pending`.
2. Reversal Orchestrator records durable state and audit event before downstream submission.
3. Processor Reversal Adapter submits processor reversal with reversal reference, original payment reference, amount, currency, idempotency/correlation references, and reason code.
4. Ledger Reversal Adapter submits ledger reversal with reversal reference, original payment reference, amount, currency, correlation references, and reason code.
5. Reversal becomes `Reversed` only when both processor and ledger outcomes are successful and references are recorded.
6. If either outcome is unknown or delayed, reversal remains `Reversal Pending` with operations-visible details and alerts.
7. If either outcome fails or an unresolved split outcome breaches approved handling thresholds, reversal becomes `Reversal Failed` and is published to the exception queue.
8. Reconciliation Data Publisher emits reversal evidence for matching and mismatch handling.

## Processor / Ledger Split Outcome Model

| Processor Outcome | Ledger Outcome | Reversal Status | Required Handling |
| --- | --- | --- | --- |
| Success | Success | `Reversed` | Store both references, audit completion, publish reconciliation evidence. |
| Success | Pending / Unknown | `Reversal Pending` | Do not resubmit processor reversal. Make case operations-visible; continue ledger inquiry/recovery only after approved policy. |
| Pending / Unknown | Success | `Reversal Pending` | Do not resubmit ledger reversal. Make case operations-visible; continue processor inquiry/recovery only after approved policy. |
| Success | Failed | `Reversal Failed` | Do not auto-compensate. Publish exception; Finance/Ops decision required. |
| Failed | Success | `Reversal Failed` | Do not auto-compensate. Publish exception; Finance/Ops decision required. |
| Failed | Failed | `Reversal Failed` | Publish exception and audit failure. |
| Pending / Unknown | Pending / Unknown | `Reversal Pending` | Monitor age, alert, and expose to operations. |

Pending-to-failed thresholds for MVP:

| Threshold | Handling |
| --- | --- |
| 5 minutes after downstream submission with no terminal processor or ledger outcome | Keep `Reversal Pending`, emit alert, and expose pending-age detail to operations. |
| 15 minutes after downstream submission with no terminal outcome for either dependency | Keep `Reversal Pending`, publish exception queue case, and require operations ownership. |
| 60 minutes after downstream submission with no terminal outcome after approved inquiry attempts | Move to `Reversal Failed`, preserve all references, and require Finance / Operations decision before retry or manual correction. |
| Explicit processor or ledger terminal failure at any time | Move to `Reversal Failed` unless both dependencies have already completed successfully. |

Timeouts do not imply downstream failure by themselves. They create pending or failed local reversal state according to the thresholds above while preventing blind resubmission.

## Settlement Cutoff Source

The approved architecture source of truth for settlement cutoff is the Merchant Settlement Service cutoff status interface.

Expected interface behavior:

- Input: original payment ID, merchant ID when available, amount, currency, and correlation ID.
- Output status: `not_finally_settled`, `finally_settled`, `unknown`, or `unavailable`.
- Output evidence: settlement batch ID when available, settlement status timestamp, source system timestamp, and response generated timestamp.
- Freshness rule: cutoff status is usable only when generated no more than 60 seconds before the reversal decision point.
- Request-time check: required before creating an executable reversal request.
- Pre-execution check: required after checker approval and immediately before processor or ledger reversal submission.

If the interface returns `unknown` or `unavailable`, if required evidence is missing, or if the response is older than 60 seconds, the reversal must not execute. The request is rejected before checker approval when detected at request time, or moved to `Reversal Rejected` / operations-visible non-executed state when detected after checker approval but before execution.

## API Design Guidance

Architecture expects operations-only APIs. The approved OpenAPI contract is captured in `domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/contracts/openapi.yaml`.

Operations:

- `POST /operations/khqr-payment-reversals`
- `GET /operations/khqr-payment-reversals/{reversalId}`
- `POST /operations/khqr-payment-reversals/{reversalId}/decision`

API requirements:

- Require authenticated operations identity.
- Require maker/checker/status entitlements.
- Require idempotency key on command operations.
- Require correlation ID.
- Use approved MVP reason codes.
- Return actor-safe errors for entitlement, eligibility, duplicate, settlement cutoff, idempotency conflict, and invalid state.
- Do not expose sensitive processor, ledger, customer, merchant, or risk details in responses.

## Security And Control Context

- Operations users must have explicit maker, checker, and status-view entitlements.
- Maker and checker must be different users.
- Reversal request payloads must be bound to idempotency key fingerprints.
- A unique active reversal constraint must exist per original payment.
- Settlement cutoff must be checked at request time and again immediately before execution.
- Sensitive data must be masked in logs, operations views, audit, reporting, and test evidence unless explicitly authorized.
- Material events must produce immutable audit records before or atomically with durable state change.
- Reversal must be distinguishable from QR Refund in records, reporting, audit, and reconciliation.

## Observability Context

Required metrics and alerts:

- Reversal request count.
- Reversal approval and rejection count.
- Settlement cutoff rejection count.
- Settlement cutoff unavailable/stale/contradictory count.
- Duplicate reversal attempt count.
- Idempotency replay and conflict count.
- Processor reversal success, pending, unknown, and failure count.
- Ledger reversal success, pending, unknown, and failure count.
- Split-outcome count.
- Reversal pending age.
- Reversal failed count and age.
- Audit event failure count.
- Reconciliation mismatch count.

## Failure Handling Context

| Failure | Expected Handling |
| --- | --- |
| Operations entitlement unavailable | Reject or defer safely; do not create executable reversal without entitlement evidence. |
| Original payment lookup unavailable | Reject or defer safely; do not create executable reversal without payment evidence. |
| Settlement cutoff unavailable, stale beyond 60 seconds, unknown, or contradictory | Reject before checker approval when detected at request time; after checker approval move to `Reversal Rejected` or operations-visible non-executed state; do not execute reversal. |
| Idempotency store unavailable | Reject or defer safely; do not execute command without duplicate protection. |
| Audit persistence unavailable | Do not complete material state change unless durable audit buffering is approved. |
| Processor timeout | Preserve state; do not blindly resubmit; set or keep `Reversal Pending`; expose to operations. |
| Ledger timeout | Preserve state; do not blindly resubmit; set or keep `Reversal Pending`; expose to operations. |
| Processor/ledger split outcome | Follow split outcome model; no automatic compensation until policy approval. |
| Reconciliation feed failure | Reversal records remain replayable/re-extractable; alert operations. |

## Data Classification

| Data | Classification | Handling |
| --- | --- | --- |
| Customer identifier | Confidential | Mask in logs, operations views, reports, and test evidence unless explicitly authorized. |
| Merchant identifier | Confidential | Display only to authorized operations and finance users. |
| Original payment ID | Confidential | Required for traceability; protect in external views. |
| Reversal ID | Confidential | Required for status, support, audit, and reconciliation. |
| Amount and currency | Confidential | Display to authorized users; protect in logs and analytics. |
| Reason code and reason notes | Internal / Confidential | Visible only to authorized operations, support, risk, and finance users. |
| Processor reference | Confidential | Internal support and reconciliation use. |
| Ledger reference | Restricted | Finance, operations, and reconciliation use only. |
| Audit events | Restricted | Immutable, access controlled, retained by approved policy. |

## Implementation Planning Notes

Implementation slices are not approved by this architecture draft. Candidate slices after architecture and test design approval:

| Candidate Slice | Scope | Dependency |
| --- | --- | --- |
| Slice 1 Reversal Request Foundation | Reversal aggregate, maker request, entitlement check, reason code validation, idempotency, duplicate prevention, request audit. | Architecture approval. |
| Slice 2 Maker-Checker Decision | Checker decision, maker/checker separation, approval/rejection audit, status transition to rejected or pending. | Slice 1. |
| Slice 3 Settlement Eligibility | Settlement cutoff adapter, request-time and pre-execution checks, settlement rejection/hold behavior. | Settlement source approval. |
| Slice 4 Processor And Ledger Execution | Processor reversal adapter, ledger reversal adapter, split-outcome state handling, exception queue publication. | Processor/ledger split outcome approval. |
| Slice 5 Operations Visibility And Reconciliation | Status view, pending/failed operational visibility, reconciliation evidence feed. | Slices 1-4. |

## Context Open Questions

| Question | Owner | Source | Status |
| --- | --- | --- | --- |
| Which exact Settlement Platform / Merchant Settlement Service interface is approved for cutoff checks? | Payments Architect / Finance Lead | GAP-KHQRREV-002 | Resolved by Merchant Settlement Service cutoff status interface |
| What stale-age threshold makes a settlement cutoff result unusable? | Payments Architect / Finance Lead | GAP-KHQRREV-002 | Resolved as 60 seconds |
| What timeout thresholds move processor/ledger unknown outcomes from pending to failed? | Payments Architect / Operations Lead | GAP-KHQRREV-003 | Resolved as 5-minute alert, 15-minute exception queue, 60-minute failed threshold |
| Are retries allowed for pending or failed reversals, and what limits apply? | Operations Lead / Payments Architect | GAP-KHQRREV-004 | Open before final test design |
| Are customer or merchant notifications in MVP scope? | Product Owner / Compliance Lead | GAP-KHQRREV-006 | Open before final test design |
| What reversal completion and reconciliation success targets apply? | Product Owner / Finance Lead / QA Lead | GAP-KHQRREV-007 | Open before validation planning |

## Human Approval

| Gate | Jira Placeholder | Required Approver | Status |
| --- | --- | --- | --- |
| Architecture approval | JIRA-KHQRREV-062 | Payments Architect | Approved |
| Finance architecture input | JIRA-KHQRREV-066 | Finance Lead | Pending |
| Operations architecture input | JIRA-KHQRREV-065 | Operations Lead | Pending |
| Security and risk architecture input | JIRA-KHQRREV-064 | Security and Risk Lead | Pending |

## Next Step

Run `Review.` for the architecture draft. Architecture approval is required before test design relies on this context. Do not create application code from this context.
