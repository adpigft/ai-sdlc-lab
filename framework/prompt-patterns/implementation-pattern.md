# Implementation Pattern

## Role

Developer implementation assistant.

## Purpose

Implement one approved slice at a time using approved artifacts and deterministic placement metadata.

## Required Inputs

- Approved upstream artifacts
- Approved implementation plan
- Active slice
- Placement metadata
- Current workflow state

## Required Reads

- `framework/context/stage-context-packs.md`
- `.codex/skills/implementation/SKILL.md`
- Approved intent, specification, architecture, API, tests, traceability, and implementation plan
- Active `workflow-state.yaml`
- Approved `allowed_paths` and `restricted_paths`

## Optional Reads

- Source and tests inside approved `allowed_paths`
- Relevant coding, testing, and security standards
- Ownership docs referenced by placement metadata

## Forbidden Reads

- Source outside approved `allowed_paths`
- Restricted paths
- Unrelated domains, services, frontend modules, and release artifacts

## Constraints

- Do not write code before all required approvals exist.
- Do not read or write outside `allowed_paths`.
- Do not expand beyond the approved slice.

## Expected Outputs

- Slice implementation
- Unit or focused tests
- Implementation evidence
- PR readiness evidence
- Updated workflow state when applicable

## Validation Checks

- Build/tests for the approved slice pass or failures are reported.
- Changes remain within allowed paths.
- Traceability links can be updated from implemented evidence.
- PR review can identify changed files, allowed paths, tests, and traceability evidence.

## Stop Conditions

- Any upstream approval is missing.
- Placement metadata is missing.
- The requested work needs restricted paths or another squad's area.

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
