---
name: refactoring
description: Propose or apply safe refactoring with no functional change. Use when code needs structural improvement without changing behavior.
---

# Refactoring Skill

## Purpose
Propose or apply safe refactoring with no functional change.

## When to use
Use when code structure needs improvement but functional behavior must remain unchanged.

## Inputs
- code
- tests
- traceability
- review findings

## Process
1. Identify safe refactoring scope.
2. Preserve external behavior.
3. Update or add tests if needed.
4. Ask for approval before modifying code.

## Outputs
- refactoring proposal or refactored code

## Quality checks
- no functional change
- tests still pass
- architecture remains intact
- security posture is unchanged

## Human gate
Approval is required before code modification.

## Next skill
code-review

