---
name: change-request
description: User-friendly orchestration for change requests using impact analysis and targeted artifact updates.
---

# Change Request Skill

## Purpose
Handle change requests without regenerating the full solution, while keeping impacted artifacts, approvals, and traceability controlled.

## When to use
Use `$change-request` when an approved or in-flight capability needs a scoped change to behavior, rules, APIs, tests, implementation, or release scope.

## Inputs
- Change ID
- Change request summary
- Existing capability or artifact references
- Reason for change
- Impact deadline or release target
- Domain context, such as `domains/<domain>/domain-context.md`, when available
- Optional Jira change, story, or stakeholder reference

## Process
1. Require or assign a Change ID before impact analysis.
2. Read `domains/<domain>/domain-context.md` when the domain is known and the file exists.
3. Perform change impact analysis within this orchestration skill.
4. Identify impacted intent, specification, architecture, API, tests, code, traceability, validation, release, and feedback artifacts.
5. Confirm whether Jira Stories or Tasks already exist and whether new work items are needed.
6. Summarize impact, risk, affected owners, traceability impact, feedback entry impact, and recommended update sequence.
7. Ask for approval before editing impacted artifacts.
8. Update only approved and impacted artifacts.
9. Update traceability and create or update the feedback entry after approval.
10. Update or prepare `workflow-state.yaml` after approvals when workflow-state is adopted.
11. Route specialist work to `$intent`, `$specification`, `$architecture`, `$test-design`, `$implementation`, or `$validation` as needed.
12. Preserve existing approved content that is not impacted.

## Outputs
- Change impact summary
- Change ID
- List of impacted artifacts and owners
- Traceability impact summary
- Feedback entry requirement
- Approval request for targeted updates
- Updated impacted artifacts only after approval
- Jira Story, Task, or Subtask guidance when appropriate

## Quality checks
- Full solution is not regenerated.
- Impact scope is explicit and reviewable.
- Updates are limited to approved impacted artifacts.
- Traceability changes are identified.
- Feedback entry is created or explicitly marked not required.
- Required approvals are identified by artifact owner.
- Domain context was reviewed when available.
- Code changes are deferred until required upstream artifacts are approved.

## Human gate
Change impact and each artifact update require approval from the relevant owner before changes proceed.

## Next skill or next workflow step
Route to the first impacted specialist stage, then continue through validation and `$release` if release scope changes.

## Example usage
`$change-request Analyze change request: support partial refunds for approved QR refunds`
