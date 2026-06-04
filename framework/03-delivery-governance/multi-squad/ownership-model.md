# Multi-Squad Ownership Model

## Purpose

Define how AI-native delivery routes implementation work to the correct owning squad when multiple squads share apps, services, libraries, and events.

This model applies to framework docs, Jira planning, PR review, CODEOWNERS, and dependency governance. It does not replace domain artifacts or team operating agreements.

## Ownership Principles

1. Every implementation slice must map to one primary owned target.
2. A target is one of:
   - application
   - service
   - library
   - event contract
3. The owning squad is determined by the canonical catalog entry for that target.
4. Shared assets have a named primary owner and explicit consumer reviewers.
5. Changes that cross ownership boundaries require cross-squad impact review before merge.
6. Git remains the source of truth for the slice implementation and the owning artifact path.

## How Ownership Is Determined

### 1. Identify the implementation slice target

The slice definition must say which target is being changed:

- `app`
- `service`
- `library`
- `event`

If a slice touches more than one target, the slice must nominate one primary target and list the secondary impacted targets.

### 2. Resolve the canonical catalog entry

Match the target path to the relevant catalog:

- `framework/03-delivery-governance/frontend/app-catalog-template.md` for frontend apps
- `framework/03-delivery-governance/service-architecture/service-catalog-template.md` for services
- `framework/03-delivery-governance/libraries/library-catalog-template.md` for shared libraries
- `framework/03-delivery-governance/events/event-catalog-template.md` for events

### 3. Resolve the owning squad

The catalog entry must name:

- owning squad
- technical owner
- business owner
- CODEOWNERS path pattern
- required reviewers
- contract-test responsibilities

### 4. Validate path ownership

The implementation slice must only modify files under the owned path set unless the PR explicitly includes cross-squad impact review.

## Ownership Rules By Asset Type

### Frontend app

- Owned by one frontend/product squad.
- Shared shell or shared runtime code requires the platform/front-end foundation owner.
- Feature teams own feature modules only when the catalog allows that module boundary.

### Service

- Owned by one service squad.
- One service may host multiple features, but feature ownership does not override service ownership.
- Cross-service API or data model changes require impact review.

### Shared library

- Owned by one platform or domain engineering squad.
- Consumer squads may contribute only through the library owner’s review path.
- Breaking library changes require consumer impact review and versioning discipline.

### Event contract

- Owned by the emitting service or by the domain platform owner if the event is shared infrastructure.
- Consumers must review any schema, ordering, semantics, or retry contract changes.

## Banking Examples

### Shared mobile banking app

Example target: `mobile-banking-app`

Features:

- local payments
- remittance
- cards

Ownership rule:

- the app shell, routing, auth bootstrap, shared design system integration, and shared telemetry are owned by the mobile app squad
- feature modules are owned by their feature squads only if the app catalog allows that module boundary

### Services

- `local-payment-service` owned by Local Payments squad
- `remittance-service` owned by Remittance squad
- `card-management-service` owned by Cards squad

### Shared library

- `payment-common` owned by the Payments platform squad
- any feature squad consuming `payment-common` must review changes that alter public APIs or behavior

### Shared event

- `PaymentCompleted` owned by the service that emits it
- notification and reconciliation teams are mandatory consumers for compatibility review

## Do / Don't Rules

Do:

- choose one primary owning squad per slice
- record all secondary impacted targets
- use catalogs to resolve ownership, not assumptions
- require cross-squad review for shared assets

Do not:

- let a PR modify multiple owning squads’ paths without explicit impact review
- use Jira ownership labels as a substitute for catalog ownership
- treat a shared library as privately owned by one consuming feature

