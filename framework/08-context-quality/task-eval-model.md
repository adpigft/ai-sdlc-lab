# Task Eval Model

## Purpose

Define task evaluations for verifying that context supports useful agent work.

## Evaluation Types

| Eval | Input Set | Expected Output | Judge Rubric | Pass/Fail Threshold | Evidence Captured |
| --- | --- | --- | --- | --- | --- |
| BA eval | PRD/context -> Intent | Candidate intent with business outcome, scope, exclusions, and questions | Intent quality rubric | Pass when the candidate is complete enough for review and no critical business gaps remain. | Input references, output summary, judge score, reviewer notes. |
| SA eval | Intent/spec/context -> Design/API | Candidate design with boundaries, APIs, events, integrations, and placement notes | Design quality rubric | Pass when the design is technically coherent and implementation-ready at a review level. | Inputs, design summary, judge score, traceability references. |
| Dev eval | Spec/design/context -> implementation plan | Candidate implementation plan with slices, affected paths, dependencies, and validation approach | Implementation readiness rubric | Pass when a developer can start work without major ambiguity. | Inputs, plan summary, judge score, blockers. |
| QA eval | Spec/context -> test scenarios | Candidate test scenarios, acceptance cases, and negative coverage | Test quality rubric | Pass when the scenarios cover the critical acceptance and risk paths. | Inputs, scenario set, judge score, coverage gaps. |
| DevOps eval | release context -> release readiness | Candidate release readiness summary with risks, rollback, and validation evidence | Release readiness rubric | Pass when release blockers are explicit and the release can be reviewed. | Inputs, readiness summary, judge score, release risks. |

## Rules

- Evals should be repeatable against the same input set.
- Evals should record both the candidate output and the reasons for failure.
- Passing an eval does not replace human approval for business or risk decisions.

## Notes

- The model is intended for future automation and review scaffolding.
- It does not require any external system calls.
