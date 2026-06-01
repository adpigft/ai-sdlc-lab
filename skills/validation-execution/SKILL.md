---
name: validation-execution
description: Execute validation plan.
---

# Validation Execution Skill

## Purpose
Execute validation plan.

## When to use
Use after implementation is available and a validation plan is approved.

## Inputs
- `validation-plan.md`
- code
- tests
- APIs

## Process
1. Execute the planned validation checks.
2. Capture evidence and failures.
3. Map results to requirements and APIs.
4. Summarize the validation outcome.

## Output
- `validation-report.md`

## Checks
- requirement coverage
- API coverage
- test coverage
- security validation
- audit validation
- reconciliation validation
- NFR validation

## Result
- pass
- conditional pass
- fail

## Rules
- validation only
- do not modify artifacts

## Human gate
Validation results require human review before release readiness.
