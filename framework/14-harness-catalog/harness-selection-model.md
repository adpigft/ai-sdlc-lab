# Harness Selection Model

## Purpose

Choose the smallest harness that still covers the risk and context of the change.

## Selection Inputs

- greenfield vs brownfield
- new feature vs change
- major vs minor
- regulatory impact
- integration impact
- production incident
- migration scope

## Selection Rules

- Use the Greenfield Feature Harness for net-new delivery with approved intent.
- Use the Brownfield Discovery Harness when the current state is not yet understood.
- Use the In-Flight Change Harness when approved work is changing before release.
- Use the Major Change Harness when the change can break contracts, data, or release risk.
- Use the Bug Fix Harness for contained defect correction.
- Use the PR Review Harness for review-only work.
- Use the Release Readiness Harness before release approval.
- Use the Context Recovery Harness when context is stale or incomplete.
- Use the Migration Harness for planned movement across platforms, services, or contexts.

## Decision Heuristics

- Prefer the least powerful harness that satisfies the required governance checks.
- Escalate to a major-change harness when the impact analysis says the change crosses API, data, security, or release boundaries.
- Escalate to migration when the change includes coordinated cutover or compatibility work.
- Escalate to recovery when the context itself is stale or unreliable.

## Notes

- The harness selection model is guidance, not automation.
- Approval rules still apply regardless of harness.
