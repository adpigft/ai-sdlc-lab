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
| Specification | `domains/payments/capabilities/qr-refund/specs/spec.md` | Approved |
| Architecture Context | `domains/payments/capabilities/qr-refund/context/context.md` | Approved |
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
| IdempotencyRecord | Command fingerprint and replay result. | `idempotencyKey`, `operation`, `requestFingerprint`, `refundId`, `status`, `createdAt`, `expiresAt`. |
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

## 4. Service Responsibilities

| Service / Component | Responsibilities |
| --- | --- |
| RefundApplicationService | Coordinates command flow for merchant creation, operations creation, status inquiry, override request, override decision, and retry. |
| RefundEligibilityService | Applies completed-payment, ownership, 30-day window, post-settlement, merchant suspension, duplicate-refund, reason-code, and high-value review rules. |
| IdempotencyService | Validates idempotency key presence, computes request fingerprints, returns replay results, rejects conflicting payloads, and protects concurrent command execution. |
| RefundStateService | Creates, updates, and queries refund aggregate state. |
| OverrideApprovalService | Enforces operations entitlement, maker-checker separation, reason code, and approved override control rules. |
| RefundExecutionService | Coordinates processor and ledger execution according to approved safe-degradation and accounting decisions. |
| RetryService | Validates failed refund retry eligibility and coordinates retry attempt state. |
| AuditService | Produces immutable audit events and prevents unaudited material state changes unless durable audit buffering is approved. |
| NotificationPublisher | Emits completed and failed refund notification events without changing authoritative refund outcome when notification fails. |
| ExceptionQueuePublisher | Publishes failed or stuck refunds to operations exception handling. |
| ReconciliationPublisher | Publishes or exposes refund records for end-of-day reconciliation. |
| ReportingPublisher | Publishes or exposes approved reporting data once reporting delivery model is finalized. |

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
| `refunds` | Canonical refund lifecycle records. | Unique `refundId`; unique active/full-refund constraint on `originalPaymentId`; indexed `merchantId`, `status`, `createdAt`, `correlationId`. |
| `refund_idempotency_records` | Command idempotency and replay records. | Unique `operation + idempotencyKey`; request fingerprint required; maps to refund/override/retry result. |
| `refund_overrides` | Maker-checker override workflow records. | Unique `overrideId`; maker/checker separation enforced; `refundId` indexed. |
| `refund_retry_attempts` | Retry attempt metadata. | `refundId`, retry sequence, actor, reason, outcome, timestamp. |
| `refund_audit_outbox` | Durable audit event publishing buffer if approved. | Append-only semantics; no sensitive unmasked customer data. |
| `refund_domain_outbox` | Notification, exception, reconciliation, and reporting event publication. | Idempotent event keys; replayable publication state. |
| `refund_reconciliation_projection` | End-of-day reconciliation extract or projection. | `refundId`, original payment, processor, ledger, merchant settlement references. |

Implementation must not rely on merchant balance availability for MVP refund eligibility. Accounting and settlement adjustment persistence cannot be finalized until `ADR-QRREF-001` is approved.

## 7. Event Design

Events are integration contracts or internal outbox records depending on final platform decisions. Event payloads must use synthetic/masked-safe fields in tests and logs.

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
- Full audit event schema remains an internal contract unless API/architecture approval requires external publication.

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

## 9. Idempotency Design

Idempotency is required for every command API.

Rules:

- `Idempotency-Key` is mandatory for merchant refund creation, operations refund creation, override request, override decision, and retry.
- Request fingerprint must include operation name, actor scope, original payment/refund ID, reason code, control or decision where applicable, and normalized payload.
- Same key and same fingerprint returns the original result without creating a second refund or second operation.
- Same key and different fingerprint returns an idempotency conflict.
- Concurrent refund submissions for the same original payment must be protected by both idempotency record locking and a unique original-payment refund constraint.
- Idempotency records must be correlated to audit events and `X-Correlation-Id`.
- Idempotency retention must align with compliance retention once `JIRA-QRREF-008` is resolved.

Recommended implementation approach:

1. Validate required command headers.
2. Start transaction or equivalent unit of work.
3. Insert or lock idempotency record for `operation + idempotencyKey`.
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

Audit failure behavior:

- A material refund state change must not complete without durable audit evidence unless a durable audit buffering architecture is explicitly approved.
- If audit persistence fails, the refund must remain traceable by refund ID or correlation ID, be operations-visible, and emit an alert.
- Audit records must be immutable and retention-ready once compliance confirms retention requirements.

## 12. Testing Strategy

| Test Layer | Coverage |
| --- | --- |
| Unit tests | Domain rules for eligibility, status transitions, duplicate prevention, reason code validation, high-value review routing, override controls, maker-checker separation, retry eligibility, and audit-required state changes. |
| Application service tests | Command orchestration for merchant create, operations create, status inquiry, override request/decision, retry, dependency failure handling, and outbox publication. |
| Repository tests | Unique original-payment refund constraint, idempotency replay/conflict, transactional consistency, refund state updates, and projections. |
| Contract tests | OpenAPI request/response schemas, required headers, response codes, and actor-safe error responses. |
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

