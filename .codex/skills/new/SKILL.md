---
name: new
description: User-friendly orchestration for a new capability or feature from Jira Epic discovery through intent and specification gates.
---

# New Capability Skill

## Purpose
Start a new capability or feature in a way that is simple for PO, BA, SA, QA, Dev, and DevSecOps users while preserving the governed AI SDLC gates.

## When to use
Use `$new` when a user wants to start a new product capability, feature, or business outcome.

## Inputs
- Feature or capability name
- Business problem or opportunity
- Known domain, channel, user, or customer segment
- Optional Jira Epic reference
- Optional Confluence or stakeholder notes

## Process
1. If Jira is available, create or reference a lightweight Jira Epic shell as a discovery container.
2. Confirm that Git remains the source of truth and Jira is used for work management and approval tracking.
3. Begin intent discovery using `ba-intent`.
4. Ask discovery questions before creating Git artifacts.
5. Summarize users, outcomes, scope, constraints, risks, and success measures.
6. Stop for PO / BA approval before creating or updating intent.
7. After intent approval, continue to specification using `ba-specification`.
8. Stop at every approval gate and do not generate code.

## Outputs
- Optional Jira Epic shell or Epic reference
- Intent discovery summary
- Approved `domains/**/intent/intent.md` only after approval
- Specification handoff only after intent approval

## Quality checks
- Jira Epic, if present, is lightweight and does not replace Git artifacts.
- Intent is created in Git only after discovery and approval.
- Specification is created only after intent approval.
- No source code is generated.
- Approval evidence is recorded in chat, Jira, or artifact metadata.

## Human gate
PO / BA approval is required before intent is created or updated, and again before specification starts.

## Next skill or next workflow step
Use `$specification` after intent approval.

## Example usage
`$new Start new capability: merchant QR refund`
