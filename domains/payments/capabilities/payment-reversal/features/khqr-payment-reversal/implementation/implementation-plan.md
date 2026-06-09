# KHQR Payment Reversal Implementation Plan

## Metadata

| Field | Value |
| --- | --- |
| Implementation Plan ID | IMPLPLAN-KHQRREV-001 |
| Intent ID | INT-KHQRREV-001 |
| Requirements ID | REQ-KHQRREV-001 |
| Context ID | CTX-KHQRREV-001 |
| Jira Epic | JIRA-KHQRREV-001 |
| Confluence Page | CONF-PAY-KHQRREV-IMPLEMENTATION |
| Domain | Payments |
| Capability | KHQR Payment Reversal |
| MVP Scope | Operations-initiated full reversal of completed, not-finally-settled KHQR payments due to processor, ledger, or system error |
| Status | Slice 1 approved for implementation |
| Created | 2026-06-01 |

## Source Artifacts

| Artifact | Path | Status |
| --- | --- | --- |
| Domain Context | `domains/payments/domain-context.md` | Reviewed |
| Intent | `domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/intent/intent.md` | Approved |
| Requirements | `domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/requirements/requirements.md` | Approved |
| Architecture Context | `domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/design/design.md` | Approved |
| API Contract | `domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/contracts/openapi.yaml` | Approved |
| Acceptance Tests | `domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/tests/acceptance.feature` | Approved |
| Traceability Matrix | `traceability/traceability-matrix.md` | Approved for KHQR reversal |

## Implementation Decision

Do not add application code yet.

The capability is ready for implementation planning, and Slice 1 is approved for implementation. The lab stack is Java 21 with a plain Java package structure, compiled with `javac`, and tested with executable `main`-method tests until Maven/Gradle and CI are added later. The current repository also has no existing application implementation under `src/`, so the first code slice must establish the minimal approved application structure using that plain Java approach.

## Guardrails

- Implement one approved slice at a time.
- Use TDD for each approved slice: failing unit test, implementation, passing test, refactor.
- Keep KHQR Payment Reversal separate from QR Refund.
- Do not implement partial reversals, post-settlement reversals, merchant/customer initiated reversals, automatic retry, notification delivery, processor internals, ledger internals, settlement platform internals, audit platform internals, or reporting platform internals.
- Require idempotency for all reversal command operations.
- Do not persist or log raw idempotency keys.
- Mask customer, account, merchant, processor, ledger, and settlement identifiers in logs, operations views, audit payloads, and test evidence unless explicitly authorized.
- Material state changes must be committed only with durable audit evidence or an approved durable audit outbox pattern.
- Unknown processor or ledger outcomes must remain traceable and operations-visible; do not blindly resubmit downstream commands.
- No hardcoded secrets, credentials, URLs, operational thresholds, or service tokens.

## Proposed Package / Module Structure

Selected stack for this lab:

- Java 21
- plain Java package structure
- `javac` compilation
- executable `main`-method tests
- no Maven or Gradle yet
- no CI pipeline yet

The structure below maps that selected stack to implementation areas.

| Area | Responsibility |
| --- | --- |
| `reversal/domain` | Reversal aggregate, statuses, reason codes, value objects, and state-transition rules. |
| `reversal/application` | Command and query handlers for request, checker decision, status, execution orchestration, and pending/failure handling. |
| `reversal/ports` | Interfaces for payment lookup, settlement cutoff, processor reversal, ledger reversal, entitlement, audit, exception queue, reconciliation, idempotency, and persistence. |
| `reversal/adapters` | Concrete adapters only for approved local or external integrations. |
| `reversal/api` | Operations-only API handlers generated or implemented from approved OpenAPI. |
| `reversal/tests` | Unit tests for domain/application logic and integration-contract tests for ports/adapters. |

## Domain Model

| Concept | Description | Key Fields |
| --- | --- | --- |
| Reversal | Aggregate for one operational reversal against one original KHQR payment. | `reversalId`, `originalPaymentId`, `amount`, `currency`, `status`, `reasonCode`, `maker`, `checker`, `processorReference`, `ledgerReference`, `settlementReference`, `correlationId`, `version`. |
| ReversalRequest | Maker command to request a full reversal. | `originalPaymentId`, `reasonCode`, `evidenceReference`, `idempotencyKey`, `correlationId`, `maker`. |
| CheckerDecision | Checker approval or rejection command. | `reversalId`, `decision`, `reasonCode`, `checker`, `correlationId`. |
| SettlementCutoffResult | Request-time and pre-execution settlement eligibility evidence. | `status`, `settlementBatchId`, `sourceTimestamp`, `generatedAt`, `freshnessSeconds`. |
| IdempotencyRecord | Duplicate prevention for reversal commands. | `operation`, `idempotencyKeyHash`, `requestFingerprint`, `resultReference`, `actorScope`, `createdAt`. |
| DownstreamOutcome | Processor or ledger reversal outcome. | `dependency`, `status`, `reference`, `receivedAt`, `rawStatusClass`. |
| AuditEvent | Immutable material event evidence. | `eventType`, `reversalId`, `originalPaymentId`, `actor`, `reasonCode`, `outcome`, `correlationId`, `timestamp`. |
| ReconciliationRecord | Finance and operations matching evidence. | `reversalId`, `originalPaymentId`, `processorReference`, `ledgerReference`, `settlementReference`, `status`, `amount`, `currency`, `correlationId`. |

