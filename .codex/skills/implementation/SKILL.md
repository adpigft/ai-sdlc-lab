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

## Context pack
Use the `Implementation` pack in `framework/context/stage-context-packs.md`.

Required reads:
- This skill document.
- Active `workflow-state.yaml`.
- Active domain context.
- Approved intent, specification, architecture, API, test design, traceability, and implementation plan.
- Placement metadata, including `allowed_paths` and `restricted_paths`.
- Coding, testing, and security standards relevant to the approved slice.

Optional reads:
- Existing source and tests only inside approved `allowed_paths`.
- Service, frontend, or shared asset ownership docs referenced by placement metadata.

Forbidden reads:
- Source outside `allowed_paths`.
- Restricted paths.
- Unrelated domains, services, frontend modules, and release artifacts unless preparing approved release evidence.

Escalation rule: Stop and request approval before reading or editing any path outside approved `allowed_paths`.

Token discipline rule: Load only the approved slice, its placement metadata, and files in allowed paths; full framework reads are allowed only for framework assessment or framework changes.

Stop conditions:
- Upstream approvals are missing.
- `allowed_paths` or `restricted_paths` are missing.
- The requested change needs restricted paths.
- Scope expands beyond the approved implementation slice.

## Process
1. Confirm all upstream approvals and traceability are present.
2. Read `domains/<domain>/domain-context.md` when the domain is known and the file exists.
3. Check implementation placement metadata before writing code.
4. Stop if `allowed_paths` or `restricted_paths` are missing for a code-impacting slice.
5. Use `developer-implementation`.
6. Use TDD for the approved slice: failing test, implementation, passing test, refactor.
7. Keep changes limited to the approved slice and do not write outside `allowed_paths`.
8. Stop and report gaps instead of coding around missing or conflicting approved artifacts.
9. When implementation slice planning, build readiness, code, unit tests, or PR evidence are created or updated, create or update `domains/<domain>/capabilities/<capability>/workflow-state.yaml`.
10. For build readiness or slice planning, set workflow state to `implementation_ready`, pending gate to `implementation_start_approval`, next state to `implementation_in_progress`, and next skill to `implementation`.
11. For an implemented slice or PR evidence, set workflow state to `implementation_in_progress`, current artifact to the slice/PR evidence, pending gate to `implementation_slice_approval`, next state to `validation_ready`, and next skill to `validation`.
12. Use `framework/workflow/workflow-state-guide.md` for state-aware `Review.`, `Approved.`, and `Status.` behavior.
13. After implementation slice approval, update `workflow-state.yaml` to move from `implementation_in_progress` to `validation_ready`.
14. Prepare the slice for review and validation.

## Placement metadata
Before implementation or a code-impacting change, the approved slice must define:

- `target_app`, if frontend is impacted
- `target_frontend_module`, if frontend is impacted
- `target_service`, if backend is impacted
- `target_library`, if shared library is impacted
- `owning_squad`
- `allowed_paths`
- `restricted_paths`
- `required_approvals`
- `impacted_capabilities`
- `regression_scope`

Implementation must stop if `allowed_paths` or `restricted_paths` are missing. Implementation must not write outside `allowed_paths`; if work requires a restricted or unapproved path, stop for architecture and owner review.

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
- Missing placement metadata blocks code-impacting implementation.
- Code changes stay inside approved `allowed_paths`.
- Domain context was reviewed when available.
- Workflow state distinguishes build readiness from implemented-slice review.
- `Review.`, `Approved.`, and `Status.` can identify the active slice or blocker from workflow state.

## Human gate
Developer and Architect review is required before QA validation.

## Next skill or next workflow step
Use `$validation` after implementation review.

## Example usage
`$implementation Implement approved slice: refund request idempotency`
