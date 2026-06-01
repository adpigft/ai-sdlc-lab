# Jira Board Model

## Purpose

Define role-friendly Jira boards for AI-native SDLC delivery using a shared lifecycle view across Product Owner, BA, Solution Architect, QA, Developer, and DevSecOps.

## Model

Shared board columns:

```text
Backlog -> Discovery -> Design -> Ready for Build -> In Progress -> Validation -> Release Ready -> Done
```

| Column | Meaning |
| --- | --- |
| Backlog | Accepted demand, defect, decision, or release work waiting to start. |
| Discovery | Intent, impact analysis, RCA, or clarification work is active. |
| Design | Specification, architecture, test design, decision, or implementation planning is active. |
| Ready for Build | Required approvals and traceability are complete enough for implementation. |
| In Progress | Implementation, artifact update, RCA correction, or engineering task is underway. |
| Validation | QA validation, evidence gathering, defect retest, or release verification is underway. |
| Release Ready | Validated scope is ready for release approval or change management. |
| Done | Work is approved, linked to Git evidence, and closed. |

## Role Boards

| Role | Primary Focus |
| --- | --- |
| PO | Ideas, Epics, scope, business approval, release approval. |
| BA | Intent, requirements, business rules, Story-to-FR traceability. |
| SA | Architecture, API impacts, ADRs, dependency and blocker resolution. |
| QA | Test design, validation, defect verification, release recommendation. |
| Developer | Approved slices, Tasks/Subtasks, TDD, PRs, implementation evidence. |
| DevSecOps | CI/CD, quality gates, deployment, monitoring, rollback, release evidence. |

## Example

QR Refund board examples:

| Column | Example Item |
| --- | --- |
| Backlog | Release: QR Refund MVP |
| Discovery | Defect: Duplicate Refund Created Under Concurrency |
| Design | Decision: ADR-QRREF-004 High-value manual review state model |
| Ready for Build | Story: Merchant Refund Creation |
| In Progress | Task: Slice 1 Refund Creation Foundation |
| Validation | QA Task: Validate concurrency and idempotency evidence |
| Release Ready | Release: QR Refund MVP after validation approval |
| Done | Decision: ADR-QRREF-003 after conditions close |

## Do / Don't Rules

Do:

- Use the same board columns across roles.
- Use filters or swimlanes for role-specific views.
- Make blocked items visible with owner and next action.
- Require Git links before Done.

Do not:

- Create separate incompatible status models for each role.
- Move work to Ready for Build without approvals and traceability.
- Move work to Release Ready without validation approval.
- Close board items that lack Git evidence.
