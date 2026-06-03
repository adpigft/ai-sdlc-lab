# Domain Index Template

## Purpose

Navigation aid for one domain. This index helps users and AI agents find domain context, owners, capabilities, APIs, events, integrations, and placement assumptions without reading unrelated domains.

## Authority

- `domains/<domain>/domain-context.md` is authoritative for domain context.
- Capability artifacts are authoritative for capability-specific content.
- `workflow-state.yaml` is authoritative for lifecycle state.
- If this index disagrees with source artifacts, source artifacts win.

## Domain

| Field | Value |
| --- | --- |
| Domain | `<domain>` |
| Domain context | `domains/<domain>/domain-context.md` |
| Domain owner | `<owner or open question>` |
| Primary squad | `<squad>` |
| Architect | `<architect or open question>` |

## Capabilities

| Capability | Path | Current State Source | Notes |
| --- | --- | --- | --- |
| `<capability>` | `domains/<domain>/capabilities/<capability>/` | `domains/<domain>/capabilities/<capability>/workflow-state.yaml` | `<notes>` |

## APIs

| API | Owner | Source Artifact | Status |
| --- | --- | --- | --- |
| `<api>` | `<owner>` | `<path>` | `<status>` |

## Events

| Event | Producer | Consumers | Source Artifact | Status |
| --- | --- | --- | --- | --- |
| `<event>` | `<producer>` | `<consumers>` | `<path>` | `<status>` |

## Integrations

| Integration | Owner / Reviewer | Capabilities | Notes |
| --- | --- | --- | --- |
| `<integration>` | `<owner>` | `<capabilities>` | `<notes>` |

## Placement Assumptions

| Area | Path | Owner | Notes |
| --- | --- | --- | --- |
| Frontend module | `<apps/...>` | `<owner>` | Navigation only. |
| Backend service | `<services/...>` | `<owner>` | Navigation only. |
| Shared libraries | `<libraries/...>` | `<owner>` | Requires approval. |

## Maintenance

This file should be generated or validated in the future from domain context, capability artifacts, workflow state, and catalogs.

