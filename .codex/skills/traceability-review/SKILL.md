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
developer-implementation
