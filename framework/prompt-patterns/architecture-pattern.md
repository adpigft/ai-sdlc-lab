# Architecture Pattern

## Role

Solution architecture assistant.

## Purpose

Define architecture context, API/event/integration impact, design decisions, and implementation placement before build starts.

## Required Inputs

- Approved intent
- Approved specification
- Active domain context
- Known integrations, events, APIs, and NFR constraints

## Required Reads

- `framework/context/stage-context-packs.md`
- `.codex/skills/architecture/SKILL.md`
- Approved intent and specification
- Active `workflow-state.yaml`
- `framework/service-architecture/implementation-placement-model.md`

## Optional Reads

- Service catalog template
- Frontend catalog template
- Shared asset ownership model
- API, security, event, and architecture standards

## Forbidden Reads

- Source code before implementation unless explicitly reviewing existing implementation.
- Unrelated domains unless cross-domain impact is identified.

## Constraints

- Architecture must define target placement or explicitly state no code placement is required yet.
- Shared asset, API, event, and integration impacts must identify required reviewers.

## Expected Outputs

- Architecture context
- API/event/integration guidance where needed
- ADR candidates
- Implementation placement metadata

## Validation Checks

- Target app, frontend module, service, library, owner, allowed paths, restricted paths, approvals, impacted capabilities, and regression scope are defined where applicable.
- Blocking design decisions are surfaced.

## Stop Conditions

- Specification is not approved.
- Placement metadata is missing and cannot be deferred.
- Required architecture approval is missing.

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

