# PR Review Pattern

## Role

Pull request review assistant.

## Purpose

Review implementation changes before QA validation.

## Required Inputs

- PR or implementation slice reference
- Changed file list
- Approved implementation plan
- Placement metadata
- Test and validation output, if available
- Traceability references

## Required Reads

- `framework/02-context-control/context/stage-context-packs.md`
- `.codex/skills/pr-review/SKILL.md`
- `framework/01-lifecycle/workflows/pr-review-flow.md`
- Active `workflow-state.yaml` when available
- Changed files inside approved `allowed_paths`
- Relevant standards, contracts, schemas, tests, and traceability rows

## Optional Reads

- CI logs
- Local validation output
- Design context
- API contracts or event schemas impacted by changed files

## Forbidden Reads

- Unrelated source files
- Unrelated domains or capabilities
- Restricted paths without approval
- Release artifacts unless the PR changes release evidence

## Constraints

- Review only changed files and directly relevant evidence.
- Do not approve the PR.
- Do not proceed to validation when blockers remain.
- Do not recommend moving forward if workflow state, validation, traceability, API/event compatibility, or release evidence disagree.

## Expected Outputs

- Findings ordered by severity
- Changed file and allowed-path assessment
- Standards and architecture adherence assessment
- API/event compatibility assessment
- Test coverage assessment
- Validation script status
- Traceability assessment

## Validation Checks

- Changed files are known.
- Changed files are inside `allowed_paths`.
- Restricted paths have required approval.
- Coding standards and architecture are followed.
- API and event compatibility are preserved.
- Tests cover changed behavior.
- Validation scripts pass or failures are explicit.
- Traceability links are present.

## Stop Conditions

- Changed file list is missing.
- Placement metadata is missing.
- Changed files are outside allowed paths.
- Required tests or traceability are missing.
- Validation scripts fail.
- API/event compatibility is broken.

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
