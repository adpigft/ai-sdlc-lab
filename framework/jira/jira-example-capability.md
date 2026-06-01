# Jira Example Capability: QR Refund

## Purpose

Show how Jira issue types, Git artifacts, approvals, and traceability work together for the QR Refund capability.

This is an example operating model. The source-of-truth business artifacts remain under `domains/payments/capabilities/qr-refund/` and `traceability/`.

## Lifecycle Example

```text
Idea
-> Epic
-> Intent
-> Specification
-> Architecture
-> Story Breakdown
-> Slice Planning
-> Tasks
-> PR
-> Validation
-> Release
```

## Idea

| Field | Example |
| --- | --- |
| Idea | Merchants need a controlled way to refund completed KHQR payments. |
| Intake ID | `PAY-IDEA-001` |
| Requester | Digital Payments Product Owner |
| Initial Decision | Accepted for discovery |
| Next Jira Item | `JIRA-QRREF-001` Epic |

Approval gate:

| Gate | Approver | Evidence |
| --- | --- | --- |
| Idea accepted | Product Owner | `PAY-IDEA-001` moved to Accepted |

## Epic

| Field | Example |
| --- | --- |
| Epic ID | `JIRA-QRREF-001` |
| Epic Name | QR Refund |
| Domain | Payments |
| Capability Folder | `domains/payments/capabilities/qr-refund/` |
| Product Owner | Digital Payments Product Owner |
| BA | Payments BA |
| Solution Architect | Payments Architect |
| QA Lead | Payments QA Lead |
| Dev Lead | Payments Developer Lead |
| DevSecOps Lead | Payments DevSecOps Lead |

Git links:

| Artifact | Link |
| --- | --- |
| Intent | `domains/payments/capabilities/qr-refund/intent/intent.md` |
| Specification | `domains/payments/capabilities/qr-refund/specs/spec.md` |
| Architecture | `domains/payments/capabilities/qr-refund/context/context.md` |
| API Contract | `domains/payments/capabilities/qr-refund/contracts/openapi.yaml` |
| Acceptance Tests | `domains/payments/capabilities/qr-refund/tests/acceptance.feature` |
| Implementation Plan | `domains/payments/capabilities/qr-refund/design/implementation-plan.md` |
| Validation Plan | `domains/payments/capabilities/qr-refund/validation/validation-plan.md` |
| Traceability | `traceability/traceability-matrix.md` |

## Intent

| Field | Example |
| --- | --- |
| Intent ID | `INT-QRREF-001` |
| Jira Epic | `JIRA-QRREF-001` |
| Git Artifact | `domains/payments/capabilities/qr-refund/intent/intent.md` |
| Status | Approved for artifact creation |

Approval gate:

| Gate | Jira ID | Approver | Git Evidence |
| --- | --- | --- | --- |
| Intent approved | `JIRA-QRREF-001` | Product Owner / BA | `intent/intent.md` Human Approval section |

## Specification

| Field | Example |
| --- | --- |
| Spec ID | `SPEC-QRREF-001` |
| Jira Approval | `JIRA-QRREF-050` |
| Git Artifact | `domains/payments/capabilities/qr-refund/specs/spec.md` |
| Status | Approved for architecture context |

Approval gate:

| Gate | Jira ID | Approver | Git Evidence |
| --- | --- | --- | --- |
| Specification approved | `JIRA-QRREF-050` | Product Owner / BA | `specs/spec.md` Human Approval section |

## Architecture

| Field | Example |
| --- | --- |
| Context ID | `CTX-QRREF-001` |
| Jira Approval | `JIRA-QRREF-060` |
| Git Artifact | `domains/payments/capabilities/qr-refund/context/context.md` |
| Status | Approved for API contract design |

Decision records:

| Decision Issue | Decision Record | Impact |
| --- | --- | --- |
| `JIRA-QRREF-061` | `ADR-QRREF-001` Accounting treatment and settlement adjustment | Blocks Slice 2 until conditions close |
| `JIRA-QRREF-062` | `ADR-QRREF-003` Idempotency and concurrency boundary | Blocks cross-system behavior until conditions close |
| `JIRA-QRREF-063` | `ADR-QRREF-004` High-value manual review state model | Blocks final API/test baseline |
| `JIRA-QRREF-064` | `ADR-QRREF-006` Safe degradation behavior | Blocks processor/ledger failure-mode closure |

Approval gate:

| Gate | Jira ID | Approver | Git Evidence |
| --- | --- | --- | --- |
| Architecture approved | `JIRA-QRREF-060` | Payments Architect | `context/context.md` Human Approval section |

