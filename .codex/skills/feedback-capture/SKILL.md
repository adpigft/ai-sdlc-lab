---
name: feedback-capture
description: Capture findings, stakeholder feedback, defects, change requests, risks, and lessons learned as controlled follow-up.
---

# Feedback Capture Skill

## Purpose

Capture feedback and convert it into traceable, owner-approved corrections or follow-up actions.

## When To Use

Use `$feedback-capture` whenever review findings, stakeholder feedback, defects, change requests, risks, release lessons, or improvement ideas are received.

## Inputs Needed

- Feedback source and date
- Feedback summary
- Affected artifact, feature, capability, domain, component, or release
- Severity, priority, or business impact where known
- Owner or impacted stakeholder where known

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and feedback log location are defined by:

- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/01-lifecycle/skill-orchestration-adapter.md`

## Procedure

1. Record the feedback item.
2. Classify it as clarification, review finding, defect, change request, risk, improvement, or lesson learned.
3. Identify affected artifacts, owners, approvals, and traceability impact.
4. Propose targeted corrections or follow-up actions.
5. Ask for owner approval before applying corrections.
6. Apply only approved targeted changes.
7. Update traceability or follow-up references where required.

## Outputs Produced

- Feedback entry or feedback summary
- Classification and owner
- Impacted artifact or scope list
- Proposed correction or follow-up plan
- Traceability impact where applicable

## Example Output

- Classification: `defect`
- Owner: `QA`
- Follow-up: `raise change request`

## Artifact Structure

1. Feedback Source
2. Summary
3. Classification
4. Impacted Areas
5. Owner
6. Proposed Follow-up
7. Status
8. Traceability Impact

## Quality Checks

- Feedback has source, owner, status, and impact.
- Affected artifacts or scope are identified.
- Corrections are targeted and traceable.
- Customer-sensitive details are masked.
- No unrelated rewrite is performed.

## Stop Conditions

- Feedback source or impacted scope is unclear.
- Owner approval is missing for corrections.
- Feedback requires change-request or defect-fix handling before edits.
- Customer-sensitive details cannot be safely captured.

## Human Approval Expectations

Artifact owner approval is required before corrections are applied. Customer, risk, security, or release owners may be required depending on impact.

## Do Not

- Do not modify external systems unless explicitly approved.
- Do not create, update, delete, or transition Jira, Confluence, GitHub, Wynxx Story Creator, or source-code artifacts unless the skill explicitly allows it and the user approves.
- Do not expose secrets, tokens, credentials, or sensitive data.
- Do not fabricate missing requirements, evidence, source references, or approval status.
- Do not treat inferred content as confirmed fact.
- Do not bypass validation, traceability, approval, or stop-for-review rules.
- Do not perform unrelated rewrites.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
