# QR Refund Implementation Plan

## Metadata

| Field | Value |
| --- | --- |
| Implementation Plan ID | IMPLPLAN-QRREF-001 |
| Intent ID | INT-QRREF-001 |
| Spec ID | SPEC-QRREF-001 |
| Context ID | CTX-QRREF-001 |
| Validation Plan ID | VALPLAN-QRREF-001 |
| Traceability ID | TRACE-QRREF-001 |
| Jira Epic | JIRA-QRREF-001 |
| Confluence Page | CONF-PAY-QRREF-IMPLEMENTATION |
| Domain | Payments |
| Capability | QR Refund |
| MVP Scope | Full refunds for completed KHQR payments |
| Status | Draft for implementation plan approval |
| Created | 2026-06-01 |

## Source Artifacts

| Artifact | Path | Status |
| --- | --- | --- |
| Intent | `domains/payments/capabilities/qr-refund/intent/intent.md` | Approved |
| Specification | `domains/payments/capabilities/qr-refund/specification/specification.md` | Approved |
| Architecture Context | `domains/payments/capabilities/qr-refund/design/design.md` | Approved |
| API Contract | `domains/payments/capabilities/qr-refund/contracts/openapi.yaml` | Approved |
| Acceptance Tests | `domains/payments/capabilities/qr-refund/tests/acceptance.feature` | Approved |
| Traceability Matrix | `traceability/traceability-matrix.md` | Approved |
| Validation Plan | `domains/payments/capabilities/qr-refund/validation/validation-plan.md` | Approved |

## Implementation Guardrails

- Do not create application code until this implementation plan is approved.
- Implement only full refunds for completed KHQR payments in MVP.
- Do not implement partial refunds, customer-initiated refunds, non-KHQR refunds, velocity limits, suspicious merchant screening, AML/sanctions screening, intraday reconciliation, or reporting platform implementation.
- Use synthetic or masked test data only.
- Do not log unmasked customer, account, processor, ledger, or sensitive payment identifiers.
- Do not hardcode secrets, credentials, thresholds, service URLs, or tokens.
- Every implementation slice must map to Jira placeholders, requirement IDs, acceptance scenarios, and traceability entries.
- Codex and developers must implement only one approved slice at a time.
- If a requested implementation depends on a blocked slice, stop and report the dependency instead of coding around it.

## 1. Bounded Context

QR Refund is a Payments bounded context responsible for the lifecycle of full refunds against completed KHQR payments. It owns refund eligibility orchestration, refund state, idempotency records, audit event production, operations override control records, retry coordination, and refund data required for reconciliation and reporting.

External bounded contexts and systems remain outside QR Refund ownership:

| External Context / System | QR Refund Dependency |
| --- | --- |
| KHQR Payment Service | Original payment lookup, payment status, merchant ownership, payment date, amount, currency, settlement state, existing refund linkage. |
| Merchant Identity / Authorization | Merchant user authentication and merchant ownership/permission checks. |
| Merchant Profile / Status | Suspended merchant status and other merchant restrictions. |
| Operations Entitlement | Operations create, retry, override-maker, and override-checker permissions. |
| Payment Processor | Full refund execution and processor refund reference. |
| Ledger / Core Banking | Refund posting and ledger reference. |
| Notification Service | Customer-safe completed and failed refund notifications. |
| Audit Store | Immutable audit event persistence. |
| Reconciliation Platform | End-of-day matching and mismatch evidence. |
| Reporting Platform | Refund history, failed refunds, pending refunds, and daily totals through approved reporting channel. |

## 2. Domain Model

