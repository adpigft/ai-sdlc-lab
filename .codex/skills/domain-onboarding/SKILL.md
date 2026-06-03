---
name: domain-onboarding
description: User-facing orchestration for onboarding a new banking domain before creating capabilities with $intent.
---

# Domain Onboarding Skill

## Purpose
Onboard a new banking domain before `$intent` capability creation is used.

Domain onboarding creates the domain-level delivery context, ownership assumptions, service placement assumptions, frontend placement assumptions, APIs, events, integrations, shared asset impacts, and open questions needed before capability artifacts are created.

## When to use
Use `$domain-onboarding` when a domain does not exist yet.

Examples:

```text
$domain-onboarding Cards
$domain-onboarding Deposits
$domain-onboarding Lending
```

Do not use this skill for an existing capability. Use `$intent` only after the domain context has been reviewed and approved.

## Inputs
- Domain name
- Domain owner
- Candidate capabilities
- Key integrations
- Frontend module expectation
- Backend service expectation
- Events or APIs, if known

## Required reads
Before drafting domain artifacts, read:

- `framework/service-architecture/domain-onboarding-model.md`
- `framework/multi-squad/domain-ownership-model.md`
- `framework/service-architecture/service-catalog-template.md`
- `framework/frontend/frontend-catalog-template.md`
- `framework/multi-squad/shared-asset-ownership-model.md`
- `framework/service-architecture/implementation-placement-model.md`

## Context pack
Use the `Domain Onboarding` pack in `framework/context/stage-context-packs.md`.

Required reads:
- This skill document.
- Domain onboarding, domain ownership, service catalog, frontend catalog, shared asset ownership, and implementation placement framework documents.

Optional reads:
- `README.md`, `AGENTS.md`, and existing domain contexts for style only.

Forbidden reads:
- Source code, capability artifacts, traceability, feedback, and app/service/library/platform folders unless the user explicitly asks for framework impact.

Escalation rule: Read related domains only when the new domain boundary or ownership model depends on them.

Token discipline rule: Keep context to onboarding templates and the target domain; do not load full framework content unless performing a framework change or assessment.

Stop conditions:
- The domain already exists and update approval is missing.
- Required owner or placement assumptions cannot be captured as assumptions or open questions.
- The user asks to create capabilities, source code, or implementation folders.

## Process
1. Confirm the requested domain name and normalize the folder name, such as `cards`, `deposits`, or `lending`.
2. Check whether `domains/<domain>/` already exists.
3. If the domain exists, do not overwrite it.
4. If `domains/<domain>/domain-context.md` already exists, review it and ask for approval before any update.
5. Ask for missing onboarding inputs when domain owner, candidate capabilities, integrations, frontend placement, backend service placement, APIs, or events are unclear.
6. Record unknown services, frontend modules, events, APIs, or integrations as assumptions or open questions.
7. Create only the approved domain-level artifacts.
8. Stop for human review after creating domain artifacts.
9. Recommend `Review.`.
10. Do not proceed to `$intent` automatically.

## Output artifacts
Create only:

- `domains/<domain>/domain-context.md`
- `domains/<domain>/README.md`

Do not create:

- capabilities
- source code
- `apps/`, `services/`, `libraries/`, or `platform/` folders
- workflow-state files
- Jira or Confluence API calls

## Domain context content
`domains/<domain>/domain-context.md` must include:

- domain purpose
- business scope
- boundaries
- glossary
- core entities
- candidate capabilities
- owned APIs
- published events
- consumed events
- integrations
- ownership
- frontend placement assumptions
- backend service placement assumptions
- shared asset impacts
- NFR considerations
- out of scope
- next steps

## Review behavior
After creating domain artifacts:

- stop for human review
- do not proceed to `$intent` automatically
- recommend `Review.`
- after approval, the user may run `$intent <Capability Name>`

## Guardrails
- If the domain already exists, do not overwrite it.
- If `domain-context.md` already exists, review and update only with approval.
- If candidate services or frontend modules are unknown, record them as assumptions or open questions.
- Do not invent implementation code.
- Do not modify unrelated domains.
- Do not create capabilities during domain onboarding.
- Do not create source, app, service, library, or platform folders.
- Keep Git as the source of truth.

## Quality checks
- Domain purpose, scope, and boundaries are clear.
- Domain owner is identified or recorded as an open question.
- Candidate capabilities are captured without creating capability folders.
- Service and frontend placement assumptions are documented without creating implementation folders.
- API, event, integration, and shared asset impacts are captured or marked unknown.
- Open questions are explicit and reviewable.
- No source code or unrelated domain artifacts are modified.

## Human gate
Domain owner and Solution Architect review is required before the domain is treated as ready for `$intent` capability creation.

## Next skill or next workflow step
After domain onboarding approval, use:

```text
$intent <Capability Name>
```

## Example usage
```text
$domain-onboarding Cards
$domain-onboarding Deposits
$domain-onboarding Lending
```
