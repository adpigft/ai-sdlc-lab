---
name: capability-onboarding
description: Create or update capability context for an existing domain before feature delivery begins.
---

# Capability Onboarding Skill

## Purpose

Create or update the business-function boundary for a capability so feature work has a clear parent context.

## When To Use

Use `$capability-onboarding` when a new parent business function is needed under an existing domain before features are created.

## Inputs Needed

- Domain context
- Capability name
- Business purpose
- Owned features, if known
- Shared APIs, events, and integrations, if known
- Owner or squad
- Assumptions and open questions

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval handling, and source-of-truth guidance are defined by:

- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/01-lifecycle/skill-orchestration-adapter.md`

## Procedure

1. Confirm the parent domain and current ownership context.
2. Clarify the capability purpose and business boundary.
3. Capture owned features, shared flows, shared APIs, shared events, shared integrations, and state model assumptions.
4. Capture ownership, out-of-scope items, assumptions, and open questions.
5. Stop for human review before treating the capability context as approved.

## Outputs Produced

- Capability context artifact
- Review summary for the capability owner or architect
- Assumptions and open questions

## Artifact Structure

1. Capability Purpose
2. Business Boundary
3. Owned Features
4. Shared Flows
5. Shared APIs
6. Shared Events
7. Shared Integrations
8. Shared State Model
9. Ownership
10. Out of Scope
11. Open Questions

## Quality Checks

- Capability purpose is clear.
- The capability boundary is distinct from the domain boundary.
- Owned features are identified.
- Shared APIs, events, integrations, and state model assumptions are captured where known.
- Ownership and out-of-scope notes are explicit.
- No feature artifacts or source code are created by this skill.

## Stop Conditions

- The parent domain context is missing.
- Required ownership information is missing.
- The user asks to create feature artifacts or source code.

## Human Approval Expectations

Capability owner and architect review are expected before feature delivery uses the capability context.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
