# Context Index Template

## Purpose

Define optional lightweight indexes that help Codex and users find the right artifacts without reading the whole repository.

These indexes are navigation aids only. They must not replace source artifacts.

## When Indexes Are Needed

| Scale | Recommendation |
| --- | --- |
| Lab or one capability | Optional |
| One to two squads | Optional |
| Three or more squads | Recommended |
| Ten or more squads | Required |

Indexes should be generated or validated where possible. Manual indexes can become stale.

## Rules

- Source artifacts remain authoritative.
- Indexes summarize paths, current state, owners, and blockers.
- Indexes must be short.
- Indexes must link to source artifacts instead of duplicating full content.
- Indexes should identify stale or missing source artifacts when validation exists.
- Indexes should not include secrets, customer data, or unmasked sensitive data.

## Optional Framework Index

Suggested path:

```text
framework/context-index.md
```

Template:

```markdown
# Framework Context Index

## Canonical Documents

| Topic | Canonical File | Notes |
| --- | --- | --- |
| Workflow state | framework/workflow/workflow-state-guide.md | Current state behavior |
| Review flow | framework/workflows/review-approval-flow.md | Status/Review/Approved |
| Placement | framework/service-architecture/implementation-placement-model.md | Required before implementation |

## Validation Scripts

| Check | Script |
| --- | --- |
| Workflow state | scripts/validate-workflow-state.sh |
| Workflow consistency | scripts/validate-workflow-consistency.sh |
| Release readiness | scripts/validate-release-readiness.sh |

## Notes

- Git is source of truth.
- Jira and Confluence are generated views unless API integration is approved.
```

## Optional Domain Index

Suggested path:

```text
domains/<domain>/domain-index.md
```

Template:

```markdown
# <Domain> Domain Index

## Domain Context

- Source: domains/<domain>/domain-context.md
- Domain owner:
- Primary squad:
- Architect:

## Capabilities

| Capability | Path | Current State | Owner | Notes |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Placement

| Area | Planned Path | Owner | Status |
| --- | --- | --- | --- |
| Frontend module |  |  |  |
| Backend service |  |  |  |

## Open Questions

| Question | Owner | Impact |
| --- | --- | --- |
|  |  |  |
```

## Optional Capability Artifact Index

Suggested path:

```text
domains/<domain>/capabilities/<capability>/artifact-index.md
```

Template:

```markdown
# <Capability> Artifact Index

## Workflow

- Workflow state: workflow-state.yaml
- Current state:
- Current skill:
- Pending gate:
- Blockers:

## Approved Inputs

| Artifact | Path | Status |
| --- | --- | --- |
| Intent | intent/intent.md |  |
| Specification | specs/spec.md |  |
| Design | context/context.md |  |
| API Contract | contracts/openapi.yaml |  |
| Test Design | tests/acceptance.feature |  |
| Implementation Plan | design/implementation-plan.md |  |

## Implementation Context

| Field | Value |
| --- | --- |
| Active slice |  |
| target_app |  |
| target_frontend_module |  |
| target_service |  |
| target_library |  |
| owning_squad |  |
| allowed_paths |  |
| restricted_paths |  |
| regression_scope |  |

## Validation And Release

| Artifact | Path | Status |
| --- | --- | --- |
| Validation report | validation/validation-report.md |  |
| Release notes | release/release-notes.md |  |
| Traceability | traceability/traceability-matrix.md |  |

## Notes

- This index is a navigation aid only.
- Source artifacts remain authoritative.
- Regenerate or validate this index when source artifacts change.
```

## Avoid Heavy Indexing Until Needed

Do not add vector databases, embeddings, or search infrastructure for normal lab usage.

Start with:

- predictable paths
- `workflow-state.yaml`
- stage context packs
- short Markdown indexes when scale requires them
