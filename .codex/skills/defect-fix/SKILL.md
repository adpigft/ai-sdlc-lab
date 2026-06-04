---
name: defect-fix
description: Analyze defects through RCA and apply targeted corrections with validation and regression evidence.
---

# Defect Fix Skill

## Purpose

Analyze and resolve defects through evidence, root cause classification, targeted correction, and validation.

## When To Use

Use `$defect-fix` when users report incorrect behavior, failed validation, escaped defects, production issues, incidents, or test failures.

## Inputs Needed

- Defect ID or defect summary
- Observed behavior and expected behavior
- Environment, build, release, or reproduction details
- Logs, screenshots, traces, test evidence, or incident references
- Known affected artifact, component, owner, or customer impact

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, impact routing, and path governance are defined by:

- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/03-delivery-governance/service-architecture/implementation-placement-model.md`
- `framework/01-lifecycle/skill-orchestration-adapter.md`

## Procedure

1. Require or assign a defect ID.
2. Confirm evidence is sufficient for root cause analysis.
3. Classify root cause as requirement, design, code, test, data, integration, operational, or environment gap.
4. Identify impacted artifacts, owners, tests, paths, and regression scope.
5. Determine whether upstream artifacts need correction before code changes.
6. Recommend a targeted correction path.
7. Ask for approval before changing artifacts, tests, code, validation evidence, or release notes.
8. Apply only approved targeted fixes.
9. Capture validation, regression, traceability, and feedback impacts where required.

## Outputs Produced

- Defect analysis summary
- Root cause classification
- Impacted artifact, owner, path, and test list
- Targeted correction plan
- Regression and validation evidence needs
- Traceability, feedback, and release impact summary

## Artifact Structure

1. Defect Summary
2. Symptoms
3. Expected Behavior
4. Root Cause
5. Impact Analysis
6. Fix Plan
7. Regression Scope
8. Validation Plan

## Quality Checks

- Root cause is classified before fixes are made.
- Requirement, design, code, test, data, integration, and operational causes are considered.
- Fixes do not bypass missing upstream approval.
- Corrections are targeted and traceable.
- Regression and validation needs are identified.

## Stop Conditions

- Defect evidence is insufficient for RCA.
- Owner, impacted scope, or regression scope is unclear.
- Upstream artifact gaps must be resolved before code changes.
- Required placement or path constraints are missing for code-impacting fixes.

## Human Approval Expectations

The root cause and correction path require owner approval before artifacts or code are changed. QA approval is expected before closure.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
