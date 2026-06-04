# Workflow 01: Intent To Specification

## Purpose

Convert a stakeholder request into an approved, traceable specification candidate.

## Inputs

- Jira epic or intake ticket.
- Business problem, customer journey, and measurable outcome.
- Existing domain context and feedback.

## Steps

1. Read `domains/<domain>/domain-context.md` when available.
2. Capture intent using `framework/07-templates/intent-template.md`.
3. Identify stakeholders, customers, operations teams, risk owners, and approval owners.
4. Record payment-specific assumptions, such as rails, limits, currency, QR format, settlement behavior, fees, notifications, and reconciliation needs.
5. Convert intent into requirements and acceptance criteria using `framework/07-templates/spec-template.md`.
6. Add Jira references to the traceability matrix.
7. List open questions and classify them as product, architecture, QA, security, legal, compliance, or operations.
8. Request human approval to proceed to spec review.
9. After approval, update or prepare `workflow-state.yaml` so the capability can move from `intent_review` to `specification_review` when workflow-state is adopted.

## Outputs

- Intent artifact.
- Draft specification.
- Initial traceability rows.
- Open question list.

## Human Gate

Product owner approval in Jira is required before the specification review workflow starts.