## Story Breakdown

Stories represent business capability slices. A Story is not one Functional Requirement; it can map to multiple FRs.

| Story ID | Story | Example FR Mapping | Git Source |
| --- | --- | --- | --- |
| `JIRA-QRREF-020` | Merchant Refund Creation | `FR-QRREF-001`, `FR-QRREF-003`, `FR-QRREF-004`, `FR-QRREF-005`, `FR-QRREF-006`, `FR-QRREF-007`, `FR-QRREF-008`, `FR-QRREF-009`, `FR-QRREF-010`, `FR-QRREF-020` | `specs/spec.md` |
| `JIRA-QRREF-021` | Operations Refund and Override | `FR-QRREF-002`, `FR-QRREF-012`, `FR-QRREF-014`, `FR-QRREF-020` | `specs/spec.md` |
| `JIRA-QRREF-035` | Refund Status Tracking | `FR-QRREF-016`, `NFR-QRREF-007` | `specs/spec.md`, `contracts/openapi.yaml` |
| `JIRA-QRREF-037` | Reconciliation and Reporting | `FR-QRREF-018`, `FR-QRREF-019`, `NFR-QRREF-008` | `specs/spec.md`, `design/implementation-plan.md` |

Approval gate:

| Gate | Jira ID | Approver | Evidence |
| --- | --- | --- | --- |
| Story breakdown approved | `JIRA-QRREF-070` | Product Owner / BA / QA Lead | Traceability review in `traceability/traceability-matrix.md` |

## Slice Planning

Implementation Slice sits between Story and Task.

```text
Story -> Implementation Slice -> Tasks/Subtasks
```

| Slice ID | Slice | Status | Git Source |
| --- | --- | --- | --- |
| `SLICE-QRREF-001` | Slice 1 Refund Creation Foundation | Can start after implementation plan approval | `design/implementation-plan.md` |
| `SLICE-QRREF-002` | Slice 2 Processor and Ledger Integration | Blocked pending ADR/config approval | `design/implementation-plan.md` |
| `SLICE-QRREF-003` | Slice 3 Operations Override | Blocked pending override policy approval | `design/implementation-plan.md` |
| `SLICE-QRREF-004` | Slice 4 Retry and Exception Handling | Starts after Slice 2 | `design/implementation-plan.md` |
| `SLICE-QRREF-005` | Slice 5 Reconciliation | Blocked pending reconciliation design | `design/implementation-plan.md` |
| `SLICE-QRREF-006` | Slice 6 Reporting Projection Seam | Future phase / projection seam only | `design/implementation-plan.md` |

Approval gate:

| Gate | Jira ID | Approver | Git Evidence |
| --- | --- | --- | --- |
| Implementation slice plan approved | `JIRA-QRREF-090` | Payments Architect / Developer Lead | `design/implementation-plan.md` Human Approval section |

## Tasks

Example Tasks for Slice 1:

| Task ID | Parent Story | Slice | Task | Git / PR Link |
| --- | --- | --- | --- | --- |
| `JIRA-QRREF-091` | `JIRA-QRREF-020` | `SLICE-QRREF-001` | Implement Refund aggregate and state transitions | `src/` after approval, PR `PR-QRREF-001` |
| `JIRA-QRREF-092` | `JIRA-QRREF-020` | `SLICE-QRREF-001` | Implement idempotency record locking and fingerprint checks | `src/` after approval, PR `PR-QRREF-001` |
| `JIRA-QRREF-093` | `JIRA-QRREF-020` | `SLICE-QRREF-001` | Implement duplicate-prevention repository contract | `src/` after approval, PR `PR-QRREF-001` |
| `JIRA-QRREF-094` | `JIRA-QRREF-035` | `SLICE-QRREF-001` | Implement merchant refund status query | `src/` after approval, PR `PR-QRREF-002` |

Example Subtasks:

| Subtask ID | Parent Task | Work |
| --- | --- | --- |
| `JIRA-QRREF-091-1` | `JIRA-QRREF-091` | Add failing unit tests for valid and invalid state transitions |
| `JIRA-QRREF-091-2` | `JIRA-QRREF-091` | Implement aggregate behavior |
| `JIRA-QRREF-091-3` | `JIRA-QRREF-091` | Refactor and update traceability evidence |

## PR