| Concept | Description | Key Fields |
| --- | --- | --- |
| Refund | Core domain entity for a full KHQR refund. | `refundId`, `originalPaymentId`, `merchantId`, `amount`, `currency`, `status`, `reasonCode`, `requestedBy`, `createdAt`, `updatedAt`, `processorRefundReference`, `ledgerReference`, `correlationId`. |
| OriginalPaymentSnapshot | Immutable eligibility snapshot captured from KHQR Payment Service. | `originalPaymentId`, `merchantId`, `amount`, `currency`, `paymentStatus`, `paymentDate`, `settlementState`, `alreadyRefunded`. |
| RefundRequest | Command input for merchant or operations refund creation. | `originalPaymentId`, `reasonCode`, `actor`, `idempotencyKey`, `correlationId`, `channel`. |
| Actor | Initiator or approver identity summary. | `actorType`, `actorId`, `role`, `channel`, `merchantId` where applicable. |
| ReasonCode | Controlled reason for refund, override, retry, approval, or rejection. | Uppercase code, configured catalog reference. |
| IdempotencyRecord | Command fingerprint and replay result. | `idempotencyKeyHash`, `operationType`, `merchantId`, `originalPaymentId`, `requestPayloadHash`, `refundId`, `status`, `createdAt`, `expiresAt`. |
| OverrideRequest | Maker-checker request for an explicitly permitted control. | `overrideId`, `refundId`, `control`, `maker`, `checker`, `status`, `reasonCode`, `createdAt`, `decidedAt`. |
| ReviewDecision | High-value review metadata. | `required`, `status`, `reason`, `thresholdConfigReference`. |
| AuditEvent | Immutable material-event payload. | `eventType`, `originalPaymentId`, `refundId`, `initiator`, `userRole`, `reasonCode`, `timestamp`, `approvalUser`, `correlationId`. |
| ReconciliationRecord | EOD matching projection. | `refundId`, `originalPaymentId`, `processorReference`, `ledgerReference`, `merchantSettlementReference`, `status`, `amount`, `currency`, `correlationId`. |

Refund statuses for MVP remain `Requested`, `Processing`, `Completed`, `Rejected`, and `Failed`. High-value review is represented as review metadata on a `Requested` refund until `ADR-QRREF-004` finalizes the state model.

## 3. Aggregate Design

### Refund Aggregate

The `Refund` aggregate is the consistency boundary for one full refund against one original KHQR payment.

Responsibilities:

- Enforce one full refund per original payment.
- Enforce valid state transitions.
- Store refund lifecycle state and downstream references.
- Capture reason code, initiator, timestamps, and correlation ID.
- Expose state changes that must produce audit events.
- Support safe retry only from eligible failed states.
- Own all refund invariants and state-transition rules. Application services and repositories must not duplicate refund transition logic.

Expected state transitions:

| From | To | Trigger |
| --- | --- | --- |
| None | Requested | Eligible refund request accepted or high-value review required. |
| Requested | Processing | Eligibility passes and no manual review is pending. |
| Requested | Rejected | Business rule, authorization, reason-code, override, or review rejection. |
| Processing | Completed | Processor and ledger outcomes confirm successful refund. |
| Processing | Failed | Processor, ledger, or internal failure requires operations handling. |
| Failed | Processing | Authorized retry accepted. |

Invalid transitions must be rejected with actor-safe errors and audited where material.

### Override Aggregate

The `OverrideRequest` aggregate enforces privileged maker-checker controls.

Rules:

- Maker must have override-maker entitlement.
- Checker must have override-checker entitlement.
- Maker and checker must be different users.
- Override must include a reason code.
- Only approved controls can be overridden.
- Every request, approval, rejection, and invalid attempt is audited.

### Idempotency Consistency Boundary

The idempotency record must be created or locked before creating or mutating a refund. Concurrent same-payment refund attempts must be serialized by a unique original-payment refund constraint and command-level idempotency.

Refund persistence must include optimistic locking, aggregate versioning, or an equivalent row-locking strategy so concurrent state changes cannot overwrite each other.

## 4. Service Responsibilities