## State Model

| From | To | Trigger |
| --- | --- | --- |
| None | Internal `AwaitingApproval` | Maker request passes Slice 1 request controls using a prevalidated payment eligibility snapshot and is ready for checker decision. |
| Internal `AwaitingApproval` | `Reversal Pending` | Checker approves an eligible request, pre-execution settlement cutoff passes, and execution starts. |
| None | `Reversal Rejected` | Request-time eligibility, entitlement, duplicate, reason-code, idempotency, or settlement cutoff check fails before execution. |
| Internal `AwaitingApproval` | `Reversal Rejected` | Checker rejects or pre-execution settlement cutoff fails. |
| `Reversal Pending` | `Reversed` | Processor and ledger outcomes both succeed and reconciliation references are available. |
| `Reversal Pending` | `Reversal Failed` | Processor or ledger terminal failure occurs, or pending threshold reaches approved failed handling. |

Use internal `AwaitingApproval` for the pre-approval persistence state created by Slice 1. This state is not an externally approved reversal outcome for customer, merchant, reporting, or reconciliation views. Externally approved outcomes remain `Reversal Pending`, `Reversed`, `Reversal Failed`, and `Reversal Rejected`.

## Proposed Implementation Slices

| Slice | Jira Placeholder | Scope | Requirement Coverage | Acceptance Coverage | Code Readiness |
| --- | --- | --- | --- | --- | --- |
| Slice 1 Reversal Request Foundation | JIRA-KHQRREV-070 | Reversal aggregate, request command, maker entitlement port, reason-code validation, full-amount check from a prevalidated payment snapshot, idempotency record, duplicate original-payment guard, internal `AwaitingApproval` state, request audit outbox. Settlement cutoff integration is represented only by a test double / prevalidated snapshot in this slice; the live cutoff port belongs to Slice 3. | FR-KHQRREV-001, FR-KHQRREV-002, FR-KHQRREV-006, FR-KHQRREV-008, FR-KHQRREV-009, FR-KHQRREV-010, FR-KHQRREV-011, FR-KHQRREV-012, FR-KHQRREV-013, FR-KHQRREV-020 | Scenarios tagged JIRA-KHQRREV-020 through JIRA-KHQRREV-032, JIRA-KHQRREV-051, JIRA-KHQRREV-054 | Approved for implementation using Java 21, plain Java, `javac`, and executable `main`-method tests. |
| Slice 2 Maker-Checker Decision | JIRA-KHQRREV-071 | Checker decision command, checker entitlement port, maker-checker separation, decision reason-code validation, approval/rejection audit, transition to executable pending or rejected. | FR-KHQRREV-003, FR-KHQRREV-004, FR-KHQRREV-005, FR-KHQRREV-009, FR-KHQRREV-020 | Scenarios tagged JIRA-KHQRREV-022, JIRA-KHQRREV-023, JIRA-KHQRREV-024, JIRA-KHQRREV-028 | Blocked pending Slice 1 and approved API contract. |
| Slice 3 Settlement Eligibility | JIRA-KHQRREV-072 | Merchant Settlement Service cutoff port, request-time and pre-execution checks, stale/unknown/unavailable/finally-settled handling, operations-visible non-execution outcome. | FR-KHQRREV-007, FR-KHQRREV-020 | Scenarios tagged JIRA-KHQRREV-026 | Blocked pending Slice 1 and settlement cutoff contract details. |
| Slice 4 Processor And Ledger Execution | JIRA-KHQRREV-073 | Processor and ledger reversal ports, execution orchestration, split outcome model, pending thresholds, failed-state handling, exception queue publication. | FR-KHQRREV-014, FR-KHQRREV-015, FR-KHQRREV-016, FR-KHQRREV-017, NFR-KHQRREV-006, NFR-KHQRREV-008 | Scenarios tagged JIRA-KHQRREV-033 through JIRA-KHQRREV-036 | Blocked pending Slices 1-3 and downstream contract test seams. |
| Slice 5 Status, Audit, Reconciliation, Observability | JIRA-KHQRREV-074 | Status query, status-view entitlement, masking, reference preservation, audit evidence, reconciliation projection, metrics/logs/traces/alerts. | FR-KHQRREV-018, FR-KHQRREV-019, FR-KHQRREV-020, FR-KHQRREV-021, FR-KHQRREV-022, NFR-KHQRREV-003, NFR-KHQRREV-004, NFR-KHQRREV-005, NFR-KHQRREV-007 | Scenarios tagged JIRA-KHQRREV-037 through JIRA-KHQRREV-041, JIRA-KHQRREV-056 through JIRA-KHQRREV-058 | Blocked pending Slices 1-4 and reconciliation evidence approval. |
| Slice 6 MVP Exclusions And Release Guards | JIRA-KHQRREV-075 | Explicitly disabled retry command behavior, notification exclusion guard, validation hooks for completion/reconciliation targets once approved. | FR-KHQRREV-023, FR-KHQRREV-024, NFR-KHQRREV-001, NFR-KHQRREV-009 | Scenarios tagged JIRA-KHQRREV-042, JIRA-KHQRREV-043, JIRA-KHQRREV-050 | Blocked pending Product/Compliance/QA validation target decisions. |

