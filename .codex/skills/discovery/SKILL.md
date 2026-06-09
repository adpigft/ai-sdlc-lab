---
name: discovery
description: Analyze an existing application or repository in read-only mode to extract current-state understanding.
---

# Discovery Skill

## Purpose

Analyze an existing application or repository in read-only mode and extract current-state understanding that can support greenfield bootstrap, brownfield modernization, or repository analysis.

## When To Use

Use `$discovery` when the user needs a current-state baseline from an existing system, whether the source is an application, service, repository, or delivery context.

## Inputs Needed

- Source application or repository path
- Scope of analysis
- Technology stack hints, if available
- Target discovery outputs
- Known constraints or boundaries
- Mode hint, when the user wants greenfield bootstrap, brownfield modernization, or repository standards discovery

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and lifecycle behavior are defined by:

- `framework/01-lifecycle/skill-orchestration-adapter.md`
- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/24-discovery-engineering/discovery-engineering-model.md`

## Procedure

1. Inspect the source in read-only mode.
2. Identify architecture, inventory, APIs, data model, business rules, integrations, deployment assumptions, technical debt, state machines, and technology stack.
3. Produce or consider the required discovery artifacts, including quick-scan, business-rules catalog, application inventory, architecture overview, API inventory, data model, state machine, integration inventory, domain decomposition, technical debt, current-state discovery, and discovery evidence.
4. Separate evidence from inference.
5. Separate current-state facts from target-state thinking.
6. Cite file paths, classes, functions, endpoints, configuration, or docs as evidence where possible.
7. Document discovery limitations explicitly.
8. Stop before creating target-state artifacts, implementation plans, or code changes.

## Outputs Produced

- Current-state discovery summary
- Quick scan
- Business rules catalog
- Architecture overview
- Application inventory
- API inventory
- Data model summary
- State machine summary
- Integration inventory
- Domain decomposition
- Technical debt summary
- Discovery evidence

## Artifact Structure

1. Quick Scan
2. Business Rules Catalog
3. Application Inventory
4. Architecture Overview
5. API Inventory
6. Data Model
7. State Machine
8. Integration Inventory
9. Domain Decomposition
10. Technical Debt
11. Current-State Discovery
12. Discovery Evidence
13. Evidence and Inference
14. Limitations
15. Unknowns

## Quality Checks

- Findings are grounded in inspected files or observable behavior.
- Evidence is separated from inference.
- Current-state and target-state thinking are clearly separated.
- Discovery limitations are explicit.
- No source code is modified.
- No target-state artifacts are created.

## Stop Conditions

- Source path is missing.
- The user asks for target-state design instead of discovery.
- The analysis would require modifying source application files.

## Human Approval Expectations

Human review is required before discovery outputs become the basis for modernization readiness, intent, requirements, design, gap analysis, or impact analysis.

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
