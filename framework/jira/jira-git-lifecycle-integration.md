# Jira-Git Lifecycle Integration

## Purpose

Define when Jira issues and Git artifacts are created during the AI-native SDLC lifecycle, and how humans and AI collaborate at each step.

Git remains the source of truth for approved delivery artifacts. Jira remains the workflow system for ownership, status, approvals, sprint planning, dependencies, and blockers.

This is a design only. It does not implement automation.

## Model

Lifecycle:

```text
Idea
-> Epic
-> Intent
-> Specification
-> Architecture
-> Test Design
-> Story Breakdown
-> Implementation Slice Planning
-> Tasks/Subtasks
-> PR
-> Validation
-> Release
```

Source-of-truth split:

| System | Owns |
| --- | --- |
| Git | Intent, specification, architecture, API contracts, tests, ADRs, implementation plans, validation reports, release notes, traceability. |
| Jira | Ownership, delivery status, approvals, sprint planning, dependencies, blockers, work management. |
| Confluence | Published stakeholder summaries and management communication. |

## Lifecycle Integration

| Step | When Created | Human Responsibility | AI Responsibility | Jira Update | Git Update | Approval Gate |
| --- | --- | --- | --- | --- | --- | --- |
| Epic | After an idea is accepted for discovery and before intent is written. The Epic can be a lightweight discovery container. | Product Owner accepts the idea, names the capability, assigns owner roles, and confirms the domain. | Summarize the idea, check existing domain context and related capabilities, and propose the Epic shell and initial links. | Create Epic with owner, domain, capability name, status, dependencies, and placeholder Git links. | No required Git artifact yet. Git links are added when artifacts are created. | Idea accepted. |
| Intent | After discovery questions are answered and the PO/BA agrees the intent is ready to capture. | PO and BA confirm business outcome, scope boundaries, stakeholders, assumptions, and open questions. | Use `$new` or `$intent` to structure discovery output and create the intent artifact for review. | Update Epic with intent status, approver, decision, and Git path. | Create or update `domains/<domain>/capabilities/<capability>/intent/intent.md`. | Intent approved. |
| Specification | After intent approval. | PO and BA approve functional requirements, NFRs, business rules, acceptance criteria, and unresolved questions. | Use `$specification` to derive requirements from approved intent and domain context. | Record specification review status and approval evidence. Do not create build Stories until specification approval. | Create or update `domains/<domain>/capabilities/<capability>/specs/spec.md`. | Specification approved. |
| Stories | After specification approval and before build planning. | PO, BA, and QA agree the Story breakdown represents business capability slices and can be prioritized. | Group approved FRs and NFRs into business capability Stories. Do not map one Story to one FR by default. | Create Stories under the Epic, each linked to the FR/NFR group, acceptance scenario references, owner, priority, and dependencies. | Update traceability with Story keys mapped to Git requirement IDs. The specification remains canonical. | Story breakdown and traceability approved. |
| Implementation Slices | After architecture, test design, and traceability are approved or during build readiness planning for an approved scope. | Architect, Dev Lead, QA Lead, and PO approve slice boundaries, dependencies, risks, and sequencing. | Use `$architecture` and `$implementation` to propose vertical slices, dependencies, tests, rollback concerns, and one-slice-at-a-time execution. | Record slice IDs on Stories or planning Tasks, and mark dependent Stories as ready or blocked. | Create or update implementation planning artifacts such as `domains/<domain>/capabilities/<capability>/design/implementation-plan.md`. | Implementation slice plan approved. |
| Tasks/Subtasks | After implementation slices are approved and the work is ready for sprint planning. | Dev Lead and squad assign owners, sprint scope, estimates if used, and review responsibilities. | Break each approved slice into implementation Tasks and Subtasks, including tests, code, refactoring, documentation, and traceability evidence updates. | Create Tasks/Subtasks linked to the parent Story and Slice ID. Add PR placeholders, blockers, and dependency links. | No source code update until implementation is approved for the slice. Later PRs update `src/`, tests, and traceability as approved. | Task readiness and slice approval. |
| Defects | When validation, testing, production monitoring, review, or stakeholder feedback identifies incorrect behavior. | Reporter, QA, PO, and owner triage severity, business impact, fix priority, and approval to proceed. | Use `$defect` to perform RCA, classify root cause, identify impacted artifacts, and propose targeted fixes without broad regeneration. | Create Defect linked to affected Epic, Story, Slice, Release, PR, and validation evidence. Track RCA approval, fix approval, and retest status. | Create or update approved RCA, validation evidence, feedback log entry, and traceability impact entries as applicable. | RCA approved, fix approved, and validation approved. |
| Decisions | When a material architecture, integration, security, data, operational, or product choice is unresolved or blocks downstream work. | Architect and impacted stakeholders approve the decision, conditions, and downstream impact. | Use `$decision` to draft options, tradeoffs, recommendation, affected artifacts, and blocked work. | Create Decision issue linked to affected Epic, Stories, Slices, Defects, or Release. Mark dependent work blocked until decision is accepted. | Create or update ADR or decision record in Git and update traceability where required. | Decision approved. Unresolved decisions block implementation where applicable. |
| Release | After validation is approved and the release package has scope, evidence, rollback, risks, and approvals. | PO, QA Lead, Architect, DevSecOps, and Release Manager approve readiness, known risks, rollback, and deployment timing. | Use `$release` to assemble validation evidence, release notes, rollback plan, known risks, and readiness summary. | Create Release issue or change package linked to included Stories, Defects, PRs, validation evidence, and approvals. | Create or update validation report, release notes, rollback evidence, and traceability release references. | Release approved. |