| Service / Component | Responsibilities |
| --- | --- |
| RefundApplicationService | Coordinates command flow for merchant creation, operations creation, status inquiry, override request, override decision, and retry. |
| RefundEligibilityService | Applies completed-payment, ownership, 30-day window, post-settlement, merchant suspension, duplicate-refund, reason-code, and high-value review rules. |
| IdempotencyService | Validates idempotency key presence, computes request fingerprints, returns replay results, rejects conflicting payloads, and protects concurrent command execution. |
| RefundRepository / RefundStatePort | Persists and loads refund aggregates. It must not own or duplicate state-transition logic; `Refund` aggregate methods own invariants and transitions. |
| OverrideApprovalService | Enforces operations entitlement, maker-checker separation, reason code, and approved override control rules. |
| RefundExecutionService | Coordinates processor and ledger execution according to approved safe-degradation and accounting decisions. |
| RetryService | Validates failed refund retry eligibility and coordinates retry attempt state. |
| AuditOutboxService | Writes durable transactional audit outbox records for every material state change and privileged action. |
| NotificationPort | Emits completed and failed refund notification events when the notification integration decision is approved; until then keep as an outbound port with minimal adapter. |
| ExceptionQueuePort | Publishes failed or stuck refunds to operations exception handling when the queue design is approved; until then keep as an outbound port with minimal adapter. |
| ReconciliationPort | Publishes or exposes refund records for end-of-day reconciliation when the feed/extract decision is approved; until then keep as projection seam. |
| ReportingProjectionPort | Projection seam only for MVP. Do not implement a concrete reporting publisher until `ADR-QRREF-008` is approved. |

## 5. API Layer Design

The implementation must conform to `contracts/openapi.yaml`.

| Operation | Application Command / Query | Required Controls |
| --- | --- | --- |
| `POST /qr-refunds` | `InitiateMerchantRefundCommand` | Bearer auth, merchant ownership, `X-Correlation-Id`, `Idempotency-Key`, reason code, eligibility checks, audit. |
| `GET /qr-refunds/{refundId}` | `GetRefundStatusQuery` | Bearer auth, merchant ownership or operations entitlement, masked response fields. |
| `POST /operations/qr-refunds` | `CreateOperationsRefundCommand` | Bearer auth, operations create entitlement, reason code, idempotency, correlation ID, audit. |
| `POST /operations/qr-refunds/{refundId}/overrides` | `RequestOverrideCommand` | Override-maker entitlement, reason code, approved control, idempotency, audit. |
| `POST /operations/qr-refunds/{refundId}/overrides/{overrideId}/decision` | `DecideOverrideCommand` | Override-checker entitlement, maker/checker separation, reason code, idempotency, audit. |
| `POST /operations/qr-refunds/{refundId}/retry` | `RetryRefundCommand` | Retry entitlement, failed-state eligibility, reason code, idempotency, audit. |

API layer rules:

- Validate schema and required headers before domain execution.
- Return `400` for malformed requests and missing required fields.
- Return `401` for missing/invalid authentication.
- Return `403` for unauthorized merchant, operations, or entitlement failures.
- Return `404` for missing refund resources.
- Return `409` for duplicate refund, idempotency conflict, or invalid state transition.
- Return `422` for business rule rejections.
- Return `429` for rate limiting where gateway or platform controls apply.
- Return actor-safe error responses with `correlationId`.

## 6. Persistence Design

Persistence must support refund consistency, idempotency, audit traceability, retry visibility, and reconciliation extraction.

| Store / Table | Purpose | Key Constraints |
| --- | --- | --- |
| `refunds` | Canonical refund lifecycle records. | Unique `refundId`; unique active/full-refund constraint on `originalPaymentId`; aggregate `version` or equivalent optimistic-lock field; indexed `merchantId`, `status`, `createdAt`, `correlationId`. |
| `refund_idempotency_records` | Command idempotency and replay records. | Unique `operation + idempotencyKeyHash`; raw idempotency keys must not be persisted; request fingerprint required; maps to refund/override/retry result. |
| `refund_overrides` | Maker-checker override workflow records. | Unique `overrideId`; maker/checker separation enforced; `refundId` indexed. |
| `refund_retry_attempts` | Retry attempt metadata. | `refundId`, retry sequence, actor, reason, outcome, timestamp. |
| `refund_audit_outbox` | MVP audit reliability pattern. Durable transactional audit outbox records must be written in the same unit of work as material refund state changes. | Append-only semantics; aggregate version/correlation reference; no sensitive unmasked customer data. |
| `refund_domain_outbox` | Notification, exception, reconciliation, and reporting event publication. | Idempotent event keys; replayable publication state. |
| `refund_reconciliation_projection` | End-of-day reconciliation extract or projection. | `refundId`, original payment, processor, ledger, merchant settlement references. |

