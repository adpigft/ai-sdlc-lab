---
name: release-readiness
description: Determine if release is ready.
---

# Release Readiness Skill

## Purpose
Determine if release is ready.

## When to use
Use after validation is complete and release approval is being assessed.

## Inputs
- validation report
- release notes
- open defects
- traceability

## Process
1. Review validation results.
2. Review release notes and known defects.
3. Check traceability and approval status.
4. Assess deployment and rollback readiness.
5. Return a release decision.

## Output
- release readiness assessment

## Checks
- deployment readiness
- rollback readiness
- approval status
- known issues
- open risks

## Result
- ready
- ready with conditions
- not ready

## Rules
- review only
- do not modify artifacts

## Human gate
Release approval is required before deployment or publication.
