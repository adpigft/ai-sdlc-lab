---
name: traceability-review
description: Review and maintain end-to-end traceability from intent through requirements, design, tests, implementation, validation, release, and external workflow references.
---

# Traceability Review Skill

## Purpose

Ensure business intent, requirements, design decisions, contracts, tests, implementation evidence, validation, release evidence, and external workflow references remain connected and auditable.

## When To Use

Use `$traceability-review` whenever scope, requirements, design, contracts, tests, implementation, validation, release, Jira, Confluence, or feedback links change.

## Inputs Needed

- Intent and requirements
- Design, decisions, APIs, events, or integrations
- Test scenarios and validation evidence
- Implementation or PR evidence where applicable
- Release evidence where applicable
- External workflow or publication references where applicable

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and traceability matrix location are defined by:

- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/01-lifecycle/skill-orchestration-adapter.md`

## Procedure

1. Identify the active scope and source artifacts.
2. Map intent to requirements.
3. Map requirements to design, decisions, APIs, events, and integrations.
4. Map requirements to tests.
5. Map tests to implementation and validation evidence where available.
6. Map release evidence to approved scope where available.
7. Identify orphan requirements, orphan tests, missing evidence, stale links, and contradictions.
8. Report gaps and update traceability only when approved or requested.

## Outputs Produced

- Traceability assessment
- Traceability matrix or traceability update where the framework asks for one
- Gap, blocker, and owner list
- Review request for BA, Architect, QA, or release owners as needed

## Artifact Structure

1. Context
2. Decision / Requirement Links
3. Design Links
4. Test Links
5. Validation Links
6. Release Links
7. Gaps
8. Actions

## Quality Checks

- No orphan requirements.
- No orphan tests.
- APIs, events, and major decisions map to approved requirements.
- Implementation and validation evidence map to approved scope.
- Released items map to approved and validated scope.
- Gaps are clearly marked and not hidden.

## Stop Conditions

- Mandatory source artifacts are missing.
- Traceability gaps block implementation, validation, or release.
- Source artifacts disagree and need owner review before traceability can be trusted.

## Human Approval Expectations

BA, Architect, QA, and impacted owners should review traceability before implementation, validation, or release gates depend on it.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
