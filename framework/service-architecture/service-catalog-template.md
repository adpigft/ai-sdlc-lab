# Service Catalog Template

## Purpose

Register every service with its owning squad, contract boundaries, runtime responsibilities, and dependency review requirements.

## Template

| Field | Value |
| --- | --- |
| Service Name |  |
| Service Path |  |
| Owning Squad |  |
| Technical Owner |  |
| Business Owner |  |
| Primary Capabilities |  |
| Public APIs |  |
| Emits Events |  |
| Consumes Events |  |
| Shared Libraries |  |
| Data Stores |  |
| CODEOWNERS Path |  |
| Required Reviewers |  |
| Contract Tests |  |
| Regression Tests |  |
| Rollback Notes |  |

## Example

| Field | Value |
| --- | --- |
| Service Name | local-payment-service |
| Service Path | `services/local-payment-service/` |
| Owning Squad | Local Payments squad |
| Technical Owner | Local Payments engineering lead |
| Business Owner | Local Payments product owner |
| Primary Capabilities | Local payment initiation, status, and completion orchestration |
| Public APIs | `POST /local-payments`, `GET /local-payments/{paymentId}` |
| Emits Events | `PaymentInitiated`, `PaymentCompleted`, `PaymentFailed` |
| Consumes Events | `PaymentCompleted` from upstream payment processor or ledger when applicable |
| Shared Libraries | `payment-common` |
| Data Stores | local payment ledger, idempotency store |
| CODEOWNERS Path | `/services/local-payment-service/` |
| Required Reviewers | Local Payments squad, Payments platform when contract changes |
| Contract Tests | API contract tests, event contract tests |
| Regression Tests | local payments regression suite, shared shell smoke tests |
| Rollback Notes | revert service deployment and disable event publication if needed |

## Do / Don't Rules

Do:

- keep one primary owning squad per service
- list public APIs and emitted events
- record consumer-facing dependencies

Do not:

- leave a service uncataloged
- omit shared library dependencies
- change service ownership without updating the catalog and CODEOWNERS