Package names and framework-specific conventions must be adjusted to the final application stack when code is approved.

## 14. Build Plan

Build automation must align with existing GitHub Actions and SonarCloud placeholders.

| Build Step | Required Behavior |
| --- | --- |
| Compile/build | Compile implementation and fail on warnings where project standard requires. |
| Unit tests | Run domain and application service tests. |
| Integration tests | Run persistence, idempotency, dependency adapter, outbox, and failure-mode tests. |
| Contract tests | Validate implementation against `openapi.yaml`. |
| Acceptance tests | Execute `acceptance.feature` scenarios or mapped automated acceptance tests. |
| Security scan | Run dependency, secret, and static security scanning. |
| SonarCloud | Run quality gate once application code exists. |
| Traceability check | Verify requirements map to code/tests and validation evidence. |
| Evidence publication | Store build/test/security/Sonar evidence for validation and release artifacts. |

CI remains the system of record for build and quality gates. Jira and Confluence remain collaboration channels, not the source of truth.

## 15. Implementation Slices

Implementation should proceed in small, reviewable slices. Each slice requires tests and traceability updates before merge.

| Slice | Scope | Requirements | Acceptance / Evidence |
| --- | --- | --- | --- |
| 1. Domain foundation | Domain model, statuses, value objects, reason code validation, domain errors. | FR-QRREF-008, FR-QRREF-017 | Unit tests for values, statuses, reason codes, safe errors. |
| 2. Eligibility validation | Completed-payment-only, 30-day window, post-settlement eligibility, merchant balance non-blocking, suspended merchant rejection. | FR-QRREF-003, FR-QRREF-005, FR-QRREF-006, FR-QRREF-007 | Eligibility unit tests and acceptance mappings. |
| 3. Merchant refund command | `POST /qr-refunds` orchestration, merchant ownership, accepted/rejected outcomes. | FR-QRREF-001, FR-QRREF-020 | API/contract tests and merchant success/rejection scenarios. |
| 4. Operations refund command | `POST /operations/qr-refunds`, operations entitlement, forbidden rejection. | FR-QRREF-002, FR-QRREF-008 | Operations happy path and entitlement rejection tests. |
| 5. Idempotency and concurrency | Mandatory idempotency key, replay, conflict, same-payment concurrency lock/constraint. | FR-QRREF-004, FR-QRREF-009, FR-QRREF-010, NFR-QRREF-005 | Idempotency, conflict, and concurrency tests. |
| 6. High-value review routing | Configurable threshold routing and review metadata without automatic processor submission. | FR-QRREF-011 | High-value review tests; threshold config evidence. |
| 7. Override workflow | Override request, non-approved control rejection, maker-checker decision, same-user rejection. | FR-QRREF-012 | Override acceptance and security tests. |
| 8. Processor and ledger execution | Refund execution, downstream references, timeout/failure handling. | FR-QRREF-014, FR-QRREF-017, NFR-QRREF-008 | Processor/ledger integration and failure-mode tests; depends on ADR-QRREF-001 and ADR-QRREF-006. |
| 9. Retry and exception queue | Failed refund visibility and authorized retry. | FR-QRREF-013, FR-QRREF-014 | Exception queue and retry tests; retry policy evidence. |
| 10. Audit integration | Immutable material-event audit, audit failure handling, masked fields. | FR-QRREF-020, NFR-QRREF-006, NFR-QRREF-007 | Audit completeness and failure tests. |
| 11. Notification integration | Completed/failed customer-safe notification event and failure handling. | FR-QRREF-015 | Notification success/failure tests; template/channel approval. |
| 12. Status inquiry | `GET /qr-refunds/{refundId}`, merchant ownership, safe response masking. | FR-QRREF-016, NFR-QRREF-007 | Status access and cross-merchant rejection tests. |
| 13. Reconciliation projection | EOD reconciliation data and match/mismatch support. | FR-QRREF-018 | Reconciliation tests; depends on ADR-QRREF-007. |
| 14. Reporting projection | Refund history, failed refunds, pending refunds, daily totals through approved channel. | FR-QRREF-019 | Reporting validation; depends on ADR-QRREF-008. |
| 15. Observability and release evidence | Metrics, logs, traces, alerts, CI/Sonar evidence, validation hooks. | NFR-QRREF-002, NFR-QRREF-003, NFR-QRREF-004 | Operational readiness and validation-plan evidence. |

## Implementation Blockers Before Coding

| Blocker | Source | Required Approval |
| --- | --- | --- |
| Accounting treatment and settlement adjustment mechanism. | ADR-QRREF-001 | Payments Architect / Finance Lead |
| Idempotency and concurrency boundary. | ADR-QRREF-003 | Payments Architect |
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
