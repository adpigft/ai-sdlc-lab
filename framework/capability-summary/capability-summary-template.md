# Capability Summary Template

## Identity

| Field | Value |
| --- | --- |
| Domain | `<domain>` |
| Capability | `<capability name>` |
| Owner | `<owning squad or owner>` |
| Capability path | `domains/<domain>/capabilities/<capability>/` |

## Workflow

| Field | Value |
| --- | --- |
| `current_state` | `<state from workflow-state.yaml>` |
| `current_skill` | `<skill from workflow-state.yaml>` |
| Active artifact | `<path from workflow-state.yaml>` |
| Pending gate | `<gate from workflow-state.yaml>` |
| Next command | `<next command or skill>` |

## Approved Artifacts

| Artifact | Path | Status |
| --- | --- | --- |
| Intent | `intent/intent.md` | `<status>` |
| Specification | `specification/specification.md` | `<status>` |
| Design | `design/design.md` | `<status>` |
| API Contract | `contracts/openapi.yaml` | `<status>` |
| Test Design | `tests/acceptance.feature` | `<status>` |
| Implementation Plan | `implementation/implementation-plan.md` | `<status>` |
| Validation Report | `validation/validation-report.md` | `<status>` |
| Release Notes | `release/release-notes.md` | `<status>` |

## Blockers

- `<blocker or none>`

## Implementation Placement

| Field | Value |
| --- | --- |
| Target frontend module | `<target_frontend_module or none>` |
| Target service | `<target_service or none>` |
| Target library | `<target_library or none>` |
| Allowed paths | `<allowed_paths>` |
| Restricted paths | `<restricted_paths>` |

## APIs

| API | Source Artifact | Status |
| --- | --- | --- |
| `<api>` | `<path>` | `<status>` |

## Events

| Event | Producer | Consumers | Status |
| --- | --- | --- | --- |
| `<event>` | `<producer>` | `<consumers>` | `<status>` |

## Integrations

| Integration | Owner / Reviewer | Status |
| --- | --- | --- |
| `<integration>` | `<owner>` | `<status>` |

## NFR Highlights

| NFR | Summary | Status |
| --- | --- | --- |
| `<nfr>` | `<summary>` | `<status>` |

## Validation And Release

| Area | Status | Source |
| --- | --- | --- |
| Validation status | `<status>` | `validation/validation-report.md` |
| Release status | `<status>` | `release/release-notes.md` |
| Traceability status | `<status>` | `traceability/traceability-matrix.md` |

## Next

`<next command>`

## Authority Note

This summary is a navigation aid only. Source artifacts and `workflow-state.yaml` remain authoritative.
