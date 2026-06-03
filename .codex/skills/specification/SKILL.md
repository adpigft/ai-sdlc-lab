---
name: specification
description: User-friendly wrapper around ba-specification for approved intent to functional and non-functional requirements.
---

# Specification Skill

## Purpose
Turn approved intent into clear requirements, business rules, acceptance criteria, and open questions.

## When to use
Use `$specification` after intent is approved and before architecture, API, test design, or implementation.

## Inputs
- Approved `intent.md`
- Business policies and rules
- Stakeholder clarifications
- Domain standards and constraints
- Optional Jira Epic reference

## Context pack
Use the `Specification` pack in `framework/context/stage-context-packs.md`.

Required reads:
- This skill document.
- Approved intent.
- Active domain context.
- Active `workflow-state.yaml`.
- Specification template.

Optional reads:
- API, security, and testing standards.
- Similar approved specs in the same domain for style.

Forbidden reads:
- Source code, implementation plans, release artifacts, and unrelated domains.

Escalation rule: Read another domain only when the requirement explicitly impacts that domain or an integration owner must be identified.

Token discipline rule: Keep context centered on approved intent and domain rules; do not load full framework content outside framework assessment or framework changes.

Stop conditions:
- Intent is not approved.
- Open questions block requirement definition.
- Required approver is missing.

## Process
1. Confirm intent approval exists.
2. Use `ba-specification`.
3. Capture functional requirements, non-functional requirements, business rules, data needs, acceptance criteria, and open questions.
4. When specification is created or updated, create or update `domains/<domain>/capabilities/<capability>/workflow-state.yaml` using `framework/workflow/workflow-state-template.yaml` when needed.
5. Set workflow state to `specification_review`, current artifact to `specs/spec.md`, pending gate to `specification_approval`, next state to `design_review`, and next skill to `design`.
6. Use `framework/workflow/workflow-state-guide.md` for state-aware `Review.`, `Approved.`, and `Status.` behavior.
7. Identify Jira Stories after specification approval, not before.
8. Ask for BA / PO approval before downstream design starts.

## Outputs
- Approved `domains/**/specs/spec.md` after approval
- Created or updated `domains/**/workflow-state.yaml` after specification artifact creation
- Jira Story creation guidance after specification approval
- Open questions and dependency list

## Quality checks
- Requirements are testable and unambiguous.
- NFRs are explicit.
- Business rules and edge cases are captured.
- Acceptance criteria map to requirements.
- Jira Stories are not treated as the source of truth.
- Workflow state points `Review.` to the specification draft and `Approved.` to the architecture stage.

## Human gate
BA / PO approval is required before design and test-design proceed.

## Next skill or next workflow step
Use `$design` and `$test-design`; create Jira Stories after specification approval.

## Example usage
`$specification Draft requirements from approved QR refund intent`
