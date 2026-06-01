# ADR-QRREF-003: QR Refund Cross-System Idempotency And Concurrency

## Status

Proposed

## Date

2026-06-01

## Context

Slice 1 established local refund creation controls: keyed HMAC idempotency hashes, request payload hashes, refund creation unit-of-work contract, unique original payment constraint, and aggregate versioning contract. Slice 2 extends idempotency and concurrency across processor and ledger integrations.

The approved implementation plan requires that downstream outages must not create duplicate refunds or duplicate ledger postings. Processor and ledger integrations may have their own idempotency keys, timeout behavior, and inquiry mechanisms.

## Decision Options

| Option | Description | Pros | Cons |
| --- | --- | --- | --- |
| A. QR Refund owns cross-system idempotency | Generate stable outbound client references from refund ID and operation type; persist attempts and references. | Strong local control and traceability. | Requires careful mapping to processor/ledger behavior. |
| B. Delegate idempotency to processor and ledger | Depend on external systems to reject duplicates. | Less local logic. | Weakens bank control and complicates unknown outcomes. |
| C. API gateway idempotency only | Use gateway idempotency for inbound calls. | Simple inbound replay protection. | Does not protect downstream processor/ledger commands. |
| D. Ledger lock as global control | Serialize on ledger before processor. | Strong accounting guard. | May not prevent processor duplicate submissions and can couple refund flow to ledger availability. |

## Recommended Decision

QR Refund owns cross-system idempotency and concurrency orchestration.

Use stable outbound client references derived from refund ID, original payment ID, operation type, and attempt sequence. Persist outbound attempt records before calling processor or ledger. Use processor and ledger idempotency features where available, but do not depend on them as the only control.

Concurrency controls:

- Keep the Slice 1 unique original-payment full-refund constraint.
- Keep aggregate versioning or optimistic locking for refund state changes.
- Serialize downstream execution per refund ID.
- Never submit a second processor refund while the previous processor outcome is unknown.
- Never submit a second ledger posting while the previous ledger outcome is unknown.
- Use inquiry/reconciliation before retrying unknown downstream outcomes.

## Consequences

- Slice 2 needs outbound attempt state for processor and ledger calls.
- Processor and ledger ports must accept client references and correlation IDs.
- If external systems do not support idempotency or inquiry, Slice 2 remains high risk and may require manual operations controls before coding.
- Retry design in Slice 4 must consume the same attempt records and unknown-outcome classification.
- CI/integration tests must prove duplicate prevention across inbound and downstream execution paths.

## Impacted Requirements

- `FR-QRREF-004`: One full refund per payment.
- `FR-QRREF-009`: Idempotency required.
- `FR-QRREF-010`: Idempotency conflict.
- `FR-QRREF-014`: Retry failed refund.
- `FR-QRREF-017`: Separate refund references.
- `FR-QRREF-020`: Audit events.
- `NFR-QRREF-005`: Idempotency and concurrency.
- `NFR-QRREF-008`: Safe degradation.

## Impacted APIs

- `POST /qr-refunds`: inbound idempotency remains required; downstream idempotency is internal.
- `POST /operations/qr-refunds`: same control if operations creation is implemented later.
- `POST /operations/qr-refunds/{refundId}/retry`: future retry must use stored attempt state and cannot bypass unknown-outcome controls.
- `GET /qr-refunds/{refundId}`: may need safe display of pending/downstream reference state.
- No OpenAPI change is approved by this ADR draft yet.

## Impacted Tests

- Concurrent same-payment refund submissions create only one refund.
- Same inbound idempotency key and payload replays original result.
- Same inbound idempotency key with different payload rejects conflict.
- Processor timeout does not trigger duplicate processor submission.
- Ledger timeout does not trigger duplicate ledger posting.
- Retry cannot proceed while downstream outcome is unknown.
- Outbound client references are stable for replay and unique per operation/attempt.
- Audit captures duplicate attempts, idempotency conflicts, downstream submissions, and unknown outcomes.

## Open Questions

| Question | Owner |
| --- | --- |
| What idempotency key or client reference format does the processor require? | Payments Architect |
| Does the processor support inquiry by outbound client reference? | Payments Architect |
| What idempotency key or client reference format does ledger/core banking require? | Finance Lead / Payments Architect |
| Does ledger/core banking support inquiry by outbound client reference? | Finance Lead / Payments Architect |
| What attempt sequence and retry policy is allowed before Slice 4? | Operations Lead |
| How long must downstream attempt records be retained? | Compliance Lead |

## Approval Required

| Approver | Approval Reference |
| --- | --- |
| Payments Architect | `JIRA-QRREF-090` |
| Security and Risk Lead | `JIRA-QRREF-091` |
| DevSecOps Lead | `JIRA-QRREF-093` |
| Operations Lead | `JIRA-QRREF-093` |
| Finance Lead | `JIRA-QRREF-094` |

