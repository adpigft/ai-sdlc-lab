# Jira Status Model

## Purpose

Define a consistent Jira status model for AI-native SDLC work across Product Owner, BA, Solution Architect, QA, Developer, and DevSecOps activities.

## Model

Recommended board/status flow:

```text
Backlog -> Discovery -> Design -> Ready for Build -> In Progress -> Validation -> Release Ready -> Done
```

Blocked work should be visible using a blocked flag or swimlane, with owner, reason, and next action.

## Status Definitions

| Status | Meaning | Typical Workflow State |
| --- | --- | --- |
| Backlog | Accepted demand, idea, change, defect, decision, or release item not yet started. | `idea` |
| Discovery | Intent discovery, change impact analysis, RCA, or clarification underway. | `intent_review` or `blocked` |
| Design | Specification, architecture, test design, decision, or implementation planning underway. | `specification_review`, `architecture_review`, `test_review` |
| Ready for Build | Upstream approvals and traceability are complete enough for implementation. | `implementation_ready` |
| In Progress | Implementation, artifact update, RCA correction, or engineering work underway. | `implementation_in_progress` |
| Validation | QA validation, evidence gathering, retest, or release verification underway. | `validation_ready` |
| Release Ready | Validated scope is ready for release approval or deployment/change management. | `release_ready` |
| Done | Work is approved, linked to Git evidence, and closed. | `released` |

## Issue-Type Status Guidance

| Issue Type | Normal Path |
| --- | --- |
| Initiative | Backlog -> Discovery -> Design -> In Progress -> Done |
| Epic | Backlog -> Discovery -> Design -> Ready for Build -> In Progress -> Validation -> Release Ready -> Done |
| Story | Backlog -> Design -> Ready for Build -> In Progress -> Validation -> Done |
| Task | Backlog -> Ready for Build -> In Progress -> Validation -> Done |
| Subtask | Backlog -> In Progress -> Done |
| Defect | Backlog -> Discovery -> Design -> In Progress -> Validation -> Done |
| Decision | Backlog -> Discovery -> Design -> Done, or Blocked until resolved |
| Release | Backlog -> Validation -> Release Ready -> Done |

## Example

QR Refund status examples:

| Item | Status | Reason |
| --- | --- | --- |
| Epic: QR Refund | Design / Ready for Build | Intent, spec, architecture, tests, traceability, and implementation plan exist with some blockers. |
| Story: Merchant Refund Creation | Ready for Build | Slice 1 can start after implementation plan approval. |
| Task: Slice 1 Refund Creation Foundation | Ready for Build | Covers refund aggregate, idempotency, duplicate prevention, status query, and audit outbox. |
| Task: Slice 2 Processor and Ledger Integration | Blocked | Conditions remain for accounting, processor/ledger references, and failure behavior. |
| Decision: ADR-QRREF-003 | Done or Blocked With Conditions | Accepted with conditions; dependent slices remain blocked until conditions close. |
| Release: QR Refund MVP | Backlog / Validation | Release cannot proceed until validation evidence exists. |

## Do / Don't Rules

Do:

- Use statuses to show work progress, not artifact truth.
- Keep blockers visible with owner and next action.
- Move to Ready for Build only after required upstream approvals.
- Move to Done only when Git evidence and approval evidence are linked.

Do not:

- Use Done when Git artifacts are missing.
- Use Ready for Build before traceability approval.
- Use Release Ready before validation approval.
- Hide blocked work in Backlog without blocker details.
