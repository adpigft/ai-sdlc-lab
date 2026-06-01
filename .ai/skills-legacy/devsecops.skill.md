# DevSecOps Skill

## Mission

Define and operate the delivery controls that make AI-assisted software changes auditable, secure, repeatable, and releasable.

## Inputs

- Repository standards and workflows.
- GitHub Actions configuration.
- SonarCloud project and quality gate configuration.
- Jira release, change, and approval records.
- Validation and traceability artifacts.

## Outputs

- CI/CD workflow design.
- Quality gate recommendations.
- Security scanning requirements.
- Release evidence checklist.
- Operational readiness findings.

## Baseline Gate Expectations

- GitHub Actions runs formatting, linting, tests, coverage, dependency scanning, secret scanning, traceability checks, and artifact validation.
- SonarCloud runs static analysis with a quality gate for reliability, maintainability, security, duplications, and coverage.
- Release workflows require human approval for production deployment.
- Every release can be linked to Jira scope, commits, pull requests, validation evidence, and release notes.

## Banking Payments Checklist

- Include segregation of duties between author, reviewer, and release approver.
- Capture change windows, rollback plans, monitoring dashboards, and incident contacts.
- Protect secrets, keys, payment processor credentials, and signing material.
- Ensure audit logs and deployment records are retained according to policy.

## Guardrails

- Do not weaken quality gates to pass a release without explicit risk acceptance.
- Do not store secrets in repository files.
- Do not deploy untraceable changes.
- Do not use AI-generated release evidence without human verification.

## Human Gate

Production release requires named approval in Jira or the change-management system, with the approval reference added to the release notes.
