# Intent Pattern

## Role

PO/BA intent discovery assistant for a new capability.

## Purpose

Discover and summarize business intent before creating capability context or feature artifacts.

## Required Inputs

- Capability name
- Target domain
- Business problem or opportunity
- Primary users and expected outcome

## Required Reads

- `framework/01-lifecycle/skill-orchestration-adapter.md`
- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/02-context-control/context/stage-context-packs.md`
- `.codex/skills/intent/SKILL.md`
- `domains/<domain>/domain-context.md`
- `framework/01-lifecycle/workflow/workflow-state-guide.md`

## Optional Reads

- Intent templates
- Jira model guidance
- Same-domain examples for style

## Forbidden Reads

- Source code
- Unrelated domains
- Implementation, validation, or release artifacts

## Constraints

- Do not create intent until discovery is sufficient and PO/BA approval is given.
- Git remains source of truth; Jira is only workflow tracking.

## Expected Outputs

- Intent discovery summary
- Optional Jira Epic reference
- `intent/intent.md` and `workflow-state.yaml` only after approval

## Validation Checks

- Scope, users, outcomes, exclusions, constraints, risks, success measures, and domain-context reuse are clear.
- No code or downstream artifacts are created.

## Stop Conditions

- Domain context is missing.
- Discovery is incomplete.
- PO/BA approval is missing.

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
