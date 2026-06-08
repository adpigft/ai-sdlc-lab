---
name: intent-extraction
description: Recover business intent from an existing application, behavior, and documentation.
---

# Intent Extraction Skill

## Purpose

Recover the business intent behind an existing application so modernization work can preserve the right outcomes, boundaries, and constraints.

## When To Use

Use `$intent-extraction` after discovery engineering when the user needs recovered business outcomes, boundaries, assumptions, and confidence on what the existing system is trying to achieve.

## Inputs Needed

- Discovery findings
- Existing behavior, workflows, and documentation
- Stakeholder or work-management references, if available
- Known business outcomes or pain points

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and lifecycle behavior are defined by:

- `framework/01-lifecycle/skill-orchestration-adapter.md`
- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/24-discovery-engineering/brownfield-modernization-flow.md`

## Procedure

1. Review discovery outputs and recover the business intent from observed behavior and documentation.
2. Mark all findings as recovered intent, not fresh product invention.
3. Separate evidence from inference.
4. Capture business outcomes, scope boundaries, assumptions, and confidence.
5. Call out ambiguity or competing interpretations clearly.
6. Stop before creating specification, design, or implementation artifacts.

## Outputs Produced

- Recovered intent summary
- Business outcomes
- Scope boundaries
- Assumptions
- Confidence assessment

## Artifact Structure

1. Recovered Business Intent
2. Business Outcomes
3. Scope Boundaries
4. Assumptions
5. Evidence
6. Inference
7. Confidence Assessment
8. Open Questions

## Quality Checks

- Intent is clearly marked as recovered from the existing system.
- Confidence is stated as High, Medium, or Low.
- Evidence and inference are separated.
- No target-state requirements are invented.

## Stop Conditions

- Discovery evidence is too sparse to infer intent safely.
- The user asks for target-state requirements rather than recovered intent.

## Human Approval Expectations

Human review is required before recovered intent is used to create or update specifications, designs, tests, or implementation plans.

## Do Not

- Do not modify external systems unless explicitly approved.
- Do not create, update, delete, or transition Jira, Confluence, GitHub, Wynxx Story Creator, or source-code artifacts unless the skill explicitly allows it and the user approves.
- Do not expose secrets, tokens, credentials, or sensitive data.
- Do not fabricate missing requirements, evidence, source references, or approval status.
- Do not treat inferred content as confirmed fact.
- Do not bypass validation, traceability, approval, or stop-for-review rules.
- Do not claim recovered content is business-approved.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