## First Slice Recommendation

First implement Slice 1 only after build readiness approval.

Slice 1 establishes the lowest-risk foundation for the reversal aggregate, idempotent command handling, duplicate prevention, request validation, internal `AwaitingApproval` state, and audit evidence. It should not submit processor or ledger commands, call the live Merchant Settlement Service, or expose final external APIs until the approved API contract exists.

## TDD Plan For Slice 1

Write failing unit tests first for:

- Authorized operations maker can create a full reversal request for a completed KHQR payment using a prevalidated payment eligibility snapshot.
- Created reversal request enters internal `AwaitingApproval` state and does not expose `Reversal Pending` until checker approval and pre-execution controls pass.
- User without reversal-maker entitlement is rejected.
- Non-completed original payment is rejected.
- Partial reversal request is rejected.
- Missing or invalid request reason code is rejected.
- Missing idempotency key is rejected.
- Same idempotency key and same request fingerprint returns the existing reversal reference.
- Same idempotency key and different request fingerprint is rejected.
- Existing active reversal for the original payment prevents a second reversal execution path.
- Concurrent same-payment request simulation creates only one reversal request or maps the second attempt safely.
- Request creation persists durable audit evidence in the same unit of work or fails safely.
- Sensitive identifiers are masked in emitted audit/test evidence.

Slice 1 tests must not exercise the live Merchant Settlement Service cutoff adapter. Settlement cutoff status, freshness, unknown, unavailable, stale, and contradictory outcomes are implemented in Slice 3.

## Integration And Contract Test Plan

Do not implement integration adapters until contracts are approved. Planned test seams:

| Port | Contract Need |
| --- | --- |
| Operations Entitlement | Maker, checker, and status-view entitlement decisions. |
| KHQR Payment Service | Original payment lookup with status, amount, currency, merchant/customer references, and payment identity. |
| Merchant Settlement Service | `not_finally_settled`, `finally_settled`, `unknown`, and `unavailable` cutoff outcomes plus freshness evidence. |
| Payment Processor | Reversal command and terminal, pending, unknown, timeout, and failure outcomes. |
| Ledger / Core Banking | Ledger reversal command and terminal, pending, unknown, timeout, and failure outcomes. |
| Audit Store | Durable audit outbox or audit event persistence contract. |
| Exception Queue | Pending, failed, and split-outcome operations case publication. |
| Reconciliation Platform | Reversal evidence projection or extract fields. |

## Required Build Readiness Before Code

| Item | Owner | Status |
| --- | --- | --- |
| Operations OpenAPI contract for request, status, and checker decision endpoints | Solution Architect / Developer Lead | Approved |
| KHQR reversal traceability rows linking Jira, FRs, ADRs, tests, planned slices, validation, and release evidence | BA / Architect / QA | Draft pending approval |
| Implementation start approval | Product Owner / Solution Architect / Developer Lead / QA Lead | Pending |
| First slice approval | Developer Lead / Solution Architect | Pending |
| Target implementation language/framework and test runner | Developer Lead | Approved: Java 21 / plain Java / `javac` / executable `main`-method tests |
| CI expectations for first application code under `src/` | DevSecOps Lead | Deferred until Maven/Gradle and CI are introduced |
| Completion-time and reconciliation success targets for validation planning | Product Owner / Finance Lead / Operations Lead / QA Lead | Pending before validation planning |

## Human Gate

Implementation start requires Product Owner, Solution Architect, Developer Lead, and QA Lead approval. After start approval, each slice still requires Developer Lead and Solution Architect review before QA validation.

## Next Step

Review this implementation plan, then begin Slice 1 implementation in the approved Java 21 / plain Java stack.
