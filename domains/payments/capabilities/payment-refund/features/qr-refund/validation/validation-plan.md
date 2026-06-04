# QR Refund Validation Plan

## Metadata

| Field | Value |
| --- | --- |
| Validation Plan ID | VALPLAN-QRREF-001 |
| Intent ID | INT-QRREF-001 |
| Spec ID | SPEC-QRREF-001 |
| Context ID | CTX-QRREF-001 |
| Traceability ID | TRACE-QRREF-001 |
| Jira Epic | JIRA-QRREF-001 |
| Confluence Page | CONF-PAY-QRREF-VALIDATION |
| Domain | Payments |
| Capability | QR Refund |
| MVP Scope | Full refunds for completed KHQR payments |
| Status | Draft for QA validation approval |
| Created | 2026-06-01 |

## Source Artifacts

| Artifact | Path | Approval Status |
| --- | --- | --- |
| Intent | `domains/payments/capabilities/payment-refund/features/qr-refund/intent/intent.md` | Approved |
| Specification | `domains/payments/capabilities/payment-refund/features/qr-refund/specification/specification.md` | Approved |
| Architecture Context | `domains/payments/capabilities/payment-refund/features/qr-refund/design/design.md` | Approved |
| API Contract | `domains/payments/capabilities/payment-refund/features/qr-refund/contracts/openapi.yaml` | Approved |
| Acceptance Tests | `domains/payments/capabilities/payment-refund/features/qr-refund/tests/acceptance.feature` | Approved |
| Traceability Matrix | `traceability/traceability-matrix.md` | Approved |

## Validation Scope

This plan defines the evidence required to validate QR Refund before release. It does not create implementation code and does not assert that validation has passed. Validation execution can start only after approved implementation exists and required release entry criteria are met.

## 1. Requirement Coverage Validation

| Area | Validation Required | Evidence |
| --- | --- | --- |
| Merchant full refund | Validate merchant can request a full refund for an owned completed KHQR payment within 30 days. | Acceptance test result for `FR-QRREF-001`; API request/response evidence; audit event evidence. |
| Operations full refund | Validate authorized operations users can create refunds and unauthorized users are rejected. | Acceptance test results for `FR-QRREF-002`; entitlement test evidence. |
| Completed-payment-only rule | Validate non-completed original payment statuses are rejected and no refund transaction is created. | Scenario outline result for `FR-QRREF-003`; state-store evidence. |
| One full refund only | Validate second refund attempt is rejected or safely returns existing refund under idempotency. | Test results for `FR-QRREF-004`, `FR-QRREF-009`, `FR-QRREF-010`. |
| 30-day window | Validate expired refund requests are rejected unless approved override applies. | Test result for `FR-QRREF-005`; override approval evidence. |
| Post-settlement refund eligibility | Validate merchant settlement state and merchant balance availability do not block MVP refund eligibility. | Test results for `FR-QRREF-006`; finance review evidence. |
| Suspended merchant block | Validate suspended merchant refunds are blocked unless approved policy allows override. | Test result for `FR-QRREF-007`; override policy evidence. |
| High-value manual review | Validate high-value refunds are held for manual review and do not auto-submit to processor. | Test result for `FR-QRREF-011`; configured threshold evidence. |
| Exception queue and retry | Validate failed refunds become operations-visible and retry is controlled, idempotent, and audited. | Test results for `FR-QRREF-013`, `FR-QRREF-014`; operations queue evidence. |
| Status tracking | Validate merchant status access is scoped to owned refunds and safe response details. | Test results for `FR-QRREF-016`; authorization evidence. |
| Reporting data | Validate required refund reporting data is produced through the approved reporting channel. | Reporting extract/API evidence after `ADR-QRREF-008` is resolved. |

## 2. API Coverage Validation

| API Operation | Validation Required | Evidence |
| --- | --- | --- |
| `POST /qr-refunds` | Validate required headers, request schema, business-rule rejections, idempotency behavior, and accepted refund response. | Contract test results; acceptance test results; negative API tests. |
| `GET /qr-refunds/{refundId}` | Validate authorized status inquiry, forbidden cross-merchant access, not-found behavior, and masked response fields. | Contract test results; security test evidence. |
| `POST /operations/qr-refunds` | Validate operations create entitlement, reason code, idempotency, correlation ID, and accepted/rejected outcomes. | Contract test results; entitlement test evidence. |
| `POST /operations/qr-refunds/{refundId}/overrides` | Validate maker entitlement, reason code, override control, idempotency key, and audit capture. | Contract test results; maker-control evidence. |
| `POST /operations/qr-refunds/{refundId}/overrides/{overrideId}/decision` | Validate checker entitlement, maker-checker separation, decision capture, and rejection of invalid state transitions. | Contract test results; maker-checker evidence. |
| `POST /operations/qr-refunds/{refundId}/retry` | Validate failed-only retry, retry entitlement, idempotency key, reason code, and audit capture. | Contract test results; retry test evidence. |

