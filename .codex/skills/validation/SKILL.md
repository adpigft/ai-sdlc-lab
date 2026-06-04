---
name: validation
description: Validate implementation against approved requirements, tests, evidence, and release readiness expectations.
---

# Validation Skill

## Purpose

Execute or review validation evidence and determine whether the implemented scope satisfies approved requirements, tests, and quality expectations.

## When To Use

Use `$validation` after implementation and PR review are ready for QA validation, or when validation evidence must be assembled for release readiness.

## Inputs Needed

- Approved requirements, design, tests, and traceability
- Implemented code, PR reference, or delivery evidence
- Test execution results
- CI, security, quality, or validation outputs when available
- Defects, risks, waivers, or blocked evidence

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and lifecycle behavior are defined by:

- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/01-lifecycle/skill-orchestration-adapter.md`

## Procedure

1. Confirm implementation and review evidence are ready for validation.
2. Execute or review acceptance, regression, integration, security, and NFR evidence as applicable.
3. Compare results to approved requirements, tests, and traceability.
4. Record passed, failed, blocked, waived, or unvalidated scope.
5. Record defects, risks, limitations, and missing evidence.
6. State release readiness clearly and conservatively.
7. Stop for QA review before release depends on the validation evidence.

## Outputs Produced

- Validation report or validation evidence summary
- Test execution evidence summary
- Defect, gap, risk, and waiver summary
- Release readiness recommendation

## Artifact Structure

1. Scope Validated
2. Evidence
3. Test Results
4. Defects
5. Coverage
6. Approval Recommendation

## Quality Checks

- Evidence maps to approved requirements and tests.
- Failed, blocked, waived, or partial validation is visible.
- Defects and gaps are linked to correction or follow-up.
- CI and quality gate status is referenced where applicable.
- Release readiness is not claimed without evidence.

## Stop Conditions

- Implementation evidence is missing.
- Tests cannot map to approved requirements.
- Validation evidence is incomplete but release readiness is requested.
- Workflow, traceability, validation, or release evidence disagrees in frameworks that track them.

## Human Approval Expectations

QA approval is required before release readiness depends on validation output.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
