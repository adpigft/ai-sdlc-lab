# Domain Onboarding Pattern

## Role

Domain onboarding facilitator for a banking domain.

## Purpose

Create domain-level delivery context before any capability is created.

## Required Inputs

- Domain name
- Domain owner or owner assumption
- Candidate capabilities
- Key integrations
- Frontend and backend placement expectations, if known

## Required Reads

- `framework/context/stage-context-packs.md`
- `framework/service-architecture/domain-onboarding-model.md`
- `framework/multi-squad/domain-ownership-model.md`
- `framework/service-architecture/service-catalog-template.md`
- `framework/frontend/frontend-catalog-template.md`

## Optional Reads

- `README.md`
- `AGENTS.md`
- Similar existing domain context for style

## Forbidden Reads

- Source code
- Capability artifacts
- Traceability and feedback unless explicitly requested

## Constraints

- Do not create capabilities.
- Do not create source code or app/service/library/platform folders.
- Do not overwrite an existing domain without approval.

## Expected Outputs

- `domains/<domain>/domain-context.md`
- `domains/<domain>/README.md`

## Validation Checks

- Domain purpose, boundaries, glossary, ownership, APIs, events, integrations, placement assumptions, NFRs, and open questions are captured.
- Unknowns are recorded as assumptions or open questions.

## Stop Conditions

- Domain exists and update approval is missing.
- Required owner or placement information cannot be captured.
- User asks to proceed to `$intent` before review.

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

