---
name: release
description: Prepare release readiness evidence, release notes, rollback, monitoring, risks, and approvals.
---

# Release Skill

## Purpose

Prepare release readiness evidence and make release blockers, risks, approvals, rollback, monitoring, and support needs explicit.

## When To Use

Use `$release` when validated scope is ready for release readiness review or release management.

## Inputs Needed

- Release scope
- Validation report and test evidence
- CI, build, security, quality, or deployment evidence
- Known risks, limitations, and waivers
- Rollback, monitoring, smoke test, and support notes
- Required approval references where available

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and lifecycle behavior are defined by:

- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/01-lifecycle/skill-orchestration-adapter.md`

## Procedure

1. Confirm validation evidence exists and does not block release.
2. Confirm release scope and excluded scope.
3. Review CI, security, quality, operational, and deployment readiness evidence.
4. Define rollback approach, monitoring checks, smoke checks, known risks, and support handoff.
5. Record release blockers or partial/non-production constraints when applicable.
6. Prepare release notes or release readiness summary.
7. Stop for required release approvals before claiming release approval.

## Outputs Produced

- Release readiness summary
- Release notes or release package evidence
- Rollback and monitoring plan
- Known risks, limitations, and support handoff notes
- Approval checklist and blocker summary

## Example Output

- Scope: `feature release`
- Status: `not ready`
- Blockers: `missing validation evidence`

## Artifact Structure

1. Scope
2. Changes Included
3. Validation Evidence
4. Deployment Approach
5. Risks
6. Rollback Plan
7. Monitoring & Smoke Checks
8. Approval Status

## Quality Checks

- Validation evidence supports the release claim.
- CI, quality, and security gate status is visible.
- Rollback and monitoring are practical.
- Known risks and exclusions are explicit.
- Required approvers are identified.
- Release approval is not claimed without human approval.

## Stop Conditions

- Validation says release is not ready.
- Release notes, CI/security/quality evidence, rollback, monitoring, or approval package is missing.
- Remaining slices or scope are not validated unless explicitly marked as partial/non-production release.
- Release evidence conflicts with validation or traceability.

## Human Approval Expectations

PO, QA, Architect, DevSecOps, and any required operational owners must approve before production release.

## Do Not

- Do not modify external systems unless explicitly approved.
- Do not create, update, delete, or transition Jira, Confluence, GitHub, Wynxx Story Creator, or source-code artifacts unless the skill explicitly allows it and the user approves.
- Do not expose secrets, tokens, credentials, or sensitive data.
- Do not fabricate missing requirements, evidence, source references, or approval status.
- Do not treat inferred content as confirmed fact.
- Do not bypass validation, traceability, approval, or stop-for-review rules.
- Do not execute releases.
- Do not create tags, deployments, or production changes.
- Do not claim release readiness without traceability and validation evidence.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
