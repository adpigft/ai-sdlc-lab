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
- Domain context, such as `domains/<domain>/domain-context.md`, when available
- Integration and data constraints
- Security and compliance requirements
- Relevant standards and ADRs

## Context pack
Use the `Architecture` pack in `framework/context/stage-context-packs.md`.

Required reads:
- This skill document.
- Approved intent and specification.
- Active domain context.
- Active `workflow-state.yaml`.
- Implementation placement model.

Optional reads:
- Service catalog, frontend catalog, shared asset ownership, API/security standards, and event guidance when impacted.

Forbidden reads:
- Source code before implementation unless the user explicitly requests review of existing implementation.
- Unrelated domains unless cross-domain impact is identified.
- Validation and release artifacts unless checking drift.

Escalation rule: Read another domain, service, frontend module, or shared asset guidance only after architecture impact identifies it.

Token discipline rule: Prefer the active capability, placement model, and relevant standards; full framework reads are allowed only for framework assessment or framework changes.

Stop conditions:
- Specification is not approved.
- Material design decisions are unresolved.
- Target placement cannot be defined or explicitly deferred.

## Process
1. Confirm specification approval exists.
2. Read `domains/<domain>/domain-context.md` when the domain is known and the file exists.
3. Use `architect-context` to define boundaries, components, integrations, data, risks, and assumptions.
4. Identify API contract needs and document them through the active architecture workflow.
5. Identify ADR needs and route material unresolved decisions to `$decision`.
6. Include integration, data, security, observability, error handling, operational considerations, and reusable domain patterns.
7. Define target implementation placement before downstream implementation, or explicitly state that no code placement is required yet.
8. Define implementation slices only after architecture and API decisions are approved.
9. When architecture context, API guidance, ADR draft, or implementation planning artifact is created or updated, create or update `domains/<domain>/capabilities/<capability>/workflow-state.yaml`.
10. Set workflow state to `architecture_review`, current artifact to the architecture-owned draft, pending gate to `architecture_approval`, next state to `test_review`, and next skill to `test-design`.
11. Use `framework/workflow/workflow-state-guide.md` for state-aware `Review.`, `Approved.`, and `Status.` behavior.
12. After architecture approval, update `workflow-state.yaml` to move from `architecture_review` to `test_review`.
13. Ask for Architect approval before downstream implementation.

## Placement metadata
Before implementation or a code-impacting change, architecture must check or produce placement metadata:

- `target_app`, if frontend is impacted
- `target_frontend_module`, if frontend is impacted
- `target_service`, if backend is impacted
- `target_library`, if shared library is impacted
- `owning_squad`
- `allowed_paths`
- `restricted_paths`
- `required_approvals`
- `impacted_capabilities`
- `regression_scope`

Use `framework/service-architecture/implementation-placement-model.md`, `framework/service-architecture/service-catalog-template.md`, `framework/frontend/frontend-catalog-template.md`, and `framework/multi-squad/shared-asset-ownership-model.md`. If no code placement is required yet, say that explicitly in the architecture output.

## Outputs
- Architecture context or design updates
- API contract guidance when needed
- ADR candidates or approved ADR links
- Integration, data, security, and implementation planning notes
- Created or updated `domains/**/workflow-state.yaml` after architecture artifact creation

## Quality checks
- Approved requirements drive the design.
- API changes are explicit and reviewable.
- Security and data concerns are addressed.
- ADRs are created for material decisions.
- Implementation does not start while blocking decisions are unresolved.
- Implementation placement is defined before implementation, or architecture explicitly says no code placement is required yet.
- Domain context was reviewed when available.
- Workflow state points `Review.` to the architecture draft and blocks implementation while material decisions are unresolved.

## Human gate
Architect approval is required for architecture and API contract changes.

## Next skill or next workflow step
Use `$test-design` for QA scenarios and `$implementation` only after required architecture, API, tests, and traceability are approved.

## Example usage
`$architecture Design the approved QR refund capability`
