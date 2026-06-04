# Jira Operating Model For AI-Native SDLC

## Purpose

Define how Jira supports AI-native software delivery while Git remains the source of truth for approved delivery artifacts and Confluence remains the publishing channel for stakeholder-facing summaries.

## Model

### Source Of Truth

| System | Source Of Truth For |
| --- | --- |
| Git | Intent, specification, design, API contracts, tests, ADRs, implementation plans, PR review evidence, validation reports, release notes, traceability. |
| Jira | Ownership, delivery status, approvals, sprint planning, dependencies, blockers, work management. |
| Confluence | Stakeholder-facing published summaries, operating model pages, management communication. |

### Recommended Lifecycle

```text
Idea
-> Epic
-> Intent
-> Specification
-> Design
-> Test Design
-> Story Breakdown
-> Implementation Slice Planning
-> Tasks/Subtasks
-> PR
-> PR Review
-> Validation
-> Release
```

### Jira Issue Types

| Issue Type | Purpose |
| --- | --- |
| Initiative | Optional container for large programs spanning multiple capabilities. |
| Epic | Capability business-function container. |
| Story | Feature delivery container; not one functional requirement. |
| Task | Implementation slice or engineering activity. |
| Subtask | Optional detailed engineering work under a Task. |
| Defect | Test, validation, or production defect. |
| Release | Release or change package. |
| Decision | Independent decision issue linked to affected Epics and capabilities. |

### Core Mapping

| Jira | Git |
| --- | --- |
| Epic | Capability folder and `capability-context.md` |
| Story | Feature folder and grouped FR/NFR scope |
| Task | Implementation slice |
| Defect | Defect/RCA and validation evidence |
| Decision | ADR |
| Release | Validation report and release notes |

Important rules:

- A Jira Story is not equal to one Functional Requirement.
- A Story may contain multiple FRs.
- FRs live in Git specification.
- Feature artifacts map to Jira Stories.
- Implementation slices map to Jira Tasks.
- PR review is normally per slice or PR.
- Feature validation and release happen after required slices are complete.
- The build breakdown is `Epic -> Story -> Task -> Subtask`.

## Example

QR Refund:

| Jira Level | Example |
| --- | --- |
| Epic | QR Refund |
| Story | Merchant Refund Creation |
| Story | Operations Refund and Override |
| Story | Refund Status Tracking |
| Story | Reconciliation and Reporting |
| Slice | Slice 1 Refund Creation Foundation |
| Slice | Slice 2 Processor and Ledger Integration |
| Slice | Slice 3 Operations Override |
| Slice | Slice 4 Retry and Exception Handling |
| Slice | Slice 5 Reconciliation |
| Slice | Slice 6 Reporting Projection Seam |

Example Git mapping:

| Jira Item | Git Source |
| --- | --- |
| Payment Refund Epic | `domains/payments/capabilities/payment-refund/capability-context.md` |
| QR Refund Story | `domains/payments/capabilities/payment-refund/features/qr-refund/` |
| Slice 1 Task | `implementation/implementation-plan.md` Slice 1 |
| Idempotency Decision | ADR or architecture decision linked to `ADR-QRREF-003` |
| QR Refund Release | `validation/validation-report.md` and `release/release-notes.md` |

## Do / Don't Rules

Do:

- Use Jira to show ownership, status, blockers, sprint scope, and approval evidence.
- Link every meaningful Jira item to Git paths or stable artifact IDs.
- Create Stories after specification approval.
- Create Tasks after implementation slices are defined.
- Use Decision issues for unresolved choices that block design, tests, implementation, PR review, validation, or release.
- Keep Confluence summaries linked back to Git and Jira.

Do not:

- Use Jira as the canonical store for requirements.
- Treat one Story as one FR.
- Create implementation Tasks before approved intent, specification, design, tests, and traceability.
- Use Jira status to override missing Git evidence, failed CI, failed quality gates, or missing validation.
- Store secrets, credentials, customer data, or sensitive operational data in Jira.
