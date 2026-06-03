# Cards Domain

This folder contains Cards domain delivery context.

## Source Of Truth

- Domain context: `domains/cards/domain-context.md`
- Capability artifacts will be created only after domain onboarding is reviewed and approved.

## Current Status

Cards domain onboarding draft exists for review.

No capabilities have been created yet.

## Ownership

| Area | Owner |
| --- | --- |
| Domain context | Cards Domain Owner, pending confirmation |
| Primary squad | Cards Squad, pending confirmation |
| Architecture | Cards Architect, pending confirmation |
| Frontend feature module | Cards Squad, with Channel Platform approval for shell/shared changes |
| Backend service | Cards Squad, planned `card-management-service` |

## Placement Assumptions

Frontend:

```text
apps/mobile-banking-app/features/cards/
```

Backend:

```text
services/cards/card-management-service/
```

These are placement assumptions only. This onboarding does not create app or service folders.

## Candidate Capabilities

- Card Replacement
- Card Activation
- Card Controls
- Card Status Inquiry

## Review

Review `domain-context.md` before creating capabilities.

After domain onboarding approval, use:

```text
$new Card Replacement
```