| PR | Jira Links | Required Evidence |
| --- | --- | --- |
| `PR-QRREF-001` | `JIRA-QRREF-091`, `JIRA-QRREF-092`, `JIRA-QRREF-093` | Unit tests, repository tests, concurrency tests, code review |
| `PR-QRREF-002` | `JIRA-QRREF-094` | Status query tests, authorization tests, code review |

Approval gate:

| Gate | Jira / PR ID | Approver | Evidence |
| --- | --- | --- | --- |
| PR approved | `PR-QRREF-001` | Developer Reviewer / Payments Architect | PR approval and passing checks |

## Defects

| Defect ID | Defect | RCA Mapping | Validation Evidence |
| --- | --- | --- | --- |
| `DEF-QRREF-001` | Duplicate Refund Created Under Concurrency | RCA using `framework/templates/defect-rca-template.md` | `VAL-QRREF-CONC-001` |

Example impacted traceability:

| Defect | Requirements | Slice | Expected Update |
| --- | --- | --- | --- |
| `DEF-QRREF-001` | `FR-QRREF-004`, `FR-QRREF-009`, `FR-QRREF-010`, `NFR-QRREF-005` | `SLICE-QRREF-001` | Add concurrency validation evidence and implementation correction task |

## Validation

| Field | Example |
| --- | --- |
| Validation Plan | `domains/payments/capabilities/qr-refund/validation/validation-plan.md` |
| Validation Report | `domains/payments/capabilities/qr-refund/validation/validation-report.md` when produced |
| QA Jira ID | `JIRA-QRREF-080` |
| Evidence Example | `VAL-QRREF-CONC-001`, `VAL-QRREF-OPS-001`, `VAL-QRREF-OBS-001` |

Approval gate:

| Gate | Jira ID | Approver | Git Evidence |
| --- | --- | --- | --- |
| Validation approved | `JIRA-QRREF-080` | QA Lead | Validation report and test evidence |

## Release

| Field | Example |
| --- | --- |
| Release ID | `REL-QRREF-001` |
| Jira Release | `JIRA-QRREF-100` |
| Change Record | `CHG-QRREF-001` |
| Release Notes | `domains/payments/capabilities/qr-refund/release/release-notes.md` |
| Included Stories | `JIRA-QRREF-020`, `JIRA-QRREF-021`, `JIRA-QRREF-035`, `JIRA-QRREF-037` as approved |
| Included PRs | `PR-QRREF-001`, `PR-QRREF-002` as approved |

Approval gate:

| Gate | Jira ID | Approver | Evidence |
| --- | --- | --- | --- |
| Release approved | `JIRA-QRREF-100` | Product Owner / QA Lead / Payments Architect / DevSecOps Lead / Release Manager | Validation report, release notes, rollback plan, CI evidence |

## Example Traceability

| Epic | Story | FRs | Slice | Task | PR | Validation | Release |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `JIRA-QRREF-001` | `JIRA-QRREF-020` Merchant Refund Creation | `FR-QRREF-001`, `FR-QRREF-004`, `FR-QRREF-009`, `FR-QRREF-010` | `SLICE-QRREF-001` | `JIRA-QRREF-091`, `JIRA-QRREF-092`, `JIRA-QRREF-093` | `PR-QRREF-001` | `VAL-QRREF-CONC-001` | `REL-QRREF-001` |
| `JIRA-QRREF-001` | `JIRA-QRREF-021` Operations Refund and Override | `FR-QRREF-002`, `FR-QRREF-012`, `FR-QRREF-014` | `SLICE-QRREF-003`, `SLICE-QRREF-004` | `JIRA-QRREF-120` | `PR-QRREF-003` | `VAL-QRREF-OPS-001` | `REL-QRREF-001` |
| `JIRA-QRREF-001` | `JIRA-QRREF-037` Reconciliation and Reporting | `FR-QRREF-018`, `FR-QRREF-019` | `SLICE-QRREF-005`, `SLICE-QRREF-006` | `JIRA-QRREF-150` | `PR-QRREF-005` | `VAL-QRREF-RECON-001` | `REL-QRREF-001` |

## Do / Don't Rules

Do:

- Keep Jira IDs linked to Git artifact paths and stable requirement IDs.
- Treat Stories as business capability slices.
- Plan implementation slices before creating engineering Tasks.
- Link PRs to Tasks and validation evidence.
- Link Defects to RCA and validation evidence.
- Link Release to validation report and release notes.

Do not:

- Treat one Story as one FR.
- Implement directly from Epic without specification, architecture, tests, and traceability.
- Create source code before approval gates are satisfied.
- Close Release without validation evidence and human approval.
