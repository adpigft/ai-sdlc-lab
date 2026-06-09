# Modernization Readiness Review

## Purpose

Assess whether discovery is sufficient to begin brownfield modernization intent work.

This review distinguishes:

- demo replacement readiness
- production replacement readiness
- current-state understanding
- target-state readiness

## Decision Questions

- Is the current-state baseline credible enough to proceed?
- Are the most important business rules, interfaces, data dependencies, and operational constraints identified?
- Are evidence quality and discovery limitations explicit?
- Is the team ready to define a target-state vision, or is further discovery still required?

## Review Inputs

- discovery outputs
- discovery evidence
- limitations log
- recovered business rules
- application inventory
- architecture overview
- API inventory
- data model
- state machine
- integration inventory
- technical debt summary

## Output

- `modernization-readiness-review.md`

## Readiness Guidance

- Demo replacement readiness may be acceptable with partial evidence if the goal is a short-lived or low-risk lab replacement.
- Production replacement readiness requires materially higher evidence quality, explicit operational constraints, and traceable understanding of dependencies.
- Current-state understanding is about whether the team knows what exists now.
- Target-state readiness is about whether the team can safely define what should exist next.

## Expected Review Sections

1. Review Scope
2. Current-State Understanding
3. Evidence Quality
4. Limitations
5. Demo Replacement Readiness
6. Production Replacement Readiness
7. Target-State Readiness
8. Risks
9. Recommendation

## Recommendation Outcomes

- `Ready for intent definition`
- `Ready for further discovery`
- `Demo only`
- `Not ready`

## Quality Checks

- Evidence is separated from inference.
- Limitations are explicit.
- Readiness is stated separately for demo and production replacement use cases.
- The review does not invent missing facts.

