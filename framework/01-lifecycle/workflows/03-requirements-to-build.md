# Workflow 03: Requirements To Build

## Purpose

Prepare implementation work from approved requirements without starting application code prematurely.

## Inputs

- Approved requirements and review gate.
- Jira epic and stories.
- API contract and acceptance scenarios.
- Coding, security, API, and testing standards.

## Steps

1. Read `domains/<domain>/domain-context.md` when available.
2. Split the approved requirements into Jira stories that each deliver testable value.
3. Link each story to requirement IDs and acceptance scenarios.
4. Identify implementation dependencies, data migrations, feature flags, observability, rollback needs, and implementation readiness gaps.
5. Confirm GitHub branch, pull request, review, and CI expectations.
6. Define implementation planning, vertical slice planning, and implementation architecture inputs before implementation starts.
7. Define required tests and SonarCloud quality gate expectations before implementation starts.
8. Update traceability with planned code, test, and validation evidence placeholders.
9. Hold a build readiness gate.
10. After design, impact-analysis, and readiness approvals, update or prepare `workflow-state.yaml` so the capability can move through `implementation_ready` and `implementation_in_progress` when workflow-state is adopted.

## Outputs

- Build-ready Jira stories.
- Implementation readiness review.
- Implementation plan.
- Vertical slice plan.
- Implementation architecture inputs.
- Test plan.
- Traceability updates.

## Human Gate

The build readiness gate must be approved by product, architecture, QA, and engineering before any application code is added under `src/`.
