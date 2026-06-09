---
name: impact-analysis
description: Assess implementation impact across requirements, code, tests, integrations, and delivery readiness.
---

# Impact Analysis Skill

## Purpose

Assess the impact of proposed changes on requirements, architecture, code, tests, integrations, operations, and release readiness before a major change proceeds.

## When To Use

Use `$impact-analysis` when a proposed change needs an impact assessment before implementation planning or implementation continues.

## Inputs Needed

- Current-state and target-state artifacts
- Traceability where available
- Proposed change description
- Affected systems, APIs, data, tests, integrations, and operational concerns
- Known owners or stakeholders

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and lifecycle behavior are defined by:

- `framework/01-lifecycle/skill-orchestration-adapter.md`
- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/12-impact-analysis/impact-analysis-model.md`

## Procedure

1. Identify the proposed change and the affected scope.
2. Trace the impact across requirements, components, data, APIs, integrations, tests, operations, and implementation sequencing.
3. Identify impacted artifacts, owners, risks, and dependencies.
4. Classify residual risk and whether the change is ready to continue.
5. Do not create the implementation plan itself.

## Outputs Produced

- Change impact assessment
- Impacted components
- Impacted data
- Impacted APIs
- Impacted integrations
- Impacted tests
- Impacted operations
- Implementation sequencing
- Risk impact summary
- Impact traceability

## Artifact Structure

1. Impact Analysis
2. Component Impact
3. Data Impact
4. API Impact
5. Integration Impact
6. Testing Impact
7. Operational Impact
8. Implementation Sequencing
9. Risk Impact
10. Impact Traceability

## Quality Checks

- Impacted areas are explicitly identified.
- Traceability is used where available.
- Owners and next actions are visible.
- Major changes do not proceed without impact assessment.

## Stop Conditions

- The change scope is missing or ambiguous.
- The user asks to bypass impact assessment for a major change.
- The requested work is actually implementation planning.

## Human Approval Expectations

Human review is required before impact analysis is treated as approval to proceed.

## Do Not

- Do not modify external systems unless explicitly approved.
- Do not create, update, delete, or transition Jira, Confluence, GitHub, Wynxx Story Creator, or source-code artifacts unless the skill explicitly allows it and the user approves.
- Do not expose secrets, tokens, credentials, or sensitive data.
- Do not fabricate missing requirements, evidence, source references, or approval status.
- Do not treat inferred content as confirmed fact.
- Do not bypass validation, traceability, approval, or stop-for-review rules.
- Do not treat impact analysis as implementation approval.
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
