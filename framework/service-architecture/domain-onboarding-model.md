# Domain Onboarding Model

## Purpose

Define how to onboard a new domain before creating capability artifacts or implementation slices.

Domain onboarding creates shared delivery context, ownership, service placement, frontend placement, API/event/integration ownership, and approval rules.

## When To Onboard A New Domain

Onboard a new domain when:

- the business language is materially different from existing domains
- capabilities need distinct ownership
- services or frontend modules need domain-specific ownership
- APIs, events, data, or integrations need a new domain boundary
- cross-domain dependencies need stable ownership rules

## Steps To Create A New Domain

1. Create `domains/<domain>/domain-context.md`.
2. Define domain glossary and boundaries.
3. Define initial backend services in the service catalog.
4. Define frontend feature modules in the frontend catalog.
5. Define APIs, events, integrations, and owners.
6. Define required approvers.
7. Review domain onboarding artifacts.
8. Record approval.
9. Run `$intent <Capability>`.

Do not run `$intent` for a new domain until domain context and ownership placement are ready.

## Required `domain-context.md` Sections

The domain context should include:

- purpose
- glossary
- domain boundaries
- capability map or candidate capabilities
- shared APIs
- shared events
- integrations and third parties
- business rules
- data ownership
- security and compliance constraints
- observability expectations
- reusable patterns
- owner and approval model

## Required Service Catalog Entries

For each initial service, define:

- `domain`
- `service_name`
- `service_path`
- `owning_squad`
- `capabilities_served`
- `APIs_owned`
- `events_published`
- `events_consumed`
- `database_ownership`
- `integrations`
- `allowed_paths`
- `restricted_paths`
- `required_approvers`
- `regression_scope`

These may be planned entries. The service folder does not need to exist yet.

## Required Frontend Catalog Entries

For each frontend module, define:

- app name
- app path
- shell owner
- shared component owner
- feature module path
- feature owner squad
- allowed paths
- restricted paths
- approval rules

The feature module folder does not need to exist yet.

## Required Event And Integration Ownership

For each event or integration, define:

- producer owner
- consumer owners
- schema or contract owner
- compatibility expectations
- third-party owner
- operational owner
- review requirements

## Required Approval

Domain onboarding requires approval from:

- domain owner
- solution architect
- impacted platform/channel owner where frontend placement exists
- impacted service or shared asset owners
- security/risk/compliance where domain controls require it

## Cards Domain Example

New domain:

```text
cards
```

First capability:

```text
Card Replacement
```

Flow:

1. Create `domains/cards/domain-context.md`.
2. Define Cards glossary and boundaries.
3. Define `card-management-service` in the service catalog:
   - `domain`: `cards`
   - `service_name`: `card-management-service`
   - `service_path`: `services/cards/card-management-service/`
   - `owning_squad`: Cards Squad
   - `capabilities_served`: Card Replacement, Card Activation, Card Controls
4. Define `mobile-banking-app/features/cards` in the frontend catalog:
   - app: `mobile-banking-app`
   - feature module: `apps/mobile-banking-app/features/cards/`
   - feature owner: Cards Squad
   - shell/shared owner: Channel Platform Squad
5. Define integrations:
   - card processor
   - notification service
   - core banking
6. Review.
7. Approved.
8. Run:

```text
$intent Card Replacement
```
