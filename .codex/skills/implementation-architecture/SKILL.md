---
name: implementation-architecture
description: Define module, package, migration, standards, and delivery architecture before implementation.
---

# Implementation Architecture Skill

## Purpose

Define module, package, migration, standards, and delivery architecture before implementation starts.

## When To Use

Use `$implementation-architecture` after vertical slice planning when the team needs the bridge between planning and code execution.

## Inputs Needed

- Vertical slice plan
- Implementation plan
- Approved design
- Placement metadata
- Testing and delivery standards

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and lifecycle behavior are defined by:

- `framework/01-lifecycle/skill-orchestration-adapter.md`
- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/03-delivery-governance/service-architecture/implementation-placement-model.md`

## Procedure

1. Review the vertical slice plan and implementation plan.
2. Define module and package structure.
3. Define database migration strategy, API implementation standards, domain-layer standards, transaction boundary strategy, outbox-worker strategy, testing strategy, and CI/CD strategy.
4. Confirm implementation placement and ownership metadata.
5. Produce an implementation architecture review before code starts.

## Outputs Produced

- Module structure
- Package structure
- Database migration strategy
- API implementation standards
- Domain-layer standards
- Transaction boundary strategy
- Outbox-worker strategy
- Testing strategy
- CI/CD strategy
- Implementation architecture review

## Artifact Structure

1. Module Structure
2. Package Structure
3. Database Migration Strategy
4. API Implementation Standards
5. Domain-Layer Standards
6. Transaction Boundary Strategy
7. Outbox Worker Strategy
8. Testing Strategy
9. CI/CD Strategy
10. Implementation Architecture Review

## Quality Checks

- Module/package boundaries are explicit.
- Migration, transaction, and outbox strategies are defined when relevant.
- Testing and CI/CD expectations are visible.
- Placement and ownership are clear enough for implementation.

## Stop Conditions

- Vertical slice plan or implementation plan is missing.
- Placement metadata is missing and cannot be safely deferred.
- The user asks to implement instead of finalize architecture.

## Human Approval Expectations

Human review is required before implementation depends on the architecture.

## Do Not

- Do not modify external systems unless explicitly approved.
- Do not create, update, delete, or transition Jira, Confluence, GitHub, Wynxx Story Creator, or source-code artifacts unless the skill explicitly allows it and the user approves.
- Do not expose secrets, tokens, credentials, or sensitive data.
- Do not fabricate missing requirements, evidence, source references, or approval status.
- Do not treat inferred content as confirmed fact.
- Do not bypass validation, traceability, approval, or stop-for-review rules.
- Do not change code.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
