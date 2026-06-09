# Card Replacement Intent

## Metadata

| Field | Value |
| --- | --- |
| Intent ID | INT-CARDREP-001 |
| Jira Epic | TBD |
| Domain | Cards |
| Capability | Card Lifecycle Management |
| Feature | Card Replacement |
| Owner | Cards Squad |
| Created | 2026-06-05 |
| Status | Approved |

## Business Outcome

Allow eligible customers and operations users to request replacement for lost, stolen, or damaged cards through approved digital channels with full auditability, request traceability, and replacement status visibility.

## Problem Statement

Customers need a secure and convenient way to replace lost, stolen, or damaged cards without visiting a branch. The bank needs to reduce branch dependency and operational effort while preserving authorization controls, audit evidence, card blocking expectations, and clear status visibility.

## Stakeholders

| Role | Name or Team | Responsibility |
| --- | --- | --- |
| Product Owner | TBD | Business scope and intent approval |
| Business Analyst | TBD | Business rules and requirement elaboration |
| Capability Owner | Cards Squad | Capability ownership and delivery coordination |
| Domain Owner | TBD | Cards domain ownership |
| Architect | TBD | Architecture and integration approval |
| QA Lead | TBD | Validation approach |
| Security / Risk | TBD | Replacement authorization, card blocking, and audit controls |
| Operations | Operations team | Operations Portal replacement journey and support visibility |
| Channel Platform | Channel Platform Squad | Mobile App and Operations Portal shell/shared component review where impacted |

## In Scope

- Customer-initiated card replacement through Mobile App.
- Operations-user card replacement through Operations Portal.
- Replacement reasons:
  - Lost Card
  - Stolen Card
  - Damaged Card
- Address confirmation before request submission.
- Card blocking for Lost Card and Stolen Card replacement.
- No card blocking requirement for Damaged Card replacement.
- No replacement fee for pilot.
- Replacement request submission.
- Replacement status tracking.
- Full auditability for material replacement actions.
- End-to-end replacement request traceability.
- Authorization controls that prevent unauthorized replacement requests.

## Out of Scope

- Branch-assisted replacement.
- Web Banking.
- Expired Card replacement.
- Fraud Reissue.
- Name Change.
- Product Upgrade/Downgrade.
- Instant digital card issuance.
- Card manufacturing and logistics tracking.
- Fraud investigation workflows.
- Card renewal journeys.
- Integration with external courier tracking services.
- Maker-checker approval for pilot.
- Replacement fee charging for pilot.
- Notification implementation.
- Customer Profile management.
- Card Controls capability features outside blocking required for Lost and Stolen replacement.
- Card transaction processing.
- Card authorization.
- Card settlement.

## Assumptions

- Cards Squad owns the Card Replacement feature under Card Lifecycle Management.
- Mobile App and Operations Portal are the only pilot channels.
- Lost and Stolen replacement requests require card blocking as part of the replacement journey.
- Damaged card replacement does not require card blocking for pilot.
- Address confirmation is mandatory before replacement request submission.
- No fee is charged during the pilot.
- Maker-checker approval is not required for the pilot.
- Customer Profile Capability provides customer profile and address context but remains outside this feature's ownership.
- Notification Capability may be consumed where notification is required but remains outside this feature's ownership.
- Card Processor integration is required for replacement execution or downstream lifecycle coordination, subject to design approval.

## Dependencies

| Dependency | Purpose | Ownership |
| --- | --- | --- |
| Card Processor | Coordinate replacement lifecycle action and processor references. | Card Processor owner / Cards Squad |
| Customer Profile Capability | Provide customer profile and address context for confirmation. | Customer Profile Capability owner |
| Notification Capability | Support customer-safe notifications where approved. | Notification Capability owner |
| Mobile App | Customer replacement request channel. | Channel Platform / Cards Squad |
| Operations Portal | Operations-user replacement request channel. | Operations owner / Cards Squad |
| Audit Store | Persist material card replacement audit evidence. | Audit platform owner |

## Risks

| Risk | Impact | Owner | Mitigation |
| --- | --- | --- | --- |
| Unauthorized replacement request | Customer harm and operational loss | Cards Squad / Security | Require actor authorization and auditable request evidence. |
| Incorrect address confirmation | Replacement may be sent to an incorrect address | Cards Squad / Customer Profile owner | Require address confirmation before submission and trace confirmed address source. |
| Lost or stolen card not blocked | Continued unauthorized card use risk | Cards Squad / Card Processor owner | Require blocking for Lost and Stolen replacement reasons. |
| Status visibility is inaccurate | Customer and operations support confusion | Cards Squad | Track replacement request status and processor references. |
| Dependency ownership is unclear | Delayed design and validation | Cards Squad | Confirm Card Processor, Customer Profile, Notification, and channel reviewers before design. |

## Success Measures

- Successful replacement requests submitted digitally.
- Reduced branch dependency for replacement requests.
- End-to-end request traceability.
- Accurate replacement status visibility.
- No unauthorized replacement requests.

## Open Questions

| Question | Owner | Impact |
| --- | --- | --- |
| Who is the named Product Owner for Card Replacement? | Cards Squad / Product leadership | Required for ongoing approval evidence. |
| Who is the named Business Analyst for Card Replacement? | Cards Squad / Product leadership | Required for requirements ownership. |
| Who is the named Cards Domain Owner? | Product / Technology leadership | Required before final domain approval. |
| Who is the named Cards Architect? | Architecture leadership | Required before design approval. |
| Which Card Processor implementation is in scope for pilot replacement? | Cards Squad / Card Processor owner | Affects design, integration tests, and validation. |
| What replacement status values are customer-safe versus operations-only? | Product / Operations / Security | Affects status tracking scope and visibility. |
| Which notifications are required for Lost, Stolen, and Damaged replacement? | Product / Notification Capability owner | Affects integration scope and exclusions. |

## Human Approval Gate

| Approval | Reference | Approver | Date | Decision |
| --- | --- | --- | --- | --- |
| Intent approval | chat-approval-2026-06-05 | User acting as approval authority | 2026-06-05 | Approved to create the Card Replacement intent artifact. |
