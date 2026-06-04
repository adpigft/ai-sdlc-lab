# Slice Ownership Model

## Purpose

Define how an implementation slice identifies the target app, service, library, or event and how that target maps to the owning squad.

## Slice Identification Fields

Every implementation slice should carry these fields in the slice plan or PR metadata:

| Field | Meaning |
| --- | --- |
| Slice ID | Stable slice identifier. |
| Primary target type | `app`, `service`, `library`, or `event`. |
| Primary target path | Repo path or artifact path owned by the slice. |
| Owning squad | Squad responsible for the target. |
| Secondary targets | Additional impacted paths or contracts. |
| Boundary class | `internal`, `shared`, `contract`, or `cross-squad`. |
| Required reviewers | Primary and secondary reviewers. |
| Test scope | Unit, contract, regression, and consumer tests required. |

## Target Resolution Rules

### Frontend app slice

If the slice changes a UI module, routing, shell, or shared component set:

- primary target type is `app`
- primary target path must match the app catalog
- owning squad is the app catalog owner

### Service slice

If the slice changes domain behavior, API handlers, orchestrators, or persistence:

- primary target type is `service`
- primary target path must map to one service catalog entry
- owning squad is the service catalog owner

### Library slice

If the slice changes shared logic, utilities, models, serialization, or client packages:

- primary target type is `library`
- primary target path must map to one library catalog entry
- owning squad is the library owner

### Event slice

If the slice changes an emitted or consumed event schema, ordering guarantee, or compatibility rule:

- primary target type is `event`
- primary target path must map to one event catalog entry
- owning squad is the event owner

## Slice Ownership Decision Tree

1. Does the slice modify only one owned path set?
   - yes: assign the owning squad from the catalog
   - no: continue
2. Is there one primary business capability?
   - yes: assign the squad for that capability as primary owner
   - no: split the slice
3. Does the slice change a shared asset?
   - yes: require cross-squad impact review
4. Does the slice cross app, service, or library boundaries?
   - yes: add the secondary owners and contract-test scope

## Examples

### Mobile banking app

Slice: shared navigation change in the shell

- target type: `app`
- target path: `apps/mobile-banking-app/`
- owning squad: Mobile Banking squad
- reviewers: Mobile Banking, Platform Frontend

Slice: local payments module update

- target type: `app`
- target path: `apps/mobile-banking-app/features/local-payments/`
- owning squad: Local Payments squad if module ownership is delegated; otherwise Mobile Banking squad

### Services

Slice: `local-payment-service` adds a new idempotency rule

- target type: `service`
- target path: `services/local-payment-service/`
- owning squad: Local Payments squad

Slice: `remittance-service` consumes `PaymentCompleted`

- target type: `service`
- target path: `services/remittance-service/`
- owning squad: Remittance squad

### Shared library

Slice: `payment-common` changes a public DTO

- target type: `library`
- target path: `libraries/payment-common/`
- owning squad: Payments Platform squad
- reviewers: all known consumer squads

## Do / Don't Rules

Do:

- identify the primary target before coding
- keep slices small enough to map to one owner
- use the catalog as the source of ownership truth

Do not:

- start coding before the slice owner is known
- allow a slice to silently expand into a different owner’s path
- mix unrelated app, service, and library changes in one slice unless all owners approve

