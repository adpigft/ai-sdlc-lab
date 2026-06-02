# Event Consumer Impact Review

## Purpose

Define the review required when an emitted or consumed event changes and may affect one or more squads.

## When Review Is Required

Trigger review when an event change:

- adds, removes, or renames fields
- changes field meaning
- changes event name or topic
- changes ordering or deduplication semantics
- changes producer retries or delivery guarantees
- changes retention or replay expectations

## Required Inputs

- event diff
- producer service
- consumer list
- schema compatibility result
- consumer regression plan
- rollback or deprecation plan

## Review Checklist

| Area | Question |
| --- | --- |
| Producer ownership | Which squad owns the event? |
| Consumer set | Which services consume it? |
| Compatibility | Is the change additive or breaking? |
| Contract tests | Are schema and consumer contract tests present? |
| Regression tests | Are downstream consumer regressions covered? |
| Rollback | Can the producer revert safely? |
| Deprecation | Is there a migration window for removals? |

## Banking Example: `PaymentCompleted`

Consumers:

- notification-service
- reconciliation-service

Review required when:

- payment status semantics change
- processor or ledger references change shape
- correlation ID rules change

## Test Selection

- schema compatibility tests for the event contract
- producer tests for emission behavior
- consumer regression tests for each downstream service
- replay tests if the consumer depends on deduplication or ordering

## Review Outcomes

- approved
- approved with conditions
- changes required
- blocked pending consumer review

## Do / Don't Rules

Do:

- include every consumer owner in review
- prefer backward-compatible payload evolution
- document migration or deprecation steps

Do not:

- publish a breaking event change without consumer review
- rely on consumers to discover event changes from runtime failure
- remove event fields without a migration window

