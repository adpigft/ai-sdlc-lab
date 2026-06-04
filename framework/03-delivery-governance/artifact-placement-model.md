# Artifact Placement Model

## Purpose

Define where AI-SDLC framework artifacts are stored.

Skills are reusable procedures. This model is the framework adapter that maps generic skill outputs to repository paths.

## Domain Artifact

Domain = architecture boundary.

```text
domains/<domain>/domain-context.md
```

Purpose:

- domain boundary
- ownership
- glossary
- core services
- integrations
- APIs
- events
- shared rules and patterns

## Capability Artifact

Capability = business function boundary.

```text
domains/<domain>/capabilities/<capability>/capability-context.md
```

Purpose:

- capability purpose
- owned features
- shared business flow
- shared APIs, events, integrations, and state model where applicable
- ownership and out-of-scope notes

## Feature Artifact Root

Feature = delivery boundary.

```text
domains/<domain>/capabilities/<capability>/features/<feature>/
```

The feature owns delivery lifecycle artifacts.

## Canonical Feature Artifact Paths

| Artifact | Canonical Path |
| --- | --- |
| Intent | `intent/intent.md` |
| Specification | `specification/specification.md` |
| Design | `design/design.md` |
| API contract | `contracts/openapi.yaml` |
| Test design | `tests/acceptance.feature` |
| Implementation plan | `implementation/implementation-plan.md` |
| PR review | `pr-review/pr-review-report.md` |
| Validation | `validation/validation-report.md` |
| Release | `release/release-notes.md` |
| Workflow state | `workflow-state.yaml` |

## Placement Rules

- Domain context is owned at domain level.
- Capability context is owned at capability level.
- Lifecycle delivery artifacts are owned at feature level.
- Implementation slices are increments inside a feature; they are not separate features.
- Workflow state belongs to the feature and tracks the feature lifecycle.
- Source code placement is governed separately by implementation placement, path governance, and ownership catalogs.

## Migration Compatibility

Existing migration aliases may be supported by scripts for one migration cycle. New framework guidance and new artifacts should use the canonical paths above.
