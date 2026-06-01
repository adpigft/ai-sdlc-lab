# Workflow 03: Specification To Build

## Purpose

Prepare implementation work from an approved specification without starting application code prematurely.

## Inputs

- Approved spec and review gate.
- Jira epic and stories.
- API contract and acceptance scenarios.
- Coding, security, API, and testing standards.

## Steps

1. Read `domains/<domain>/domain-context.md` when available.
2. Split the approved specification into Jira stories that each deliver testable value.
3. Link each story to requirement IDs and acceptance scenarios.
4. Identify implementation dependencies, data migrations, feature flags, observability, and rollback needs.
5. Confirm GitHub branch, pull request, review, and CI expectations.
6. Define required tests and SonarCloud quality gate expectations before implementation starts.
7. Update traceability with planned code, test, and validation evidence placeholders.
8. Hold a build readiness gate.
9. After architecture and test design approvals, update or prepare `workflow-state.yaml` so the capability can move through `test_review`, `implementation_ready`, and `implementation_in_progress` when workflow-state is adopted.

## Outputs

- Build-ready Jira stories.
- Implementation plan.
- Test plan.
- Traceability updates.

## Human Gate

The build readiness gate must be approved by product, architecture, QA, and engineering before any application code is added under `src/`.
