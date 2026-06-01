---
name: defect
description: User-friendly orchestration for bugs and defects using defect analysis, root cause analysis, and targeted fixes.
---

# Defect Skill

## Purpose
Analyze and resolve bugs or defects through controlled root cause classification and targeted correction.

## When to use
Use `$defect` when users report incorrect behavior, failed validation, escaped defects, production issues, or test failures tied to a product capability.

## Inputs
- Defect summary
- Observed behavior and expected behavior
- Environment, build, or release reference
- Logs, screenshots, test evidence, or reproduction steps
- Related Jira issue or incident reference if available

## Process
1. Perform defect analysis within this orchestration skill.
2. Classify the root cause as requirement, architecture, design, code, test, or operational issue.
3. Identify impacted artifacts and whether upstream approvals are missing or obsolete.
4. Recommend a targeted correction path.
5. Ask for approval before updating artifacts, tests, code, validation evidence, or release notes.
6. Apply only approved targeted fixes.
7. Route to `$validation` for QA evidence after correction.

## Outputs
- Defect analysis summary
- Root cause classification
- Impacted artifact list
- Targeted correction plan
- Validation and release evidence needs

## Quality checks
- Root cause is classified before fixes are made.
- Requirement, architecture, test, operational, and code causes are considered.
- Fixes do not bypass missing upstream approval.
- Corrections are targeted and traceable.
- Regression and negative test needs are identified.

## Human gate
The root cause and correction path require owner approval before artifacts or code are changed.

## Next skill or next workflow step
Use the impacted specialist skill, then `$validation`, then `$release` if the fix is release-bound.

## Example usage
`$defect Analyze defect: duplicate refund created when retrying failed QR refund`
