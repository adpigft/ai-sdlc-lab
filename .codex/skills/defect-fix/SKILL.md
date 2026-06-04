---
name: defect-fix
description: User-friendly orchestration for bugs and defects using defect analysis, root cause analysis, and targeted fixes.
---

# Defect Skill

## Purpose
Analyze and resolve bugs or defects through controlled root cause classification and targeted correction.

## When to use
Use `$defect-fix` when users report incorrect behavior, failed validation, escaped defects, production issues, or test failures tied to a product capability.

## Inputs
- Defect ID
- Defect summary
- Observed behavior and expected behavior
- Environment, build, or release reference
- Logs, screenshots, test evidence, or reproduction steps
- Domain context, such as `domains/<domain>/domain-context.md`, when available
- Related Jira issue or incident reference if available

## Context pack
Use the `Defect Fix` pack in `framework/02-context-control/context/stage-context-packs.md`.

Required reads:
- This skill document.
- Defect report or user evidence.
- Active domain context.
- Impacted feature artifacts.
- Active `workflow-state.yaml` when the capability exists.
- Placement guidance for code-impacting fixes.

Optional reads:
- Source and tests only after RCA identifies code impact and approved impacted paths.
- Traceability, validation report, and feedback log.

Forbidden reads:
- Unrelated source, unrelated capabilities, and restricted paths without approval.

Escalation rule: Read impacted paths only after RCA maps the defect to owner, allowed paths, impacted tests, and regression scope.

Token discipline rule: Keep context to evidence, RCA, impacted artifacts, and approved impacted paths; full framework reads are allowed only for framework assessment or framework changes.

Stop conditions:
- Defect evidence is insufficient for RCA.
- Owner or allowed paths are missing for code-impacting fixes.
- An upstream artifact gap must be resolved before code changes.

## Process
1. Require or assign a Defect ID before RCA.
2. Read `domains/<domain>/domain-context.md` when the domain is known and the file exists.
3. Perform defect analysis within this orchestration skill.
4. Classify the root cause as requirement, architecture, design, code, test, or operational issue.
5. Identify impacted artifacts and whether upstream approvals are missing or obsolete.
6. Map the defect to the owning squad, allowed paths, impacted tests, and regression scope when code may be impacted.
7. Identify required validation evidence and regression coverage.
8. Identify traceability impact and feedback entry impact.
9. Recommend a targeted correction path.
10. Ask for approval before updating artifacts, tests, code, validation evidence, or release notes.
11. Apply only approved targeted fixes.
12. Update traceability and create or update the feedback entry after approval.
13. Update or prepare `workflow-state.yaml` after approvals when workflow-state is adopted.
14. Route to `$validation` for QA evidence after correction.

## Placement metadata
For any code-impacting defect fix, RCA must check or produce:

- `target_app`, if frontend is impacted
- `target_frontend_module`, if frontend is impacted
- `target_service`, if backend is impacted
- `target_library`, if shared library is impacted
- `owning_squad`
- `allowed_paths`
- `restricted_paths`
- `required_approvals`
- `impacted_capabilities`
- `regression_scope`

Defect fixes must map the defect to the responsible owner, impacted tests, and regression scope. If `allowed_paths` or `restricted_paths` are missing for a code fix, stop for architecture or implementation planning before editing code.

## Outputs
- Defect analysis summary
- Defect ID
- Root cause classification
- Impacted artifact list
- Targeted correction plan
- Validation and release evidence needs
- Traceability impact summary
- Feedback entry requirement

## Quality checks
- Root cause is classified before fixes are made.
- Requirement, architecture, test, operational, and code causes are considered.
- Fixes do not bypass missing upstream approval.
- Corrections are targeted and traceable.
- Regression and negative test needs are identified.
- Code-impacting fixes identify owner, allowed paths, impacted tests, and regression scope.
- Validation evidence is identified before closure.
- Feedback entry is created or explicitly marked not required.
- Domain context was reviewed when available.

## Human gate
The root cause and correction path require owner approval before artifacts or code are changed.

## Next skill or next workflow step
Use the impacted specialist skill, then `$validation`, then `$release` if the fix is release-bound.

## Example usage
`$defect-fix Analyze defect: duplicate refund created when retrying failed QR refund`
