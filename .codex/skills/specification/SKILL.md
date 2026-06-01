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

## Process
1. Confirm intent approval exists.
2. Use `ba-specification`.
3. Capture functional requirements, non-functional requirements, business rules, data needs, acceptance criteria, and open questions.
4. Identify Jira Stories after specification approval, not before.
5. Ask for BA / PO approval before downstream design starts.

## Outputs
- Approved `domains/**/specs/spec.md` after approval
- Jira Story creation guidance after specification approval
- Open questions and dependency list

## Quality checks
- Requirements are testable and unambiguous.
- NFRs are explicit.
- Business rules and edge cases are captured.
- Acceptance criteria map to requirements.
- Jira Stories are not treated as the source of truth.

## Human gate
BA / PO approval is required before architecture and test design proceed.

## Next skill or next workflow step
Use `$architecture` and `$test-design`; create Jira Stories after specification approval.

## Example usage
`$specification Draft requirements from approved QR refund intent`
