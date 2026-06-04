---
name: pr-review
description: Review pull request readiness against changed files, allowed paths, standards, architecture, API/event compatibility, tests, validation scripts, and traceability before QA validation.
---

# PR Review Skill

## Purpose
Review an implementation slice or pull request before QA validation. This skill checks whether the change is ready to proceed without replacing human review, CI, GitHub Actions, or approval gates.

## When to use
Use `$pr-review` after implementation evidence exists and before `$validation`.

## Inputs
- PR reference or implementation slice reference
- Changed file list
- Approved implementation plan
- Placement metadata, including `allowed_paths` and `restricted_paths`
- Test and validation output, if available
- Traceability references

## Context pack
Use the `PR Review` pack in `framework/02-context-control/context/stage-context-packs.md`.

Required reads:
- This skill document.
- `framework/01-lifecycle/workflows/pr-review-flow.md`.
- Active `workflow-state.yaml` when available.
- Approved implementation plan and placement metadata.
- Changed file list.
- Source and tests only inside changed files and approved `allowed_paths`.
- Relevant coding, API, event, security, testing, and architecture standards.
- Traceability matrix when checking implementation links.

Optional reads:
- CI or local validation output.
- API contracts and event schemas impacted by the changed files.
- Design context for the active capability.

Forbidden reads:
- Unrelated source files.
- Unrelated domains or capabilities.
- Restricted paths without explicit owner approval.
- Release artifacts unless the PR explicitly changes release evidence.

Escalation rule: If review needs files outside changed files or approved `allowed_paths`, stop and report the missing approval or ownership reason.

Token discipline rule: Read changed files first, then only directly referenced standards, contracts, tests, and traceability rows. Full framework reads are allowed only for framework assessment or framework changes.

Stop conditions:
- Changed files are unknown.
- `allowed_paths` or `restricted_paths` are missing.
- Changed files include restricted or unapproved paths.
- Required implementation evidence is missing.
- Validation, traceability, API/event compatibility, or workflow evidence disagrees.

## Process
1. Identify the active domain, capability, PR or slice, and changed files.
2. Confirm placement metadata exists and changed files stay inside `allowed_paths`.
3. Check no changed file is in `restricted_paths` without required approval.
4. Review coding standards, security standards, and testing standards relevant to the changed files.
5. Check architecture adherence against approved design and implementation plan.
6. Check API and event compatibility for changed contracts, schemas, handlers, producers, or consumers.
7. Check test coverage for changed behavior, including unit, acceptance, negative, integration, security, and NFR coverage where applicable.
8. Run or review validation scripts when applicable.
9. Check traceability links from changed implementation to approved requirements, tests, and validation evidence.
10. Report findings first, ordered by severity.
11. Do not approve the PR. Recommend `Ready for human PR review`, `Changes required`, or `Blocked`.

## Outputs
- `domains/<domain>/capabilities/<capability>/features/<feature>/pr-review/pr-review-report.md` when PR review evidence is captured as an artifact
- PR review findings
- Changed file and allowed-path assessment
- Standards and architecture adherence assessment
- API/event compatibility assessment
- Test coverage assessment
- Validation script results or missing evidence
- Traceability assessment
- Recommendation for the next step

## Quality checks
- Changed files are explicit.
- Allowed and restricted paths are checked.
- Architecture, API/event compatibility, tests, validation, and traceability are reviewed.
- Findings distinguish blockers from recommendations.
- No source or business artifact changes are made by review.

## Human gate
Human PR review and required owner approvals are mandatory. AI can recommend readiness but cannot approve itself.

## Next skill or next workflow step
Use `$validation` only after PR review findings are resolved and required human PR approval exists.

## Example usage
`$pr-review Review implemented slice before validation`
