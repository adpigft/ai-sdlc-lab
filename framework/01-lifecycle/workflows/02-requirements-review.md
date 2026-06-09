# Workflow 02: Requirements Review

## Purpose

Assess whether requirements are complete, testable, secure, operable, and ready for implementation planning.

## Reviewers

- Product owner.
- Business analyst.
- Architect.
- QA lead.
- Security or risk representative.
- Operations representative where payment support or reconciliation is affected.

## Steps

1. Read `domains/<domain>/domain-context.md` when available.
2. Check every requirement has an ID, source, acceptance criteria, priority, and Jira reference.
3. Review payment flows for pending states, duplicate handling, limits, fraud screening, customer messaging, and reconciliation.
4. Review non-functional requirements for latency, availability, security, auditability, observability, and recoverability.
5. Validate API contract completeness where an API is in scope.
6. Confirm tests can be derived from the acceptance criteria.
7. Update traceability for reviewed requirements, controls, and review evidence.
8. Record approvals, required changes, or rejected scope in Jira.
9. After approval, update or prepare `workflow-state.yaml` so the capability can move from `requirements_review` to `design_review` when workflow-state is adopted.

## Outputs

- Reviewed requirements.
- Review gate record using `framework/07-templates/review-gate-template.md`.
- Updated traceability matrix.
- ADR request if a major architecture decision is discovered.

## Human Gate

Implementation planning cannot start until required reviewers approve or explicitly defer their concerns with documented risk acceptance.
