---
name: modernization-readiness
description: Assess whether discovery is sufficient to begin brownfield modernization intent work.
---

# Modernization Readiness Skill

## Purpose

Assess whether discovery is sufficient to begin brownfield modernization intent work.

## When To Use

Use `$modernization-readiness` after discovery when the team needs a readiness decision before defining target-state intent.

## Inputs Needed

- Discovery outputs
- Discovery evidence
- Discovery limitations
- Current-state understanding
- Brownfield modernization goals

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and lifecycle behavior are defined by:

- `framework/01-lifecycle/skill-orchestration-adapter.md`
- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/24-discovery-engineering/modernization-readiness-review.md`

## Procedure

1. Review discovery artifacts and evidence.
2. Evaluate current-state understanding, evidence quality, limitations, and target-state readiness.
3. Distinguish demo replacement readiness from production replacement readiness.
4. Identify missing information, risks, and remediation needs.
5. Produce a readiness recommendation and stop before defining intent.

## Outputs Produced

- Modernization readiness review
- Readiness score or qualitative readiness judgment
- Missing information and limitations
- Recommendation to proceed, remediate, or continue discovery

## Artifact Structure

1. Review Scope
2. Current-State Understanding
3. Evidence Quality
4. Limitations
5. Demo Readiness
6. Production Readiness
7. Target-State Readiness
8. Risks
9. Recommendation

## Quality Checks

- Evidence is separated from inference.
- Limitations are explicit.
- Demo and production readiness are assessed separately.
- The skill does not invent missing facts.

## Stop Conditions

- Discovery evidence is too sparse.
- Target-state goals are not clear enough to judge readiness.
- The user asks for intent or design instead of readiness assessment.

## Human Approval Expectations

Human review is required before discovery outputs become the basis for target-state intent.

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
