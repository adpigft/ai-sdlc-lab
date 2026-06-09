---
name: implementation-readiness
description: Classify what must close before implementation can start.
---

# Implementation Readiness Skill

## Purpose

Classify what must close before implementation can start and what can proceed with assumptions or be deferred.

## When To Use

Use `$implementation-readiness` after design and impact analysis when the team needs a readiness gate before implementation planning or code changes.

## Inputs Needed

- Gap analysis
- Impact analysis
- Approved design
- Traceability
- Known blockers, dependencies, and assumptions

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and lifecycle behavior are defined by:

- `framework/01-lifecycle/skill-orchestration-adapter.md`
- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`

## Procedure

1. Review the approved design, gap analysis, and impact analysis.
2. Classify items into must-close, can-proceed-with-assumptions, and can-defer groups.
3. Identify readiness blockers, unresolved decisions, and ownership gaps.
4. Record assumptions that may be used to continue planning.
5. Stop before creating the implementation plan itself.

## Outputs Produced

- Implementation readiness review
- Must-close items
- Assumptions that can proceed
- Deferred items
- Readiness recommendation

## Artifact Structure

1. Review Scope
2. Must Close
3. Can Proceed With Assumptions
4. Can Defer
5. Risks
6. Recommendation

## Quality Checks

- Readiness categories are explicit.
- Owner and decision gaps are visible.
- Assumptions are separated from confirmed facts.
- The skill does not create the implementation plan.

## Stop Conditions

- Gap analysis or impact analysis is missing.
- The design is not approved.
- The user asks to start implementation planning instead of readiness review.

## Human Approval Expectations

Human review is required before implementation planning or implementation depends on the readiness assessment.

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