## QR Refund Example

### 1. Epic

QR Refund starts as an accepted idea: merchants need a controlled way to refund completed KHQR payments.

| Field | Example |
| --- | --- |
| Jira Epic | `JIRA-QRREF-001` |
| Epic Name | QR Refund |
| Git Capability Folder | `domains/payments/capabilities/qr-refund/` |
| Approval Gate | Idea accepted |

The Epic exists before the intent artifact as a lightweight Jira discovery container.

### 2. Intent

After PO/BA discovery, the AI creates the Git intent artifact for review.

| Field | Example |
| --- | --- |
| Intent ID | `INT-QRREF-001` |
| Jira Link | `JIRA-QRREF-001` |
| Git Artifact | `domains/payments/capabilities/qr-refund/intent/intent.md` |
| Approval Gate | Intent approved |

Jira records the owner, status, approval decision, and link. Git stores the approved intent.

### 3. Specification

After intent approval, the BA specification is created in Git.

| Field | Example |
| --- | --- |
| Specification ID | `SPEC-QRREF-001` |
| Jira Approval | `JIRA-QRREF-050` |
| Git Artifact | `domains/payments/capabilities/qr-refund/specs/spec.md` |
| Approval Gate | Specification approved |

Stories are not created as build-ready work until this gate is approved.

### 4. Stories

After specification approval, Jira Stories are created as business capability slices.

| Story ID | Story | Git Requirement Mapping |
| --- | --- | --- |
| `JIRA-QRREF-020` | Merchant Refund Creation | `FR-QRREF-001`, `FR-QRREF-003`, `FR-QRREF-004`, `FR-QRREF-005`, `FR-QRREF-006`, `FR-QRREF-007`, `FR-QRREF-008`, `FR-QRREF-009`, `FR-QRREF-010`, `FR-QRREF-020` |
| `JIRA-QRREF-021` | Operations Refund and Override | `FR-QRREF-002`, `FR-QRREF-012`, `FR-QRREF-014`, `FR-QRREF-020` |
| `JIRA-QRREF-035` | Refund Status Tracking | `FR-QRREF-016`, `NFR-QRREF-007` |
| `JIRA-QRREF-037` | Reconciliation and Reporting | `FR-QRREF-018`, `FR-QRREF-019`, `NFR-QRREF-008` |

A Story is not one FR. FRs stay in Git specification.

### 5. Implementation Slices

After architecture, test design, and traceability are ready, implementation slices are planned.

| Slice ID | Slice | Git Source |
| --- | --- | --- |
| `SLICE-QRREF-001` | Slice 1 Refund Creation Foundation | `domains/payments/capabilities/qr-refund/design/implementation-plan.md` |
| `SLICE-QRREF-002` | Slice 2 Processor and Ledger Integration | `domains/payments/capabilities/qr-refund/design/implementation-plan.md` |
| `SLICE-QRREF-003` | Slice 3 Operations Override | `domains/payments/capabilities/qr-refund/design/implementation-plan.md` |
| `SLICE-QRREF-004` | Slice 4 Retry and Exception Handling | `domains/payments/capabilities/qr-refund/design/implementation-plan.md` |
| `SLICE-QRREF-005` | Slice 5 Reconciliation | `domains/payments/capabilities/qr-refund/design/implementation-plan.md` |
| `SLICE-QRREF-006` | Slice 6 Reporting Projection Seam | `domains/payments/capabilities/qr-refund/design/implementation-plan.md` |

Implementation Slice sits between Story and Task:

```text
Story -> Implementation Slice -> Tasks/Subtasks
```

### 6. Tasks/Subtasks

Tasks are created only after slice approval.

