# Review Approval Flow

## Purpose

Explain how simple lifecycle commands move a capability through review and approval without changing the existing lifecycle.

## Commands

```text
Status.
Review.
Resolve findings.
Approved.
Proceed.
```

## Status.

`Status.` is the main navigation command for users.

`Status.` reads `workflow-state.yaml` and, when available, checks validation report, release notes, and traceability for consistency.

Status output must always show:

- domain
- capability
- current_state
- current_skill
- active artifact
- pending gate
- required approvers
- blockers
- next command
- whether code changes are allowed
- whether release is blocked
- validation consistency status

Status does not review or approve anything.

If `workflow-state.yaml`, validation report, release notes, or traceability disagree, `Status.` must:

- report the inconsistency
- mark forward movement as blocked
- avoid recommending `Approved.`, `Proceed.`, `$implementation`, `$pr-review`, `$validation`, or `$release` until the inconsistency is resolved or explicitly accepted by the required human approver

### Status Output Shape

```text
Domain:
Capability:
Current State:
Current Skill:
Active Artifact:
Pending Gate:
Required Approvers:
Blockers:
Code Changes Allowed:
Release Blocked:
Validation Consistency:
Next Command:
```

### Navigation Rules

- If there are blockers, next command is `Resolve findings.` or the specific skill needed to clear the blocker.
- If the current artifact is ready for review, next command is `Review.`.
- If review is complete and human approval is still missing, next command is `Approved.`.
- If approval is complete and the next lifecycle step is clear, next command is the next skill.
- If artifacts disagree, next command is `Resolve findings.`.

## Review.

`Review.` reviews the current artifact against the pending gate.

Review should return:

- blocking findings
- major findings
- minor findings
- open questions
- recommendation

Review does not approve.

AI can recommend `Approve`, `Approve with conditions`, `Changes required`, or `Blocked`, but AI cannot approve itself.

## Resolve findings.

`Resolve findings.` means apply targeted corrections to the reviewed artifact or impacted supporting artifacts.

Rules:

- fix only approved impacted files
- preserve unrelated content
- update traceability when required
- run review again after corrections

## Approved.

`Approved.` records human approval for the current pending gate.

Approved advances workflow state when:

- the user has explicitly provided approval
- required approvers are satisfied for the lab context
- no blocking findings remain

Approval updates `workflow-state.yaml` from the current state to the next state.

AI can record approval evidence supplied by a human, but AI cannot create approval on its own.

## Proceed.

`Proceed.` starts or recommends the next lifecycle step after the current gate is approved.

If the current gate is not approved, `Proceed.` should stop and report the missing approval.

## Human Approval Rule

Human approval is mandatory.

Review can inform approval. Approval is a separate human decision.