Implementation must not rely on merchant balance availability for MVP refund eligibility. Accounting and settlement adjustment persistence cannot be finalized until `ADR-QRREF-001` is approved.

## 7. Event Design

Events are internal outbox records or integration contracts depending on final platform decisions. MVP implementation should define outbound ports/interfaces first and add concrete publishers only after the corresponding integration decision is approved. Event payloads must use synthetic/masked-safe fields in tests and logs.

| Event | Trigger | Consumers |
| --- | --- | --- |
| `RefundRequested` | Refund accepted into `Requested`. | Audit, observability, reporting. |
| `RefundProcessingStarted` | Refund moves to `Processing`. | Audit, observability. |
| `RefundCompleted` | Processor and ledger outcomes complete successfully. | Notification, audit, reconciliation, reporting. |
| `RefundRejected` | Eligibility, authorization, reason-code, duplicate, or override rejection. | Audit, observability, reporting. |
| `RefundFailed` | Processing failure requiring operations review. | Exception queue, notification, audit, reconciliation, reporting. |
| `RefundRetryRequested` | Authorized retry accepted. | Audit, operations, observability. |
| `OverrideRequested` | Maker submits override request. | Audit, operations workflow. |
| `OverrideDecided` | Checker approves or rejects override. | Audit, operations workflow. |
| `HighValueReviewRequired` | Refund exceeds configured threshold. | Operations/risk review workflow, audit. |
| `ReconciliationRecordReady` | Refund data is ready for EOD reconciliation. | Reconciliation platform. |

Open event-contract decisions:

- Notification event schema remains out-of-contract until notification integration is approved.
- Reconciliation feed/extract contract remains out-of-contract until `ADR-QRREF-007`.
- Reporting delivery event/extract remains out-of-contract until `ADR-QRREF-008`.
- Full audit events must be written to the durable transactional audit outbox for MVP. External audit publication remains an integration detail behind the audit port.

## 8. Error Handling Design

Error handling must be explicit and actor-safe.

| Error Category | Example Conditions | API Response |
| --- | --- | --- |
| Validation error | Missing `reasonCode`, invalid reason code format, missing idempotency key, invalid ID format. | `400 Bad Request` with safe details. |
| Authentication error | Missing or invalid bearer token. | `401 Unauthorized`. |
| Authorization error | Merchant does not own payment/refund; operations user lacks entitlement. | `403 Forbidden`. |
| Not found | Refund ID does not exist or is not visible to actor. | `404 Not Found` or `403 Forbidden` based on information-disclosure policy. |
| Conflict | Duplicate refund, idempotency conflict, invalid state transition, same maker/checker. | `409 Conflict`. |
| Business rejection | Non-completed payment, expired refund window, suspended merchant, non-approved override control. | `422 Unprocessable Entity` unless conflict semantics apply. |
| Dependency unavailable | KHQR lookup, processor, ledger, audit, notification, reconciliation dependency failure. | Safe failure state, retryable operational signal, or `503` if platform standard allows. |

Refund processing must never silently swallow failures that affect money movement, audit, reconciliation, or duplicate prevention. Notification failure must not change the authoritative refund outcome.

Dependency-specific failure behavior:

