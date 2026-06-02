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

`Status.` reads `workflow-state.yaml` and reports:

- capability
- current state
- current artifact
- pending gate
- blockers
- next state
- next skill

Status does not review or approve anything.

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
