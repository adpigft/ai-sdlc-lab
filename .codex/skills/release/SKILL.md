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

## Context pack
Use the `Release` pack in `framework/02-context-control/context/stage-context-packs.md`.

Required reads:
- This skill document.
- Active `workflow-state.yaml`.
- Validation report.
- Traceability matrix.
- Release notes template.
- CI and quality evidence when code exists.

Optional reads:
- Implementation plan, feedback log, operational standards, and generated Jira/Confluence summaries.

Forbidden reads:
- Source code unless needed to verify release evidence.
- Unrelated capabilities.

Escalation rule: Read implementation or operational details only when release readiness evidence references them.

Token discipline rule: Keep context to validation, traceability, release evidence, and active capability risks; full framework reads are allowed only for framework assessment or framework changes.

Stop conditions:
- Validation says release is not ready.
- Release notes, CI/security/rollback/NFR evidence, or release approval is missing.

## Process
1. Confirm validation evidence exists or route to `$validation`.
2. Assess release readiness against validation evidence, risks, and CI gates.
3. Use `devsecops-release` to prepare release notes, rollback, monitoring checks, and approval evidence.
4. Confirm GitHub Actions status remains authoritative for CI gates.
5. Record known risks, operational readiness, rollback, and support handoff.
6. When release notes or release readiness evidence are created or updated, create or update `domains/<domain>/capabilities/<capability>/features/<feature>/workflow-state.yaml`.
7. Set workflow state to `release_ready`, current artifact to `release/release-notes.md`, pending gate to `release_approval`, next state to `released`, and next skill to `feedback-capture`.
8. Use `framework/01-lifecycle/workflow/workflow-state-guide.md` for state-aware `Review.`, `Approved.`, and `Status.` behavior.
9. Stop for PO, QA, Architect, and DevSecOps approval.

## Outputs
- Release readiness summary
- Release notes
- Rollback plan
- Known risks and limitations
- Approval evidence checklist
- Created or updated `domains/**/features/**/workflow-state.yaml` after release readiness artifact creation

## Quality checks
- Validation evidence is complete or explicitly blocked.
- CI gate status is referenced.
- Rollback and monitoring are practical.
- Known risks are visible.
- Required release approvers are identified.
- Workflow state points `Review.` to release readiness and `Approved.` to `released`.

## Human gate
PO, QA, Architect, and DevSecOps approval is required before release.

## Next skill or next workflow step
Use `feedback-capture` or production feedback capture after release.

## Example usage
`$release Prepare release readiness for QR refund pilot`
