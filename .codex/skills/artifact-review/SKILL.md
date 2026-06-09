---
name: artifact-review
description: Review AI-generated artifact quality before human approval.
---

# Artifact Review Skill

## Purpose

Review the quality of an AI-generated artifact before human approval.

## When To Use

Use `$artifact-review` when intent, requirements, design, test design, implementation plan, PR review, validation report, release notes, decision records, or brownfield readiness artifacts need quality review.

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
3. Review artifact quality, evidence quality, traceability quality, cross-artifact consistency, completeness, business-rule coverage, dependency impact, and readiness for the next phase.
4. Identify strengths, weaknesses, risks, and recommendations.
5. Produce a go/no-go recommendation and a readiness score.
6. Stop for human review before treating the artifact as approved.

## Outputs Produced

- Strengths
- Weaknesses
- Risks
- Recommendations
- Go/no-go recommendation
- Readiness score

## Example Output

- Review Scope: `intent/intent.md`
- Strengths: `clear scope boundary`
- Weaknesses: `missing target operating model detail`
- Risks: `unresolved policy decision`
- Recommendation: `changes required`
- Go/No-Go: `no-go`
- Readiness Score: `62/100`

## Artifact Structure

1. Review Scope
2. Strengths
3. Weaknesses
4. Evidence Quality
5. Traceability Quality
6. Cross-Artifact Consistency
7. Completeness
8. Business-Rule Coverage
9. Dependency Impact
10. Readiness for Next Phase
11. Risks
12. Recommendations
13. Go/No-Go Recommendation
14. Readiness Score

## Quality Checks

- Review scope is explicit.
- Findings are separated from recommendations.
- Evidence quality is visible.
- Readiness for the next phase is explicit.
- AI does not approve artifacts.

## Stop Conditions

- The artifact type is unclear.
- Required upstream artifacts are missing.
- The user asks for approval instead of review.

## Human Approval Expectations

Human approval is required after review; AI can recommend readiness but cannot approve itself.

## Do Not

- Do not modify external systems unless explicitly approved.
- Do not create, update, delete, or transition Jira, Confluence, GitHub, Wynxx Story Creator, or source-code artifacts unless the skill explicitly allows it and the user approves.
- Do not expose secrets, tokens, credentials, or sensitive data.
- Do not fabricate missing requirements, evidence, source references, or approval status.
- Do not treat inferred content as confirmed fact.
- Do not bypass validation, traceability, approval, or stop-for-review rules.
- Do not approve artifacts automatically.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
