---
name: context-extraction
description: Extract legacy context required for brownfield modernization.
---

# Context Extraction Skill

## Purpose

Extract the legacy context required to modernize an existing application without losing architecture, operational, integration, or security assumptions.

## When To Use

Use `$context-extraction` after specification extraction when the user needs the modernization-relevant context captured from the current system.

## Inputs Needed

- Discovery findings
- Recovered intent
- Current-state specification
- Architecture, deployment, integration, and operations evidence

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and lifecycle behavior are defined by:

- `framework/01-lifecycle/skill-orchestration-adapter.md`
- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/24-discovery-engineering/current-state-extraction-model.md`

## Procedure

1. Extract the legacy architecture, domain, capability, integration, operational, deployment, security, and data context.
2. Separate current-state context from any target-state recommendations.
3. Capture dependencies, constraints, and assumptions that must be preserved or deliberately changed.
4. Note any modernization-relevant risks or hidden coupling.
5. Stop before defining target-state architecture or implementation plans.

## Outputs Produced

- Legacy context summary
- Architecture context
- Domain context
- Capability context
- Integration context
- Operational context

## Artifact Structure

1. Legacy Context
2. Architecture Context
3. Domain Context
4. Capability Context
5. Integration Context
6. Operational Context
7. Constraints and Assumptions
8. Current-State vs Target-State Notes

## Quality Checks

- Legacy context is clearly distinguished from target-state recommendations.
- Stack, architecture style, dependencies, integrations, and deployment assumptions are captured.
- Security and operational constraints are visible.
- No source code is modified.

## Stop Conditions

- The user asks for target-state design instead of legacy context extraction.
- The source material is insufficient to describe the operational or architectural context safely.

## Human Approval Expectations

Human review is required before legacy context is used to drive gap analysis or target-state design decisions.

## Do Not

- Do not modify external systems unless explicitly approved.
- Do not create, update, delete, or transition Jira, Confluence, GitHub, Wynxx Story Creator, or source-code artifacts unless the skill explicitly allows it and the user approves.
- Do not expose secrets, tokens, credentials, or sensitive data.
- Do not fabricate missing requirements, evidence, source references, or approval status.
- Do not treat inferred content as confirmed fact.
- Do not bypass validation, traceability, approval, or stop-for-review rules.
- Do not create target-state recommendations unless explicitly requested.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
