---
name: decision
description: Create, review, and manage architecture or delivery decisions so unresolved choices do not leak into implementation.
---

# Decision Skill

## Purpose

Make material choices explicit by documenting context, options, selected decision, consequences, risks, owners, and approval status.

## When To Use

Use `$decision` when a design, technology, integration, security, data, operational, ownership, or release choice needs a decision record before downstream work can proceed.

## Inputs Needed

- Decision topic
- Context and constraints
- Options considered
- Recommendation or selected option, if known
- Consequences, risks, tradeoffs, and affected owners
- Related artifacts, systems, APIs, events, releases, or work items where applicable

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and links to relevant artifacts are defined by:

- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/01-lifecycle/skill-orchestration-adapter.md`

## Procedure

1. Determine whether a new decision record is needed or an existing decision should be reviewed.
2. Capture context, constraints, options, selected option, rejected options, consequences, and risks.
3. Identify impacted artifacts, owners, tests, implementation, validation, and release evidence.
4. Mark unresolved material decisions as blockers.
5. Ask for required owner or architect approval before treating the decision as accepted.

## Outputs Produced

- Draft or reviewed decision record
- Decision status and owner
- Options, selected choice, consequences, and risks
- Impacted artifact and follow-up list
- Blocker or approval recommendation

## Artifact Structure

1. Context
2. Decision
3. Alternatives Considered
4. Trade-offs
5. Consequences

## Quality Checks

- Context and constraints are explicit.
- Options and rejected alternatives are documented.
- Consequences and risks are visible.
- Impacted artifacts and owners are identified.
- Implementation is blocked while material decisions remain unresolved.

## Stop Conditions

- Decision context is insufficient.
- Impacted owners cannot be identified.
- A material decision is unresolved but downstream work is requested.
- Approval is missing for an accepted decision.

## Human Approval Expectations

Architect or designated owner approval is required before a decision can unblock downstream work.

## Do Not

- Do not modify external systems unless explicitly approved.
- Do not create, update, delete, or transition Jira, Confluence, GitHub, Wynxx Story Creator, or source-code artifacts unless the skill explicitly allows it and the user approves.
- Do not expose secrets, tokens, credentials, or sensitive data.
- Do not fabricate missing requirements, evidence, source references, or approval status.
- Do not treat inferred content as confirmed fact.
- Do not bypass validation, traceability, approval, or stop-for-review rules.
- Do not turn unresolved choices into implementation decisions without approval.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
