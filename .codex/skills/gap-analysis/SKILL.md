---
name: gap-analysis
description: Compare current-state extracted artifacts with target-state goals and identify modernization gaps.
---

# Gap Analysis Skill

## Purpose

Compare current-state extracted artifacts with target-state goals and identify the gaps, retained behavior, changed behavior, removed behavior, and new behavior needed for modernization.

## When To Use

Use `$gap-analysis` after discovery, intent extraction, specification extraction, and context extraction when the user needs a structured modernization delta.

## Inputs Needed

- Current-state discovery
- Recovered intent
- Current-state specification
- Legacy context
- Target-state goals or constraints

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and lifecycle behavior are defined by:

- `framework/01-lifecycle/skill-orchestration-adapter.md`
- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/24-discovery-engineering/brownfield-modernization-flow.md`

## Procedure

1. Compare the current-state artifacts with the target-state goals.
2. Identify business, technical, data, integration, security, and operational gaps.
3. Classify each gap by severity and owner role.
4. Separate retained behavior, changed behavior, removed behavior, and new behavior.
5. Capture modernization risks and assumptions.
6. Stop before creating an implementation plan.

## Outputs Produced

- Gap analysis summary
- Retained behavior list
- Changed behavior list
- Removed behavior list
- New behavior list
- Modernization risks

## Artifact Structure

1. Gap Analysis
2. Retained Behavior
3. Changed Behavior
4. Removed Behavior
5. New Behavior
6. Risk Register
7. Severity
8. Owner Role
9. Evidence and Assumptions

## Quality Checks

- Gaps are categorized consistently.
- Severity and owner role are explicit.
- Retained and changed behaviors are not mixed together.
- No implementation plan is created.

## Stop Conditions

- Target-state goals are missing or too vague to compare.
- The user asks for implementation planning instead of gap analysis.

## Human Approval Expectations

Human review is required before gap analysis is used to justify target-state specification, design, or implementation work.

## Do Not

- Do not modify external systems unless explicitly approved.
- Do not create, update, delete, or transition Jira, Confluence, GitHub, Wynxx Story Creator, or source-code artifacts unless the skill explicitly allows it and the user approves.
- Do not expose secrets, tokens, credentials, or sensitive data.
- Do not fabricate missing requirements, evidence, source references, or approval status.
- Do not treat inferred content as confirmed fact.
- Do not bypass validation, traceability, approval, or stop-for-review rules.
- Do not create implementation plans.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
