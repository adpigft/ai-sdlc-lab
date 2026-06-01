# Workflow 02: Specification Review

## Purpose

Assess whether a specification is complete, testable, secure, operable, and ready for implementation planning.

## Reviewers

- Product owner.
- Business analyst.
- Architect.
- QA lead.
- Security or risk representative.
- Operations representative where payment support or reconciliation is affected.

## Steps

1. Check every requirement has an ID, source, acceptance criteria, priority, and Jira reference.
2. Review payment flows for pending states, duplicate handling, limits, fraud screening, customer messaging, and reconciliation.
3. Review non-functional requirements for latency, availability, security, auditability, observability, and recoverability.
4. Validate API contract completeness where an API is in scope.
5. Confirm tests can be derived from the acceptance criteria.
6. Update traceability for reviewed requirements, controls, and review evidence.
7. Record approvals, required changes, or rejected scope in Jira.

## Outputs

- Reviewed specification.
- Review gate record using `.ai/templates/review-gate-template.md`.
- Updated traceability matrix.
- ADR request if a major architecture decision is discovered.

## Human Gate

Implementation planning cannot start until required reviewers approve or explicitly defer their concerns with documented risk acceptance.
