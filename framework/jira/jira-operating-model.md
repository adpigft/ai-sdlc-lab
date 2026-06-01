# Jira Operating Model

## Purpose

Define how Jira supports the AI SDLC workflow while Git remains the source of truth for delivery artifacts.

## Principle

Jira manages work, ownership, workflow status, and approval evidence. Git stores the approved content: intent, specification, architecture, contracts, tests, implementation, validation, release artifacts, traceability, standards, and decisions.

## Lifecycle Flow

```text
Idea -> Epic -> Intent -> Specification -> Stories -> Implementation Slices -> Tasks/Subtasks -> PRs -> Validation -> Release
```

## Jira Responsibilities

| Jira Area | Responsibility |
| --- | --- |
| Intake | Capture raw idea, requester, business area, urgency, and triage decision. |
| Epic | Hold discovery scope, high-level outcome, owner, approvals, and links to Git artifacts. |
| Story | Track approved business value after specification approval. |
| Task | Track implementation, architecture, QA, DevSecOps, or documentation work. |
| Subtask | Track small execution steps under a Story or Task. |
| Defect | Track incorrect behavior, validation failures, production defects, and fixes. |
| Release | Track release readiness, approval, deployment window, rollback, and known risks. |

## Git Responsibilities

| Git Artifact | Responsibility |
| --- | --- |
| `domains/**/intent/intent.md` | Approved business intent. |
| `domains/**/specs/spec.md` | Approved functional and non-functional specification. |
| `domains/**/context/context.md` | Approved architecture context and design assumptions. |
| `domains/**/contracts/openapi.yaml` | Approved API contract. |
| `domains/**/tests/acceptance.feature` | Approved acceptance test design. |
| `domains/**/design/implementation-plan.md` | Approved implementation slices when used. |
| `src/` | Approved application source code. |
| `domains/**/validation/validation-report.md` | QA validation evidence and release recommendation. |
| `domains/**/release/release-notes.md` | Release scope, risks, rollback, and approvals. |
| `traceability/traceability-matrix.md` | End-to-end mapping from intent to release evidence. |
| `feedback/feedback-log.md` | Feedback, defects, change requests, and learning loop. |

## Confluence Responsibilities

Confluence publishes stakeholder-facing summaries of approved Git content. It may include capability summaries, operating model pages, release summaries, diagrams, and support notes, but it must link back to Git and Jira.

## Approval Evidence

Approval can be recorded in Jira status, Jira approval fields, PR approvals, signed artifacts, or lab chat confirmation. The Git artifact should reference the approval evidence when the approval affects lifecycle progress.

## Non-Goals

- Do not store canonical specifications only in Jira.
- Do not use Confluence as the source of truth for approved artifacts.
- Do not create implementation Tasks before the relevant intent, specification, architecture, tests, and traceability are approved.
- Do not use Jira status to override GitHub Actions, SonarCloud, or validation evidence.
