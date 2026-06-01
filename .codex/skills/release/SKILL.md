---
name: release
description: User-friendly orchestration for validation evidence, release readiness, release notes, rollback, known risks, and approvals.
---

# Release Skill

## Purpose
Prepare release readiness evidence and coordinate approval without replacing GitHub Actions, validation, or human release gates.

## When to use
Use `$release` when a capability, change, or defect fix is ready for release readiness review or release management.

## Inputs
- Release scope
- Validation report and test evidence
- PR, build, CI, or GitHub Actions references
- Known risks and limitations
- Rollback and monitoring notes
- Jira release, version, or approval reference if available

## Process
1. Confirm validation evidence exists or route to `$validation`.
2. Assess release readiness against validation evidence, risks, and CI gates.
3. Use `devsecops-release` to prepare release notes, rollback, monitoring checks, and approval evidence.
4. Confirm GitHub Actions status remains authoritative for CI gates.
5. Record known risks, operational readiness, rollback, and support handoff.
6. Stop for PO, QA, Architect, and DevSecOps approval.

## Outputs
- Release readiness summary
- Release notes
- Rollback plan
- Known risks and limitations
- Approval evidence checklist

## Quality checks
- Validation evidence is complete or explicitly blocked.
- CI gate status is referenced.
- Rollback and monitoring are practical.
- Known risks are visible.
- Required release approvers are identified.

## Human gate
PO, QA, Architect, and DevSecOps approval is required before release.

## Next skill or next workflow step
Use `feedback` or production feedback capture after release.

## Example usage
`$release Prepare release readiness for QR refund pilot`
