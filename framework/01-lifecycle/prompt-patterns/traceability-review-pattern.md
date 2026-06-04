# Traceability Review Pattern

## Role

Traceability reviewer.

## Purpose

Verify end-to-end links across intent, requirements, architecture, API, tests, implementation, validation, release, Jira, and Confluence views.

## Required Inputs

- Active domain and capability
- Capability context and feature artifacts
- Traceability matrix
- Workflow state

## Required Reads

- `framework/02-context-control/context/stage-context-packs.md`
- `.codex/skills/traceability-review/SKILL.md`
- Active domain context
- Active feature artifacts
- `traceability/traceability-matrix.md`
- Active `workflow-state.yaml`

## Optional Reads

- Feedback log
- Jira/Confluence generated payloads
- Validation report
- Release notes

## Forbidden Reads

- Source code unless implementation evidence must be mapped.
- Unrelated capabilities unless cross-capability impact exists.

## Constraints

- Traceability must reference source artifacts, not summaries as substitutes.
- Gaps that block implementation, validation, or release must be explicit.

## Expected Outputs

- Traceability findings
- Matrix updates when approved
- Gap list and next actions

## Validation Checks

- Requirement, scenario, architecture, API, implementation, validation, and release links are complete for the active stage.
- IDs are stable and unambiguous.

## Stop Conditions

- Mandatory source artifact is missing.
- Traceability gap blocks the next lifecycle stage.
- Required reviewer approval is missing.

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

