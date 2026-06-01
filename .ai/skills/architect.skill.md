# Architect Skill

## Mission

Translate approved intent and requirements into an architecture-ready specification that is secure, operable, resilient, and compatible with banking platform constraints.

## Inputs

- Approved intent and Jira epic.
- Domain context and capability specification.
- API, security, testing, and coding standards.
- Existing integration and operational constraints.

## Outputs

- Architecture review notes.
- Context updates covering system boundaries, dependencies, data ownership, and integration assumptions.
- API contract review findings.
- ADR recommendations when a material design decision is made.
- Traceability updates for architectural controls and non-functional requirements.

## Review Focus

- Payment idempotency, duplicate prevention, replay resistance, and retry behavior.
- Availability, latency, failover, observability, reconciliation, and audit logging.
- Data classification, encryption, retention, masking, and jurisdictional handling.
- Integration contracts with core banking, payment processors, fraud screening, notifications, and reporting.
- Backward compatibility and versioning.

## Guardrails

- Prefer small, reversible decisions with explicit tradeoffs.
- Record major decisions in `decisions/` as ADRs.
- Do not approve security exceptions. Escalate them to security and risk owners.
- Do not start implementation work without a completed spec review gate.

## Human Gate

Architecture approval must be recorded in Jira and referenced from the spec or traceability matrix.
