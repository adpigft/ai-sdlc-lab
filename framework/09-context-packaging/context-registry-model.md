# Context Registry Model

## Purpose

Define how context packages are catalogued, versioned, resolved, and filtered.

## Registry File

The registry is represented by `context-registry.yaml`.

## Required Fields

- package id
- version
- status
- owner
- scope
- dependencies
- compatibility rules
- provenance
- security scan status
- last reviewed date
- expiry date

## Package Status

- draft
- approved
- deprecated

## Versioning

- Package versions should be semantic where practical.
- Breaking scope changes require a new major version.
- Non-breaking content updates should increment the minor or patch version.

## Dependency Resolution

- Resolve the requested package first.
- Load declared dependencies before optional overlays.
- Reject unresolved or incompatible dependencies.
- Prefer approved packages over draft packages when both exist.

## Compatibility Rules

- A package must declare whether it is compatible with a project, domain, capability, squad, or feature scope.
- A package must not be used outside its declared scope without review.
- A package must not be distributed if its security scan is failed or stale.

## Context Filtering Rules

- Filter to the smallest useful scope.
- Remove duplicated facts when a higher-level package already supplies them.
- Keep token budgets explicit.
- Preserve provenance and source references even when content is filtered.

## Notes

- The registry is a governance artifact, not an execution engine.
- Future automation should read this model before packaging or distribution.
