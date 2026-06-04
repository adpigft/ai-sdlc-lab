# KHQR Payment Release Notes

## Metadata

| Field | Value |
| --- | --- |
| Release ID | REL-KHQR-001 |
| Jira Release | JIRA-KHQR-090 |
| Change Record | CHG-KHQR-001 |
| Confluence Page | CONF-PAY-KHQR-RELEASE |
| Capability | KHQR payment initiation |
| Status | Draft, not approved for release |
| Deployment Window | Pending |

## Release Summary

This planned release will introduce mobile banking KHQR merchant payment initiation with customer confirmation, idempotency-based duplicate prevention, risk screening integration points, payment status inquiry, audit evidence, and operational reconciliation support.

No application code has been created yet. These release notes define the expected release evidence and approval gates.

## Planned Scope

| Jira | Requirement | Included | Notes |
| --- | --- | --- | --- |
| JIRA-KHQR-010 | QR payload validation | Yes | Must reject malformed, unsupported, or expired payloads. |
| JIRA-KHQR-011 | Customer confirmation details | Yes | Merchant, amount, currency, and funding account must be confirmed. |
| JIRA-KHQR-012 | Funding account authorization | Yes | Unauthorized debit attempts rejected. |
| JIRA-KHQR-013 | Limits enforcement | Yes | Limits to be approved before build. |
| JIRA-KHQR-014 | Idempotency required | Yes | Header required by API contract. |
| JIRA-KHQR-015 | Duplicate prevention | Yes | Same key and payload returns original payment. |
| JIRA-KHQR-016 | Duplicate conflict rejection | Yes | Same key with conflicting payload rejected. |
| JIRA-KHQR-017 | Fraud and sanctions path | Yes | Customer-safe handling required. |
| JIRA-KHQR-018 | Processor pending state | Yes | Timeout must not be shown as false failure. |
| JIRA-KHQR-019 | Status inquiry | Yes | Customer can view only own payment. |
| JIRA-KHQR-020 | Notifications | Conditional | Subject to channel configuration. |
| JIRA-KHQR-021 | Audit events | Yes | Required for all material state changes. |

## Required Release Evidence

| Evidence | Placeholder | Status |
| --- | --- | --- |
| Jira release scope | JIRA-KHQR-090 | Pending |
| GitHub pull requests | PR-KHQR-001 | Pending |
| GitHub Actions run | GHA-KHQR-001 | Pending |
| SonarCloud quality gate | SONAR-KHQR-001 | Pending |
| Validation report | VAL-KHQR-001 | Draft |
| Traceability matrix | TRACE-KHQR-001 | Draft |
| Confluence release page | CONF-PAY-KHQR-RELEASE | Pending |
| Operations runbook | CONF-PAY-KHQR-RUNBOOK | Pending |

## Known Risks Before Release

| Risk | Jira | Required Decision |
| --- | --- | --- |
| Pending expiry duration not approved. | JIRA-KHQR-070 | Product and architecture approval. |
| Fraud and sanctions display mapping not approved. | JIRA-KHQR-071 | Security and risk approval. |
| Performance targets not approved. | JIRA-KHQR-072 | Architecture and product approval. |

## Rollback And Support

- Rollback owner: Release Manager.
- Rollback trigger: duplicate execution defect, unauthorized payment defect, unreconciled processor mismatch, critical security issue, or failed post-release verification.
- Support path: Mobile banking support triages customer cases using payment reference, correlation ID, masked customer ID, and processor reference when available.
- Monitoring: dashboards and alerts must cover initiation rate, rejection rate, duplicate rate, pending age, processor failures, and reconciliation exceptions.

## Human Approval Gates

| Gate | Jira Placeholder | Required Approver | Status |
| --- | --- | --- | --- |
| Product release approval | JIRA-KHQR-091 | Product Owner | Pending |
| Technology release approval | JIRA-KHQR-092 | Engineering Lead | Pending |
| Security and risk release approval | JIRA-KHQR-093 | Security and Risk Lead | Pending |
| Operations release approval | JIRA-KHQR-094 | Operations Lead | Pending |
| Change approval | CHG-KHQR-001 | Release Manager | Pending |
