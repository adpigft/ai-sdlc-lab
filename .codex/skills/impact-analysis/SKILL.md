---
name: impact-analysis
description: Assess change impact on requirements, APIs, data model, code, tests, integrations, and release readiness.
---

# Impact Analysis Skill

## Purpose

Assess the impact of proposed changes on requirements, APIs, data model, code, tests, integrations, and release readiness before a major change proceeds.

## When To Use

Use `$impact-analysis` when a proposed change needs an impact assessment before modernization continues.

## Inputs Needed

- Current-state and target-state artifacts
- Traceability where available
- Proposed change description
- Affected systems, APIs, data, tests, and integrations
- Known owners or stakeholders

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and lifecycle behavior are defined by:

- `framework/01-lifecycle/skill-orchestration-adapter.md`
- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/12-impact-analysis/impact-analysis-model.md`

## Procedure

1. Identify the proposed change and the affected scope.
2. Trace the impact across requirements, APIs, data, code, tests, integrations, and release readiness.
3. Identify impacted artifacts, tests, integrations, and owners.
4. Record recommended next actions and residual risk.
5. Mark unresolved high-impact changes as not ready to proceed.

## Outputs Produced

- Change impact assessment
- Impacted artifacts
- Impacted tests
- Impacted integrations
- Impact risk summary

## Artifact Structure

1. Change Summary
2. Impacted Requirements
3. Impacted APIs / Data / Code
4. Impacted Tests
5. Impacted Integrations
6. Impacted Owners
7. Risk Summary
8. Recommended Next Actions

## Quality Checks

- Impacted areas are explicitly identified.
- Traceability is used where available.
- Owners and next actions are visible.
- Major changes do not proceed without impact assessment.

## Stop Conditions

- The change scope is missing or ambiguous.
- The user asks to bypass impact assessment for a major change.

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

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
