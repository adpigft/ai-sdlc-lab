# CODEOWNERS Guidelines For Multi-Squad Delivery

## Purpose

Define how CODEOWNERS should enforce path ownership for apps, services, libraries, events, and shared framework assets.

## Principles

1. CODEOWNERS is a guardrail, not the only ownership system.
2. Catalogs define ownership intent.
3. CODEOWNERS enforces review on the paths the catalog names.
4. Shared paths must have explicit shared ownership and escalation reviewers.

## Recommended Structure

Group ownership by path boundary:

```text
/apps/mobile-banking-app/              @mobile-banking @platform-frontend
/services/local-payment-service/       @local-payments
/services/remittance-service/          @remittance
/services/card-management-service/     @cards
/libraries/payment-common/             @payments-platform @local-payments @remittance @cards
/events/payment-completed/             @payments-platform @notification @reconciliation
```

## Guidelines

### App ownership

- The app shell path should list the app owner and platform owner.
- Feature modules should list the feature squad if the module boundary is delegated.
- Shared design system or shell paths should not be owned by every feature squad.

### Service ownership

- Each service root should have one primary owning squad.
- Shared infrastructure directories inside a service should not weaken ownership of the service root.

### Library ownership

- Shared libraries should include owner and consumer review groups.
- Breaking changes require both owner review and known consumer review.

### Event ownership

- Event schema paths should be owned by the emitting squad.
- Event catalog or schema directories should include mandatory consumer reviewers.

## Review Enforcement

CODEOWNERS should trigger review for:

- ownership path changes
- shared contract changes
- public API or schema changes
- build, deployment, and test path changes that affect multiple squads

## Do / Don't Rules

Do:

- keep CODEOWNERS aligned to catalog paths
- use shared reviewer groups for shared assets
- review path exceptions as governance changes, not ad hoc edits

Do not:

- assign every squad to every path
- use CODEOWNERS to hide ownership conflicts
- leave shared libraries or events without consumer reviewers

