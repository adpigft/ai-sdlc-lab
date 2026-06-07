# Context Versioning Policy

## Purpose

Context packages are versioned assets.

Versioning controls compatibility, reuse, deprecation, and controlled rollout.

## Version Scheme

Use semantic versioning:

- major for incompatible change
- minor for backward-compatible capability growth
- patch for clarifications, fixes, and low-risk updates

## Package States

- draft
- approved
- deprecated
- retired

## Compatibility Rules

- approved packages may depend on approved packages of equal or lower major version when compatible
- major version changes may break consumers and require explicit review
- minor and patch changes should remain backward compatible unless documented otherwise
- deprecated packages may still be read but should not be selected for new work
- retired packages must not be selected for new work

## When To Bump Versions

- major: context structure changes, incompatible assumptions, or altered governance meaning
- minor: added guidance, added examples, expanded scope, or new non-breaking sections
- patch: wording corrections, typo fixes, clarifications, or metadata adjustments that do not change meaning

## Context Lock File Concept

A feature or harness may lock to a specific set of package versions so that review, validation, and replay use the same context bundle.

The lock file records the selected package IDs and versions and prevents accidental drift.

## Feature Context Manifest

Each feature should reference a manifest that records the selected context packages, their versions, and their provenance.

## Examples

- `ctx.enterprise.security@1.2.0`
- `ctx.domain.cards@2.0.0`
- `ctx.capability.card-lifecycle@1.1.0`

## Notes

- Git is the source of truth for package version history.
- Context packages are reusable libraries, not loose notes.
- A package should only advance to approved when review criteria are satisfied.
