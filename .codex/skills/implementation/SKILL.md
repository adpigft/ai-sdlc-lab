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
- Coding, security, and testing standards
- Existing source and test code
- Jira Task or Subtask if available

## Process
1. Confirm all upstream approvals and traceability are present.
2. Use `developer-implementation`.
3. Use TDD for the approved slice: failing test, implementation, passing test, refactor.
4. Keep changes limited to the approved slice.
5. Stop and report gaps instead of coding around missing or conflicting approved artifacts.
6. Prepare the slice for review and validation.

## Outputs
- Unit tests and implementation code for the approved slice
- Focused refactoring where needed
- Developer notes for validation
- PR readiness summary

## Quality checks
- One approved slice is implemented at a time.
- Unit tests are included and passing where runnable.
- Code maps to approved requirements and test design.
- No secrets are committed.
- Missing upstream approval blocks implementation.

## Human gate
Developer and Architect review is required before QA validation.

## Next skill or next workflow step
Use `$validation` after implementation review.

## Example usage
`$implementation Implement approved slice: refund request idempotency`
