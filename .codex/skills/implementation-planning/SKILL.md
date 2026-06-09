---
name: implementation-planning
description: Prepare the delivery plan, dependencies, risks, and traceability placeholders before implementation.
---

# Implementation Planning Skill

## Purpose

Prepare the delivery plan, dependencies, risks, and traceability placeholders before implementation starts.

## When To Use

Use `$implementation-planning` after implementation readiness when the team needs a build-ready plan.

## Inputs Needed

- Implementation readiness review
- Approved design
- Approved traceability
- Scope and slice candidates
- Dependencies, risks, and assumptions

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and lifecycle behavior are defined by:

- `framework/01-lifecycle/skill-orchestration-adapter.md`
- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`

## Procedure

1. Confirm implementation readiness inputs are complete.
2. Split scope into delivery slices and sequence the work.
3. Identify dependencies, risks, observability needs, data migrations, and rollback needs.
4. Create traceability placeholders for planned code, tests, and validation evidence.
5. Stop before code implementation starts.

## Outputs Produced

- Implementation plan
- Implementation slices
- Implementation dependencies
- Implementation risks
- Implementation traceability
- Sprint plan

## Artifact Structure

1. Scope
2. Slices
3. Target Components
4. Target Files
5. Dependencies
6. Risks
7. Testing Approach
8. Traceability

## Quality Checks

- Slices are specific and reviewable.
- Dependencies and risks are explicit.
- Traceability placeholders are present.
- The plan does not create code.

## Stop Conditions

- Implementation readiness is missing.
- The scope is too broad to slice.
- Required design or traceability inputs are missing.

## Human Approval Expectations

Developer and architect review are required before implementation depends on the plan.

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
