# Spec-Aware PR Review Model

## Purpose

Requirements-aware PR review checks whether the pull request still matches approved intent, requirements, design, tests, and release expectations.

It supplements normal code review with governance checks.

## Review Layers

1. code quality review
2. spec compliance review
3. design compliance review
4. API contract review
5. test coverage review
6. security review
7. traceability review
8. release readiness review

## Reviewer Roles

- developer reviewer
- architect reviewer
- QA reviewer
- security reviewer
- release reviewer
- product owner or BA reviewer when scope changes affect intent or requirements

## Check Types

### Deterministic Checks

- changed files match approved scope
- API contract remains backward compatible
- tests exist for the changed behavior
- traceability entries are present
- required artifacts exist in the expected paths

### LLM Judge Checks

- requirements clarity
- design consistency
- release risk explanation quality
- review comment usefulness

### Tool-Assisted Checks

- git diff inspection
- test execution
- static analysis
- contract validation
- traceability validation
- release-readiness validation

## Pass / Fail Criteria

- Pass only when all required layers meet the minimum threshold for the change type.
- Fail when a required artifact is missing, inconsistent, or unreviewed.
- Fail when the PR introduces a spec, design, API, or test mismatch that is not explained and approved.
- Fail when traceability is incomplete for a governed change.

## PR Comment Categories

- scope mismatch
- spec mismatch
- design mismatch
- API compatibility issue
- missing test coverage
- security concern
- traceability gap
- release risk
- clarification required

## Notes

- The PR review is not a substitute for approval.
- The reviewer should refer to the approved artifact set and workflow state before commenting.
- Repeated review feedback should feed back into the relevant skill, context package, or standard.