API validation must include schema validation against `openapi.yaml`, error response validation for `400`, `401`, `403`, `404`, `409`, `422`, and `429` where applicable, and verification that every response includes an actor-safe `correlationId`.

## 3. Acceptance Test Coverage

Acceptance validation must execute all scenarios in `acceptance.feature` and produce scenario-level evidence linked to Jira placeholders.

| Coverage Group | Scenarios |
| --- | --- |
| Happy path | Successful merchant full refund; Successful operations full refund creation. |
| Eligibility controls | Non-completed payment rejection; 30-day window rejection; post-settlement eligibility; merchant balance non-blocking; suspended merchant rejection. |
| Duplicate and idempotency controls | Duplicate refund prevention; same-key replay; missing idempotency key; conflicting idempotency key; concurrent same-payment submissions. |
| Reason and review controls | Missing/invalid reason code rejection; high-value manual review. |
| Operations controls | Override request; non-approved override control rejection; maker-checker approval; same-user maker/checker rejection; failed refund retry. |
| Failure handling | Processor timeout; ledger timeout; failed notification handling; audit failure handling. |
| Access and status | Merchant own-status inquiry; cross-merchant status rejection. |
| Audit and reconciliation | Material audit event outline; end-of-day match; end-of-day mismatch. |

## 4. Security Validation

| Security Control | Validation Required | Evidence |
| --- | --- | --- |
| Authentication | Validate bearer token required for every API operation. | API security test results. |
| Merchant authorization | Validate merchant users can act only on payments/refunds owned by their merchant. | Negative authorization tests; access-control logs. |
| Operations entitlement | Validate separate create, retry, override-maker, and override-checker permissions. | Entitlement matrix; negative tests. |
| Maker-checker separation | Validate maker cannot approve own override. | Acceptance and security test result. |
| Sensitive data masking | Validate customer, account, merchant, processor, and ledger identifiers are masked in logs, reports, notifications, operations views, and merchant responses unless explicitly authorized. | Log review; response inspection; report sample review. |
| Safe errors | Validate errors are actor-safe and do not disclose internal risk, ledger, processor, or customer data. | Negative API test evidence. |
| Abuse monitoring | Validate alerts or monitoring exist for high-value refunds, override usage, duplicate attempts, idempotency conflicts, and failed refunds. | Observability dashboard and alert evidence. |

## 5. Audit Validation

| Audit Requirement | Validation Required | Evidence |
| --- | --- | --- |
| Material event coverage | Validate request, approval, rejection, retry, completion, failure, and override events produce immutable audit records. | Audit event test results; audit store query evidence. |
| Required fields | Validate original payment ID, refund ID, initiator, user role, reason code, timestamp, approval user when applicable, and correlation ID. | Audit payload samples with synthetic data. |
| Immutability | Validate audit records cannot be altered by normal application or operations users. | Control test evidence or platform attestation. |
| Masking | Validate sensitive customer data is masked in audit views. | Audit view inspection. |
| Audit failure behavior | Validate refund does not complete without audit evidence, or durable audit buffering is proven if approved by architecture. | Failure-mode test result; architecture decision evidence. |
| Retention | Validate retention policy after compliance confirms retention requirements. | Compliance approval and retention configuration evidence. |

## 6. Reconciliation Validation

| Reconciliation Area | Validation Required | Evidence |
| --- | --- | --- |
| Match coverage | Validate completed refunds match original payment, refund transaction, payment processor, ledger, and merchant settlement records. | End-of-day reconciliation test result; synthetic match report. |
| Mismatch detection | Validate processor-ledger mismatch is identified and traceable by refund ID, original payment ID, processor reference, ledger reference, and correlation ID. | Mismatch test result; operations/finance evidence. |
| Replay/re-extract | Validate reconciliation data can be replayed or re-extracted after feed failure. | Reconciliation feed failure test after feed design is approved. |
| Finance visibility | Validate finance can access daily totals and mismatch evidence through the approved channel. | Finance report or extract evidence. |
| Open decision dependency | Validate final mismatch workflow after `ADR-QRREF-007` is approved. | ADR approval and test update evidence. |

## 7. NFR Validation

