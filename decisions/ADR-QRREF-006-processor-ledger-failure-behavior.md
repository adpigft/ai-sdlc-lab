# ADR-QRREF-006: QR Refund Processor And Ledger Failure Behavior

## Status

Proposed

## Date

2026-06-01

## Context

Slice 2 introduces processor refund submission, ledger refund posting, timeout handling, failure handling, and integration tests. The approved implementation plan requires safe degradation: processor, ledger, audit, notification, and reconciliation failures must not create duplicate or untraceable refund states.

Processor or ledger timeout can create unknown money-movement outcomes. The architecture context requires preserving refund state, avoiding duplicate retry, and making unresolved cases operations-visible. Slice 4 will implement retry and exception handling later, so Slice 2 must define a minimal safe state and evidence model without implementing retry workflows.

## Decision Options

| Option | Description | Pros | Cons |
| --- | --- | --- | --- |
| A. Synchronous fail-fast | Call processor and ledger synchronously; fail request on timeout. | Simple API behavior. | Unsafe when outcome is unknown; increases duplicate retry risk. |
| B. Durable orchestration with pending/processing state | Persist refund and outbound attempts, record unknown outcomes, and require investigation before retry. | Strong traceability and duplicate protection. | More implementation complexity and operational state. |
| C. Fully asynchronous processing | Accept refund and process downstream via background workers. | Resilient and scalable. | Requires worker/runtime decisions beyond current repo scaffold. |
| D. Processor-only completion | Mark completed after processor succeeds; ledger/reconciliation catches up later. | Fast customer/merchant response. | Risky accounting gap if ledger fails or is delayed. |

## Recommended Decision

Use durable orchestration with explicit downstream attempt records and safe unknown-outcome handling.

For Slice 2:

- Move eligible refunds from `Requested` to `Processing` before downstream submission.
- Use idempotent outbound commands to the processor and ledger.
- Capture processor and ledger references as soon as they are available.
- If processor outcome is unknown, keep the refund traceable in `Processing` with an unresolved processor state; do not resubmit automatically.
- If processor succeeds and ledger outcome is unknown or failed, preserve processor reference and keep the refund unresolved or `Failed` according to approved finance handling; do not duplicate ledger posting.
- Mark `Completed` only after processor and ledger/accounting outcomes are both safely recorded under `ADR-QRREF-001`.
- Emit durable audit outbox events for processing start, downstream submission, reference capture, timeout, failure, and completion.
- Expose enough status for operations visibility, but do not implement Slice 4 retry or exception queue behavior in Slice 2.

## Consequences

- Slice 2 must introduce processor and ledger ports plus attempt/reference state.
- Refund state transitions must remain owned by the `Refund` aggregate.
- Retry remains blocked until Slice 4 and `ADR-QRREF-005`.
- Operations may see unresolved processing status before full exception queue support exists.
- API response semantics may stay as accepted/processing, but documented timeout behavior must be validated.

## Impacted Requirements

- `FR-QRREF-014`: Retry failed refund, because retry eligibility depends on failure classification.
- `FR-QRREF-017`: Separate refund references.
- `FR-QRREF-020`: Audit events.
- `NFR-QRREF-003`: Maximum non-terminal duration.
- `NFR-QRREF-008`: Safe degradation.

## Impacted APIs

- `POST /qr-refunds`: may return accepted/processing while downstream execution is unresolved.
- `POST /operations/qr-refunds`: same downstream behavior if operations creation is approved separately.
- `GET /qr-refunds/{refundId}`: must expose safe status and approved downstream reference availability.
- `POST /operations/qr-refunds/{refundId}/retry`: not implemented in Slice 2; behavior depends on this ADR and later `ADR-QRREF-005`.
- No OpenAPI change is approved by this ADR draft yet.

## Impacted Tests

- Processor success followed by ledger success completes refund.
- Processor timeout keeps refund traceable and prevents automatic duplicate submission.
- Ledger timeout after processor success preserves processor reference and prevents duplicate ledger posting.
- Processor failure creates safe failure evidence without retry implementation.
- Ledger failure creates safe failure evidence without retry implementation.
- Audit event exists for each downstream material event.
- Status inquiry returns safe state for processing, failed, completed, and unresolved downstream outcomes.

## Open Questions

| Question | Owner |
| --- | --- |
| Does processor provide idempotent refund submission and inquiry by client reference? | Payments Architect |
| What exact processor statuses map to success, failure, pending, or unknown? | Payments Architect |
| Does ledger support idempotent posting by refund ID or ledger client reference? | Finance Lead / Payments Architect |
| Should ledger failure after processor success be `Processing` unresolved or `Failed`? | Finance Lead / Operations Lead |
| What is the maximum age before an unresolved `Processing` refund becomes operations-visible? | Operations Lead |
| Which metrics and alerts are mandatory for processor/ledger timeouts? | DevSecOps Lead |

## Approval Required

| Approver | Approval Reference |
| --- | --- |
| Payments Architect | `JIRA-QRREF-090` |
| DevSecOps Lead | `JIRA-QRREF-093` |
| Operations Lead | `JIRA-QRREF-093` |
| Finance Lead | `JIRA-QRREF-094` |
| QA Lead | `JIRA-QRREF-080` |

