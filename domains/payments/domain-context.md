# Payments Domain Context

## Purpose

Capture shared Payments domain language, APIs, events, integrations, business rules, and reusable delivery patterns used across payment capabilities.

This file is domain-level context. Capability context remains under `domains/payments/capabilities/<capability>/capability-context.md`; feature delivery source of truth remains under `domains/payments/capabilities/<capability>/features/<feature>/`.

## Glossary

| Term | Meaning |
| --- | --- |
| KHQR | QR payment standard used for merchant payment initiation. |
| Payment | A customer-initiated money movement instruction to a merchant. |
| Refund | A money movement that returns funds for a completed payment to the original payer. |
| Original Payment | The completed payment record used as the source for refund eligibility, amount, merchant ownership, and reconciliation. |
| Merchant | Business entity receiving payments and, where authorized, initiating refunds. |
| Customer | Original payer for a payment and recipient of refund notifications. |
| Operations User | Bank user with privileged access to create, override, retry, or investigate payment and refund cases. |
| Maker | Operations user who initiates a privileged override request. |
| Checker | Separate authorized operations user who approves or rejects an override request. |
| Idempotency Key | Client-supplied key that prevents duplicate command execution for retries or resubmissions. |
| Request Fingerprint | Normalized hash of command inputs used to detect conflicting reuse of an idempotency key. |
| Correlation ID | Identifier used to trace a request across APIs, services, logs, events, and support evidence. |
| Processor Reference | Reference returned by a payment processor for executed payment or refund activity. |
| Ledger Reference | Reference returned by ledger or core banking for accounting postings. |
| Reconciliation | Matching payment and refund records across bank, processor, ledger, settlement, and reporting views. |
| Audit Event | Immutable record of a material business, control, or state-change event. |
| Exception Queue | Operations-visible queue for failed, stuck, or unresolved money movement cases. |
| Safe Degradation | Failure handling approach that avoids duplicate money movement, preserves traceability, and exposes unresolved outcomes to operations. |

## Shared APIs

| API | Capability | Purpose | Shared Rules |
| --- | --- | --- | --- |
| `POST /khqr/payments` | KHQR Payment | Initiate a KHQR merchant payment. | Requires idempotency key, customer authorization, QR payload validation, and audit evidence. |
| `GET /khqr/payments/{paymentId}` | KHQR Payment | Retrieve customer-owned payment status. | Requires ownership authorization and sensitive-data masking. |
| `POST /qr-refunds` | QR Refund | Initiate merchant refund for a completed KHQR payment. | Requires idempotency key, merchant ownership, reason code, duplicate prevention, and audit evidence. |
| `GET /qr-refunds/{refundId}` | QR Refund | Retrieve merchant-safe refund status. | Requires merchant ownership or privileged operations entitlement. |
| `POST /operations/qr-refunds` | QR Refund | Create refund through bank operations. | Requires operations entitlement, reason code, idempotency, correlation ID, and audit evidence. |
| `POST /operations/qr-refunds/{refundId}/overrides` | QR Refund | Request privileged override. | Requires maker entitlement, approved control, reason code, idempotency, and audit evidence. |
| `POST /operations/qr-refunds/{refundId}/overrides/{overrideId}/decision` | QR Refund | Approve or reject override. | Requires checker entitlement, maker/checker separation, reason code, and audit evidence. |
| `POST /operations/qr-refunds/{refundId}/retry` | QR Refund | Retry failed refund from operations flow. | Requires retry entitlement, failed-state eligibility, reason code, idempotency, and audit evidence. |

## Shared Events

| Event | Producer | Consumers | Purpose |
| --- | --- | --- | --- |
| PaymentInitiated | Payment capability | Audit, operations, reconciliation, reporting | Records accepted payment initiation. |
| PaymentCompleted | Payment capability / processor integration | Customer notification, reconciliation, reporting | Records successful payment completion. |
| PaymentFailed | Payment capability / processor integration | Operations, notification, reconciliation | Records failed payment outcome. |
| PaymentPending | Payment capability / processor integration | Operations, status inquiry, monitoring | Records delayed or unresolved processor outcome. |
| RefundRequested | Refund capability | Audit, operations, reporting | Records accepted refund request. |
| RefundProcessingStarted | Refund capability | Audit, monitoring, operations | Records refund moving into processing. |
| RefundCompleted | Refund capability / processor or ledger integration | Notification, reconciliation, reporting | Records successful refund completion. |
| RefundRejected | Refund capability | Audit, operations, reporting | Records business, authorization, reason-code, duplicate, or override rejection. |
| RefundFailed | Refund capability | Exception queue, operations, monitoring | Records refund failure requiring investigation or retry. |
| OverrideRequested | Refund capability | Operations, audit | Records privileged override request. |
| OverrideDecided | Refund capability | Operations, audit | Records checker approval or rejection. |
| RetryRequested | Refund capability | Operations, audit, monitoring | Records retry attempt for failed refund. |
| AuditEventRecorded | Payment or refund capability | Audit platform, compliance | Confirms immutable audit capture for material events. |
| ReconciliationRecordPublished | Payment or refund capability | Reconciliation platform, finance, operations | Provides data for matching and mismatch handling. |

Event contracts may be internal outbox records, platform events, or integration-specific schemas depending on the approved architecture for each capability.

## Shared Integrations