| Dependency | Failure Behavior |
| --- | --- |
| KHQR payment lookup | Do not create a refund if original payment eligibility cannot be confirmed. Return a safe retryable rejection or dependency error, emit an operational signal, and record an audit event where request context is sufficient. |
| Payment processor | Preserve refund state and idempotency record. If outcome is unknown, do not submit duplicate processor refunds; keep the refund traceable and operations-visible for investigation or approved retry. |
| Ledger / Core Banking | Preserve refund state, processor reference if available, and correlation ID. Do not duplicate ledger postings; route unresolved or failed postings to operations exception handling and reconciliation. |
| Audit outbox | Material state changes must be committed only with a durable transactional audit outbox record. If the audit outbox write fails, abort the material state change and emit an operational alert. |
| Notification service | Do not change authoritative refund outcome because of notification failure. Record notification failure for recovery, emit metrics/alerts, and avoid sensitive customer details in logs. |
| Reconciliation feed/extract | Keep canonical refund records replayable or re-extractable, emit operations alert, and do not mutate refund outcome solely because reconciliation publication failed. |

## 9. Idempotency Design

Idempotency is required for every command API.

Rules:

- `Idempotency-Key` is mandatory for merchant refund creation, operations refund creation, override request, override decision, and retry.
- Raw idempotency keys must be treated as sensitive replay controls. Store only a keyed hash or approved tokenized representation; never log raw idempotency keys.
- Idempotency records must bind the hashed idempotency key to merchant ID where applicable, original payment ID, request payload hash, and operation type.
- Request fingerprint must include operation type, actor scope, merchant ID where applicable, original payment/refund ID, reason code, control or decision where applicable, and normalized payload hash.
- Same key and same fingerprint returns the original result without creating a second refund or second operation.
- Same key and different fingerprint returns an idempotency conflict.
- Concurrent refund submissions for the same original payment must be protected by both idempotency record locking and a unique original-payment refund constraint.
- Idempotency records must be correlated to audit events and `X-Correlation-Id`.
- Idempotency retention must align with compliance retention once `JIRA-QRREF-008` is resolved.

Recommended implementation approach:

1. Validate required command headers.
2. Start transaction or equivalent unit of work.
3. Insert or lock idempotency record for `operation + idempotencyKeyHash`.
4. Compare fingerprint for replay or conflict.
5. Enforce original-payment refund uniqueness.
6. Execute domain command.
7. Store result reference and response summary.
8. Commit and return response.

## 10. Security Design

Security controls:

- Require authenticated bearer token for every API operation.
- Scope merchant users to payments and refunds owned by their merchant.
- Require operations entitlements for create, retry, override-maker, and override-checker actions.
- Enforce maker-checker separation.
- Validate reason codes against a controlled catalog.
- Reject non-approved override controls.
- Mask sensitive identifiers in logs, traces, responses, notifications, reports, operations views, and audit views unless explicitly authorized.
- Never log raw bearer tokens, idempotency keys, full customer identifiers, account identifiers, processor internals, or ledger internals.
- Emit security-relevant audit events for authorization failures, duplicate attempts, idempotency conflicts, override attempts, and retry attempts.
- Use service credentials and secrets from managed configuration only; never hardcode secrets.

Security validation must cover `NFR-QRREF-007` and evidence IDs `EVD-QRREF-004` and `EVD-QRREF-005`.

## 11. Audit Design

Audit is mandatory for material events and privileged actions.

Material events:

- Request.
- Approval.
- Rejection.
- Retry.
- Completion.
- Failure.
- Override.
- Authorization failure.
- Duplicate refund attempt.
- Idempotency conflict.

Required audit fields:

- Original payment ID.
- Refund ID where available.
- Initiator.
- User role.
- Reason code.
- Timestamp.
- Approval user for approvals and overrides.
- Correlation ID.
- Event type.
- Masked sensitive identifiers.

Audit reliability pattern:

- MVP uses a durable transactional audit outbox. A material refund state change and its audit outbox record must commit in the same unit of work.
- A material refund state change must not complete without a durable audit outbox record.
- If audit outbox persistence fails, abort the material state change, keep the request traceable by correlation ID, make the failure operations-visible, and emit an alert.
- Audit records must be immutable and retention-ready once compliance confirms retention requirements.

## 12. Testing Strategy

