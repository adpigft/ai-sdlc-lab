---
name: intent
description: User-friendly wrapper around ba-intent for business intent discovery and approval.
---

# Intent Skill

## Purpose
Make business intent discovery easier for PO and BA users while using the governed `ba-intent` skill underneath.

## When to use
Use `$intent` when capturing or revising the business intent for a capability.

## Inputs
- Business request
- Target users and stakeholders
- Problem, opportunity, or outcome
- Known scope and constraints
- Optional Jira Epic or discovery notes

## Process
1. Use `ba-intent`.
2. Scan existing domain and capability patterns before asking discovery questions.
3. Ask focused questions about users, outcomes, scope, out of scope, assumptions, constraints, risks, and success metrics.
4. Summarize understanding.
5. Ask for PO / BA approval.
6. Create or update only `domains/**/intent/intent.md` after approval.

## Outputs
- Intent discovery summary
- Approved intent artifact after approval
- Reuse or similar capability recommendation when relevant

## Quality checks
- Problem and outcome are clear.
- Scope and out of scope are explicit.
- Success measures are testable.
- Existing capabilities were considered.
- No specification, architecture, tests, or code are created early.

## Human gate
PO / BA approval is required before specification starts.

## Next skill or next workflow step
Use `$specification`.

## Example usage
`$intent Capture intent for merchant QR refund`
