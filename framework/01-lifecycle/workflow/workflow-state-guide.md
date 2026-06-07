# Workflow State Guide

## Purpose

Define lifecycle navigation for AI SDLC capabilities so users can say `Review.`, `Approved.`, or `Status.` without restating long prompts, artifact paths, or skill names.

This guide does not implement Jira integration or automation. It defines how skills should maintain `workflow-state.yaml` when artifacts are created and how Codex should interpret simple lifecycle commands.

Canonical workflow state definitions live in `framework/01-lifecycle/canonical-workflow-state-model.md`. Legacy labels are mapped in `framework/01-lifecycle/legacy-workflow-state-mapping.md`.

## Location

Every feature may contain:

```text
domains/<domain>/capabilities/<capability>/features/<feature>/workflow-state.yaml
```

The workflow state belongs to the feature. `domain` identifies the architecture boundary, `capability` identifies the parent business-function boundary, and `feature` identifies the delivery boundary.

Use `framework/01-lifecycle/workflow/workflow-state-template.yaml` when creating a new workflow-state file.

Git remains the source of truth for workflow state. Jira may mirror state later, but Jira integration is out of scope for this design.

## States

| State | Meaning | Current Artifact | Review Gate | Next Skill On Approval |
| --- | --- | --- | --- | --- |
| `idea` | Idea or Epic shell exists, but intent is not drafted. | None | Idea accepted | `intent` |
| `intent_review` | Intent draft exists and is awaiting review. | `intent/intent.md` | `intent_approval` | `specification` |
| `specification_review` | Specification draft exists and is awaiting review. | `specification/specification.md` | `specification_approval` | `design` |
| `design_review` | Design/API/ADR/implementation planning draft exists and is awaiting review. | `design/design.md`, API guidance, ADRs, or implementation plan | `design_approval` | `test-design` |
| `test_review` | Acceptance or QA test design draft exists and is awaiting review. | `tests/acceptance.feature` or test design artifact | `test_design_approval` | `implementation` |
| `implementation_ready` | Upstream artifacts are approved and slice planning is ready for build approval. | `implementation/implementation-plan.md` | `implementation_start_approval` | `implementation` |
| `implementation_in_progress` | One approved implementation slice is active. | PR, unit tests, source changes, slice evidence | `implementation_slice_approval` | `pr-review` |
| `pr_review_ready` | Implementation changes are ready for pull request review before QA validation. | PR, changed file list, validation script output, traceability evidence | `pr_review_approval` | `validation` |
| `validation_ready` | Implementation is ready for QA validation or validation evidence is drafted. | `validation/validation-report.md` | `validation_approval` | `release` |
| `release_ready` | Validation is approved and release readiness is drafted. | `release/release-notes.md` | `release_approval` | `feedback-capture` |
| `released` | Release is approved and complete. | Release notes and release approval evidence | None | `feedback-capture` |
| `blocked` | Required approval, decision, evidence, dependency, or artifact is missing. | Current blocked artifact | Blocking gate | Current owner |

## Skill Responsibilities

When a lifecycle skill creates or updates its owned artifact, it must create or update `workflow-state.yaml` in the feature folder.

Minimum update:

- `domain.name`
- `domain.path`
- `capability.name`
- `capability.id`
- `capability.path`
- `feature.name`
- `feature.id`
- `feature.path`
- `workflow.current_state`
- `workflow.current_skill`
- `workflow.next_state`
- `workflow.next_skill`
- `current_artifact.type`
- `current_artifact.path`
- `current_artifact.status`
- `artifacts.<artifact_key>`
- `pending_gate.gate`
- `pending_gate.artifact_type`
- `pending_gate.artifact_path`
- `pending_gate.required_approvers`
- append a `history` entry

The skill should preserve unrelated workflow fields and approval history.

## Artifact Creation Mapping

| Artifact Created | State To Set | Current Skill | Pending Gate | Next State After Approval | Next Skill |
| --- | --- | --- | --- | --- | --- |
| `intent/intent.md` | `intent_review` | `intent` | `intent_approval` | `specification_review` | `specification` |
| `specification/specification.md` | `specification_review` | `specification` | `specification_approval` | `design_review` | `design` |
| `design/design.md`, API guidance, ADR draft, or implementation plan | `design_review` | `design` | `design_approval` | `test_review` | `test-design` |
| `tests/acceptance.feature` or QA test design | `test_review` | `test-design` | `test_design_approval` | `implementation_ready` | `implementation` |
| approved slice plan / build readiness package | `implementation_ready` | `implementation` | `implementation_start_approval` | `implementation_in_progress` | `implementation` |
| implemented slice / PR evidence | `implementation_in_progress` | `implementation` | `implementation_slice_approval` | `pr_review_ready` | `pr-review` |
| PR review evidence | `pr_review_ready` | `pr-review` | `pr_review_approval` | `validation_ready` | `validation` |
| `validation/validation-report.md` | `validation_ready` | `validation` | `validation_approval` | `release_ready` | `release` |
| `release/release-notes.md` | `release_ready` | `release` | `release_approval` | `released` | `feedback-capture` |

