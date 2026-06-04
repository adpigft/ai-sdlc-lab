# Skill Orchestration Adapter

## Purpose

Define how generic Codex skills are used inside this AI-SDLC framework.

Skills are reusable procedures. This adapter owns framework-specific lifecycle order, workflow-state behavior, approval gates, and navigation commands.

## Canonical Lifecycle

```text
intent
-> specification
-> design
-> test-design
-> implementation
-> pr-review
-> validation
-> release
```

Supporting skills:

- `domain-onboarding` runs before `intent` when the domain does not exist.
- `capability-onboarding` runs before feature work when a parent capability context is needed under an existing domain.
- `source-ingestion` converts external source documents into AI-readable summaries before delivery artifacts are created.
- `repo-discovery` extracts conventions from an existing repository to inform standards and bootstrap decisions.
- `artifact-review` reviews AI-generated artifacts before human approval.
- `change-request` performs impact analysis and routes only impacted work through the lifecycle.
- `defect-fix` performs RCA and routes only impacted work through the lifecycle.
- `traceability-review` can run whenever traceability needs review or update.
- `feedback-capture` can run whenever findings, feedback, defects, changes, risks, or lessons are captured.
- `decision` can run during design or any later stage when a material decision blocks delivery.

## Next Skill Mapping

| Current Skill | Normal Next Skill |
| --- | --- |
| `domain-onboarding` | `intent` after domain approval |
| `intent` | `specification` |
| `specification` | `design` and `test-design` |
| `design` | `test-design` or `implementation` when test design and traceability are ready |
| `test-design` | `traceability-review` or `implementation` |
| `implementation` | `pr-review` |
| `pr-review` | `validation` |
| `validation` | `release` |
| `release` | `feedback-capture` |
| `change-request` | First impacted lifecycle skill |
| `defect-fix` | First impacted lifecycle skill, then `validation` |
| `traceability-review` | The blocked or requested lifecycle skill |
| `feedback-capture` | The impacted follow-up skill |
| `decision` | The blocked lifecycle skill after approval |

## Approval Gates

| Gate | Required Human Approval |
| --- | --- |
| Domain onboarding | Domain Owner / Solution Architect |
| Intent | PO / BA |
| Specification | BA / PO |
| Design | Solution Architect and impacted owners |
| API, event, integration, or shared asset changes | Owning Architect / Platform / impacted producer-consumer owners |
| Test design | QA |
| Implementation slice start | Developer Lead / Architect / impacted owners |
| PR review | Human reviewer and required owners |
| Validation | QA |
| Release | PO, QA, Architect, DevSecOps, and required operations owners |
| Change request | Impacted artifact and owner approvals |
| Defect fix | RCA owner, impacted owner, and QA closure |
| Decision | Architect or designated decision owner |

AI can recommend approval readiness, but it cannot approve itself.

## Workflow-State Update Responsibilities

`workflow-state.yaml` belongs to the feature. It records lifecycle state, active skill, active artifact, pending gate, blockers, approvals, and history.

When a skill creates or updates a framework-owned artifact, the framework adapter is responsible for updating workflow state according to:

- `framework/01-lifecycle/workflow/workflow-state-guide.md`
- `framework/01-lifecycle/workflow/workflow-state-template.yaml`
- `framework/01-lifecycle/workflow-state/state-machine.md`
- `framework/01-lifecycle/workflow-state/approval-events.md`

Generic skills should not duplicate workflow-state transition rules. They should produce outputs and evidence; this adapter decides how those outputs affect framework state.

## Status. Behavior

`Status.` is the user navigation command.

It must report:

- domain
- capability
- feature
- current state
- current skill
- active artifact
- pending gate
- required approvers
- blockers
- next command
- whether code changes are allowed
- whether release is blocked
- validation consistency status

If workflow state, validation report, release notes, or traceability disagree, `Status.` must report the inconsistency and must not recommend moving forward.

## Review. Behavior

`Review.` evaluates the current artifact or gate for readiness. Review does not approve. It reports findings, blockers, missing evidence, and recommended corrections.

## Approved. Behavior

`Approved.` records explicit human approval for the current gate. Approval advances workflow state only when required evidence is present and consistency checks pass.

## Proceed. Behavior

`Proceed.` runs or recommends the next allowed skill only when the current gate is approved, no blockers remain, and workflow-state consistency is acceptable.
