# Jira Approval Model

## Purpose

Define how Jira records human approval gates while Git remains the source of truth for the approved artifact content.

## Model

Approval gates:

```text
Idea accepted
-> Intent approved
-> Specification approved
-> Design approved
-> Test design approved
-> Traceability approved
-> Implementation slice approved
-> PR review approved
-> Validation approved
-> Release approved
```

Jira records approval status and approver evidence. Git stores the approved artifact and should reference the Jira approval where practical.

## Approval Gates

| Gate | Jira Evidence | Git Source | Required Approver |
| --- | --- | --- | --- |
| Idea accepted | Epic or intake status | Optional discovery notes | Product Owner |
| Intent approved | Epic approval field or approval issue | `intent/intent.md` | Product Owner / BA |
| Specification approved | Story creation approval or approval issue | `specification/specification.md` | Product Owner / BA |
| Design approved | Decision or design approval issue | `design/design.md`, ADRs, API guidance | Solution Architect |
| Test design approved | QA approval Task | `tests/acceptance.feature` | QA Lead |
| Traceability approved | traceability-review task | `traceability/traceability-matrix.md` | BA / Architect / QA Lead |
| Implementation slice approved | Build readiness Task | `implementation/implementation-plan.md` slice | Product Owner / Architect / QA Lead / Dev Lead as needed |
| PR review approved | PR review issue, PR approval, or review evidence | PR review findings and changed-file evidence | Developer Lead / Architect / impacted owners |
| Validation approved | QA validation issue | `validation/validation-report.md` | QA Lead |
| Release approved | Release issue or change record | `release/release-notes.md` | Product Owner / QA Lead / Architect / DevSecOps / Release Manager |

## Approval Decisions

| Decision | Meaning | Next Action |
| --- | --- | --- |
| Approved | Gate is approved without blocking conditions. | Move to next lifecycle state. |
| Approved With Conditions | Gate is approved with stated conditions. | Continue only if conditions are non-blocking; otherwise block dependent work. |
| Changes Required | Artifact needs correction. | Return to the owning skill/workflow stage. |
| Rejected | Artifact or scope is not accepted. | Stop or re-scope. |

## Example

QR Refund approval examples:

| Gate | Jira Placeholder | Git Artifact | Status |
| --- | --- | --- | --- |
| Intent approved | `JIRA-QRREF-001` | `intent/intent.md` | Approved by chat confirmation in lab context. |
| Specification approved | `JIRA-QRREF-050` | `specification/specification.md` | Approved by chat confirmation in lab context. |
| Design approved | `JIRA-QRREF-060` | `design/design.md` | Approved by chat confirmation in lab context. |
| traceability-review | `JIRA-QRREF-070` | `traceability/traceability-matrix.md` | Pending. |
| Implementation plan approval | `JIRA-QRREF-090` | `implementation/implementation-plan.md` | Pending. |
| Validation plan approval | `JIRA-QRREF-080` | `validation/validation-plan.md` | Pending. |

## Do / Don't Rules

Do:

- Record approver, role, date, decision, and Jira reference.
- Link the approval to the exact Git artifact version or path.
- Record conditions and identify whether they block downstream work.
- Keep approval evidence visible in traceability.

Do not:

- Treat AI-generated content as approved without a human gate.
- Let Jira approval override missing Git artifacts.
- Continue implementation when approval conditions block the slice.
- Close a release approval without validation evidence.