| Test Layer | Coverage |
| --- | --- |
| Unit tests | Domain rules for eligibility, status transitions, duplicate prevention, reason code validation, high-value review routing, override controls, maker-checker separation, retry eligibility, and audit-required state changes. |
| Application service tests | Command orchestration for merchant create, operations create, status inquiry, override request/decision, retry, dependency failure handling, and outbox publication. |
| Repository tests | Unique original-payment refund constraint, idempotency replay/conflict, transactional consistency, refund state updates, and projections. |
| Contract tests | OpenAPI request/response schemas, required headers, documented `400`, `401`, `403`, `404`, `409`, `422`, and `429` responses where applicable, and actor-safe error responses. |
| Acceptance tests | All scenarios in `acceptance.feature`, mapped to Jira and requirement IDs. |
| Security tests | Authentication, merchant authorization, operations entitlements, maker-checker separation, safe errors, and masking. |
| Failure-mode tests | Processor timeout, ledger timeout, notification failure, audit failure, reconciliation feed failure, stuck processing visibility. |
| Concurrency tests | Same original payment submitted concurrently with different idempotency keys; same idempotency key replay under load. |
| Performance tests | 95% successful refunds within 60 seconds after MVP volume assumptions are approved. |
| Operational tests | Metrics, logs, traces, alerts, exception queue visibility, retry workflow, runbook verification. |

All tests must use synthetic or masked data. Test evidence must feed the validation report and release evidence.

## 13. Package Structure

No application code is created by this plan. The proposed package structure for later implementation should follow clean/hexagonal architecture and keep domain logic independent of frameworks.

```text
src/
  main/
    <language-root>/
      payments/
        qrrefund/
          api/
            RefundController
            OperationsRefundController
            ErrorResponseMapper
          application/
            RefundApplicationService
            commands/
            queries/
            handlers/
          domain/
            model/
            value/
            policy/
            events/
            errors/
          ports/
            inbound/
            outbound/
          infrastructure/
            persistence/
            processor/
            ledger/
            paymentlookup/
            authorization/
            notification/
            audit/
            reconciliation/
            reporting/
            observability/
  test/
    <language-root>/
      payments/
        qrrefund/
          unit/
          application/
          contract/
          integration/
          acceptance/
          security/
```

Package names and framework-specific conventions must be adjusted to the final application stack when code is approved. For MVP, outbound packages should start as ports/interfaces with minimal adapters or stubs; concrete notification, exception queue, reconciliation, and reporting publishers should be added only after their integration decisions are approved.

## 14. Build Plan

Build automation must align with existing GitHub Actions and SonarCloud placeholders.

| Build Step | Required Behavior |
| --- | --- |
| Compile/build | Compile implementation and fail on warnings where project standard requires. |
| OpenAPI validation | Validate `openapi.yaml` syntax and implementation compatibility. |
| Gherkin validation | Validate `acceptance.feature` syntax and scenario/tag integrity. |
| Unit tests | Run domain and application service tests. |
| Integration tests | Run persistence, idempotency, dependency adapter, outbox, and failure-mode tests. |
| Contract tests | Validate implementation against `openapi.yaml`. |
| Acceptance tests | Execute `acceptance.feature` scenarios or mapped automated acceptance tests. |
| Secret scan | Verify no secrets, tokens, or raw credentials are committed. |
| Dependency scan | Check third-party dependencies for known vulnerabilities. |
| Static analysis | Run lint/static analysis and fail on configured quality thresholds. |
| SonarCloud | Run quality gate once application code exists. |
| Traceability validation | Verify requirements map to code/tests and validation evidence. |
| Evidence publication | Store build/test/security/Sonar evidence for validation and release artifacts. |

CI remains the system of record for build and quality gates. Jira and Confluence remain collaboration channels, not the source of truth.

## 15. Implementation Slices

Implementation must proceed in small, reviewable slices. Codex and developers must implement only one approved slice at a time. If a requested implementation depends on a blocked slice, stop and report the dependency instead of coding around it.

All six slices are defined upfront so scope, sequencing, and traceability are explicit before code begins. Concrete publishers and external adapters should be minimal in MVP and added only when the corresponding integration decision is approved.

### Startable Now

