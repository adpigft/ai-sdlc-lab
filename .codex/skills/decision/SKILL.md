---
name: decision
description: User-friendly orchestration for architecture decisions and ADR lifecycle management.
---

# Decision Skill

## Purpose
Create, review, and manage architecture decisions so unresolved design choices do not leak into implementation.

## When to use
Use `$decision` when a capability has an architecture choice, integration tradeoff, technology decision, security pattern, data decision, or operational decision that needs an ADR.

## Inputs
- Decision topic
- Context and constraints
- Options considered
- Consequences and risks
- Related capability, architecture, API, or release references

## Process
1. Determine whether a new ADR is needed or an existing ADR should be reviewed.
2. Draft the ADR when a new decision is needed.
3. Review the ADR for approval readiness.
4. Link the ADR to impacted architecture, API, implementation, test, validation, and release artifacts.
5. Block implementation if the decision remains unresolved.
6. Ask for Architect approval before marking the decision accepted.

## Outputs
- Draft or reviewed ADR
- Decision status and owner
- Impacted artifact list
- Implementation block or approval signal

## Quality checks
- Decision context and options are explicit.
- Consequences and risks are documented.
- Rejected options are explained.
- Impacted artifacts are identified.
- Implementation is blocked while material decisions are unresolved.

## Human gate
Architect approval is required before an ADR can unblock implementation.

## Next skill or next workflow step
Return to `$design` after ADR approval, or proceed to `$implementation` only when all blocking decisions are resolved.

## Example usage
`$decision Create ADR for refund idempotency strategy`
