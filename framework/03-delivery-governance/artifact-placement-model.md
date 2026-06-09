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

The `capability-onboarding` support skill may create or update this artifact when a new capability is being introduced under an existing domain.

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
| Requirements | `requirements/requirements.md` |
| Design | `design/design.md` |
| API contract | `contracts/openapi.yaml` |
| Test design | `tests/acceptance.feature` |
| Implementation plan | `implementation/implementation-plan.md` |
| PR review | `pr-review/pr-review-report.md` |
| Validation | `validation/validation-report.md` |
| Release | `release/release-notes.md` |
| Workflow state | `workflow-state.yaml` |

## Brownfield Support Artifacts

Brownfield modernization phases may create additional phase-specific artifacts under the feature root. These are dynamic and project-specific, but the framework should expect them to live in clearly named subfolders such as:

- `discovery/`
- `modernization-readiness/`
- `design/`
- `analysis/`
- `implementation-readiness/`
- `implementation-planning/`
- `implementation-architecture/`

Examples include:

- `discovery/quick-scan.md`
- `discovery/business-rules-catalog.md`
- `discovery/application-inventory.md`
- `discovery/architecture-overview.md`
- `discovery/api-inventory.md`
- `discovery/data-model.md`
- `discovery/state-machine.md`
- `discovery/integration-inventory.md`
- `discovery/domain-decomposition.md`
- `discovery/technical-debt.md`
- `discovery/current-state-discovery.md`
- `discovery/discovery-evidence.md`
- `modernization-readiness/modernization-readiness-review.md`
- `design/design-input-review.md`
- `design/design-artifact-plan.md`
- `analysis/gap-analysis.md`
- `analysis/capability-gap-analysis.md`
- `analysis/architecture-gap-analysis.md`
- `analysis/data-gap-analysis.md`
- `analysis/api-gap-analysis.md`
- `analysis/business-rule-gap-analysis.md`
- `analysis/operational-gap-analysis.md`
- `analysis/implementation-readiness-gaps.md`
- `analysis/gap-traceability.md`
- `analysis/impact-analysis.md`
- `analysis/component-impact.md`
- `analysis/data-impact.md`
- `analysis/api-impact.md`
- `analysis/integration-impact.md`
- `analysis/testing-impact.md`
- `analysis/operational-impact.md`
- `analysis/implementation-sequencing.md`
- `analysis/risk-impact.md`
- `analysis/impact-traceability.md`
- `implementation-readiness/implementation-readiness-review.md`
- `implementation-readiness/implementation-assumptions.md`
- `implementation-readiness/implementation-readiness-v2.md`
- `implementation-planning/implementation-plan.md`
- `implementation-planning/implementation-slices.md`
- `implementation-planning/implementation-dependencies.md`
- `implementation-planning/implementation-risks.md`
- `implementation-planning/implementation-traceability.md`
- `implementation-planning/sprint-plan.md`
- `implementation-architecture/module-structure.md`
- `implementation-architecture/package-structure.md`
- `implementation-architecture/database-migration-strategy.md`
- `implementation-architecture/api-implementation-standards.md`
- `implementation-architecture/domain-layer-standards.md`
- `implementation-architecture/transaction-boundary-strategy.md`
- `implementation-architecture/outbox-worker-strategy.md`
- `implementation-architecture/testing-strategy.md`
- `implementation-architecture/ci-cd-strategy.md`
- `implementation-architecture/implementation-architecture-review.md`

## Placement Rules

- Domain context is owned at domain level.
- Capability context is owned at capability level.
- Lifecycle delivery artifacts are owned at feature level.
- Implementation slices are increments inside a feature; they are not separate features.
- Workflow state belongs to the feature and tracks the feature lifecycle.
- Source code placement is governed separately by implementation placement, path governance, and ownership catalogs.
- Brownfield support artifacts may be mandatory, conditional, project-specific, or not required depending on the project context and the design-artifact plan.

## Migration Compatibility

Existing migration aliases may be supported by scripts for one migration cycle. New framework guidance and new artifacts should use the canonical paths above.
