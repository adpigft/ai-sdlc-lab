# Capability Artifact Index Template

## Purpose

Navigation aid for one capability. This index helps users and AI agents find the active artifacts and lifecycle evidence without reading unrelated capabilities.

## Authority

- `workflow-state.yaml` is authoritative for current state, current skill, pending gate, approvals, blockers, and next skill.
- Capability artifacts are authoritative for their own content.
- Traceability and validation artifacts are authoritative for their evidence.
- If this index disagrees with source artifacts, source artifacts win.

## Capability

| Field | Value |
| --- | --- |
| Domain | `<domain>` |
| Capability | `<capability name>` |
| Capability ID | `<capability-id>` |
| Capability path | `domains/<domain>/capabilities/<capability>/` |
| Workflow state | `domains/<domain>/capabilities/<capability>/workflow-state.yaml` |

## Lifecycle Artifacts

| Stage | Artifact | Path | Status Source |
| --- | --- | --- | --- |
| Intent | `intent.md` | `intent/intent.md` | `workflow-state.yaml` |
| Specification | `spec.md` | `specs/spec.md` | `workflow-state.yaml` |
| Design | `context.md` | `context/context.md` | `workflow-state.yaml` |
| API Contract | `openapi.yaml` | `contracts/openapi.yaml` | `workflow-state.yaml` |
| Test Design | `acceptance.feature` | `tests/acceptance.feature` | `workflow-state.yaml` |
| Implementation Plan | `implementation-plan.md` | `design/implementation-plan.md` | `workflow-state.yaml` |
| Validation | `validation-report.md` | `validation/validation-report.md` | `workflow-state.yaml` |
| Release | `release-notes.md` | `release/release-notes.md` | `workflow-state.yaml` |

## Traceability And Feedback

| Area | Path | Notes |
| --- | --- | --- |
| Traceability matrix | `traceability/traceability-matrix.md` | Source for end-to-end mapping. |
| Feedback log | `feedback/feedback-log.md` | Source for findings, defects, changes, and corrections. |

## Placement Metadata

| Field | Value |
| --- | --- |
| `target_app` | `<value or none>` |
| `target_frontend_module` | `<value or none>` |
| `target_service` | `<value or none>` |
| `target_library` | `<value or none>` |
| `owning_squad` | `<value>` |
| `allowed_paths` | `<paths>` |
| `restricted_paths` | `<paths>` |
| `required_approvals` | `<approvals>` |
| `regression_scope` | `<scope>` |

## Maintenance

This file should be generated or validated in the future from workflow state and source artifacts. Do not use it as a replacement for workflow state.
