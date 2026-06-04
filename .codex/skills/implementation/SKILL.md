---
name: implementation
description: Implement one approved slice at a time using tests, focused code changes, and reviewable evidence.
---

# Implementation Skill

## Purpose

Implement the smallest approved delivery slice while preserving approved scope, design intent, test coverage, and reviewability.

## When To Use

Use `$implementation` only after required intent, specification, design, test design, traceability, and slice approval exist for the work being implemented.

## Inputs Needed

- Approved intent, specification, design, tests, and traceability
- Approved implementation slice or change scope
- Coding, security, and testing standards
- Existing source and test code for the approved scope
- Placement, ownership, and approval constraints when the framework defines them

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, allowed/restricted paths, approval gates, and lifecycle behavior are defined by:

- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/03-delivery-governance/service-architecture/implementation-placement-model.md`
- `framework/01-lifecycle/skill-orchestration-adapter.md`

## Procedure

1. Confirm upstream approvals and slice scope before reading or editing source code.
2. Understand the approved requirements, design, tests, and expected evidence.
3. Explain proposed module/package impact, domain model impact, service flow, and changed files before coding when not already approved.
4. Implement one approved slice at a time.
5. Prefer TDD where practical: failing test, implementation, passing test, focused refactor.
6. Update or add tests for changed behavior.
7. Avoid broad rewrites and unrelated refactors.
8. Stop and report specification, design, ownership, or test gaps instead of coding around them.
9. Prepare implementation evidence for review.

## Outputs Produced

- Source changes for the approved slice
- Unit, integration, or supporting tests as appropriate
- Focused refactoring where needed
- Developer notes, evidence, or PR readiness summary

## Artifact Structure

1. Scope
2. Slices
3. Target Components
4. Target Files
5. Testing Approach
6. Risks
7. Open Questions

## Quality Checks

- Code maps to approved requirements and design.
- Tests cover the implemented behavior.
- Sensitive data is protected and secrets are not committed.
- Error handling and failure behavior are explicit.
- Changes are limited to approved scope.
- Build or local validation is run where practical.

## Stop Conditions

- Upstream approvals are missing.
- Approved scope or target ownership is unclear.
- Required placement or path constraints are missing in frameworks that enforce them.
- The requested implementation expands beyond the approved slice.
- A requirement, design, or test gap blocks correct implementation.

## Human Approval Expectations

Developer review, architect review, and any required owner approvals are expected before PR review, validation, or release evidence depends on the implementation.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
