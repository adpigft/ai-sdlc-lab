---
name: artifact-review
description: Review AI-generated artifact quality before human approval.
---

# Artifact Review Skill

## Purpose

Review the quality of an AI-generated artifact before human approval.

## When To Use

Use `$artifact-review` when intent, specification, design, test-design, implementation-plan, PR review, validation report, release notes, or decision records need quality review.

## Inputs Needed

- Artifact under review
- Artifact type
- Relevant approved upstream artifacts
- Quality checklist
- Known approval criteria

## Framework Adapter

When this skill is used inside this repository, context loading, review expectations, and human approval expectations are defined by:

- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/01-lifecycle/skill-orchestration-adapter.md`

## Procedure

1. Identify the artifact type and review scope.
2. Compare the artifact against approved upstream inputs and checklist criteria.
3. Check completeness, correctness, traceability, consistency, risk, and missing information.
4. Recommend corrections or approval readiness.
5. Stop for human review before treating the artifact as approved.

## Outputs Produced

- Review findings
- Missing information list
- Required changes list
- Approval readiness recommendation

## Artifact Structure

1. Review Scope
2. Completeness Findings
3. Correctness Findings
4. Traceability Findings
5. Consistency Findings
6. Risk Findings
7. Missing Information
8. Recommendation
9. Required Changes
10. Approval Readiness

## Quality Checks

- Review scope is explicit.
- Findings are separated from recommendations.
- Missing information is visible.
- Approval readiness is conservative.
- AI does not approve artifacts.

## Stop Conditions

- The artifact type is unclear.
- Required upstream artifacts are missing.
- The user asks for approval instead of review.

## Human Approval Expectations

Human approval is required after review; AI can recommend readiness but cannot approve.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
