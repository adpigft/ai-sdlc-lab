# Context Drift Detection Policy

## Purpose

Context drift detection identifies when approved context, implementation, workflow, and operational reality no longer match.

## Drift Types

| Drift Type | Signal | Detection Method | Severity | Owner | Remediation Action | Control Tower Indicator |
| --- | --- | --- | --- | --- | --- | --- |
| code-spec drift | code behavior differs from spec | PR review, tests, validation | High | developer / architect | update code or spec through approved change | `codeSpecDrift` |
| API-contract drift | API differs from OpenAPI or contract | contract tests, review | High | API owner | align contract or implementation | `apiContractDrift` |
| test-spec drift | tests no longer reflect approved requirements | test review, validation gaps | Medium | QA owner | update test design or tests | `testSpecDrift` |
| Jira-Git drift | Jira state or links differ from Git truth | traceability review | Medium | delivery owner | reconcile workflow references | `jiraGitDrift` |
| Confluence-Git drift | published doc differs from Git truth | doc review, publishing checks | Medium | doc owner | republish approved content | `confluenceGitDrift` |
| production-behavior drift | runtime behavior differs from expected | telemetry, incidents, support tickets | High | service owner | fix behavior, improve monitoring, or rollback | `productionBehaviorDrift` |
| context-version drift | selected package versions are stale | manifest review, lock comparison | Medium | context owner | refresh manifest and package set | `contextVersionDrift` |
| security-standard drift | implementation or context no longer meets security standard | security scan, policy checks | High | security owner | remediate findings and update guidance | `securityStandardDrift` |

## Notes

- Drift detection is a governance signal, not an automatic fix.
- The Control Tower should only expose the indicator later as a read-only view.
- The remediation path remains tied to the approved change and review workflow.
