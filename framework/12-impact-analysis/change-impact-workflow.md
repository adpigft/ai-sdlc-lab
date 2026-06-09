# Change Impact Workflow

## Purpose

This document defines the workflow shape for common change scenarios.

It is a governance model, not an execution script.

## Minor Change

- Owner: feature owner
- Approver: feature approver
- Required artifacts: impacted intent, requirements, design, tests, traceability
- Validation gates: targeted regression, traceability check, local validation
- Jira action: update existing issue or note impact if the issue exists
- Confluence action: update published summary only if approved by process
- Control Tower visibility: flag as a minor in-flight change

## In-Flight Change After Spec Approval

- Owner: BA / feature lead
- Approver: BA / PO and design reviewer when design changes
- Required artifacts: updated requirements, impact analysis, traceability delta
- Validation gates: requirements review, design delta review, test impact review
- Jira action: mark change scope on the existing story or linked issue
- Confluence action: keep published pages synchronized after approval
- Control Tower visibility: show as an in-flight change requiring review

## Major Change After Design Approval

- Owner: architect or feature lead, depending on impact
- Approver: architect, PO / BA, QA, and release approver as needed
- Required artifacts: impact analysis, updated design, updated tests, traceability update, release assessment
- Validation gates: architecture review, API compatibility review, regression plan, release risk review
- Jira action: re-scope the existing item or create controlled follow-up only through approved process
- Confluence action: republish the reviewed summary after approval
- Control Tower visibility: show as a major change with elevated risk

## Post-Release Change

- Owner: product owner or service owner
- Approver: release owner plus affected reviewers
- Required artifacts: change request, impact analysis, defect or enhancement traceability, rollback or mitigation notes
- Validation gates: hotfix validation, regression validation, monitoring readiness
- Jira action: link to the released item and create the follow-up change record through approved process
- Confluence action: publish the post-release summary when approved
- Control Tower visibility: show as a post-release intervention or follow-up

## Brownfield Change

- Owner: domain or capability owner
- Approver: architecture, QA, and operations owners as needed
- Required artifacts: current-state context, modernization readiness review, gap analysis, impact analysis, compatibility notes, traceability
- Validation gates: brownfield discovery, readiness review, dependency review, compatibility checks, regression coverage
- Jira action: keep the change linked to the existing work container
- Confluence action: maintain the synced published view after approval
- Control Tower visibility: show as a brownfield change with context and dependency risk

## Notes

- All change types require impact analysis before approval.
- The exact approval chain depends on the workflow state and the affected artifacts.
- Git remains the source of truth.
