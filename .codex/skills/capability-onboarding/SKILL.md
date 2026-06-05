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
- Capability name, if known
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
2. Validate the hierarchy level being discussed:
   - Domain: broad business or architecture boundary.
   - Capability: durable business-function boundary under a domain.
   - Feature: deliverable behavior under a capability.
3. If only a domain is supplied, enter capability discovery mode instead of stopping immediately:
   - Summarize the known domain context.
   - Identify candidate capability areas from the domain context when available.
   - Ask structured onboarding questions for the missing capability boundary.
4. Detect probable feature names. If the requested name sounds like a narrow deliverable, user journey, transaction, screen, or workflow rather than a durable business function, ask whether it should be created under an existing capability.
5. If information is insufficient, propose a candidate capability structure with assumptions and ask for confirmation.
6. Clarify the capability purpose and business boundary.
7. Capture owned features, shared flows, shared APIs, shared events, shared integrations, and state model assumptions.
8. Capture ownership, out-of-scope items, assumptions, and open questions.
9. Stop for human review before treating the capability context as approved.

## Capability Discovery Questions

When only the domain is known, ask concise structured questions:

1. What business function should this capability own?
2. Which features or user journeys are expected under it?
3. Who owns the capability and architecture decisions?
4. What shared APIs, events, integrations, or state does it own or coordinate?
5. What is explicitly out of scope?

If the domain context already lists candidate capabilities, offer those candidates before asking for a new name.

## Feature-Like Name Detection

Treat a name as a possible feature when it appears to describe:

- a single request, action, or user journey
- a channel-specific screen or workflow
- a narrow transaction or operation
- a variant of a broader capability

Example:

`Card Replacement` may be a feature if the broader capability is `Card Lifecycle Management`. Ask whether `Card Replacement` should be created under an existing or proposed capability before creating capability context.

## Outputs Produced

- Capability context artifact
- Review summary for the capability owner or architect
- Assumptions and open questions
- Capability discovery questions when only the domain is supplied
- Hierarchy validation summary covering domain, capability, and feature placement
- Candidate capability structure when confirmed information is incomplete
- Feature-like name warning and placement question when applicable

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
- The capability boundary is distinct from feature-level delivery scope.
- Domain, capability, and feature hierarchy assumptions are explicit.
- Owned features are identified.
- Feature-like names have been challenged or confirmed as true capabilities.
- If only a domain was supplied, discovery questions were asked before stopping.
- If information was incomplete, a candidate capability structure was proposed for confirmation.
- Shared APIs, events, integrations, and state model assumptions are captured where known.
- Ownership and out-of-scope notes are explicit.
- No feature artifacts or source code are created by this skill.

## Stop Conditions

- The parent domain context is missing.
- The user confirms the requested item is a feature but no parent capability is known.
- The user asks to create feature artifacts or source code.
- A hierarchy conflict cannot be resolved after discovery questions.
- Required ownership information remains missing after asking structured onboarding questions and proposing assumptions.

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
