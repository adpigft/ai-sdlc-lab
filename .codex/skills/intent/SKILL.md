---
name: intent
description: Capture business intent for a new capability, feature, product outcome, or scoped change before requirements, design, tests, or code.
---

# Intent Skill

## Purpose

Discover and document why the work is needed, who it serves, what outcome it should produce, what is in scope, what is out of scope, and what assumptions or dependencies must be resolved.

## When To Use

Use `$intent` when a user wants to start a new business outcome, product capability, feature, or materially new scope.

## Inputs Needed

- Business problem or opportunity
- Target users or stakeholders
- Expected outcome and success measures
- Known scope and exclusions
- Constraints, assumptions, dependencies, and risks
- Relevant domain or business context, when available
- Optional work-management or stakeholder references

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and lifecycle behavior are defined by:

- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/01-lifecycle/skill-orchestration-adapter.md`

## Procedure

1. Ask focused discovery questions before creating or updating artifacts.
2. Clarify users, outcomes, scope, exclusions, constraints, assumptions, dependencies, risks, and success measures.
3. Check whether similar existing business outcomes or reusable patterns should influence the intent.
4. Summarize the intent in plain business language.
5. Identify missing inputs and open questions.
6. Stop for PO / BA review before treating the intent as approved.
7. Do not generate requirements, design, tests, or code from unapproved intent.

## Outputs Produced

- Intent discovery summary
- Intent artifact containing business outcome, scope, exclusions, stakeholders, assumptions, dependencies, risks, success measures, and open questions
- Review request for PO / BA approval

## Artifact Structure

1. Business Outcome
2. Problem Statement
3. Stakeholders
4. In Scope
5. Out of Scope
6. Assumptions
7. Dependencies
8. Risks
9. Success Measures
10. Open Questions

## Quality Checks

- Business problem and desired outcome are clear.
- Users and stakeholders are identified.
- Scope and exclusions are explicit.
- Assumptions, dependencies, constraints, and risks are visible.
- Success measures are stated where known.
- Open questions are not hidden.
- No downstream solution detail is invented to fill intent gaps.

## Stop Conditions

- The business outcome is unclear.
- Required PO / BA input is missing.
- The requested work depends on a domain or owner that cannot be identified.
- The user asks for downstream artifacts or code before intent approval.

## Human Approval Expectations

PO / BA approval is required before this intent is used as the basis for specification, design, tests, implementation, validation, or release work.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
