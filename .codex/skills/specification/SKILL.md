---
name: specification
description: Convert approved intent into functional requirements, non-functional requirements, business rules, acceptance criteria, and edge cases.
---

# Specification Skill

## Purpose

Turn approved intent into clear, testable requirements. In this framework, specification means requirements.

## When To Use

Use `$specification` after intent is approved and before design, test design, implementation, validation, or release work depends on the scope.

## Inputs Needed

- Approved intent
- Business policies and rules
- Stakeholder clarifications
- Domain standards and constraints
- Known integrations, data needs, risks, or compliance obligations
- Open questions from intent discovery

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and lifecycle behavior are defined by:

- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/01-lifecycle/skill-orchestration-adapter.md`

## Procedure

1. Confirm the intent is approved.
2. Derive functional requirements from approved scope.
3. Derive non-functional requirements from risk, policy, security, performance, availability, audit, and operational needs.
4. Define business rules, acceptance criteria, edge cases, and error/failure expectations.
5. Identify data needs, integration assumptions, and open questions.
6. Keep requirements independent of implementation design unless the business rule requires a specific constraint.
7. Stop for BA / PO review before downstream work relies on the specification.

## Outputs Produced

- Specification artifact containing FRs, NFRs, business rules, acceptance criteria, edge cases, assumptions, dependencies, and open questions
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
- The specification does not generate design, tests, or code prematurely.

## Stop Conditions

- Intent approval is missing.
- Material requirement inputs are missing.
- Open questions block requirement definition.
- The user asks to skip approval and proceed downstream.

## Human Approval Expectations

BA / PO approval is required before design, test design, implementation, validation, or release work depends on the specification.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
