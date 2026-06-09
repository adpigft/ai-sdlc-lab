---
name: vertical-slice-planning
description: Define vertically deliverable implementation slices with complete business and technical coverage.
---

# Vertical Slice Planning Skill

## Purpose

Define vertically deliverable implementation slices with frontend, backend, data, API, observability, tests, acceptance criteria, and traceability.

## When To Use

Use `$vertical-slice-planning` after implementation planning when the team needs business slices that can be delivered end to end.

## Inputs Needed

- Implementation plan
- Business scope
- Frontend, backend, data, and API context
- Acceptance criteria and traceability

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and lifecycle behavior are defined by:

- `framework/01-lifecycle/skill-orchestration-adapter.md`
- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`

## Procedure

1. Review the implementation plan and business scope.
2. Break the work into vertically deliverable slices.
3. Ensure each slice contains frontend, backend, database, API, domain logic, audit/observability, tests, acceptance criteria, and traceability.
4. Distinguish horizontal foundation work from business slices.
5. Stop before code is implemented.

## Outputs Produced

- Vertical slice plan
- Slice descriptions
- Coverage and traceability notes
- Foundation-slice distinction

## Artifact Structure

1. Slice Overview
2. Frontend Scope
3. Backend Scope
4. Database Scope
5. API Scope
6. Domain Logic
7. Audit / Observability
8. Tests
9. Acceptance Criteria
10. Traceability

## Quality Checks

- Each slice is vertically deliverable.
- Foundation work is clearly separated.
- Tests and acceptance criteria are present.
- Traceability is explicit.

## Stop Conditions

- Implementation plan is missing.
- The slice cannot be made vertical without unresolved dependencies.
- The user asks to implement instead of plan.

## Human Approval Expectations

Human review is required before implementation depends on the slice plan.

## Do Not

- Do not modify external systems unless explicitly approved.
- Do not create, update, delete, or transition Jira, Confluence, GitHub, Wynxx Story Creator, or source-code artifacts unless the skill explicitly allows it and the user approves.
- Do not expose secrets, tokens, credentials, or sensitive data.
- Do not fabricate missing requirements, evidence, source references, or approval status.
- Do not treat inferred content as confirmed fact.
- Do not bypass validation, traceability, approval, or stop-for-review rules.
- Do not change code.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
