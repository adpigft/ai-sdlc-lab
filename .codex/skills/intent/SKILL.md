---
name: intent
description: User-friendly intent-stage orchestration for a new capability or feature from discovery through intent approval.
---

# Intent Skill

## Purpose
Start a new capability or feature in a way that is simple for PO, BA, SA, QA, Dev, and DevSecOps users while preserving the governed AI SDLC gates.

## When to use
Use `$intent` when a user wants to start a new product capability, feature, or business outcome and capture approved business intent.

Temporary alias: `$new` routes to `$intent` for one migration cycle.

## Inputs
- Feature or capability name
- Business problem or opportunity
- Known domain, channel, user, or customer segment
- Domain context, such as `domains/<domain>/domain-context.md`, when available
- Optional Jira Epic reference
- Optional Confluence or stakeholder notes

## Context pack
Use the `Intent` pack in `framework/context/stage-context-packs.md`.

Required reads:
- This skill document.
- `domains/<domain>/domain-context.md`.
- Workflow-state guidance.

Optional reads:
- Intent templates, Jira model guidance, and existing capability artifacts in the same domain for style.

Forbidden reads:
- Source code, unrelated domains, unrelated implementation plans, validation artifacts, and release artifacts.

Escalation rule: Read another domain only when the user request names a cross-domain dependency or impact analysis identifies one.

Token discipline rule: Read only the active domain context and lightweight examples; full framework reads are allowed only for framework assessment or framework changes.

Stop conditions:
- The domain context is missing for a new domain.
- Intent discovery is insufficient.
- Required PO/BA approval is missing.

## Process
1. If Jira is available, create or reference a lightweight Jira Epic shell as a discovery container.
2. Confirm that Git remains the source of truth and Jira is used for work management and approval tracking.
3. Read `domains/<domain>/domain-context.md` when the domain is known and the file exists.
4. Begin intent discovery using `ba-intent`.
5. Ask discovery questions before creating Git artifacts.
6. Summarize users, outcomes, scope, constraints, risks, success measures, domain-context reuse, and domain-specific controls.
7. Stop for PO / BA approval before creating or updating intent.
8. When intent is created or updated, create or update `domains/<domain>/capabilities/<capability>/workflow-state.yaml` using `framework/workflow/workflow-state-template.yaml`.
9. Set workflow state to `intent_review`, current artifact to `intent/intent.md`, pending gate to `intent_approval`, next state to `specification_review`, and next skill to `specification`.
10. Use `framework/workflow/workflow-state-guide.md` for state-aware `Review.`, `Approved.`, and `Status.` behavior.
11. After intent approval, update `workflow-state.yaml` to move from `intent_review` to `specification_review`.
12. After intent approval, continue to specification using `ba-specification`.
13. Stop at every approval gate and do not generate code.

## Outputs
- Optional Jira Epic shell or Epic reference
- Intent discovery summary
- Approved `domains/**/intent/intent.md` only after approval
- Created or updated `domains/**/workflow-state.yaml` after intent artifact creation
- Specification handoff only after intent approval

## Quality checks
- Jira Epic, if present, is lightweight and does not replace Git artifacts.
- Intent is created in Git only after discovery and approval.
- Specification is created only after intent approval.
- No source code is generated.
- Approval evidence is recorded in chat, Jira, or artifact metadata.
- Domain context was reviewed when available.
- Workflow state is created or updated when intent is created.
- `Review.`, `Approved.`, and `Status.` can be resolved from workflow state or inferred from artifacts.

## Human gate
PO / BA approval is required before intent is created or updated, and again before specification starts.

## Next skill or next workflow step
Use `$specification` after intent approval.

## Example usage
`$intent Start new capability: merchant QR refund`
