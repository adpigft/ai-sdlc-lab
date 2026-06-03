# Skill Prerequisite Validation

## Purpose

Define lightweight checks each skill should perform before reading large context sets or creating artifacts.

This guidance keeps execution predictable without adding heavy process. It helps skills stop early when the active domain, lifecycle state, approvals, artifacts, placement metadata, validation evidence, or cross-artifact consistency are not ready.

## Common Precondition Checks

Before proceeding, confirm:

- Is the active domain known?
- Is the active capability known when the command targets an existing capability?
- Does `workflow-state.yaml` exist where required?
- Is `workflow.current_skill` compatible with the requested command?
- Is `workflow.current_state` compatible with the requested command?
- Are required artifacts present and non-empty?
- Are required approvals recorded?
- Are blockers present?
- Are validation scripts passing where applicable?
- Are target paths and placement metadata present before implementation?
- Are there inconsistencies between workflow state, validation report, traceability, and release notes?

If these checks fail, report the smallest missing prerequisite and stop before reading broad context.

## Stage-Specific Preconditions

| Command | Must Confirm Before Proceeding |
| --- | --- |
| `$domain-onboarding` | Domain does not already exist, or update approval exists. |
| `$intent` | `domains/<domain>/domain-context.md` exists. |
| `$specification` | Intent exists and intent approval is recorded. |
| `$design` | Specification exists and specification approval is recorded. |
| `$test-design` | Specification approval and architecture context exist; API contract exists when applicable. |
| `$implementation` | Architecture, test design, traceability, implementation plan, placement metadata, `allowed_paths`, and required approvals exist. |
| `$pr-review` | Implementation evidence, changed file list, placement metadata, `allowed_paths`, and `restricted_paths` exist. |
| `$validation` | Implementation evidence exists and can map to approved tests and requirements. |
| `$release` | Validation evidence, release notes, CI evidence, and release approval package exist; no release blockers remain. |
| `$change-request` | Change request is identified and impact analysis is available or can be performed before edits. |
| `$defect-fix` | Defect evidence is sufficient for RCA; RCA and regression scope are available before fixes. |
| `$traceability-review` | Source artifacts needed for the active lifecycle stage exist. |
| `$feedback-capture` | Feedback source, impacted artifact or domain, and owner are identifiable. |

## Missing-Input Behavior

When required input is missing:

1. State the missing input.
2. Explain which stage is blocked.
3. Ask only for the smallest missing information.
4. Do not create artifacts from assumptions unless the skill explicitly allows open questions.

## Missing-Approval Behavior

When required approval is missing:

- Do not proceed to the next lifecycle stage.
- Do not create downstream artifacts that depend on the approval.
- Do not claim approval from review language.
- Treat approval as valid only when the user explicitly says `Approved.` or an accepted approval reference exists.

## Blocked-State Behavior

When `workflow-state.yaml` says the capability is blocked:

- Read the blocker and pending gate first.
- Do not recommend moving forward until the blocker is resolved.
- If the requested command can resolve the blocker, explain the targeted action.
- If the requested command cannot resolve the blocker, report the correct next command or owner.

## Stale-Artifact Behavior

An artifact is stale when it disagrees with approved upstream artifacts, workflow state, validation evidence, traceability, release notes, or known review findings.

When stale artifacts are detected:

- Report the stale artifact and the source it disagrees with.
- Treat source artifacts and `workflow-state.yaml` as authoritative for their own scope.
- Stop before producing downstream artifacts that would depend on stale content.
- Recommend the smallest targeted correction.

## Placement-Metadata Behavior

Before implementation or code-impacting change, confirm placement metadata exists:

- `target_app`, if frontend is impacted
- `target_frontend_module`, if frontend is impacted
- `target_service`, if backend is impacted
- `target_library`, if shared library is impacted
- `owning_squad`
- `allowed_paths`
- `restricted_paths`
- `required_approvals`
- `impacted_capabilities`
- `regression_scope`

If placement metadata is missing, stop before reading or editing source code. Route to architecture or implementation planning as appropriate.

## Validation-Failure Behavior

When validation scripts, validation report, traceability, release notes, or workflow state disagree:

- Report the inconsistency.
- Do not recommend moving forward.
- Do not mark release ready.
- Do not create release approval language.
- Recommend the smallest correction or the validation evidence needed.

Examples:

- If validation says release is not ready, `$release` must stop.
- If release notes are missing, `release_ready` is invalid.
- If traceability does not mention the active capability, implementation, validation, or release should stop.
- If `allowed_paths` are missing, `$implementation` must stop.

## Response Guidance

Use `framework/prompt-patterns/standard-response-format.md` for the response footer. If no files are changed, say `No files changed.`
