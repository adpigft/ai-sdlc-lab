---
name: specification-extraction
description: Extract current-state functional and non-functional specifications from an existing application.
---

# Specification Extraction Skill

## Purpose

Extract the observable functional and non-functional specifications of an existing application so modernization work can preserve required behavior and constraints.

## When To Use

Use `$specification-extraction` after intent extraction when the user needs the current-state requirements surface captured from an existing system.

## Inputs Needed

- Discovery findings
- Recovered intent
- Behavior evidence, APIs, workflows, and documentation
- Known validation or acceptance evidence

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and lifecycle behavior are defined by:

- `framework/01-lifecycle/skill-orchestration-adapter.md`
- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/24-discovery-engineering/current-state-extraction-model.md`

## Procedure

1. Inspect the recovered intent and source evidence.
2. Extract functional requirements, non-functional requirements, acceptance criteria, business rules, and validation rules from current-state behavior.
3. Reference evidence where possible.
4. Mark inferred requirements clearly when direct evidence is unavailable.
5. Record gaps and uncertain requirements rather than hiding them.
6. Stop before creating target-state design or implementation artifacts.

## Outputs Produced

- Current-state specification summary
- Functional requirements
- Non-functional requirements
- Acceptance criteria
- Business rules
- Validation rules

## Artifact Structure

1. Current-State Specification
2. Functional Requirements
3. Non-Functional Requirements
4. Acceptance Criteria
5. Business Rules
6. Validation Rules
7. Evidence
8. Inferred Items
9. Gaps and Uncertainties

## Quality Checks

- Each recovered requirement cites evidence where possible.
- Inference is explicitly labeled.
- Missing behavior is called out as a gap.
- No target-state requirement is invented without labeling it as inferred.

## Stop Conditions

- Behavior evidence is insufficient to recover requirements safely.
- The user asks for target-state requirements instead of current-state extraction.

## Human Approval Expectations

Human review is required before recovered specifications drive target-state design, test design, implementation, or release planning.

## Do Not

- Do not modify external systems unless explicitly approved.
- Do not create, update, delete, or transition Jira, Confluence, GitHub, Wynxx Story Creator, or source-code artifacts unless the skill explicitly allows it and the user approves.
- Do not expose secrets, tokens, credentials, or sensitive data.
- Do not fabricate missing requirements, evidence, source references, or approval status.
- Do not treat inferred content as confirmed fact.
- Do not bypass validation, traceability, approval, or stop-for-review rules.
- Do not claim inferred requirements are business-approved.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
