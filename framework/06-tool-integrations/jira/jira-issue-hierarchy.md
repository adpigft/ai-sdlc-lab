# Jira Issue Hierarchy

## Purpose

Define the Jira issue hierarchy used for AI-native SDLC delivery and how each issue type maps to Git-owned artifacts.

## Model

```text
Initiative (optional)
  Epic (capability)
    Story (feature)
      Task (implementation slice)
        Subtask (optional engineering work)
    Defect
    Decision
    Release
```

## Issue Types

| Issue Type | Definition | Git Mapping |
| --- | --- | --- |
| Initiative | Optional large program or portfolio outcome. | Multiple capability or feature folders, or roadmap artifacts. |
| Epic | Capability business-function container. | `domains/<domain>/capabilities/<capability>/capability-context.md` |
| Story | Feature delivery container that may contain multiple FRs/NFRs. | `domains/<domain>/capabilities/<capability>/features/<feature>/` and grouped `FR-*` entries in `specification/specification.md`. |
| Task | Approved implementation slice. | Slice in `implementation/implementation-plan.md` or affected Git artifact. |
| Subtask | Optional detailed engineering work under a Task. | Parent Task Git mapping plus narrow affected path if needed. |
| Defect | Incorrect behavior from tests, validation, or production. | RCA, feedback-capture entry, validation evidence, impacted artifact paths. |
| Decision | Independent decision linked to affected Epics or capabilities. | ADR or architecture decision section. |
| Release | Release/change package. | Validation report and release notes. |

## Story To Slice To Task

Stories are not implementation units by themselves. They represent feature delivery scope. Implementation work is planned as slices and then broken into Tasks.

```text
Story -> Implementation Slice -> Tasks/Subtasks
```

## Example

QR Refund hierarchy:

```text
Epic: QR Refund
  Story: Merchant Refund Creation
    Task: Slice 1 Refund Creation Foundation
    Task: Slice 2 Processor and Ledger Integration
  Story: Operations Refund and Override
    Task: Slice 3 Operations Override
    Task: Slice 4 Retry and Exception Handling
  Story: Refund Status Tracking
    Task: Slice 1 status query work
  Story: Reconciliation and Reporting
    Task: Slice 5 Reconciliation
    Task: Slice 6 Reporting Projection Seam
  Decision: ADR-QRREF-003 Idempotency and concurrency boundary
  Defect: Duplicate Refund Created Under Concurrency
  Release: QR Refund MVP Release
```

## Do / Don't Rules

Do:

- Use Initiative only when multiple Epics need program-level coordination.
- Use Epic for a capability.
- Use Story for business value and a group of FRs.
- Use Task for implementation slices or specific engineering activities.
- Use Decision for blockers that need explicit approval.
- Link Defects to RCA, expected behavior, and validation evidence.

Do not:

- Create one Story per FR by default.
- Skip implementation slice planning.
- Put canonical requirements in Story descriptions only.
- Put detailed engineering checklists directly under an Epic when a Story and Slice exist.
- Close Defects without validation evidence or accepted risk.
