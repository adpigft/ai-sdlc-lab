---
name: devsecops-release
description: Prepare release notes, deployment readiness, rollback plan, monitoring checks, and release approval evidence.
---

# DevSecOps Release Skill

## Purpose
Prepare release package and deployment readiness evidence.

## When to use
Use after validation is approved.

## Inputs
- validation-report.md
- traceability-matrix.md
- CI/CD results
- security scan results
- release standards

## Process
1. Confirm release scope.
2. Confirm validation status.
3. Confirm security and quality gates.
4. Define deployment steps.
5. Define rollback plan.
6. Define monitoring and smoke checks.
7. Ask for release approval.

## Output
- domains/<domain>/capabilities/<capability>/features/<feature>/release/release-notes.md

## Quality checks
- Scope is clear.
- Risks are documented.
- Rollback is defined.
- Monitoring is defined.
- Approval gate is recorded.

## Human gate
PO, QA, Architect, and DevSecOps approval required before production release.

## Next skill
feedback-capture
