# Jira State Mapping

## Purpose

Map Jira workflow status to the Git-owned AI SDLC lifecycle state.

## Core Rule

Jira state shows work-management progress. Git state and artifacts show what was actually approved, built, tested, and released.

## Suggested Jira Statuses

| Jira Status | Meaning |
| --- | --- |
| Intake | Idea or request has been captured. |
| Discovery | Intent is being explored. |
| Drafting | Git artifact is being drafted. |
| In Review | Human approval is pending. |
| Approved | Gate is approved. |
| Ready for Build | Specification, architecture, tests, and traceability are approved. |
| In Progress | Active delivery work is underway. |
| In Validation | QA validation is underway. |
| Ready for Release | Validation is approved and release readiness is pending. |
| Released | Release is approved and completed. |
| Blocked | Required decision, approval, evidence, or dependency is missing. |
| Done | Jira work item is complete. |

## Jira To Workflow-State Mapping

| AI SDLC State | Typical Jira Status | Git Evidence |
| --- | --- | --- |
| `idea` | Intake | Epic or intake reference only. |
| `intent_review` | Discovery / In Review | `intent.md` draft or approved intent gate. |
| `specification_review` | Drafting / In Review | `spec.md` draft or approved specification gate. |
| `architecture_review` | Drafting / In Review | `context.md`, API guidance, ADR status, implementation planning. |
| `test_review` | Drafting / In Review | `acceptance.feature` or QA test design artifact. |
| `implementation_ready` | Ready for Build | Approved traceability and implementation slice plan. |
| `implementation_in_progress` | In Progress | PRs, commits, tests, and active Task/Subtask links. |
| `validation_ready` | In Validation | Validation report and test evidence in progress. |
| `release_ready` | Ready for Release | Approved validation report and draft release notes. |
| `released` | Released / Done | Approved release notes and release approval reference. |
| `blocked` | Blocked | Blocking decision, approval, defect, dependency, or evidence gap. |

## Approval Status Mapping

| Approval Decision | Jira Status Impact | Workflow-State Impact |
| --- | --- | --- |
| Approved | Move issue to Approved or next delivery status. | Move to next lifecycle state. |
| Approved With Conditions | Move to Approved or Blocked depending on conditions. | Continue only if conditions are non-blocking. |
| Changes Required | Keep in In Review or move back to Drafting. | Remain in current review state. |
| Rejected | Close, cancel, or block. | Move to `blocked` or return to earlier state. |

## Blocking Rules

Set Jira and workflow state to Blocked when:

- Required approval is missing.
- Required Git artifact is missing.
- Mandatory requirement, architecture, QA, security, or release question is unresolved.
- Traceability has a mandatory gap.
- CI or quality gate evidence is missing for release.
- A defect prevents validation or release.

## PR State Mapping

| PR State | Jira Impact | Git Evidence |
| --- | --- | --- |
| Open | Task or Story remains In Progress. | PR link and branch. |
| Review Approved | Task can move toward validation if tests pass. | PR approval record. |
| Changes Requested | Task remains In Progress or Blocked. | PR review comments. |
| Merged | Task can move to In Validation. | Commit SHA and PR link. |
| Closed Without Merge | Task remains open or is cancelled. | PR closure reason. |
