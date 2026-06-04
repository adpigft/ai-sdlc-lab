# Path Governance Model

## Purpose

Define how allowed paths, restricted paths, CODEOWNERS, PR boundary checks, shared asset approvals, and cross-squad reviews prevent accidental cross-service or cross-domain edits.

## Allowed Path Model

Allowed paths are the exact paths an implementation slice may modify after approval.

Examples:

- `apps/mobile-banking-app/features/payments/**`
- `services/payments/local-payment-service/**`
- `services/cards/card-management-service/**`
- `libraries/idempotency-library/**`

Allowed paths must be recorded in the implementation plan before coding starts.

## Restricted Path Model

Restricted paths are paths the slice must not modify without additional owner approval.

Examples:

- another domain's feature module
- another service owned by another squad
- shared frontend components
- shared libraries
- platform templates
- event schemas used by consumers

Restricted paths should be explicit because they prevent nearby or convenient edits from expanding the slice.

## CODEOWNERS Recommendation

Use CODEOWNERS to enforce review ownership. Do not create CODEOWNERS entries until the ownership model is approved.

Sample examples:

```text
# Frontend shell and shared assets
/apps/mobile-banking-app/shell/                 @channel-platform-squad
/apps/mobile-banking-app/shared/                @channel-platform-squad

# Frontend domain modules
/apps/mobile-banking-app/features/payments/     @payments-squad
/apps/mobile-banking-app/features/cards/        @cards-squad
/apps/mobile-banking-app/features/deposits/     @deposits-squad
/apps/mobile-banking-app/features/lending/      @lending-squad

# Backend services
/services/payments/local-payment-service/       @payments-squad
/services/payments/remittance-service/          @remittance-squad
/services/cards/card-management-service/        @cards-squad
/services/deposits/account-service/             @deposits-squad
/services/lending/loan-service/                 @lending-squad

# Shared assets
/libraries/idempotency-library/                 @platform-engineering
/framework/03-delivery-governance/events/                              @event-platform
/platform/templates/                            @platform-engineering
```

## PR Boundary Checks

PR checks should compare changed files with:

- `allowed_paths`
- `restricted_paths`
- CODEOWNERS
- service catalog
- frontend catalog
- shared asset ownership

If a PR touches paths outside `allowed_paths`, the PR should be blocked or sent back for impact analysis and owner approval.

## Shared Asset Approval

Shared assets require extra review because they impact multiple squads.

Examples:

- shared frontend components
- shared libraries
- event schemas
- API error models
- platform templates
- observability libraries

Approval must include the asset owner and impacted consumers.

## Cross-Squad Review

Cross-squad review is required when a change:

- touches another squad's path
- changes a shared asset
- changes an API consumed by another squad
- changes an event consumed by another squad
- changes frontend shell/shared behavior used by multiple features
- changes operational behavior for another domain

## Examples

Payments:

- allowed: `services/payments/local-payment-service/**`
- restricted: `services/cards/**`, `services/deposits/**`, shared libraries without approval
- extra review: event changes consumed by operations or reconciliation

Cards:

- allowed: `services/cards/card-management-service/**`, `apps/mobile-banking-app/features/cards/**`
- restricted: payments/deposits/lending services, app shell without Channel Platform approval
- extra review: card processor integration or fraud event changes

Deposits:

- allowed: `services/deposits/account-service/**`, `apps/mobile-banking-app/features/deposits/**`
- restricted: onboarding and lending paths unless impacted owners approve
- extra review: account opening events consumed by onboarding or lending

Lending:

- allowed: `services/lending/loan-service/**`, `apps/mobile-banking-app/features/lending/**`
- restricted: deposits, cards, payments services unless owner approval exists
- extra review: credit bureau, decisioning, or customer profile contract changes
