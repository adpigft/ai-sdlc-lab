---
name: discovery-engineering
description: Analyze an existing application and extract current-state understanding without modifying source code.
---

# Discovery Engineering Skill

## Purpose

Analyze an existing application in read-only mode and extract current-state understanding that can seed brownfield modernization work.

## When To Use

Use `$discovery-engineering` when the user needs a current-state baseline from an existing system before intent extraction, specification extraction, context extraction, gap analysis, or impact analysis.

## Inputs Needed

- Source application path or repository
- Scope of analysis
- Technology stack hints, if available
- Target discovery outputs
- Known constraints or boundaries

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and lifecycle behavior are defined by:

- `framework/01-lifecycle/skill-orchestration-adapter.md`
- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/24-discovery-engineering/discovery-engineering-model.md`

## Procedure

1. Inspect the source application in read-only mode.
2. Identify architecture, application inventory, APIs, data model, business rules, integrations, deployment assumptions, and technology stack.
3. Separate code-evidenced facts from AI inference.
4. Cite file paths, classes, functions, endpoints, configuration, or docs as evidence where possible.
5. Summarize current-state understanding in the requested discovery artifacts.
6. Flag gaps, uncertainties, and assumptions explicitly.
7. Stop before creating any target-state artifacts, implementation plans, or code changes.

## Outputs Produced

- Current-state discovery summary
- Architecture overview
- Application inventory
- API inventory
- Data model summary
- Business rules summary
- Integration map
- Technology stack summary

## Artifact Structure

1. Repository / Application Overview
2. Architecture Overview
3. Application Inventory
4. API Inventory
5. Data Model
6. Business Rules
7. Integration Map
8. Technology Stack
9. Evidence and Inference
10. Gaps and Unknowns

## Quality Checks

- Findings are grounded in inspected files or observable behavior.
- Evidence is separated from inference.
- Scope boundaries are explicit.
- No source code is modified.
- No target-state artifacts are created.

## Stop Conditions

- Source path is missing.
- The user asks for target-state design instead of discovery.
- The analysis would require modifying source application files.

## Human Approval Expectations

Human review is required before discovery outputs become the basis for intent extraction, specification extraction, or modernization decisions.

## Do Not

- Do not modify external systems unless explicitly approved.
- Do not create, update, delete, or transition Jira, Confluence, GitHub, Wynxx Story Creator, or source-code artifacts unless the skill explicitly allows it and the user approves.
- Do not expose secrets, tokens, credentials, or sensitive data.
- Do not fabricate missing requirements, evidence, source references, or approval status.
- Do not treat inferred content as confirmed fact.
- Do not bypass validation, traceability, approval, or stop-for-review rules.
- Do not change source code.
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
