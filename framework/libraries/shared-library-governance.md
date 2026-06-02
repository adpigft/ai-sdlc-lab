# Shared Library Governance

## Purpose

Define how shared libraries are changed, reviewed, versioned, and tested across squads.

## Governance Rules

1. Shared libraries have a single owning squad.
2. Consumers are mandatory reviewers for public API changes.
3. Breaking changes require deprecation, migration, or versioned replacement.
4. Public API changes require contract and consumer regression tests.
5. Internal refactors that do not change behavior may stay within the owner squad.

## Change Classification

### Internal refactor

- no public API change
- no consumer impact
- owner squad review only

### Additive public change

- new helper, field, or compatible function
- consumer review required if behavior affects downstream code
- contract tests required

### Breaking public change

- removed symbol
- changed return semantics
- changed serialization
- changed validation or defaulting behavior

Requires:

- consumer review
- versioning plan
- migration or deprecation plan
- regression tests for every known consumer

## Banking Example: `payment-common`

`payment-common` is shared by:

- local payments
- remittance
- cards

Governance:

- the Payments Platform squad owns the library
- all consumer squads must review public API changes
- release notes must say whether the change is compatible, additive, deprecated, or breaking

## Test Selection

- unit tests for library semantics
- consumer contract tests for public API behavior
- consumer regression tests for libraries used by multiple feature squads

## Do / Don't Rules

Do:

- keep library APIs narrow
- document deprecations
- notify all consumers before removal

Do not:

- merge a breaking change without migration plan
- treat a shared library like a private helper package
- assume consumer code will absorb signature or schema changes safely

