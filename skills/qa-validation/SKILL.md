---
name: qa-validation
description: Validate implementation against approved requirements, API contract, acceptance tests, and traceability.
---

# QA Validation Skill

## Purpose
Validate implementation against approved artifacts.

## When to use
Use after implementation is complete.

## Inputs
- spec.md
- context.md
- openapi.yaml
- acceptance.feature
- source code
- test results
- traceability matrix

## Process
1. Review implementation coverage.
2. Review test results.
3. Identify failed or missing validation.
4. Check traceability.
5. Produce validation report.
6. Ask for approval.

## Output
- domains/<domain>/capabilities/<capability>/validation/validation-report.md

## Quality checks
- All acceptance criteria are validated.
- Test failures are recorded.
- Gaps are linked to feedback.
- Release readiness is clearly stated.

## Human gate
QA approval required before release.

## Next skill
devsecops-release
