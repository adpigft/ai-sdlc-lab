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
- Defect ID
- Defect summary
- Observed behavior and expected behavior
- Environment, build, or release reference
- Logs, screenshots, test evidence, or reproduction steps
- Domain context, such as `domains/<domain>/domain-context.md`, when available
- Related Jira issue or incident reference if available

## Process
1. Require or assign a Defect ID before RCA.
2. Read `domains/<domain>/domain-context.md` when the domain is known and the file exists.
3. Perform defect analysis within this orchestration skill.
4. Classify the root cause as requirement, architecture, design, code, test, or operational issue.
5. Identify impacted artifacts and whether upstream approvals are missing or obsolete.
6. Identify required validation evidence and regression coverage.
7. Identify traceability impact and feedback entry impact.
8. Recommend a targeted correction path.
9. Ask for approval before updating artifacts, tests, code, validation evidence, or release notes.
10. Apply only approved targeted fixes.
11. Update traceability and create or update the feedback entry after approval.
12. Update or prepare `workflow-state.yaml` after approvals when workflow-state is adopted.
13. Route to `$validation` for QA evidence after correction.

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
- Validation evidence is identified before closure.
- Feedback entry is created or explicitly marked not required.
- Domain context was reviewed when available.

## Human gate
The root cause and correction path require owner approval before artifacts or code are changed.

## Next skill or next workflow step
Use the impacted specialist skill, then `$validation`, then `$release` if the fix is release-bound.

## Example usage
`$defect Analyze defect: duplicate refund created when retrying failed QR refund`
