---
name: test-design
description: QA-owned test design entry point for acceptance, negative, integration, security, and NFR scenarios.
---

# Test Design Skill

## Purpose
Create QA-owned test design from approved requirements and contracts without taking ownership of developer TDD unit tests.

## When to use
Use `$test-design` after specification approval and before implementation validation.

## Inputs
- Approved intent and specification
- Architecture context
- API contract if applicable
- Risk, security, performance, and integration constraints
- Existing acceptance tests

## Context pack
Use the `Test Design` pack in `framework/context/stage-context-packs.md`.

Required reads:
- This skill document.
- Approved specification.
- Architecture context.
- API contract when available.
- Active domain context.
- Active `workflow-state.yaml`.

Optional reads:
- Testing/security standards and traceability when coverage is being checked.

Forbidden reads:
- Source code unless the user explicitly requests regression analysis against existing implementation.
- Release artifacts and unrelated domains.

Escalation rule: Read related domains only when acceptance scenarios, integrations, or regression scope require cross-domain coverage.

Token discipline rule: Keep context to requirements, architecture, API, and test standards; full framework reads are allowed only for framework assessment or framework changes.

Stop conditions:
- Architecture or API approval is missing where required.
- Requirements lack an acceptance basis.
- NFR targets are missing and cannot be recorded as open questions.

## Process
1. Confirm approved requirements are available.
2. Use `qa-test-design` for acceptance coverage.
3. Include integration, security, and performance scenarios in the QA-owned design when those risks apply.
4. Define acceptance, negative, integration, security, and NFR scenarios.
5. Identify test data, mocks, environments, and dependencies.
6. When acceptance tests or QA test design are created or updated, create or update `domains/<domain>/capabilities/<capability>/workflow-state.yaml`.
7. Set workflow state to `test_review`, current artifact to `tests/acceptance.feature` or the QA test design artifact, pending gate to `test_design_approval`, next state to `implementation_ready`, and next skill to `implementation`.
8. Use `framework/workflow/workflow-state-guide.md` for state-aware `Review.`, `Approved.`, and `Status.` behavior.
9. Ask for QA approval before implementation relies on the test design.

## Outputs
- Acceptance scenarios
- Negative and edge-case scenarios
- Integration test scenarios
- Security test scenarios when applicable
- NFR test scenarios when applicable
- Created or updated `domains/**/workflow-state.yaml` after test design artifact creation

## Quality checks
- Tests map to approved requirements and acceptance criteria.
- Negative and failure scenarios are included.
- Integration and security risks are covered when relevant.
- Unit tests remain owned by `$implementation`.
- QA approval evidence is captured.
- Workflow state points `Review.` to the QA test design draft and `Approved.` to implementation readiness.

## Human gate
QA approval is required before implementation starts.

## Next skill or next workflow step
Use traceability updates, then `$implementation` after approved architecture, API, tests, and traceability.

## Example usage
`$test-design Create QA scenarios for approved QR refund specification`
