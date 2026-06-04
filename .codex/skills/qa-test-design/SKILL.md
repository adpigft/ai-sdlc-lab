---
name: qa-test-design
description: Create acceptance tests and coverage scenarios from approved requirements and API contracts.
---

# QA Test Design Skill

## Purpose
Create test scenarios before implementation.

## When to use
Use after API contract is approved.

## Inputs
- spec.md
- openapi.yaml
- context.md
- framework/04-engineering-standards/standards/testing-standards.md

## Process
1. Review requirements.
2. Derive happy path scenarios.
3. Derive negative scenarios.
4. Derive boundary scenarios.
5. Derive timeout, duplicate, fraud, audit, and reconciliation scenarios.
6. Check requirement coverage.
7. Ask for approval.

## Output
- domains/<domain>/capabilities/<capability>/features/<feature>/tests/acceptance.feature

## Quality checks
- Every functional requirement has test coverage.
- Key NFRs have validation scenarios.
- Negative and edge cases are covered.
- Tests are written in clear Gherkin.
- No code is generated.

## Human gate
QA approval is required before implementation.

## Next skill
traceability-review
