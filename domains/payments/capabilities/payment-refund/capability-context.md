# Payment Refund Capability Context

## Purpose

Payment refund covers refund flows that return funds for completed payments in the Payments domain.

## Owned Features

- QR Refund: `features/qr-refund/`

## Shared APIs, Events, And Integrations

- APIs: `POST /qr-refunds`, `GET /qr-refunds/{refundId}`, operations refund APIs where applicable.
- Events: refund requested, refund processing started, refund completed, refund rejected, refund failed, audit, and reconciliation events where applicable.
- Integrations: KHQR payment service, merchant identity/authorization, merchant profile/status, payment processor, ledger/core banking, operations portal, audit store, and reconciliation platform.

## Ownership

Owned by the Payments domain owner and Payments squad unless explicitly delegated.

## Out Of Scope

- New payment initiation.
- Payment reversal flows that are not refund features.
- Card, deposit, lending, onboarding, or operations domain ownership.
