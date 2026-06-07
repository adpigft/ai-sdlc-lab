# Context Drift Model

## Purpose

Define the main drift types that should be detected when context is reused over time.

## Drift Types

| Drift Type | Signal | Detection Method | Severity | Owner | Remediation Action |
| --- | --- | --- | --- | --- | --- |
| code-spec drift | Source code changed but intent/spec/design did not move with it. | Compare Git diff, traceability, and validation deltas. | High | Developer Lead | Refresh spec/design and revalidate. |
| API-contract drift | API implementation and contract diverge. | Compare OpenAPI, code, and validation evidence. | High | Solution Architect | Update the contract or implementation and rerun checks. |
| test-spec drift | Tests no longer match approved requirements. | Compare test scenarios, spec, and failing validations. | Medium | QA Lead | Update tests or specification and rerun evals. |
| Jira-Git drift | Jira status or links differ from Git-owned truth. | Compare Jira references with Git artifacts and traceability. | Medium | Delivery Lead | Resynchronize Jira tracking and traceability. |
| Confluence-Git drift | Published pages differ from Git-owned summary. | Compare Confluence references with Git-built artifacts. | Medium | Delivery Lead | Republish from Git-owned content. |
| context-version drift | A package version is old relative to the approved source. | Compare package version, expiry, and last reviewed date. | Medium | Context Owner | Repackage and reapprove. |
| production-behavior drift | Observed behavior differs from expected context. | Compare telemetry, incidents, and feedback against package assumptions. | High | Product / Delivery Lead | Investigate, update context, and revalidate. |
| security-standard drift | Context or artifacts violate current security rules. | Run security scanning and review policy gaps. | High | DevSecOps / Platform | Remove unsafe context and reissue package. |

## Notes

- Drift detection should feed context health scoring and reuse decisions.
- Drift does not automatically change source-of-truth artifacts.
