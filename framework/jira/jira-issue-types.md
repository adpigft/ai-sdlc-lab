# Jira Issue Types

## Purpose

Define the Jira issue types used by the AI SDLC workflow and their relationship to Git-owned artifacts.

## Issue Types

| Issue Type | Use For | Created When | Links To Git Source Of Truth |
| --- | --- | --- | --- |
| Epic | Capability discovery and delivery container. | Before or during intent discovery. | Intent, specification, design, tests, PR review, validation, release, traceability. |
| Story | Approved business value or user-facing behavior. | After specification approval. | Requirement IDs in `spec.md`, acceptance scenarios, traceability rows. |
| Task | Work item for implementation, architecture, QA, DevSecOps, or release preparation. | After the relevant artifact or slice is approved. | Design, implementation plan, source files, validation or release artifacts. |
| Subtask | Small execution step under a Story or Task. | When a Task needs accountable sub-steps. | Same Git artifact as parent, with narrower scope. |
| Defect | Incorrect behavior, failed validation, production issue, or regression. | When defect evidence exists. | Feedback log, validation report, tests, code, and traceability rows. |
| Release | Release readiness, change control, deployment, and approval. | When validated scope is preparing for release. | Validation report, release notes, PRs, CI results, rollback plan. |

## Epic

An Epic is a lightweight discovery and delivery container. It may exist before intent, but it must not become the source of truth for requirements.

Required fields:

- Capability name
- Business owner
- Product owner
- Domain
- Outcome summary
- Git artifact links when available
- Approval references

## Story

A Story represents approved business value derived from the specification.

Rules:

- Create Stories after specification approval.
- Link Stories to requirement IDs.
- Keep acceptance criteria aligned to Git acceptance scenarios.
- Do not use Stories to replace `spec.md`.

## Task

A Task tracks concrete delivery work.

Rules:

- Create implementation Tasks after implementation slices are defined.
- Create architecture, QA, or DevSecOps Tasks only when the related artifact is approved or explicitly assigned for review.
- Link Tasks to the Git path they affect.

## Subtask

A Subtask tracks a narrow execution step.

Rules:

- Keep Subtasks small enough for one owner.
- Link to parent Story or Task.
- Do not create Subtasks that bypass approval gates.

## Defect

A Defect tracks incorrect or failed behavior.

Rules:

- Link to expected behavior and evidence.
- Classify root cause as requirement, architecture, design, code, test, or operational.
- Link to feedback and validation evidence.
- Do not fix code until upstream artifact gaps are approved.

## Release

A Release issue tracks readiness and approval for a release scope.

Rules:

- Link to validation report, release notes, PRs, CI evidence, and rollback plan.
- Record known risks and accepted defects.
- Require PO, QA, Architect, DevSecOps, and Release Manager approval when applicable.