| NFR | Target | Validation Required | Evidence |
| --- | --- | --- | --- |
| NFR-QRREF-001 Processing time | 95% within 60 seconds | Validate under approved MVP volume. | Performance test report; blocked until `JIRA-QRREF-011` volume is approved. |
| NFR-QRREF-002 Availability | 99.9% target | Validate architecture and operations readiness for initiation/status capability. | SLO/SLA review; resilience test evidence. |
| NFR-QRREF-003 Maximum pending duration | 24 hours | Validate stuck `requested` or `processing` refunds become operations-visible and alerted. | Timeout and alert test evidence. |
| NFR-QRREF-004 Observability | Metrics, logs, traces, alerts | Validate dashboards and alerts for initiation, rejection, failure, retry, completion, overrides, high-value review, notification failure, and reconciliation mismatch. | Dashboard screenshots/links; alert test records. |
| NFR-QRREF-005 Idempotency/concurrency | No duplicate refunds | Validate same-key replay, conflicting-key rejection, and concurrent same-payment submissions. | Acceptance, integration, and concurrency test evidence. |
| NFR-QRREF-006 Audit completeness | 100% material events | Validate every material event produces immutable audit evidence. | Audit completeness report. |
| NFR-QRREF-007 Sensitive-data protection | Masking enforced | Validate masking across logs, reports, notifications, operations views, and merchant responses. | Security test report. |
| NFR-QRREF-008 Safe degradation | No duplicate or untraceable states | Validate processor, ledger, notification, audit, and reconciliation failure behavior. | Failure-mode test report. |
| NFR-QRREF-009 Retention | Pending compliance | Validate once retention period is approved. | Compliance sign-off and retention configuration evidence. |

## 8. Performance Validation

Performance validation is blocked until MVP volume assumptions are approved under `JIRA-QRREF-011`.

When volume is approved, testing must validate:

- 95% of successful refunds complete within 60 seconds.
- Refund initiation remains stable under expected peak merchant and operations traffic.
- Idempotency store and refund state store remain consistent during concurrent same-payment submissions.
- Status inquiry latency remains acceptable for merchant and operations users.
- Processor, ledger, notification, and audit dependency latency does not create duplicate or untraceable outcomes.
- High-value review routing does not submit refunds automatically to processor.

Required evidence:

- Load profile and test data assumptions.
- Performance test report.
- Error-rate and latency summary.
- Bottleneck and accepted-risk log.
- Architecture approval for any deferred performance risk.

## 9. Operational Readiness Validation

| Operational Area | Validation Required | Evidence |
| --- | --- | --- |
| Exception queue | Failed and stuck refunds are visible to operations with safe investigation fields. | Operations queue evidence. |
| Retry operations | Retry is available only for authorized users and only for eligible failed refunds. | Retry test evidence. |
| Override operations | Override maker/checker workflows enforce entitlement, reason code, distinct users, and immutable audit. | Override workflow test evidence. |
| Monitoring | Alerts exist for processor timeout, ledger timeout, notification failure, audit failure, reconciliation mismatch, duplicate attempts, high-value review, and pending-duration breach. | Dashboard and alert test evidence. |
| Runbook | Operations runbook covers failed refunds, retry, stuck refunds, audit failure, reconciliation breaks, and customer support escalation. | Confluence/runbook placeholder or approved runbook link. |
| Reporting | Refund history, failed refunds, pending refunds, and daily totals are available through approved reporting channel. | Reporting evidence after `ADR-QRREF-008`. |
| Human gates | Product, QA, Architecture, Security/Risk, Compliance, Operations, Finance, and Release approvals are captured. | Jira, PR approval, signed artifact approval, or lab chat confirmation as applicable. |

## 10. Release Entry Criteria

Release validation may start only when:

- Implementation exists and is linked to approved QR Refund artifacts.
- Intent, specification, architecture context, API contract, acceptance tests, and traceability are approved.
- All must-fix pre-implementation traceability gaps are resolved or explicitly approved for deferral.
- `ADR-QRREF-001`, `ADR-QRREF-003`, `ADR-QRREF-004`, and `ADR-QRREF-006` are approved before implementation-dependent validation.
- OpenAPI contract validation is configured in CI or local validation evidence exists.
- GitHub Actions CI evidence is available for build, tests, security scan placeholders, and SonarCloud placeholder execution once code exists.
- Test data is synthetic or masked.
- QA environment and required dependency simulators/stubs are available.
- Security, audit, and operations reviewers agree that validation can begin.

## 11. Release Exit Criteria

QR Refund can proceed to release recommendation only when:

