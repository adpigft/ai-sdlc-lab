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

## Process
1. Confirm approved requirements are available.
2. Use `qa-test-design` for acceptance coverage.
3. Include integration, security, and performance scenarios in the QA-owned design when those risks apply.
4. Define acceptance, negative, integration, security, and NFR scenarios.
5. Identify test data, mocks, environments, and dependencies.
6. Ask for QA approval before implementation relies on the test design.

## Outputs
- Acceptance scenarios
- Negative and edge-case scenarios
- Integration test scenarios
- Security test scenarios when applicable
- NFR test scenarios when applicable

## Quality checks
- Tests map to approved requirements and acceptance criteria.
- Negative and failure scenarios are included.
- Integration and security risks are covered when relevant.
- Unit tests remain owned by `$implementation`.
- QA approval evidence is captured.

## Human gate
QA approval is required before implementation starts.

## Next skill or next workflow step
Use traceability updates, then `$implementation` after approved architecture, API, tests, and traceability.

## Example usage
`$test-design Create QA scenarios for approved QR refund specification`
