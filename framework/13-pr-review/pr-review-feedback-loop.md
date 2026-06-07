# PR Review Feedback Loop

## Purpose

Repeated PR feedback should improve the framework, not just the single pull request.

The loop turns recurring review comments into updates to skills, context packages, and standards.

## Feedback Targets

- skills
- context packages
- coding standards
- test standards
- architecture guidance
- observability guidance

## Examples

- repeated idempotency comments update architecture context and service guidance
- repeated missing-test comments update QA skill guidance and test standards
- repeated logging or diagnostics comments update observability context and guidance
- repeated contract comments update API and design guidance

## Operating Rule

When the same review issue appears more than once across related work:

1. capture the pattern
2. classify the root cause
3. update the right framework asset
4. keep the update lightweight and reviewable

## Notes

- The feedback loop is governed by Git.
- Review feedback must not silently rewrite approved intent or design.
- The loop improves future reviews and delivery quality.
