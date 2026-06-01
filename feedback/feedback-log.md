# Feedback Log

This log captures learning from review, testing, operations, production monitoring, incidents, and customer feedback. Feedback may trigger requirement changes, test updates, skill updates, standards updates, Jira backlog items, Confluence updates, or ADRs.

## Intake Rules

- Use synthetic or masked examples. Do not record real customer data.
- Link every actionable item to Jira.
- Link stakeholder-facing updates to Confluence placeholders until real pages exist.
- Classify whether feedback affects product behavior, security, operations, tests, AI prompts, or delivery workflow.
- Update traceability if feedback changes requirements, validation evidence, or release scope.

## Feedback Entries

| Feedback ID | Date | Source | Capability | Observation | Impact | Jira | Confluence | Action | Status | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FB-KHQR-001 | 2026-06-01 | Baseline review | KHQR payment | Duplicate payment handling must be explicit before implementation. | Potential customer harm and reconciliation load if missed. | JIRA-KHQR-015 | CONF-PAY-KHQR-SPEC | Add idempotency requirement, duplicate scenarios, API header, and validation evidence. | Actioned in draft artifacts | Payments Architect |
| FB-KHQR-002 | 2026-06-01 | Baseline review | KHQR payment | Release evidence must include SonarCloud and GitHub Actions links once code exists. | Weak audit trail if release evidence is manual only. | JIRA-KHQR-035 | CONF-PAY-KHQR-VALIDATION | Add CI and quality gate evidence placeholders before implementation. | Actioned in draft artifacts | DevSecOps Lead |
| FB-KHQR-003 | 2026-06-01 | Product review | KHQR payment | Invalid QR payload behavior must happen before payment creation. | Reduces invalid payment instructions and support cases. | JIRA-KHQR-010 | CONF-PAY-KHQR-SPEC | Add FR-KHQR-001 and acceptance scenario. | Actioned in draft artifacts | Product Owner |
| FB-KHQR-004 | 2026-06-01 | Customer journey review | KHQR payment | Customer must see merchant, amount, currency, and funding account before confirmation. | Prevents wrong-merchant and wrong-amount complaints. | JIRA-KHQR-011 | CONF-PAY-KHQR-SPEC | Add FR-KHQR-002 and confirmation scenario. | Actioned in draft artifacts | Product Owner |
| FB-KHQR-005 | 2026-06-01 | Security review | KHQR payment | Status and initiation must enforce account ownership and customer authorization. | Prevents unauthorized debit and disclosure. | JIRA-KHQR-012 | CONF-PAY-KHQR-CONTROLS | Add authorization requirement and negative scenario. | Actioned in draft artifacts | Security and Risk Lead |
| FB-KHQR-006 | 2026-06-01 | Risk review | KHQR payment | Limits need explicit requirement and approval. | Prevents limit bypass and risk policy breach. | JIRA-KHQR-013 | CONF-PAY-KHQR-CONTROLS | Add limit requirement and open decision. | New | Product Owner |
| FB-KHQR-007 | 2026-06-01 | Financial crime review | KHQR payment | Fraud and sanctions outcomes must be customer-safe. | Prevents leakage of internal risk logic. | JIRA-KHQR-017 | CONF-PAY-KHQR-CONTROLS | Add screening requirement and customer-message open question. | New | Security and Risk Lead |
| FB-KHQR-008 | 2026-06-01 | Operations review | KHQR payment | Processor timeout must not be represented as final failure. | Reduces duplicate customer retries and reconciliation exceptions. | JIRA-KHQR-018 | CONF-PAY-KHQR-RUNBOOK | Add pending status requirement and scenario. | Actioned in draft artifacts | Payments Architect |
| FB-KHQR-009 | 2026-06-01 | Privacy review | KHQR payment | Customer must not retrieve another customer's payment status. | Prevents confidentiality breach. | JIRA-KHQR-019 | CONF-PAY-KHQR-CONTROLS | Add status authorization scenario. | Actioned in draft artifacts | Security and Risk Lead |
| FB-KHQR-010 | 2026-06-01 | Product review | KHQR payment | Notifications may depend on channel configuration. | Avoids overcommitting release scope. | JIRA-KHQR-020 | CONF-PAY-KHQR-SPEC | Mark notifications as conditional should requirement. | New | Product Owner |
| FB-KHQR-011 | 2026-06-01 | Audit review | KHQR payment | All material state changes need audit events. | Supports audit, support, and investigations. | JIRA-KHQR-021 | CONF-PAY-KHQR-CONTROLS | Add audit requirement and terminal status scenario. | Actioned in draft artifacts | Operations Lead |
| FB-KHQR-012 | 2026-06-01 | Architecture review | KHQR payment | Performance target is not yet approved. | NFR validation cannot complete. | JIRA-KHQR-030 | CONF-PAY-KHQR-SPEC | Keep NFR blocked until target is approved. | New | Payments Architect |
| FB-KHQR-013 | 2026-06-01 | SRE review | KHQR payment | Observability must include duplicate rate and pending age. | Enables early detection of payment degradation. | JIRA-KHQR-031 | CONF-PAY-KHQR-RUNBOOK | Add operational evidence placeholder. | New | DevSecOps Lead |
| FB-KHQR-014 | 2026-06-01 | Security review | KHQR payment | QR payload masking rules need explicit approval. | Prevents sensitive data leakage. | JIRA-KHQR-032 | CONF-PAY-KHQR-CONTROLS | Add data classification and masking open question. | New | Security and Risk Lead |
| FB-KHQR-015 | 2026-06-01 | Operations review | KHQR payment | Reconciliation needs payment, processor, status, timestamp, and correlation references. | Supports exception handling and customer support. | JIRA-KHQR-034 | CONF-PAY-KHQR-RUNBOOK | Add reconciliation NFR. | Actioned in draft artifacts | Operations Lead |
| FB-QRREF-001 | 2026-06-01 | Traceability gap review | QR Refund | Must-fix acceptance gaps existed for operations refund creation, post-settlement eligibility, merchant balance non-blocking behavior, reason-code rejection, missing idempotency key, concurrent duplicate prevention, non-approved override controls, and audit failure behavior. | Implementation could proceed without executable acceptance expectations for banking-grade controls. | JIRA-QRREF-070 | CONF-PAY-QRREF-SPEC | Added acceptance scenarios and updated traceability coverage before implementation. | Actioned in acceptance and traceability artifacts | QA Lead |
| FB-QRREF-002 | 2026-06-01 | Traceability gap review | QR Refund | Accounting treatment, idempotency/concurrency boundary, high-value review state model, audit event boundary, overrideable control policy, and retention policy remain design or compliance decisions. | Implementation must not start until required architecture, risk, and compliance decisions are approved or explicitly deferred by gate owners. | JIRA-QRREF-071 | CONF-PAY-QRREF-CONTEXT | Keep open design and compliance gaps visible in traceability; resolve through architecture/design approval before implementation. | Open | Payments Architect |

## Feedback Triage Questions

1. Does this change customer-visible payment behavior?
2. Does this affect risk, compliance, audit, fraud, security, or privacy posture?
3. Does this require a new or changed requirement?
4. Does this require a new or changed test?
5. Does this require a human gate, ADR, or Jira approval?
6. Does this require a Confluence stakeholder update?
7. Does this reveal a gap in AI instructions, templates, or standards?
