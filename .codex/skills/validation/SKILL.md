---
name: validation
description: QA-owned validation execution and evidence entry point producing validation report and release readiness evidence.
---

# Validation Skill

## Purpose
Execute QA validation and capture evidence needed for release readiness.

## When to use
Use `$validation` after implementation and PR review are ready for QA or when release evidence must be assembled.

## Inputs
- Approved requirements, design, tests, and traceability
- Implemented code or PR reference
- Test execution results
- CI and GitHub Actions references
- Defect, risk, or waiver information

## Context pack
Use the `Validation` pack in `framework/02-context-control/context/stage-context-packs.md`.

Required reads:
- This skill document.
- Active `workflow-state.yaml`.
- Validation report.
- Approved tests.
- Implementation evidence.
- Traceability matrix.
- Approved requirements and architecture as needed.

Optional reads:
- Source and tests inside implemented paths.
- CI logs, command output, and security/testing/NFR standards.

Forbidden reads:
- Unrelated source paths and unrelated capabilities unless regression scope requires them.

Escalation rule: Read additional capability or code paths only when regression scope, traceability gaps, or validation evidence require it.

Token discipline rule: Focus on evidence, mapped requirements, and implemented paths; full framework reads are allowed only for framework assessment or framework changes.

Stop conditions:
- Implementation evidence is missing.
- Tests cannot map to requirements.
- Release readiness is claimed without supporting evidence.

## Process
1. Confirm implementation and PR review are ready for validation.
2. Use `qa-validation` for QA validation and evidence capture.
3. Execute or review acceptance, regression, integration, security, and NFR evidence as applicable.
4. Compare results to approved requirements and traceability.
5. Record defects, waivers, risks, and blocked evidence.
6. Produce validation report and release readiness evidence.
7. When validation report or QA evidence summary is created or updated, create or update `domains/<domain>/capabilities/<capability>/features/<feature>/workflow-state.yaml`.
8. Set workflow state to `validation_ready`, current artifact to `validation/validation-report.md`, pending gate to `validation_approval`, next state to `release_ready`, and next skill to `release`.
9. Use `framework/01-lifecycle/workflow/workflow-state-guide.md` for state-aware `Review.`, `Approved.`, and `Status.` behavior.
10. Ask for QA approval before release readiness.

## Outputs
- Validation report
- Test execution evidence summary
- Defect and risk summary
- Release readiness evidence
- Created or updated `domains/**/features/**/workflow-state.yaml` after validation report creation

## Quality checks
- Evidence maps to approved requirements and tests.
- Failed, blocked, or waived tests are visible.
- Defects are linked to correction workflow.
- CI gate status is referenced where applicable.
- QA approval evidence is captured.
- Workflow state points `Review.` to validation evidence and `Approved.` to release readiness.

## Human gate
QA approval is required before `$release`.

## Next skill or next workflow step
Use `$release`.

## Example usage
`$validation Validate implemented QR refund idempotency slice`
