# Validation Pattern

## Role

QA validation assistant.

## Purpose

Validate implementation evidence against approved requirements, tests, API contract, and traceability.

## Required Inputs

- Implemented slice or completed implementation evidence
- PR review findings or approval evidence
- Approved tests
- Approved requirements and architecture as needed
- Traceability matrix
- Workflow state

## Required Reads

- `framework/02-context-control/context/stage-context-packs.md`
- `.codex/skills/validation/SKILL.md`
- Active `workflow-state.yaml`
- Validation report
- Approved tests
- Implementation evidence
- PR review evidence
- Traceability matrix

## Optional Reads

- Source/tests inside implemented paths
- CI logs
- Security, testing, and NFR standards

## Forbidden Reads

- Unrelated source paths
- Unrelated capabilities unless regression scope requires them

## Constraints

- Validation claims must be evidence-backed.
- PR review blockers must be resolved before QA validation proceeds.
- Release readiness must not be claimed when validation is partial.

## Expected Outputs

- Validation report
- Validation evidence summary
- Release readiness recommendation

## Validation Checks

- Tests map to requirements and scenarios.
- Failures, gaps, untested slices, and residual risks are explicit.

## Stop Conditions

- Implementation evidence is missing.
- PR review evidence is missing or blocking.
- Tests cannot map to requirements.
- Release readiness lacks evidence.

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
