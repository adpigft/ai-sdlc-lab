---
name: domain-onboarding
description: Onboard a new domain by capturing business scope, boundaries, ownership, integrations, APIs, events, and placement assumptions before delivery work starts.
---

# Domain Onboarding Skill

## Purpose

Create the domain-level context needed before capabilities or features are created in a new business or architecture domain.

## When To Use

Use `$domain-onboarding` when a domain does not exist yet or when an existing domain needs approved onboarding context before delivery starts.

## Inputs Needed

- Domain name
- Domain owner
- Business scope and boundaries
- Candidate capabilities
- Key integrations, APIs, and events
- Frontend, backend, service, or shared asset expectations if known
- Ownership, approval, security, data, and operational assumptions

## Framework Adapter

When this skill is used inside this repository, context loading, domain artifact placement, approval gates, and lifecycle entry behavior are defined by:

- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/03-delivery-governance/service-architecture/domain-onboarding-model.md`
- `framework/01-lifecycle/skill-orchestration-adapter.md`

## Procedure

1. Confirm the requested domain and normalize naming.
2. Check whether the domain already exists before creating or updating anything.
3. Capture purpose, scope, boundaries, glossary, core entities, candidate capabilities, APIs, events, integrations, ownership, NFR considerations, assumptions, and open questions.
4. Record frontend, backend, service, and shared asset placement assumptions when known.
5. Mark unknown services, modules, integrations, APIs, or events as assumptions or open questions rather than inventing implementation.
6. Do not create capabilities, feature artifacts, source code, or implementation folders during domain onboarding.
7. Stop for human review after the domain context is drafted or updated.

## Outputs Produced

- Domain context artifact or update
- Domain README or onboarding summary where the framework asks for one
- Open questions, assumptions, and owner list
- Review request before capability or feature creation

## Artifact Structure

1. Domain Purpose
2. Business Scope
3. Boundaries
4. Glossary
5. Core Entities
6. Candidate Capabilities
7. Owned APIs
8. Published Events
9. Consumed Events
10. Integrations
11. Ownership
12. Frontend Placement Assumptions
13. Backend Service Placement Assumptions
14. Shared Asset Impacts
15. NFR Considerations
16. Out of Scope
17. Next Steps

## Quality Checks

- Domain boundary is clear.
- Domain owner is identified.
- Candidate capabilities are listed as candidates, not approved delivery scope.
- APIs, events, integrations, services, frontend modules, and shared assets are captured when known.
- Unknowns are recorded as open questions.
- No capabilities or source code are created.

## Stop Conditions

- The domain already exists and update approval is missing.
- Domain owner or boundary cannot be identified.
- The user asks to create capabilities, feature artifacts, source code, or implementation folders during onboarding.
- Required assumptions cannot be captured safely.

## Human Approval Expectations

Domain owner and solution architect review are expected before capabilities or features are created from the new domain context.

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
