# Shared Frontend Ownership

## Purpose

Define how shared frontend assets are governed when one app is used by multiple feature squads.

## Shared Frontend Ownership Rules

1. The shared app shell has one primary owner.
2. Feature teams may own module subtrees only if the catalog delegates that boundary.
3. Shared layout, navigation, auth bootstrap, telemetry, and design-system integration belong to the shell owner or platform frontend owner.
4. Shared component changes require regression tests for all affected modules.
5. Shared routing changes require cross-squad impact review.

## Controlled Change Types

### Safe module-local change

- limited to one feature module
- no shell routing or shared state change
- no cross-squad review unless module is shared

### Shared shell change

- route changes
- auth bootstrap changes
- shared telemetry changes
- shared component library updates

These require:

- shell owner review
- impacted module owner review
- UI regression tests

### Shared design system change

- must be governed as a shared library change
- requires consumer review from all apps that use it

## Banking Example

The `mobile-banking-app` is shared by:

- local payments
- remittance
- cards

Governance:

- shell and shared runtime owned by Mobile Banking squad
- local payments module owned by Local Payments squad if delegated
- remittance module owned by Remittance squad if delegated
- cards module owned by Cards squad if delegated

If a change touches the global dashboard shell, all three feature squads must review the impact.

## Do / Don't Rules

Do:

- separate shell and module ownership
- require regression tests for shared UI changes
- use feature flags for shared rollout control

Do not:

- treat shared UI as unowned
- change shared route behavior without cross-squad review
- let one feature team modify another team’s module path

