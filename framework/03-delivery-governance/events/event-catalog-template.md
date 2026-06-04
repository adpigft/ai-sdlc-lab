# Event Catalog Template

## Purpose

Register shared events with ownership, producer/consumer contracts, retention rules, and compatibility requirements.

## Template

| Field | Value |
| --- | --- |
| Event Name |  |
| Event Topic / Schema Path |  |
| Owning Squad |  |
| Producer Service |  |
| Known Consumers |  |
| Payload Contract |  |
| Ordering Guarantee |  |
| Idempotency / Deduplication |  |
| Retention Policy |  |
| CODEOWNERS Path |  |
| Required Reviewers |  |
| Schema Contract Tests |  |
| Consumer Regression Tests |  |
| Deprecation Plan |  |

## Example

| Field | Value |
| --- | --- |
| Event Name | PaymentCompleted |
| Event Topic / Schema Path | `events/payment-completed/` |
| Owning Squad | Local Payments squad |
| Producer Service | local-payment-service |
| Known Consumers | notification-service, reconciliation-service |
| Payload Contract | payment id, amount, currency, status, processor reference, ledger reference, correlation id |
| Ordering Guarantee | best effort per payment stream unless explicitly stated |
| Idempotency / Deduplication | consumer de-duplication key required |
| Retention Policy | platform standard |
| CODEOWNERS Path | `/events/payment-completed/` |
| Required Reviewers | Local Payments squad, notification owner, reconciliation owner |
| Schema Contract Tests | schema compatibility tests |
| Consumer Regression Tests | notification and reconciliation consumer suites |
| Deprecation Plan | additive change first; deprecate fields before removal |

## Do / Don't Rules

Do:

- own each event in a catalog
- name all known consumers
- prefer additive payload evolution

Do not:

- change event meaning without consumer review
- remove fields without a deprecation path
- publish events that lack consumer contract tests

