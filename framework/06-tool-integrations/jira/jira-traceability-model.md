# Jira To Git Traceability Model

## Purpose

Define how Jira issues map to Git-owned source-of-truth artifacts and how delivery traceability is maintained across AI-native SDLC work.

## Model

Core mappings:

```text
Epic -> Capability
Story -> Feature
Task -> Implementation Slice
Defect -> Defect/RCA and validation evidence
Decision -> ADR
Release -> Validation Report and Release Notes
```

End-to-end chain:

```text
Initiative
-> Epic
-> Capability
-> Feature / Story
-> Intent
-> Specification
-> Story
-> Implementation Slice
-> Task/Subtask
-> PR
-> Test
-> Validation
-> Release
-> Feedback
```

## Mapping Table

| Jira Issue | Git Artifact | Required Stable IDs |
| --- | --- | --- |
| Initiative | Multiple capability or feature folders, or roadmap references | Initiative key, Epic keys |
| Epic | `domains/<domain>/capabilities/<capability>/capability-context.md` | Epic key, capability ID |
| Story | `domains/<domain>/capabilities/<capability>/features/<feature>/` | Story key, feature ID, `FR-*` group |
| Task | `domains/**/features/**/implementation/implementation-plan.md` | Task key, Slice ID |
| Subtask | Parent Task and affected Git path | Subtask key, parent Task key |
| Defect | RCA artifact, validation evidence, feedback-capture row | Defect key, RCA ID, validation evidence ID |
| Decision | ADR or architecture decision record | Decision key, ADR ID |
| Release | `validation-report.md`, `release-notes.md` | Release key, validation ID, release ID |

## Story To FR Rule

A Jira Story is not equal to one Functional Requirement.

Rules:

- A Story is a business capability slice.
- A Story may contain multiple FRs and NFRs.
- FRs and NFRs live in Git specification.
- Story acceptance criteria summarize Git acceptance tests.
- If FR scope changes, use change control before implementation.

## Example

QR Refund traceability:

| Jira Item | Git Mapping |
| --- | --- |
| Epic: Payment Refund | `domains/payments/capabilities/payment-refund/capability-context.md` |
| Story: QR Refund | `domains/payments/capabilities/payment-refund/features/qr-refund/` |
| Story: Merchant Refund Creation | `FR-QRREF-001`, `FR-QRREF-003`, `FR-QRREF-004`, `FR-QRREF-005`, `FR-QRREF-006`, `FR-QRREF-007`, `FR-QRREF-008`, `FR-QRREF-009`, `FR-QRREF-010`, `FR-QRREF-020` |
| Story: Operations Refund and Override | `FR-QRREF-002`, `FR-QRREF-012`, `FR-QRREF-014`, `FR-QRREF-020` |
| Story: Refund Status Tracking | `FR-QRREF-016`, `NFR-QRREF-007` |
| Story: Reconciliation and Reporting | `FR-QRREF-018`, `FR-QRREF-019`, `NFR-QRREF-008` |
| Task: Slice 1 Refund Creation Foundation | Slice 1 in `implementation/implementation-plan.md` |
| Decision: Idempotency and concurrency boundary | `ADR-QRREF-003` |
| Release: QR Refund MVP | validation report and release notes |

## Do / Don't Rules

Do:

- Record Git paths and stable IDs on Jira issues.
- Map every Story to one or more FRs.
- Map every Task to one approved slice or approved artifact update.
- Map every Defect to RCA, validation evidence, and feedback-capture when applicable.
- Map every Decision to ADR or decision record.
- Map every Release to validation and release evidence.

Do not:

- Treat Jira descriptions as canonical requirements.
- Treat Story count as requirement count.
- Close traceability gaps by adding Jira links only.
- Implement a Task that has no approved slice or artifact reference.
