---
name: requirements
description: Convert approved intent into testable requirements for greenfield or brownfield delivery.
---

# Requirements Skill

## Purpose

Turn approved intent into clear, testable requirements. In this framework, requirements means requirements.

## When To Use

Use `$requirements` after intent is approved and before design, test design, implementation, validation, or release work depends on the scope.

## Inputs Needed

- Approved intent
- Business policies and rules
- Stakeholder clarifications
- Domain standards and constraints
- Known integrations, data needs, risks, or compliance obligations
- Open questions from intent discovery
- Mode hint for greenfield or brownfield delivery when relevant

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and lifecycle behavior are defined by:

- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/01-lifecycle/skill-orchestration-adapter.md`
- `framework/24-discovery-engineering/current-state-extraction-model.md`

## Procedure

1. Confirm the intent is approved.
2. Derive functional requirements from approved scope.
3. Derive non-functional requirements from risk, policy, security, performance, availability, audit, and operational needs.
4. Define business rules, acceptance criteria, edge cases, and error/failure expectations.
5. Identify data needs, integration assumptions, and open questions.
6. Keep requirements independent of implementation design unless the business rule requires a specific constraint.
7. Support brownfield mode when current-state discovery and target-state refinement are needed.
8. Stop for BA / PO review before downstream work relies on the requirements.

## Outputs Produced

- Requirements artifact containing FRs, NFRs, business rules, acceptance criteria, edge cases, assumptions, dependencies, and open questions
- Traceability-ready requirement identifiers where the framework needs them
- Review request for BA / PO approval

## Artifact Structure

1. Overview
2. Functional Requirements
3. Non-Functional Requirements
4. Business Rules
5. Acceptance Criteria
6. Edge Cases
7. Dependencies
8. Assumptions
9. Open Questions

## Quality Checks

- Requirements are testable and unambiguous.
- Acceptance criteria are measurable.
- NFRs are explicit.
- Business rules and edge cases are captured.
- Open questions are visible and assigned where possible.
- The requirements do not generate design, tests, or code prematurely.

## Stop Conditions

- Intent approval is missing.
- Material requirement inputs are missing.
- Open questions block requirement definition.
- The user asks to skip approval and proceed downstream.

## Human Approval Expectations

BA / PO approval is required before design, test design, implementation, validation, or release work depends on the requirements.

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
