# Dependency Management

## Purpose

Define how cross-squad dependencies are managed across apps, services, libraries, and events.

## Dependency Types

- service-to-service API
- app-to-service API
- shared library dependency
- event producer/consumer dependency
- test fixture or contract dependency

## Dependency Rules

1. Every dependency must be cataloged.
2. Every public dependency must have a contract test.
3. Breaking changes require consumer impact review before merge.
4. Shared libraries must be versioned when public behavior changes.
5. Event changes must preserve backward compatibility unless a deprecation plan exists.

## Contract Test Selection

### App changes

Use:

- component tests for UI behavior
- API contract tests for backend calls
- regression tests for shared shell behavior

### Service changes

Use:

- unit tests for domain and orchestration logic
- API contract tests for public endpoints
- consumer contract tests for outbound dependencies
- regression tests for sibling features in the same service

### Library changes

Use:

- unit tests for library semantics
- consumer tests for each known consumer
- compatibility tests for public API or schema changes

### Event changes

Use:

- schema compatibility tests
- producer tests
- consumer contract tests
- replay/regression tests where ordering or idempotency matters

## Shared Asset Rules

### Multiple features in one service

When one microservice hosts multiple features:

- every feature shares the same service owner
- feature-specific changes must not rewrite unrelated feature paths
- any shared domain object or handler change requires regression tests for all affected features
- the PR must list the unaffected features that were regression checked

### Shared library

When `payment-common` is used by local payments, remittance, and cards:

- public API changes require all three consumer reviews
- internal refactors that do not alter public behavior can stay within the library owner path
- deprecations must be explicit and versioned

### Event-driven dependencies

When `PaymentCompleted` is consumed by notification and reconciliation:

- producer schema changes require both consumer owners to review
- additive fields should be preferred
- removals or semantic changes require a deprecation period and migration plan

## Do / Don't Rules

Do:

- register dependencies in a catalog
- choose contract tests before implementation
- use consumer regression tests when a shared dependency changes

Do not:

- merge a dependency change without naming the downstream consumers
- treat an internal refactor as automatically safe for consumers
- change event semantics without a deprecation plan

