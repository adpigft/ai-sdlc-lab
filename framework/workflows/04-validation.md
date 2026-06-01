# Workflow 04: Validation

## Purpose

Prove that the implemented capability satisfies approved requirements and is ready for release consideration.

## Inputs

- Pull requests and commits.
- Jira stories and requirement IDs.
- Test results and coverage.
- SonarCloud quality gate result.
- Security and operational evidence.

## Steps

1. Run automated tests and static analysis through GitHub Actions.
2. Confirm SonarCloud quality gate status.
3. Execute acceptance, regression, security, and operational checks.
4. Validate traceability from every mandatory requirement to test or review evidence.
5. Record defects, limitations, and accepted risks in Jira.
6. Complete the validation report using `framework/templates/validation-report-template.md`.
7. Request release readiness review.

## Outputs

- Validation report.
- Test evidence.
- Defect and risk summary.
- Updated traceability matrix.

## Human Gate

QA may recommend release readiness, but release approval requires product, engineering, risk, and operations acceptance for the specific release scope.
