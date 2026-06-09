---
name: design
description: Define solution design, boundaries, APIs, events, integrations, data, security, observability, decisions, and implementation placement.
---

# Design Skill

## Purpose

Translate approved requirements into a reviewable solution design without starting implementation prematurely.

## When To Use

Use `$design` after requirements approval and before implementation. Use it whenever architecture, API, event, integration, data, security, operational, or placement decisions are needed. For brownfield work, use it as the target solution design mode after readiness and requirements are approved.

## Inputs Needed

- Approved intent and requirements
- Domain or system context
- Integration, data, security, compliance, and operational constraints
- Relevant standards and existing decisions
- Known implementation ownership or placement constraints
- Mode hint for greenfield or brownfield design

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, lifecycle behavior, and placement metadata requirements are defined by:

- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/03-delivery-governance/service-architecture/implementation-placement-model.md`
- `framework/01-lifecycle/skill-orchestration-adapter.md`

## Procedure

1. Confirm approved requirements exist.
2. Define system boundaries, responsibilities, components, integrations, data ownership, state model, and sequence flow.
3. Identify API, event, and integration contracts that must be created or changed.
4. Address security, privacy, audit, observability, availability, performance, and failure handling.
5. Identify material decisions and produce decision records when needed.
6. For brownfield design, run a design-input review and use a design-artifact plan to select mandatory, conditional, project-specific, or not-required artifacts.
7. Define implementation placement or explicitly state why no code placement is required yet.
8. Define implementation slices only after design choices are stable enough to review.
9. Stop for architect and impacted-owner review before implementation depends on the design.

## Outputs Produced

- Design artifact or design update
- Brownfield design-input review and design-artifact plan when applicable
- API, event, integration, data, security, and operational design guidance
- Decision candidates or decision records when needed
- Placement and ownership metadata when implementation may be impacted
- Review request for architect and impacted-owner approval

## Artifact Structure

Artifact Structure

1. Solution Overview
2. Architecture
3. Components
4. Sequence Flows
5. APIs
6. Events
7. Integrations
8. Data Model
9. Security
10. Observability
11. ADR References
12. Open Questions
13. Design Input Review
14. Design Artifact Plan

## Quality Checks

- Design is driven by approved requirements.
- Boundaries and ownership are clear.
- API, event, data, and integration impacts are explicit.
- Security, audit, observability, and failure handling are addressed.
- Material decisions are recorded and unresolved decisions block implementation.
- Placement and ownership are clear enough for implementation planning.

## Stop Conditions

- Requirements approval is missing.
- Material design decisions are unresolved.
- Required owner, API, event, integration, or placement information is missing.
- The user asks to implement before required design approvals exist.

## Human Approval Expectations

Architect approval is required for design. Impacted service, frontend, shared asset, API, event, security, or operations owners must review where their area is affected.

## Do Not

- Do not modify external systems unless explicitly approved.
- Do not create, update, delete, or transition Jira, Confluence, GitHub, Wynxx Story Creator, or source-code artifacts unless the skill explicitly allows it and the user approves.
- Do not expose secrets, tokens, credentials, or sensitive data.
- Do not fabricate missing requirements, evidence, source references, or approval status.
- Do not treat inferred content as confirmed fact.
- Do not bypass validation, traceability, approval, or stop-for-review rules.
- Do not change source code.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