These slices can start after implementation plan approval because they do not require unresolved processor, ledger, operations override, retry, reconciliation, or reporting decisions.

#### Slice 1 - Refund Creation Foundation

Status: Can start now.

Scope:

- Refund aggregate.
- Refund creation command.
- Original payment lookup port.
- Merchant eligibility validation.
- Completed payment validation.
- 30-day refund window validation.
- Duplicate refund prevention.
- Idempotency handling.
- Basic refund status creation.
- Unit tests.

Excludes:

- Processor posting.
- Ledger posting.
- Notifications.
- Retry.
- Operations override.
- Reconciliation.
- Reporting.

Traceability:

| Requirements | APIs | Tests |
| --- | --- | --- |
| FR-QRREF-001, FR-QRREF-003, FR-QRREF-004, FR-QRREF-005, FR-QRREF-006, FR-QRREF-007, FR-QRREF-008, FR-QRREF-009, FR-QRREF-010, FR-QRREF-016, FR-QRREF-020, NFR-QRREF-005, NFR-QRREF-006, NFR-QRREF-007 | `POST /qr-refunds`, `GET /qr-refunds/{refundId}` | Successful merchant full refund; non-completed payment rejection; duplicate refund prevention; idempotency replay/conflict/missing key; concurrent same-payment submissions; 30-day window rejection; post-settlement eligibility; merchant balance non-blocking; suspended merchant rejection; missing/invalid reason code; merchant status inquiry; audit event creation; audit outbox failure tests. |

### Blocked Pending ADR / Configuration Approval

These slices must not begin until listed decisions or configuration approvals are completed.

#### Slice 2 - Processor and Ledger Integration

Status: Blocked pending ADR/config approval.

Scope:

- Processor refund port.
- Ledger refund posting port.
- Timeout handling.
- Failure handling.
- Integration tests.

Blocked by:

- Post-settlement accounting decision.
- Processor refund behavior confirmation.
- Ledger posting design.

Traceability:

| Requirements | APIs | Tests |
| --- | --- | --- |
| FR-QRREF-014, FR-QRREF-017, NFR-QRREF-008 | `POST /qr-refunds`, `POST /operations/qr-refunds`, `POST /operations/qr-refunds/{refundId}/retry` | Processor timeout; ledger timeout; downstream reference capture; failure-mode integration tests. |

#### Slice 3 - Operations Refund and Override

Status: Blocked pending override policy approval.

Scope:

- Operations refund creation.
- Override request.
- Override decision.
- Maker-checker approval.
- Reason code validation.
- Authorization checks.
- Audit trail.

Blocked by:

- Operations entitlement policy.
- Override approval policy.

Traceability:

| Requirements | APIs | Tests |
| --- | --- | --- |
| FR-QRREF-002, FR-QRREF-008, FR-QRREF-012, FR-QRREF-020, NFR-QRREF-006, NFR-QRREF-007 | `POST /operations/qr-refunds`, `POST /operations/qr-refunds/{refundId}/overrides`, `POST /operations/qr-refunds/{refundId}/overrides/{overrideId}/decision` | Successful operations full refund creation; operations create entitlement rejection; override request; non-approved override rejection; maker-checker approval; same-user maker/checker rejection; audit event creation. |

#### Slice 4 - Retry and Exception Handling

Status: Starts after Slice 2.

Scope:

- Failed refund exception queue.
- Retry failed refund.
- Retry audit events.
- Retry eligibility rules.
- Retry test scenarios.

Depends on:

- Processor and ledger integration behavior.

Traceability:

| Requirements | APIs | Tests |
| --- | --- | --- |
| FR-QRREF-013, FR-QRREF-014, FR-QRREF-020, NFR-QRREF-003, NFR-QRREF-008 | `POST /operations/qr-refunds/{refundId}/retry` | Retry failed refund from operations exception queue; processor timeout operations visibility; ledger timeout operations visibility; retry audit events. |

#### Slice 5 - Reconciliation

Status: Blocked pending reconciliation design.

Scope:

