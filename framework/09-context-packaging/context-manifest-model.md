# Context Manifest Model

## Purpose

The context manifest records the exact context package set selected for a feature or delivery slice.

It supports reproducibility, traceability, token discipline, and drift detection.

## File Name

- `context-manifest.yaml`

## Required Fields

- selected package versions
- token budget
- source provenance
- last reviewed
- approved by
- checksum or hash
- stale flag

## Example Shape

```yaml
id: ctx-manifest-card-replacement
feature_id: FEAT-CARDREP-001
token_budget: 24000
selected_packages:
  - id: ctx.enterprise.security
    version: 1.2.0
  - id: ctx.domain.cards
    version: 2.0.0
  - id: ctx.capability.card-lifecycle
    version: 1.1.0
source_provenance:
  - git: domains/cards/capabilities/card-lifecycle-management/capability-context.md
  - git: domains/cards/capabilities/card-lifecycle-management/features/card-replacement/specification/specification.md
last_reviewed: 2026-06-07T00:00:00Z
approved_by:
  - BA
  - Architect
checksum: sha256:example
stale: false
```

## Notes

- The manifest is a controlled reference, not a generated guess.
- A stale manifest should trigger review before reuse.
- The manifest should be small and focused on the selected delivery slice.
