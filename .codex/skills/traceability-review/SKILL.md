---
name: traceability-review
description: Maintain end-to-end traceability from intent to requirements, architecture, API, tests, validation, release, Jira, and Confluence.
---

# Traceability Skill

## Purpose
Maintain auditable delivery traceability.

## When to use
Use whenever intent, spec, context, API, tests, validation, release, Jira, or Confluence links change.

## Inputs
- intent.md
- spec.md
- context.md
- openapi.yaml
- acceptance.feature
- validation-report.md
- release-notes.md
- Jira references
- Confluence references

## Context pack
Use the `Traceability Review` pack in `framework/02-context-control/context/stage-context-packs.md`.

Required reads:
- This skill document.
- Active domain context.
- Active feature artifacts.
- Traceability matrix.
- Active `workflow-state.yaml`.

Optional reads:
- Feedback log, generated Jira/Confluence payloads, validation report, and release notes.

Forbidden reads:
- Source code unless implementation evidence must be mapped.
- Unrelated capabilities unless cross-capability impact exists.

Escalation rule: Read additional artifacts only when a traceability link, dependency, or cross-capability impact requires it.

Token discipline rule: Read only artifacts needed to prove links for the active capability; full framework reads are allowed only for framework assessment or framework changes.

Stop conditions:
- A mandatory source artifact is missing.
- A traceability gap blocks implementation, validation, or release.

## Process
1. Map intent to requirements.
2. Map requirements to architecture/API.
3. Map requirements to tests.
4. Map tests to validation evidence.
5. Map release notes to approved scope.
6. Identify gaps.
7. Update traceability matrix.

## Output
- traceability/traceability-matrix.md

## Quality checks
- No orphan requirements.
- No orphan tests.
- Every API maps to a requirement.
- Every released item maps to approved scope.
- Gaps are clearly marked.

## Human gate
BA, Architect, and QA review required before build/release.

## Next skill
Use `$implementation` after traceability approval when implementation prerequisites are complete.
