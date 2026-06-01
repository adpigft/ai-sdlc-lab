---
name: implementation
description: Developer-owned implementation entry point for TDD, unit tests, code, refactoring, and one approved slice at a time.
---

# Implementation Skill

## Purpose
Implement one approved delivery slice at a time using TDD, unit tests, code changes, and focused refactoring.

## When to use
Use `$implementation` only after intent, specification, architecture, API where applicable, test design, and traceability are approved.

## Inputs
- Approved intent, specification, architecture, API, tests, and traceability
- Approved implementation slice
- Domain context, such as `domains/<domain>/domain-context.md`, when available
- Coding, security, and testing standards
- Existing source and test code
- Jira Task or Subtask if available

## Process
1. Confirm all upstream approvals and traceability are present.
2. Read `domains/<domain>/domain-context.md` when the domain is known and the file exists.
3. Use `developer-implementation`.
4. Use TDD for the approved slice: failing test, implementation, passing test, refactor.
5. Keep changes limited to the approved slice.
6. Stop and report gaps instead of coding around missing or conflicting approved artifacts.
7. When implementation slice planning, build readiness, code, unit tests, or PR evidence are created or updated, create or update `domains/<domain>/capabilities/<capability>/workflow-state.yaml`.
8. For build readiness or slice planning, set workflow state to `implementation_ready`, pending gate to `implementation_start_approval`, next state to `implementation_in_progress`, and next skill to `implementation`.
9. For an implemented slice or PR evidence, set workflow state to `implementation_in_progress`, current artifact to the slice/PR evidence, pending gate to `implementation_slice_approval`, next state to `validation_ready`, and next skill to `validation`.
10. Use `framework/workflow/workflow-state-guide.md` for state-aware `Review.`, `Approved.`, and `Status.` behavior.
11. After implementation slice approval, update `workflow-state.yaml` to move from `implementation_in_progress` to `validation_ready`.
12. Prepare the slice for review and validation.

## Outputs
- Unit tests and implementation code for the approved slice
- Focused refactoring where needed
- Developer notes for validation
- PR readiness summary
- Created or updated `domains/**/workflow-state.yaml` after implementation planning or slice evidence creation

## Quality checks
- One approved slice is implemented at a time.
- Unit tests are included and passing where runnable.
- Code maps to approved requirements and test design.
- No secrets are committed.
- Missing upstream approval blocks implementation.
- Domain context was reviewed when available.
- Workflow state distinguishes build readiness from implemented-slice review.
- `Review.`, `Approved.`, and `Status.` can identify the active slice or blocker from workflow state.

## Human gate
Developer and Architect review is required before QA validation.

## Next skill or next workflow step
Use `$validation` after implementation review.

## Example usage
`$implementation Implement approved slice: refund request idempotency`
