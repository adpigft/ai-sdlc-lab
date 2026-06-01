---
name: change
description: User-friendly orchestration for change requests using impact analysis and targeted artifact updates.
---

# Change Request Skill

## Purpose
Handle change requests without regenerating the full solution, while keeping impacted artifacts, approvals, and traceability controlled.

## When to use
Use `$change` when an approved or in-flight capability needs a scoped change to behavior, rules, APIs, tests, implementation, or release scope.

## Inputs
- Change request summary
- Existing capability or artifact references
- Reason for change
- Impact deadline or release target
- Optional Jira change, story, or stakeholder reference

## Process
1. Perform change impact analysis within this orchestration skill.
2. Identify impacted intent, specification, architecture, API, tests, code, traceability, validation, and release artifacts.
3. Confirm whether Jira Stories or Tasks already exist and whether new work items are needed.
4. Summarize impact, risk, affected owners, and recommended update sequence.
5. Ask for approval before editing impacted artifacts.
6. Update only approved and impacted artifacts.
7. Route specialist work to `$intent`, `$specification`, `$architecture`, `$test-design`, `$implementation`, or `$validation` as needed.
8. Preserve existing approved content that is not impacted.

## Outputs
- Change impact summary
- List of impacted artifacts and owners
- Approval request for targeted updates
- Updated impacted artifacts only after approval
- Jira Story, Task, or Subtask guidance when appropriate

## Quality checks
- Full solution is not regenerated.
- Impact scope is explicit and reviewable.
- Updates are limited to approved impacted artifacts.
- Traceability changes are identified.
- Code changes are deferred until required upstream artifacts are approved.

## Human gate
Change impact and each artifact update require approval from the relevant owner before changes proceed.

## Next skill or next workflow step
Route to the first impacted specialist stage, then continue through validation and `$release` if release scope changes.

## Example usage
`$change Analyze change request: support partial refunds for approved QR refunds`