| Integration | Used By | Responsibility | Shared Expectations |
| --- | --- | --- | --- |
| Mobile Banking Channel | KHQR Payment | Customer payment initiation and status inquiry. | Authenticate customer, bind confirmation details, preserve correlation ID. |
| Merchant Application | QR Refund | Merchant refund initiation and status visibility. | Authenticate merchant user and prove merchant ownership. |
| Operations Portal | QR Refund and operations support | Privileged create, override, retry, and investigation workflows. | Enforce entitlements, maker/checker separation, and audit. |
| KHQR Payment Service | QR Refund | Original payment lookup and eligibility data. | Provide payment status, merchant ownership, amount, currency, date, and settlement state. |
| Merchant Identity / Authorization | Payments capabilities | Merchant or customer authorization checks. | Must fail safely when authorization cannot be confirmed. |
| Merchant Profile / Status | QR Refund | Suspended merchant and restriction checks. | Must be checked before eligible refund processing. |
| Payment Processor | Payment and refund capabilities | Payment execution, refund execution, and processor references. | Outcomes may be asynchronous; timeouts must not cause duplicate execution. |
| Ledger / Core Banking | Payment and refund capabilities | Accounting postings and ledger references. | Posting outcomes must be traceable and reconciled. |
| Notification Service | Payment and refund capabilities | Customer-safe status notifications. | Notification failure must not alter authoritative payment or refund outcome. |
| Audit Store | Payment and refund capabilities | Immutable audit record persistence. | Material state changes must be auditable. |
| Reconciliation Platform | Payment and refund capabilities | End-of-day matching and mismatch evidence. | Must support traceability by payment/refund references and correlation ID. |
| Reporting Platform | Payment and refund capabilities | Operational, merchant, and finance reporting. | Reporting views are not canonical payment or refund state. |

## Shared Business Rules

| Rule | Applies To | Description |
| --- | --- | --- |
| Idempotency is mandatory for money movement commands. | Payment initiation, refund initiation, override, retry | Commands that can create or mutate financial state require an idempotency key. |
| Duplicate execution must be prevented. | Payment and refund flows | Retries, resubmissions, and concurrent submissions must not create duplicate financial transactions. |
| Same idempotency key and same payload returns prior result. | Payment and refund flows | Replay behavior should be stable and traceable. |
| Same idempotency key and conflicting payload is rejected. | Payment and refund flows | Conflicting duplicate keys must return a safe conflict. |
| Authorization must be proven before money movement. | Payment and refund flows | Customer, merchant, or operations authority must be validated before processing. |
| Sensitive data must be masked. | APIs, logs, notifications, audit, reporting | Customer, account, merchant, processor, and ledger details must be protected according to classification. |
| Material state changes must be audited. | Payment and refund flows | Request, approval, rejection, retry, completion, failure, override, and invalid attempts require audit where applicable. |
| Processor and ledger uncertainty must degrade safely. | Payment and refund flows | Unknown outcomes must remain traceable and operations-visible; retries must not duplicate execution. |
| Reconciliation data must preserve references. | Payment and refund flows | Payment ID, refund ID, processor reference, ledger reference, settlement reference, and correlation ID must be available where applicable. |
| Notifications do not own authoritative state. | Payment and refund flows | Notification failure must be observable and recoverable without changing payment/refund outcome. |
| Operations overrides require controls. | Privileged operations flows | Overrides require entitlement, reason code, maker/checker separation, approved control, and immutable audit trail. |

## Reusable Patterns

### Idempotent Command Pattern

Use for commands that can create or mutate financial state.

- Require an idempotency key.
- Store only a keyed hash or approved tokenized representation.
- Bind the key to operation type, actor scope, original entity ID, request fingerprint, and result reference.
- Return prior result for same key and same fingerprint.
- Reject same key with different fingerprint.
- Acquire or create the idempotency record before mutating financial state.

### Transactional State And Audit Pattern

Use when a material payment or refund state change must be auditable.

- Persist business state and audit outbox record in one unit of work.
- Do not complete material state change without durable audit evidence or approved durable buffering.
- Emit audit events asynchronously only after durable persistence.
- Include correlation ID and actor context in audit payloads.

### Safe Processor / Ledger Degradation Pattern

Use for downstream processor or ledger uncertainty.

- Preserve local state and references.
- Avoid duplicate downstream submission while outcome is unknown.
- Make unresolved state visible to operations.
- Emit metrics and alerts.
- Require approved retry or reconciliation handling before resubmission.

### Ownership And Entitlement Pattern

Use for customer, merchant, and operations actions.

- Validate actor identity and scope before processing.
- Check merchant ownership for merchant-visible resources.
- Check operations entitlement for privileged actions.
- Enforce maker/checker separation for override approvals.
- Audit authorization failures and privileged attempts.

### Reconciliation Projection Pattern

Use for end-of-day matching and finance/operations evidence.

- Publish or expose records with stable payment/refund references.
- Include processor, ledger, settlement, status, amount, currency, and correlation fields.
- Treat reporting projections as consumer views, not canonical state.
- Preserve replay or re-extract capability for recovery.

### Exception Queue Pattern

Use for failed, stuck, or unresolved financial flows.

- Route unresolved cases to operations with safe details.
- Include reason, failure category, retry eligibility, age, status, and correlation ID.
- Separate operational visibility from automatic retry.
- Audit manual retry and privileged resolution actions.

### Capability Artifact Pattern

Use for new or changed Payments capabilities.

- Capture intent before requirements.
- Approve requirements before architecture and test design.
- Map APIs, tests, validation, and release evidence to requirements.
- Keep Jira for work and approval tracking.
- Keep Git as the source of truth for approved artifacts.