## State-Aware Commands

### `Review.`

When the user says `Review.`, Codex should:

1. Locate `workflow-state.yaml` for the current or most recently active capability.
2. If no workflow-state file exists, infer state from artifacts.
3. Read `current_artifact.path` and required upstream context.
4. Review the artifact against `pending_gate.gate`.
5. Return findings first, ordered by severity.
6. End with one recommendation: `Approve`, `Approve with conditions`, `Changes required`, or `Blocked`.

Review response shape:

```text
Review: Specification Draft
Artifact: domains/.../specification/specification.md
Gate: specification_approval

Findings:
1. Blocking ...
2. Major ...

Recommendation: Changes required
Next: resolve blockers, then say `Review.`
```

### `Approved.`

When the user says `Approved.`, Codex should:

1. Locate or infer the current workflow state.
2. Confirm the current review has no unresolved blocking findings.
3. Mark `pending_gate.status` and matching `approval_gates.<gate>.status` as `approved`.
4. Set `workflow.previous_state` to the current state.
5. Set `workflow.current_state` to the next state.
6. Set `workflow.current_skill` to the next skill.
7. Clear non-blocking `current_artifact` only when no draft exists for the next state.
8. Append a `history` entry.
9. Announce the transition and start or recommend the next skill.

Approval transitions:

| Gate | From | To | Next Skill |
| --- | --- | --- | --- |
| `intent_approval` | `intent_review` | `specification_review` | `specification` |
| `specification_approval` | `specification_review` | `design_review` | `design` |
| `design_approval` | `design_review` | `test_review` | `test-design` |
| `test_design_approval` | `test_review` | `implementation_ready` | `implementation` |
| `implementation_start_approval` | `implementation_ready` | `implementation_in_progress` | `implementation` |
| `implementation_slice_approval` | `implementation_in_progress` | `pr_review_ready` | `pr-review` |
| `pr_review_approval` | `pr_review_ready` | `validation_ready` | `validation` |
| `validation_approval` | `validation_ready` | `release_ready` | `release` |
| `release_approval` | `release_ready` | `released` | `feedback-capture` |

### `Status.`

When the user says `Status.`, Codex should show:

- capability
- current state
- current artifact
- pending gate
- blockers
- next state
- next skill
- approval history summary

## Inference When State File Is Missing

If `workflow-state.yaml` does not exist, infer state from the newest or most complete artifact set:

| Artifact Found | Inferred State | Pending Gate |
| --- | --- | --- |
| `release/release-notes.md` | `release_ready` | `release_approval` |
| `validation/validation-report.md` | `validation_ready` | `validation_approval` |
| PR review evidence or changed-file review tied to approved slice | `pr_review_ready` | `pr_review_approval` |
| implementation PR or source changes tied to approved slice | `implementation_in_progress` | `implementation_slice_approval` |
| `implementation/implementation-plan.md` | `implementation_ready` | `implementation_start_approval` |
| `tests/acceptance.feature` | `test_review` | `test_design_approval` |
| `design/design.md` or ADR/API design artifact | `design_review` | `design_approval` |
| `specification/specification.md` | `specification_review` | `specification_approval` |
| `intent/intent.md` | `intent_review` | `intent_approval` |
| feature folder only | `idea` | `idea_acceptance` |

If multiple capabilities are plausible, ask one concise clarification question.

## Blocking Rules

Set state to `blocked` or keep the current review state when:

- required artifact is missing
- required approval is missing
- required open question blocks downstream work
- traceability has mandatory gaps
- architecture has unresolved blocking decisions
- implementation would start before required upstream approvals
- validation, CI, security, rollback, or release evidence is missing

Do not use Jira state to override missing Git evidence.

## Out Of Scope

- Jira API integration
- Confluence publishing automation
- GitHub Actions integration
- automatic approval without human instruction
- source code generation before required approvals
