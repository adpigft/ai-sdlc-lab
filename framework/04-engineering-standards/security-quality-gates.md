# Security And Quality Gates

## Purpose

Define minimum security, code quality, CI/CD, and branch protection expectations for enterprise delivery.

## Required Gates

| Gate | Requirement |
| --- | --- |
| Formatting | Spotless passes for Java services; Flutter formatting passes for channel apps. |
| Static code quality | Checkstyle, PMD, SpotBugs, and Sonar checks pass for Java services. |
| Tests | Required unit, component, API, integration, and contract tests pass for impacted areas. |
| Coverage | JaCoCo coverage is published to Sonar; minimum target is 80% line coverage unless a project-specific threshold is approved. |
| Dependency scan | No unresolved high or critical dependency vulnerabilities. |
| Secret scan | No tokens, passwords, private keys, certificates, or credentials in repository files. |
| Container scan | No unresolved high or critical image vulnerabilities for release artifacts. |
| Infrastructure scan | Helm and deployment manifests pass policy checks where configured. |
| API contract | OpenAPI validation passes for changed contracts. |
| Event contract | Schema compatibility checks pass for changed events. |
| Release readiness | Validation evidence, rollback notes, known risks, and approvals are present before release. |

## GitHub Actions

GitHub Actions should enforce:

- framework validation scripts
- build and test execution
- OpenAPI validation
- Java validation where code exists
- Flutter validation where channel code exists
- Sonar scan and quality gate where configured
- dependency and secret scanning where configured
- artifact publication only after required checks pass

## Branch Protection

Protected branches should require:

- pull request review
- passing required CI checks
- signed or verified commits where policy requires
- branch up to date before merge where required
- CODEOWNERS review for owned paths
- no force pushes
- no direct pushes except approved emergency controls
- required conversation resolution

## Security Controls

- Use Spring Security for service authorization.
- Use OAuth2 and OIDC for user and service identities.
- Use PKCE for mobile app authentication.
- Use managed identities, workload identity, mTLS, or approved client assertions for service-to-service trust.
- Use external secret managers for runtime secrets.
- Never store credentials in source, generated artifacts, Helm values, or documentation examples.
- Mask sensitive card, customer, account, token, and processor values in logs, events, traces, and validation evidence.

## Exception Handling

Exceptions to a gate require:

- owner and approver
- reason and risk statement
- expiry date
- compensating control
- linked Jira or Git evidence
- release note entry where release risk is affected