| Task ID | Parent Story | Slice | Task |
| --- | --- | --- | --- |
| `JIRA-QRREF-091` | `JIRA-QRREF-020` | `SLICE-QRREF-001` | Implement Refund aggregate and state transitions |
| `JIRA-QRREF-092` | `JIRA-QRREF-020` | `SLICE-QRREF-001` | Implement idempotency record locking and fingerprint checks |
| `JIRA-QRREF-093` | `JIRA-QRREF-020` | `SLICE-QRREF-001` | Implement duplicate-prevention repository contract |
| `JIRA-QRREF-094` | `JIRA-QRREF-035` | `SLICE-QRREF-001` | Implement merchant refund status query |

Example Subtasks for `JIRA-QRREF-091`:

| Subtask ID | Work |
| --- | --- |
| `JIRA-QRREF-091-1` | Add failing unit tests for valid and invalid state transitions |
| `JIRA-QRREF-091-2` | Implement aggregate behavior |
| `JIRA-QRREF-091-3` | Refactor and update traceability evidence |

### 7. Defects

Defects are created when evidence shows approved behavior is not met.

| Field | Example |
| --- | --- |
| Defect ID | `DEF-QRREF-001` |
| Defect | Duplicate Refund Created Under Concurrency |
| Root Cause Category | Code, design, requirement, architecture, test, or operational after RCA |
| Affected Requirements | `FR-QRREF-004`, `FR-QRREF-009`, `FR-QRREF-010`, `NFR-QRREF-005` |
| Affected Slice | `SLICE-QRREF-001` |
| Approval Gates | RCA approved, fix approved, validation approved |

Jira tracks triage, ownership, status, and retest. Git stores RCA, traceability updates, validation evidence, and any approved artifact changes.

### 8. Decisions

Decision issues are created when an unresolved choice affects downstream delivery.

| Decision Issue | Decision Record | Impact |
| --- | --- | --- |
| `JIRA-QRREF-061` | `ADR-QRREF-001` Accounting treatment and settlement adjustment | Blocks Slice 2 until conditions close |
| `JIRA-QRREF-062` | `ADR-QRREF-003` Idempotency and concurrency boundary | Blocks cross-system behavior until conditions close |
| `JIRA-QRREF-063` | `ADR-QRREF-004` High-value manual review state model | Blocks final API/test baseline |
| `JIRA-QRREF-064` | `ADR-QRREF-006` Safe degradation behavior | Blocks processor/ledger failure-mode closure |

Implementation must not proceed through a blocked decision boundary until the decision is approved or approved with non-blocking conditions.

### 9. Release

Release is created after validation is approved and the release package is ready.

| Field | Example |
| --- | --- |
| Release Issue | `JIRA-QRREF-100` |
| Change Package | `CHG-QRREF-001` |
| Git Validation Report | `domains/payments/capabilities/qr-refund/validation/validation-report.md` |
| Git Release Notes | `domains/payments/capabilities/qr-refund/release/release-notes.md` |
| Approval Gate | Release approved |

The Release issue links included Stories, Defects, PRs, validation evidence, rollback plan, known risks, and approvers.

## Approval Gate Sequence

| Gate | Primary Human Owner | Jira Evidence | Git Evidence |
| --- | --- | --- | --- |
| Idea accepted | Product Owner | Epic or intake status | Optional discovery notes |
| Intent approved | Product Owner / BA | Epic approval field or approval issue | `intent/intent.md` |
| Specification approved | Product Owner / BA | Specification approval issue | `specs/spec.md` |
| Architecture approved | Solution Architect | Architecture approval or Decision issues | `context/context.md`, ADRs, API guidance |
| Test design approved | QA Lead | QA approval Task | `tests/acceptance.feature` and related test design |
| Traceability approved | BA / Architect / QA Lead | Traceability review Task | `traceability/traceability-matrix.md` |
| Implementation slice approved | PO / Architect / QA Lead / Dev Lead | Build readiness Task | `design/implementation-plan.md` |
| Validation approved | QA Lead | Validation issue | `validation/validation-report.md` |
| Release approved | PO / QA / Architect / DevSecOps / Release Manager | Release issue or change record | `release/release-notes.md`, validation report, rollback evidence |

## Do / Don't Rules

Do:

- Create the Jira Epic early as a lightweight discovery and ownership container.
- Create Git intent only after discovery produces enough business context.
- Create Git specification only after intent approval.
- Create Jira Stories only after specification approval.
- Create implementation slices before Tasks/Subtasks.
- Create Tasks/Subtasks only for approved slices.
- Link Jira issues to stable Git paths and artifact IDs.
- Use Jira status to expose workflow state, blockers, dependencies, and approvals.
- Use Git artifacts and traceability as the authoritative delivery evidence.

Do not:

- Treat Jira descriptions as canonical requirements.
- Treat one Jira Story as one Functional Requirement.
- Create implementation Tasks before approved slices exist.
- Use Jira approvals to bypass missing Git evidence.
- Generate source code before approved intent, specification, architecture, tests, traceability, and slice plan.
- Implement lifecycle automation from this design without a separate automation proposal and approval.
