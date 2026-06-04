# Cross-Squad Impact Review

## Purpose

Define the review required when an implementation slice, PR, API, event, or shared library change affects more than one squad.

## When Review Is Required

Trigger a cross-squad impact review when a change:

- modifies a shared app shell
- changes an API used by another squad
- changes a shared library public API
- changes an event schema or meaning
- touches more than one squad-owned path
- alters a consumer contract or regression boundary

## Required Inputs

- slice or PR summary
- target catalog entry
- list of changed paths
- consumer list
- contract diff
- test plan
- rollback note

## Review Checklist

| Area | Question |
| --- | --- |
| Ownership | Which squad owns the primary target? |
| Scope | Does the PR stay within the declared path boundary? |
| Contract | Are API, library, or event contracts backward compatible? |
| Consumers | Which squads must review or retest? |
| Tests | Are contract and regression tests selected for every affected consumer? |
| Rollback | Can the change be safely reverted or disabled? |
| Release risk | Does this change block another squad’s delivery? |

## Review Outcomes

- approved
- approved with conditions
- changes required
- blocked pending consumer review

## Banking Examples

### Mobile banking app shared by local payments, remittance, cards

Cross-squad review is required when:

- app shell navigation changes
- shared authentication flow changes
- shared telemetry or bootstrap code changes

Required reviewers:

- mobile app owner
- impacted feature squad owners
- platform frontend owner if shell code changes

### `local-payment-service`

Cross-squad review is required when:

- local-payment-service changes its public payment API
- it emits a changed `PaymentCompleted` event
- it reuses `payment-common` in a breaking way

### `payment-common` library

Cross-squad review is required when:

- public request/response types change
- serialization changes
- validation rules change

### `PaymentCompleted` event

Cross-squad review is required when:

- the event adds mandatory fields
- a field meaning changes
- event ordering or deduplication rules change

Notification and reconciliation service owners must review the consumer impact.

## Test Selection Rules

### Contract tests

Use contract tests when:

- an API changes
- a library API changes
- an event schema changes

### Regression tests

Use regression tests when:

- a change shares a microservice with other features
- a shared library is used by multiple squads
- an event consumer depends on the producer behavior

### Consumer tests

Use consumer tests when:

- the change could break another squad’s integration path
- the change affects external schema or API shape

## Do / Don't Rules

Do:

- make cross-squad review explicit
- name the exact consumer squads
- require contract and regression tests before approval

Do not:

- hide a cross-squad change in a single-squad PR
- approve a shared schema change without consumer review
- assume additive change is harmless without checking consumer parsing behavior

