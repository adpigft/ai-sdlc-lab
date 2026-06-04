# Shared Asset Ownership Model

## Purpose

Define ownership, versioning, compatibility, and approval rules for shared assets used by multiple squads or domains.

Shared assets increase reuse but also increase blast radius. They require explicit ownership and consumer impact review before changes.

## Shared Library Ownership

Shared libraries are owned by a library owner or platform squad.

Ownership responsibilities:

- maintain public APIs and semantic versioning
- document known consumers
- review compatibility impact
- define migration guidance
- require consumer regression where public behavior changes

## Shared Frontend Component Ownership

Shared frontend components are owned by the Channel Platform Squad unless delegated.

Examples:

- design-system components
- shared validation widgets
- common form controls
- app shell navigation components

Any change to shared components requires platform/channel approval and impacted feature review when behavior, layout, accessibility, telemetry, or validation changes.

## Event And Schema Ownership

Events and schemas have producer and consumer ownership.

Rules:

- producer owns event name, semantics, schema, keys, ordering assumptions, and publication guarantees
- consumers own processing assumptions and compatibility needs
- breaking schema changes require consumer impact review
- migration plans should use versioning, additive changes, or dual-publish where needed

## API Ownership

The API owner is the service or domain that owns the business operation.

API changes require:

- API owner approval
- architecture approval for material contract changes
- consumer impact review
- contract test update
- compatibility classification

## Platform Template Ownership

Platform templates are owned by platform teams.

Examples:

- `kafka-event-template`
- service bootstrap templates
- shared CI templates
- observability templates

Feature squads may request changes but must not alter templates without platform approval.

## Versioning And Compatibility Rules

| Change Type | Compatibility | Required Review |
| --- | --- | --- |
| additive optional field | usually compatible | owner review, contract test update |
| required field added | breaking | owner, consumer, architecture review |
| field removed or renamed | breaking | owner, consumer, migration plan |
| behavior changed | potentially breaking | owner, impacted consumer review |
| shared library public API changed | potentially breaking | library owner and consumer review |
| template behavior changed | potentially breaking | platform owner and consumer review |

## Approval Rules

- Shared library changes require library/platform owner approval.
- Shared frontend changes require Channel Platform approval.
- Event/schema changes require producer and consumer review.
- API changes require API owner and impacted consumer review.
- Platform template changes require platform owner approval.

## Examples

| Shared Asset | Owner | Consumers | Approval Notes |
| --- | --- | --- | --- |
| design-system | Channel Platform Squad | all frontend feature squads | platform approval and impacted module regression |
| audit-library | Platform Engineering | services producing audit events | platform approval and service regression |
| idempotency-library | Platform Engineering / Payments Platform | money movement services | platform and impacted service approval |
| error-model | API Platform | all API-producing services | API platform approval and consumer compatibility review |
| kafka-event-template | Event Platform | event-producing services | platform approval and producer/consumer review |
| observability-library | DevSecOps Platform | apps and services | platform approval and monitoring regression |
