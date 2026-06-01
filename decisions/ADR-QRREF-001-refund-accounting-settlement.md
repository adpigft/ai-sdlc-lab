# ADR-QRREF-001: QR Refund Accounting And Settlement Treatment

## Status

Proposed

## Date

2026-06-01

## Context

QR Refund MVP allows full refunds for completed KHQR payments, including payments already settled to the merchant. Merchant balance availability must not block MVP refund eligibility. Slice 2 cannot safely implement processor and ledger integration until the accounting treatment and settlement adjustment mechanism are approved.

The approved intent and specification require end-of-day reconciliation across original payment, refund transaction, payment processor, ledger, and merchant settlement records. The architecture context lists several options: merchant receivable, settlement adjustment, ledger reversal model, or processor-led refund settlement.

## Decision Options

| Option | Description | Pros | Cons |
| --- | --- | --- | --- |
| A. Merchant settlement adjustment | Post refund accounting as a merchant settlement adjustment against future merchant settlement. | Aligns with post-settlement refunds; does not require merchant balance availability at request time; clear finance control. | Requires settlement adjustment rules, reporting, and reconciliation references. |
| B. Merchant receivable | Create merchant receivable if refund occurs after settlement. | Handles insufficient future settlement volume. | Adds finance collection process and operational complexity. |
| C. Ledger reversal against original payment | Reverse or offset original ledger entries directly. | Strong traceability to original payment. | May be invalid after merchant settlement or processor settlement has completed. |
| D. Processor-led settlement only | Rely on processor settlement files to drive ledger posting. | Reduces internal orchestration. | Weak real-time control; may delay ledger state and reconciliation. |

## Recommended Decision

Use settlement adjustment as the primary MVP accounting treatment, with merchant receivable as an explicit finance-controlled fallback when settlement adjustment cannot recover the refunded amount.

Slice 2 should record separate refund, processor, ledger, and settlement adjustment references when available. Ledger posting must be traceable to the original payment ID, refund ID, merchant ID, amount, currency, correlation ID, and reason code.

Do not block refund eligibility on merchant balance availability. Do not mark a refund `Completed` until the approved processor and ledger/accounting outcomes are both safely recorded or the approved safe-degradation decision permits an alternate terminal state.

## Consequences

- Finance must approve settlement adjustment rules and receivable fallback conditions.
- Ledger posting design must support a refund posting or settlement adjustment reference.
- Reconciliation must match original payment, refund, processor refund reference, ledger reference, and settlement adjustment or receivable reference.
- Merchant reporting and operations views must expose safe status and references, not internal ledger details.
- Slice 2 remains blocked until finance confirms posting events, account mappings, and reference model.

## Impacted Requirements

- `FR-QRREF-006`: Refunds after merchant settlement.
- `FR-QRREF-017`: Separate refund references.
- `FR-QRREF-018`: End-of-day reconciliation.
- `FR-QRREF-020`: Audit events.
- `NFR-QRREF-008`: Safe degradation.

## Impacted APIs

- `POST /qr-refunds`: response status timing may depend on processor and ledger/accounting completion.
- `POST /operations/qr-refunds`: same accounting behavior as merchant initiation.
- `GET /qr-refunds/{refundId}`: should expose safe refund status and approved references when available.
- No OpenAPI change is approved by this ADR draft yet.

## Impacted Tests

- Refund after merchant settlement posts approved accounting treatment.
- Processor refund reference and ledger/accounting reference are captured.
- Ledger posting failure does not create duplicate refund or untraceable state.
- End-of-day reconciliation can match original payment, refund, processor, ledger, and merchant settlement adjustment.
- Audit records include accounting reference when available.

## Open Questions

| Question | Owner |
| --- | --- |
| Which ledger accounts and posting codes apply to post-settlement KHQR refunds? | Finance Lead |
| When should merchant receivable fallback be used? | Finance Lead |
| Does settlement adjustment require merchant notification or finance report fields? | Product Owner / Finance Lead |
| Are ledger and settlement adjustment references available synchronously? | Payments Architect |
| Can a refund be customer-visible as completed before settlement adjustment finalization? | Product Owner / Finance Lead |

## Approval Required

| Approver | Approval Reference |
| --- | --- |
| Payments Architect | `JIRA-QRREF-090` |
| Finance Lead | `JIRA-QRREF-094` |
| Operations Lead | `JIRA-QRREF-093` |
| Product Owner | `JIRA-QRREF-001` |

