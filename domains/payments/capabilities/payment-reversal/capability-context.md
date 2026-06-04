# Payment Reversal Capability Context

## Purpose

Payment reversal covers controlled reversal flows for existing payments in the Payments domain.

## Owned Features

- KHQR Payment Reversal: `features/khqr-payment-reversal/`

## Shared APIs, Events, And Integrations

- APIs: reversal APIs defined by owned feature contracts where applicable.
- Events: reversal requested, reversal processing, reversal completed, reversal failed, audit, and reconciliation events where applicable.
- Integrations: KHQR payment service, payment processor, ledger/core banking, operations support, audit store, and reconciliation platform.

## Ownership

Owned by the Payments domain owner and Payments squad unless explicitly delegated.

## Out Of Scope

- New payment initiation.
- Merchant refund flows.
- Card, deposit, lending, onboarding, or operations domain ownership.
