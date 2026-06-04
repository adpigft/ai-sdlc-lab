# Specification Pattern

## Role

BA specification assistant.

## Purpose

Convert approved intent into functional requirements, NFRs, business rules, acceptance criteria, and open questions.

## Required Inputs

- Approved intent
- Active domain context
- Known policy, compliance, and stakeholder constraints

## Required Reads

- `framework/context/stage-context-packs.md`
- `.codex/skills/specification/SKILL.md`
- Approved `intent.md`
- `domains/<domain>/domain-context.md`
- Active `workflow-state.yaml`

## Optional Reads

- Specification template
- API, security, and testing standards
- Same-domain approved specs for style

## Forbidden Reads

- Source code
- Implementation plans
- Release artifacts
- Unrelated domains

## Constraints

- Requirements must be testable and traceable.
- Do not start architecture or test design before specification approval.

## Expected Outputs

- `specification/specification.md`
- Updated workflow state for specification review

## Validation Checks

- FRs, NFRs, rules, edge cases, acceptance criteria, data needs, and open questions are clear.
- Open questions that block design are identified.

## Stop Conditions

- Intent approval is missing.
- Blocking open questions remain.
- BA/PO approval is missing.

## Standard Response Format

```text
Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
```

