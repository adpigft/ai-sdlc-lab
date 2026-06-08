---
name: pr-review
description: Review implementation or pull request readiness against changed files, approved scope, standards, tests, compatibility, and traceability.
---

# PR Review Skill

## Purpose

Review an implementation slice or pull request before validation. This skill checks readiness and risk; it does not replace human PR approval, CI, or release gates.

## When To Use

Use `$pr-review` after implementation evidence exists and before QA validation relies on the change.

## Inputs Needed

- PR reference, implementation slice reference, or changed file list
- Approved scope, design, and implementation plan
- Test and validation output, if available
- Coding, security, API, event, testing, and architecture standards
- Traceability references
- Placement or ownership constraints where the framework defines them

## Framework Adapter

When this skill is used inside this repository, context loading, report placement, allowed/restricted paths, approval gates, and lifecycle behavior are defined by:

- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/03-delivery-governance/service-architecture/implementation-placement-model.md`
- `framework/01-lifecycle/skill-orchestration-adapter.md`

## Procedure

1. Identify changed files and the approved slice or PR scope.
2. Check that changed files align with approved scope, ownership, and path constraints.
3. Review coding, security, testing, and architecture standards relevant to the change.
4. Check design adherence against approved requirements and design.
5. Check API and event compatibility for changed contracts, handlers, producers, or consumers.
6. Check test coverage for changed behavior, including negative, integration, security, and NFR coverage where applicable.
7. Run or review validation scripts where applicable.
8. Check traceability from changed implementation to approved requirements, tests, and evidence.
9. Report findings first, ordered by severity.
10. Recommend readiness, changes required, or blocked. Do not approve the PR yourself.

## Outputs Produced

- PR review findings
- Changed-file and scope assessment
- Standards, security, compatibility, test coverage, validation, and traceability assessment
- Recommendation for human reviewers
- Optional PR review evidence artifact when the framework asks for one

## Artifact Structure

1. Summary
2. Changed Files
3. Standards Compliance
4. Design Compliance
5. Test Coverage
6. Risks
7. Recommendation

## Quality Checks

- Changed files are explicit.
- Findings distinguish blockers from recommendations.
- Standards, design, tests, compatibility, and traceability are checked.
- Review does not modify source or business artifacts.
- AI does not claim human approval.

## Stop Conditions

- Changed files are unknown.
- Required implementation evidence is missing.
- Scope or ownership cannot be confirmed.
- Required path, API, event, traceability, or validation evidence disagrees.

## Human Approval Expectations

Human PR approval and impacted owner approvals are mandatory. AI may recommend readiness but cannot approve itself.

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
