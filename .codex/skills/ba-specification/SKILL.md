---
name: ba-specification
description: Convert approved intent into functional requirements, NFRs, business rules, acceptance criteria, and open questions.
---

# BA Specification Skill

## Purpose
Create a testable specification from approved intent.

## When to use
Use only after intent.md is approved.

## Inputs
- intent.md
- Domain context
- Business rules
- Jira reference

## Process
1. Read approved intent.
2. Derive functional requirements.
3. Derive non-functional requirements.
4. Define business rules.
5. Define acceptance criteria.
6. Identify edge cases and open questions.
7. Ask for approval before finalizing.

## Output
- domains/<domain>/capabilities/<capability>/specs/spec.md

## Quality checks
- Requirements are testable.
- Acceptance criteria are measurable.
- NFRs are included.
- Open questions are recorded.
- No architecture or code is generated.

## Human gate
BA / PO approval is required before architecture starts.

## Next skill
architect-context