- All Must functional requirements have passing validation evidence or approved exception records.
- All acceptance scenarios pass or have approved defect deferrals.
- All API operations pass contract validation and required negative tests.
- Security validation has no unresolved high or critical findings.
- Audit validation confirms immutable material event coverage and masking.
- Reconciliation validation confirms match and mismatch detection.
- Performance validation meets the approved target or has signed risk acceptance.
- Operational readiness validation is complete, including runbook, monitoring, alerting, exception handling, and retry evidence.
- Required Jira, Confluence, GitHub Actions, SonarCloud, traceability, feedback, validation, and release evidence links are recorded.
- Release Manager, Product Owner, QA Lead, Payments Architect, Security/Risk Lead, Compliance Lead, Operations Lead, and Finance Lead approvals are captured.

## 12. Evidence Required

| Evidence ID | Evidence | Owner | Required For |
| --- | --- | --- | --- |
| EVD-QRREF-001 | Requirement coverage checklist mapped to `FR-QRREF-001` through `FR-QRREF-020`. | QA Lead | Requirement coverage validation |
| EVD-QRREF-002 | API contract validation results for all QR Refund operations. | API Architect / QA Lead | API coverage validation |
| EVD-QRREF-003 | Gherkin acceptance execution report. | QA Lead | Acceptance test coverage |
| EVD-QRREF-004 | Authorization and entitlement test report. | Security Architect | Security validation |
| EVD-QRREF-005 | Sensitive-data masking evidence for responses, logs, notifications, reports, operations views, and audit views. | Security Architect / Compliance Lead | Security and audit validation |
| EVD-QRREF-006 | Audit event completeness report with synthetic payload samples. | Compliance Lead / QA Lead | Audit validation |
| EVD-QRREF-007 | Reconciliation match and mismatch test evidence. | Finance Lead / Operations Lead | Reconciliation validation |
| EVD-QRREF-008 | Failure-mode test report for processor, ledger, notification, audit, and reconciliation failures. | QA Lead / DevSecOps Lead | NFR and safe degradation validation |
| EVD-QRREF-009 | Performance test report against approved MVP volume. | Payments Architect / QA Lead | Performance validation |
| EVD-QRREF-010 | Observability dashboard and alert evidence. | DevSecOps Lead | Operational readiness |
| EVD-QRREF-011 | Operations runbook and exception handling evidence. | Operations Lead | Operational readiness |
| EVD-QRREF-012 | GitHub Actions CI evidence. | DevSecOps Lead | Release entry and exit |
| EVD-QRREF-013 | SonarCloud quality gate evidence once application code exists. | DevSecOps Lead | Release exit |
| EVD-QRREF-014 | Jira approval links or lab chat confirmation for required gates. | Product Owner / Release Manager | Human approval |
| EVD-QRREF-015 | Feedback log entries for validation findings and accepted risks. | QA Lead | Traceability and continuous improvement |

## Known Validation Blockers And Dependencies

| Item | Source | Impact | Required Resolution |
| --- | --- | --- | --- |
| Accounting and settlement adjustment | ADR-QRREF-001 | Blocks implementation and finance validation. | Architecture and Finance approval. |
| Idempotency and concurrency boundary | ADR-QRREF-003 | Blocks implementation and concurrency validation. | Architecture approval. |
| High-value review state model | ADR-QRREF-004 | Blocks final API/test baseline and manual-review validation. | Product, Risk, and Architecture approval. |
| Safe degradation behavior | ADR-QRREF-006 | Blocks failure-mode validation. | Architecture and DevSecOps approval. |
| Reconciliation mismatch workflow | ADR-QRREF-007 | Blocks final reconciliation operations validation. | Operations and Finance approval. |
| Reporting delivery model | ADR-QRREF-008 | Blocks reporting validation. | Product and Operations approval. |
| Regulatory retention period | JIRA-QRREF-008 | Blocks retention validation. | Compliance approval. |
| MVP volume assumptions | JIRA-QRREF-011 | Blocks performance validation. | Product and Architecture approval. |

## Human Approval

| Gate | Jira Placeholder | Required Approver | Status |
| --- | --- | --- | --- |
| Validation plan approval | JIRA-QRREF-080 | QA Lead | Pending |
| Security validation approval | JIRA-QRREF-081 | Security and Risk Lead | Pending |
| Audit and compliance validation approval | JIRA-QRREF-082 | Compliance Lead | Pending |
| Reconciliation validation approval | JIRA-QRREF-083 | Finance Lead / Operations Lead | Pending |
| Operational readiness approval | JIRA-QRREF-084 | Operations Lead / DevSecOps Lead | Pending |
| Performance validation approval | JIRA-QRREF-085 | Payments Architect / QA Lead | Pending |
| Release validation approval | JIRA-QRREF-086 | Release Manager | Pending |

## Next Step

Stop for QA validation plan approval. Do not create validation report, release notes, implementation code, or additional contracts until this plan is approved.