- End-of-day reconciliation feed.
- Match/mismatch handling.
- Reconciliation evidence.
- Reconciliation validation.

Blocked by:

- Reconciliation mismatch workflow.
- Reconciliation feed contract.

Traceability:

| Requirements | APIs | Tests |
| --- | --- | --- |
| FR-QRREF-018, NFR-QRREF-008 | Reconciliation feed/extract, not currently in OpenAPI | End-of-day reconciliation matched records; end-of-day reconciliation mismatch for investigation; reconciliation feed failure validation. |

### Future Phase / Projection Seam Only

These items remain ports, projection seams, or data-shape placeholders for MVP. Do not implement concrete publishers or platform integration until approved.

#### Slice 6 - Reporting

Status: Future phase / projection seam only.

Scope:

- Reporting event/interface placeholder only.
- No reporting platform implementation.
- No reporting API implementation.

Blocked by:

- Reporting platform decision.

Traceability:

| Requirements | APIs | Tests |
| --- | --- | --- |
| FR-QRREF-019 | Reporting event/interface placeholder only; no API in MVP | Future reporting validation after `ADR-QRREF-008`; no MVP acceptance execution beyond projection seam review. |

Additional future-phase items:

| Item | MVP Treatment | Future Approval |
| --- | --- | --- |
| Rejected refund notifications | Do not implement unless product expands MVP notification scope. | `JIRA-QRREF-014`; Product approval. |
| Intraday reconciliation | Out of scope for MVP. | Future phase approval. |
| Partial refunds | Out of scope for MVP. | Future phase approval. |

## Slice 2 Blocked Conditions

Slice 2 remains blocked until the following conditions are closed:

- Finance confirms settlement adjustment rules, receivable fallback conditions, and ledger account mappings for `ADR-QRREF-001`.
- Payments Architecture confirms processor and ledger client reference formats, inquiry support, and downstream attempt retention for `ADR-QRREF-003`.
- Payments Architecture, DevSecOps, and Operations confirm processor and ledger status mapping, timeout thresholds, and unresolved-state visibility for `ADR-QRREF-006`.
- Slice 4 retry and exception handling remains out of scope until `ADR-QRREF-005` is approved.
- No OpenAPI contract update is approved yet.

## Implementation Blockers Before Coding

| Blocker | Source | Required Approval |
| --- | --- | --- |
| Accounting treatment and settlement adjustment mechanism. | ADR-QRREF-001 | Payments Architect / Finance Lead |
| Cross-system idempotency or concurrency behavior beyond the Slice 1 hashed-key, unique original-payment constraint, and aggregate versioning rules. | ADR-QRREF-003 | Payments Architect |
| High-value manual review state model and review queues. | ADR-QRREF-004 / JIRA-QRREF-013 | Product Owner / Risk Lead / Payments Architect |
| Safe degradation behavior for processor, ledger, notification, audit, and reconciliation failures. | ADR-QRREF-006 | Payments Architect / DevSecOps Lead |
| Overrideable versus non-overrideable controls. | JIRA-QRREF-015 | Product Owner / Risk Lead / Operations Lead |
| Regulatory retention period if persistence retention design is required before coding. | JIRA-QRREF-008 | Compliance Lead |

## Human Approval

| Gate | Jira Placeholder | Required Approver | Status |
| --- | --- | --- | --- |
| Implementation plan approval | JIRA-QRREF-090 | Payments Architect / Developer Lead | Pending |
| Security design approval | JIRA-QRREF-091 | Security and Risk Lead | Pending |
| Audit design approval | JIRA-QRREF-092 | Compliance Lead | Pending |
| Operations implementation readiness | JIRA-QRREF-093 | Operations Lead | Pending |
| Finance implementation readiness | JIRA-QRREF-094 | Finance Lead | Pending |
| Development start approval | JIRA-QRREF-095 | Product Owner / Release Manager | Pending |

## Next Step

Stop for implementation plan approval. Do not create application code, tests under `src/`, database migrations, build files, or additional contracts until this plan and required implementation blockers are approved.
