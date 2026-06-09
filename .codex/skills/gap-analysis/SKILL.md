---
name: gap-analysis
description: Compare current-state discovery with target requirements and design to identify modernization gaps.
---

# Gap Analysis Skill

## Purpose

Compare current-state discovery artifacts with approved target requirements and solution design to identify modernization gaps, including confirmed, assumption-based, and deferred gaps.

## When To Use

Use `$gap-analysis` after discovery, intent definition, requirements definition, and solution design when the user needs a structured modernization delta.

## Inputs Needed

- Current-state discovery
- Approved intent
- Approved requirements
- Solution design
- Target-state goals or constraints
- Current-state evidence

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and lifecycle behavior are defined by:

- `framework/01-lifecycle/skill-orchestration-adapter.md`
- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/24-discovery-engineering/brownfield-modernization-flow.md`

## Procedure

1. Compare current-state discovery artifacts with approved target artifacts.
2. Identify business, capability, architecture, data, API, business-rule, operational, and implementation-readiness gaps.
3. Classify each gap as confirmed, assumption-based, or deferred.
4. Separate capability, architecture, data, API, business-rule, operational, and implementation-readiness perspectives.
5. Capture modernization risks and assumptions.
6. Stop before creating an implementation plan.

## Outputs Produced

- Gap analysis summary
- Capability gap analysis
- Architecture gap analysis
- Data gap analysis
- API gap analysis
- Business rule gap analysis
- Operational gap analysis
- Implementation readiness gaps
- Gap traceability

## Artifact Structure

1. Gap Analysis
2. Capability Gap Analysis
3. Architecture Gap Analysis
4. Data Gap Analysis
5. API Gap Analysis
6. Business Rule Gap Analysis
7. Operational Gap Analysis
8. Implementation Readiness Gaps
9. Confirmed Gaps
10. Assumption-Based Gaps
11. Deferred Gaps
12. Gap Traceability

## Quality Checks

- Gaps are categorized consistently.
- Confirmed, assumption-based, and deferred gaps are separated.
- Architecture, data, API, business-rule, and operational perspectives are visible.
- No implementation plan is created.

## Stop Conditions

- Target-state artifacts are missing or too vague to compare.
- The user asks for implementation planning instead of gap analysis.

## Human Approval Expectations

Human review is required before gap analysis is used to justify target-state requirements, design, or implementation work.

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
