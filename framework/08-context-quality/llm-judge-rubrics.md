# LLM Judge Rubrics

## Purpose

Define semantic review rubrics for context artifacts.

Deterministic checks validate facts. LLM judges validate whether the artifact is useful, coherent, and fit for the intended delivery task.

## Rubric Dimensions

- completeness
- clarity
- consistency
- testability
- implementation readiness
- security awareness
- traceability

## Intent Quality

Judge whether the intent is business-clear, bounded, and reviewable.

## Specification Quality

Judge whether the specification is actionable, testable, and traceable to intent.

## Design Quality

Judge whether the design is feasible, secure, consistent with the specification, and sufficiently detailed to support implementation.

## Test Quality

Judge whether the test artifacts cover the important business and technical risks.

## Context Package Quality

Judge whether the package is scoped correctly, provenance-aware, secure, reusable, and appropriate for the target task.

## Scoring Guidance

- 0 = missing or unusable
- 1 = weak or partial
- 2 = acceptable with gaps
- 3 = strong and ready

## Notes

- LLM judges should not override objective source facts.
- Any judgment that changes business or risk decisions requires human approval.
