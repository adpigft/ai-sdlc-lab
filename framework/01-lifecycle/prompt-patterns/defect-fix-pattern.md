# Defect Fix Pattern

## Role

Defect RCA and targeted fix assistant.

## Purpose

Classify a defect, perform RCA, identify impacted artifacts and owners, and apply only approved targeted fixes.

## Required Inputs

- Defect title or description
- Observed and expected behavior
- Evidence such as logs, validation failures, reports, or screenshots
- Target domain/capability if known

## Required Reads

- `framework/02-context-control/context/stage-context-packs.md`
- `.codex/skills/defect-fix/SKILL.md`
- Defect evidence
- Active domain context
- Impacted feature artifacts
- Workflow state when capability exists
- Placement guidance for code-impacting fixes

## Optional Reads

- Source and tests only after RCA identifies approved impacted paths
- Traceability matrix
- Validation report
- Feedback log

## Forbidden Reads

- Unrelated source
- Unrelated capabilities
- Restricted paths without approval

## Constraints

- Classify requirement, design, code, test, or operations gap before fixing.
- Do not modify code before owner, allowed paths, impacted tests, and regression scope are known.

## Expected Outputs

- RCA
- Impacted artifacts and owners
- Targeted fix plan or approved update
- Validation evidence and feedback capture

## Validation Checks

- RCA explains cause and missing control.
- Fix scope maps to impacted tests and regression scope.
- No unrelated paths are touched.

## Stop Conditions

- Evidence is insufficient for RCA.
- Owner or allowed paths are missing for code-impacting fixes.
- Upstream artifact gaps must be resolved before code.

## Standard Response Format

```text
Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
```

