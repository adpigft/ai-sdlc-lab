# Jira Traceability Model

## Purpose

Define how Jira issue references connect to Git-owned source-of-truth artifacts and end-to-end traceability.

## Traceability Chain

```text
Epic -> Intent -> Specification -> Story -> Implementation Slice -> Task/Subtask -> PR -> Test -> Validation -> Release -> Feedback
```

## Source Of Truth By Link Type

| Trace Item | Jira Role | Git Source Of Truth |
| --- | --- | --- |
| Epic | Capability container and approval tracking. | Intent/spec/design links in Git artifacts and traceability. |
| Intent | Approval tracking and Epic linkage. | `domains/**/intent/intent.md` |
| Requirement | Story linkage and delivery tracking. | `domains/**/specs/spec.md` |
| Story | Work tracking for approved requirement scope. | Requirement IDs and acceptance criteria in Git. |
| Implementation Slice | Work sequencing and readiness tracking. | `domains/**/design/implementation-plan.md` when used. |
| Task/Subtask | Execution tracking. | Code, tests, design updates, validation evidence in Git. |
| PR | Review and merge tracking. | GitHub PR, commits, and code in Git. |
| Test | QA execution tracking. | `domains/**/tests/acceptance.feature` and validation evidence. |
| Validation | Validation task and approval tracking. | `domains/**/validation/validation-report.md` |
| Release | Change and release approval tracking. | `domains/**/release/release-notes.md` |
| Feedback | Follow-up work and issue tracking. | `feedback/feedback-log.md` |

## Minimum Traceability Fields

| Field | Description |
| --- | --- |
| Intent ID | Stable intent identifier. |
| Jira Epic | Epic or intake reference. |
| Requirement ID | Functional or non-functional requirement ID. |
| Jira Story | Story linked to requirement delivery. |
| Slice ID | Implementation slice identifier. |
| Jira Task/Subtask | Delivery execution reference. |
| PR | Pull request or commit evidence. |
| API | API operation or contract path when applicable. |
| Test Scenario | Acceptance, negative, integration, security, or NFR scenario. |
| Validation Evidence | Validation report, test run, or evidence ID. |
| Release | Release issue, version, or change record. |
| Feedback/Defect | Feedback or Defect reference when applicable. |
| Status | Draft, Ready, Implemented, Validated, Released, or Blocked. |
| Owner | Responsible role or team. |

## Jira Link Rules

- Epic links to all Stories, major Tasks, Defects, and Release issues for a capability.
- Story links to requirement IDs and acceptance scenarios.
- Task links to implementation slice, Git paths, and PRs.
- Subtask inherits parent traceability and adds execution detail only.
- Defect links to failed requirement, failed test, validation evidence, and feedback entry.
- Release links to approved Stories, Defects, PRs, validation report, release notes, and rollback plan.

## Git Reference Rules

Every material Jira item should reference at least one Git path or stable artifact ID.

Examples:

| Jira Item | Required Git Reference |
| --- | --- |
| Epic | `intent.md`, `spec.md`, `traceability-matrix.md` when available. |
| Story | Requirement ID in `spec.md` and acceptance scenario. |
| Task | Implementation slice and affected Git path. |
| Subtask | Parent Task plus affected Git path if different. |
| Defect | Validation evidence, feedback row, test, or code path. |
| Release | `validation-report.md`, `release-notes.md`, traceability row. |

## Traceability Quality Checks

- Every Must requirement has a Jira Story or explicitly documented deferral.
- Every Story maps to at least one requirement ID.
- Every implementation slice maps to requirements, tests, and Jira Tasks.
- Every PR maps to a Task, Story, or Defect.
- Every Defect maps to expected behavior and validation evidence.
- Every Release maps to approved scope, validation evidence, known risks, and rollback.
- Every blocked item has an owner, reason, and next action.
