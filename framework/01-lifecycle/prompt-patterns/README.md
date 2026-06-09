# Prompt Patterns

## Purpose

Prompt patterns provide lightweight execution guidance for repeatable AI-SDLC work. They help the AI choose the right role, inputs, reads, constraints, outputs, checks, and stopping point for each stage.

Patterns guide execution only. They do not replace source artifacts, workflow state, skills, standards, validation scripts, Jira, or Confluence summaries.

Prompt patterns should use generic skills as procedures and the framework adapters for repository-specific orchestration:

- `framework/01-lifecycle/skill-orchestration-adapter.md`
- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`

## How To Use

Use the pattern that matches the active command or lifecycle stage:

- `domain-onboarding-pattern.md`
- `intent-pattern.md`
- `requirements-pattern.md`
- `design-pattern.md`
- `modernization-readiness-review-pattern.md`
- `design-input-review-pattern.md`
- `implementation-readiness-pattern.md`
- `implementation-planning-pattern.md`
- `vertical-slice-planning-pattern.md`
- `implementation-architecture-pattern.md`
- `test-design-pattern.md`
- `implementation-pattern.md`
- `pr-review-pattern.md`
- `validation-pattern.md`
- `release-pattern.md`
- `change-request-pattern.md`
- `defect-fix-pattern.md`
- `traceability-review-pattern.md`
- `feedback-capture-pattern.md`

Keep prompts small. Read only the stage context pack, active source artifacts, and directly relevant standards. Full framework reads are for framework assessment or framework changes only.

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
