---
name: architecture
description: User-friendly architecture wrapper combining context, API design, ADR identification, integration, data, security, and implementation planning.
---

# Architecture Skill

## Purpose
Provide one normal-user entry point for solution architecture, including context, API considerations, integration, data, security, ADRs, and implementation planning.

## When to use
Use `$architecture` after specification approval and before implementation. Normal users should not need to invoke a separate API skill.

## Inputs
- Approved intent and specification
- Existing architecture context
- Integration and data constraints
- Security and compliance requirements
- Relevant standards and ADRs

## Process
1. Confirm specification approval exists.
2. Use `architect-context` to define boundaries, components, integrations, data, risks, and assumptions.
3. Identify API contract needs and document them through the active architecture workflow.
4. Identify ADR needs and route material unresolved decisions to `$decision`.
5. Include integration, data, security, observability, error handling, and operational considerations.
6. Define implementation slices only after architecture and API decisions are approved.
7. Ask for Architect approval before downstream implementation.

## Outputs
- Architecture context or design updates
- API contract guidance when needed
- ADR candidates or approved ADR links
- Integration, data, security, and implementation planning notes

## Quality checks
- Approved requirements drive the design.
- API changes are explicit and reviewable.
- Security and data concerns are addressed.
- ADRs are created for material decisions.
- Implementation does not start while blocking decisions are unresolved.

## Human gate
Architect approval is required for architecture and API contract changes.

## Next skill or next workflow step
Use `$test-design` for QA scenarios and `$implementation` only after required architecture, API, tests, and traceability are approved.

## Example usage
`$architecture Design the approved QR refund capability`
