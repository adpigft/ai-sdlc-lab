---
name: architecture-review
description: Review architecture artifacts before approval.
---

# Architecture Review Skill

## Purpose
Review architecture artifacts before approval.

## When to use
Use after intent and specification are approved and before implementation planning or coding.

## Inputs
- `context.md`
- `spec.md`
- `intent.md`
- `implementation-plan.md`

## Process
1. Review architecture completeness.
2. Check integration risks.
3. Check security risks.
4. Check data ownership.
5. Check scalability, observability, and resiliency.
6. Check for over-engineering.
7. Classify findings by severity.
8. Return an approval recommendation.

## Output
- findings
- risks
- recommendations
- approval recommendation

## Checks
- architecture completeness
- integration risks
- security risks
- data ownership
- scalability
- observability
- resiliency
- over-engineering

## Rules
- do not modify artifacts
- review only
- classify findings by severity
- provide `approve`, `approve with conditions`, or `reject`

## Human gate
Architecture approval is required before implementation planning.
