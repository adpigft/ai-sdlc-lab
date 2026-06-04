# Payment Initiation Capability Context

## Purpose

Payment initiation covers customer or channel initiated payment creation flows in the Payments domain.

## Owned Features

- KHQR Payment: `features/khqr-payment/`

## Shared APIs, Events, And Integrations

- APIs: `POST /khqr/payments`, `GET /khqr/payments/{paymentId}` where applicable.
- Events: payment initiation, payment completion, payment failure, payment pending, audit, and reconciliation events where applicable.
- Integrations: mobile banking channel, payment processor, ledger/core banking, notification service, audit store, and reconciliation platform.

## Ownership

Owned by the Payments domain owner and Payments squad unless explicitly delegated.

## Out Of Scope

- Refunds and reversals.
- Card, deposit, lending, onboarding, or operations domain ownership.
