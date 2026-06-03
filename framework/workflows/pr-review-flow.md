# PR Review Flow

## Purpose

Define the lightweight pull request review stage between implementation and validation.

PR review checks whether an implemented slice is ready for QA validation. It does not replace human review, GitHub Actions, CI, CODEOWNERS approval, security review, or validation.

## When To Use

Use `$pr-review` after implementation evidence or a pull request exists and before `$validation`.

## Required Inputs

- PR reference or implementation slice reference
- changed files
- approved implementation plan
- placement metadata
- `allowed_paths`
- `restricted_paths`
- relevant test output
- validation script output, if available
- traceability references

## Required Checks

PR review must check:

- changed files
- `allowed_paths`
- `restricted_paths`
- coding standards
- security standards where relevant
- architecture adherence
- API compatibility
- event compatibility
- test coverage
- validation scripts
- traceability

## Review Procedure

1. Identify active domain, capability, implementation slice, and PR reference.
2. Read changed files list before reading source content.
3. Confirm every changed file is inside approved `allowed_paths`.
4. Confirm no changed file is inside `restricted_paths` without required approval.
5. Read only changed source/test files and directly relevant standards, contracts, schemas, tests, and traceability rows.
6. Check coding, testing, security, and architecture standards.
7. Check API and event compatibility when contracts, schemas, handlers, producers, or consumers are impacted.
8. Check that tests cover changed behavior and known edge cases.
9. Run or review validation scripts where applicable.
10. Check traceability from implementation to approved requirements, test scenarios, and validation evidence.
11. Return findings ordered by severity.
12. Stop before validation if blockers remain.

## Recommendation Outcomes

Use one of these outcomes:

- `Ready for human PR review`
- `Changes required`
- `Blocked`

Do not use `Approved` unless a human explicitly approves.

## Stop Conditions

Stop and report blockers when:

- changed files are unavailable
- placement metadata is missing
- `allowed_paths` or `restricted_paths` are missing
- a changed file is outside `allowed_paths`
- a changed file touches `restricted_paths` without approval
- required tests are missing
- validation scripts fail
- API or event compatibility is broken
- traceability is missing or inconsistent
- workflow state, validation evidence, traceability, or release evidence disagree

## Standard Response

Use `framework/prompt-patterns/standard-response-format.md`.

For reviews with issues, include:

```text
Findings:
- ...

Validation:
- ...

Blockers:
- ...

Next:
- ...
```

