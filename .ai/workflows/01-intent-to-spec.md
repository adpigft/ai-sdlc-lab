# Workflow 01: Intent To Specification

## Purpose

Convert a stakeholder request into an approved, traceable specification candidate.

## Inputs

- Jira epic or intake ticket.
- Business problem, customer journey, and measurable outcome.
- Existing domain context and feedback.

## Steps

1. Capture intent using `.ai/templates/intent-template.md`.
2. Identify stakeholders, customers, operations teams, risk owners, and approval owners.
3. Record payment-specific assumptions, such as rails, limits, currency, QR format, settlement behavior, fees, notifications, and reconciliation needs.
4. Convert intent into requirements and acceptance criteria using `.ai/templates/spec-template.md`.
5. Add Jira references to the traceability matrix.
6. List open questions and classify them as product, architecture, QA, security, legal, compliance, or operations.
7. Request human approval to proceed to spec review.

## Outputs

- Intent artifact.
- Draft specification.
- Initial traceability rows.
- Open question list.

## Human Gate

Product owner approval in Jira is required before the specification review workflow starts.
