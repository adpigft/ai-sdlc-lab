# Implementation Placement Model

## Purpose

Define how architecture and implementation planning determine exactly where code belongs before implementation starts.

This document provides the future enterprise placement model without creating `apps/`, `services/`, or `libraries/` folders now. Current lab implementation may use `src/`; enterprise multi-squad delivery should use `apps/`, `services/`, and `libraries/`.

## Placement Principle

Architecture decides the target ownership boundary. The implementation plan records target paths. Implementation slices are restricted to those paths.

No implementation may start until the implementation architecture and implementation plan define target code placement and allowed paths.

## Mandatory Implementation Metadata

Each implementation slice must include:

| Field | Purpose |
| --- | --- |
| `target_app` | Frontend app when UI code is impacted. |
| `target_frontend_module` | Feature module, shell, or shared frontend area. |
| `target_service` | Backend service when service code is impacted. |
| `target_library` | Shared library when shared code is impacted. |
| `owning_squad` | Primary owner accountable for the slice. |
| `allowed_paths` | Exact paths implementation may change. |
| `restricted_paths` | Paths implementation must not change without further approval. |
| `required_approvals` | Human approvals required before implementation or merge. |
| `impacted_capabilities` | Capabilities affected by the slice. |
| `regression_scope` | Unit, integration, contract, consumer, UI, or NFR tests required. |

## Implementation Architecture Artifacts

Implementation architecture should define the structure and standards that bridge design and code. Typical outputs include:

- module structure
- package structure
- database migration strategy
- API implementation standards
- domain-layer standards
- transaction boundary strategy
- outbox-worker strategy
- testing strategy
- CI/CD strategy
- implementation architecture review

## How Architecture Determines Target Frontend App Or Module

Architecture checks the frontend catalog when requirements affect:

- screens or journeys
- forms or validation UX
- navigation or routing
- shared shell behavior
- auth bootstrap
- telemetry
- shared components

The architecture context or implementation plan must record whether the target is:

- a domain feature module, such as `apps/mobile-banking-app/features/payments/**`
- app shell, such as `apps/mobile-banking-app/shell/**`
- shared frontend components, such as `apps/mobile-banking-app/shared/**`

Shared shell and shared component changes require Channel Platform approval.

## How Architecture Determines Target Backend Service

Architecture checks the service catalog when requirements affect:

- business orchestration
- API handlers
- command/query behavior
- persistence
- idempotency
- audit
- processor, ledger, or third-party integrations
- event publishing or consumption
- reconciliation or operational visibility

The architecture context or implementation plan must record the target service, service path, owning squad, allowed paths, restricted paths, APIs/events impacted, and regression scope.

## How Architecture Determines Shared Library Impact

Architecture checks shared asset ownership when a slice needs reusable code or changes existing shared behavior.

Shared library impact must record:

- target library
- library owner
- public API/model impact
- known consumers
- compatibility classification
- required approvals
- migration or versioning plan when needed

Feature work must not modify shared libraries as a side effect.

## How Architecture Determines API, Event, And Integration Impact

Architecture records whether the slice changes:

- OpenAPI contracts
- event schemas
- event semantics, keys, or ordering
- integration requests/responses
- third-party dependency behavior
- consumer expectations

API changes require API owner and consumer review. Event changes require producer and consumer review. Integration changes require owner and operational review.

## How Implementation Plan Records Target Paths

The implementation plan should include a placement table:

| Slice | target_app | target_frontend_module | target_service | target_library | owning_squad | allowed_paths | restricted_paths | required_approvals | impacted_capabilities | regression_scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Slice 1 |  |  |  |  |  |  |  |  |  |  |

The values may point to planned enterprise paths even when this lab currently uses `src/`.

## How Implementation Slices Restrict Changes

Implementation must:

1. read `workflow-state.yaml`
2. read architecture context
3. read implementation planning artifacts
4. read implementation architecture artifacts
5. check service catalog
6. check frontend catalog
7. check shared asset ownership where applicable
8. modify only `allowed_paths`
9. stop if a change is needed in `restricted_paths`

If a slice expands into another app, service, library, event, or platform area, implementation stops for owner and architecture review.

## Change And Defect Flows

Change requests and defect fixes update only impacted code and artifacts.

They must:

- perform impact analysis first
- identify impacted capabilities and owners
- update placement metadata if target paths change
- avoid regenerating the whole solution
- update traceability and feedback after approval

## Preventing Accidental Cross-Service Or Cross-Squad Edits

Use these controls:

- narrow `allowed_paths`
- explicit `restricted_paths`
- CODEOWNERS review
- service and frontend catalog lookup
- shared asset approval
- API/event consumer impact review
- PR boundary checks

Implementation must not infer permission from file proximity. Permission comes from approved placement metadata and owner approval.
