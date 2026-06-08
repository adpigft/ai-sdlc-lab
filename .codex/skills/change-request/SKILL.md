---
name: change-request
description: Analyze a scoped change request and update only impacted artifacts or implementation with approval.
---

# Change Request Skill

## Purpose

Handle change requests through impact analysis and targeted updates without regenerating the whole solution.

## When To Use

Use `$change-request` when approved or in-flight scope needs a controlled change to behavior, rules, APIs, events, tests, implementation, validation, or release scope.

## Inputs Needed

- Change ID or change summary
- Reason for change
- Affected capability, feature, artifact, component, or release scope
- Desired outcome and deadline, if any
- Known business, technical, owner, or regulatory constraints
- Evidence, stakeholder reference, or work-management reference when available

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, impact routing, approval gates, and path governance are defined by:

- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/03-delivery-governance/service-architecture/implementation-placement-model.md`
- `framework/01-lifecycle/skill-orchestration-adapter.md`

## Procedure

1. Require or assign a change ID.
2. Perform impact analysis before editing artifacts or code.
3. Identify impacted requirements, design, contracts, tests, implementation, traceability, validation, release, owners, and approvals.
4. Identify placement, owner, and regression impact for code-impacting changes.
5. Summarize impact, risks, affected owners, and recommended update sequence.
6. Ask for approval before updating impacted artifacts or code.
7. Update only approved impacted areas.
8. Preserve approved content that is not impacted.
9. Capture traceability and feedback impacts where the framework requires them.

## Outputs Produced

- Change impact summary
- Change ID
- Impacted artifact, owner, path, and approval list
- Targeted correction or update plan
- Traceability, feedback, validation, and release impact summary

## Artifact Structure

1. Request Summary
2. Impact Analysis
3. Impacted Artifacts
4. Owners and Approvals
5. Proposed Changes
6. Risks
7. Follow-up Actions

## Quality Checks

- Full solution is not regenerated.
- Impact scope is explicit and reviewable.
- Updates are limited to approved impacted areas.
- Owner and approval impacts are identified.
- Code-impacting changes include placement, path, test, and regression impact where applicable.

## Stop Conditions

- Change ID or change scope is unclear.
- Impacted owners cannot be identified.
- Approval is missing for artifact or code changes.
- Required placement, path, or regression scope is missing for code-impacting changes.

## Human Approval Expectations

Change impact and each artifact or code update require approval from the relevant owner before changes proceed.

## Do Not

- Do not modify external systems unless explicitly approved.
- Do not create, update, delete, or transition Jira, Confluence, GitHub, Wynxx Story Creator, or source-code artifacts unless the skill explicitly allows it and the user approves.
- Do not expose secrets, tokens, credentials, or sensitive data.
- Do not fabricate missing requirements, evidence, source references, or approval status.
- Do not treat inferred content as confirmed fact.
- Do not bypass validation, traceability, approval, or stop-for-review rules.
- Do not change code outside approved scope.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
