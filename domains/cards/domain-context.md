# Cards Domain Context

## Purpose

Capture shared Cards domain language, boundaries, ownership, placement assumptions, APIs, events, integrations, NFR considerations, and open questions before any Cards capabilities are created.

This file is domain-level delivery context. Capability-specific source of truth will live under `domains/cards/capabilities/<capability>/` after domain onboarding is reviewed and approved.

## Domain Purpose

The Cards domain manages customer card lifecycle and card controls for banking channels and operations.

## Business Scope

In scope for the Cards domain:

- card replacement
- card activation
- card status and lifecycle controls
- card blocking and unblocking
- card limit and control preferences, when approved
- card processor coordination
- card customer and operations visibility
- card-related audit, notification, and fraud integration events

## Boundaries

Cards owns:

- card profile and lifecycle workflow state
- card replacement workflow records
- card control changes owned by the bank
- card status APIs and events
- card processor integration behavior for card lifecycle operations
- card-domain audit and reconciliation evidence

Cards does not own:

- customer identity proofing owned by Onboarding
- deposit account lifecycle owned by Deposits
- payment execution owned by Payments
- lending decisioning owned by Lending
- operations case workflow owned by Operations
- shared mobile app shell or shared frontend components owned by Channel Platform
- shared libraries, event templates, observability templates, or platform CI templates

Cross-domain changes require impacted domain owner review.

## Glossary

| Term | Meaning |
| --- | --- |
| Card | Payment card or bank card issued to a customer. |
| Cardholder | Customer assigned to use a card. |
| Card Profile | Domain record containing card identity, masked card details, lifecycle status, and related customer/account references. |
| Card Replacement | Process for issuing a replacement card due to loss, damage, expiry, fraud, or customer request. |
| Card Activation | Process that marks a newly issued or replaced card as active after required verification. |
| Card Control | Customer or bank setting that affects card usage, such as block, unblock, channel control, or limit control. |
| Card Processor | External or internal processor that executes card lifecycle and authorization-control operations. |
| Replacement Request | Customer, branch, or operations request to replace a card. |
| Card Status | Lifecycle state such as active, inactive, blocked, replaced, expired, pending activation, or closed. |
| Processor Reference | Reference returned by the card processor for lifecycle or control actions. |
| Audit Event | Immutable record of a material card lifecycle, control, or security event. |
| Correlation ID | Identifier used to trace a request across APIs, services, events, logs, and support evidence. |

## Core Entities

| Entity | Description | Ownership |
| --- | --- | --- |
| Card Profile | Card identity, masked card detail, lifecycle state, and linked customer/account references. | Cards |
| Card Replacement Request | Request and workflow state for replacing a card. | Cards |
| Card Control Setting | Bank-owned or customer-owned card control state. | Cards |
| Card Processor Instruction | Command sent to processor for replacement, activation, block, unblock, or control change. | Cards with Card Processor integration owner review |
| Card Audit Event | Immutable evidence for lifecycle, control, security, and operations actions. | Cards / Audit platform |

## Candidate Capabilities

| Capability | Description | Initial Owner |
| --- | --- | --- |
| Card Lifecycle Management | Manage customer card lifecycle changes including replacement, activation, renewal, closure, and status inquiry. | Cards Squad |
| Card Controls | Support customer or operations controls such as block, unblock, and usage restrictions. | Cards Squad |

## Candidate Features By Capability

| Capability | Candidate Features |
| --- | --- |
| Card Lifecycle Management | Card Replacement; Card Activation; Card Renewal; Card Closure; Card Status Inquiry |
| Card Controls | Block Card; Unblock Card; Usage Controls; Limit Controls |

## Owned APIs

Planned APIs, subject to capability-level requirements and architecture approval:

| API | Purpose | Owner | Status |
| --- | --- | --- | --- |
| `POST /cards/{cardId}/replacement-requests` | Request a card replacement. | Cards Squad | Assumption |
| `GET /cards/{cardId}/status` | Retrieve customer-safe card status. | Cards Squad | Assumption |
| `POST /cards/{cardId}/activation` | Activate a card after required verification. | Cards Squad | Assumption |
| `POST /cards/{cardId}/controls` | Change card controls, if approved for scope. | Cards Squad | Open question |
| `POST /operations/cards/{cardId}/controls` | Operations card control action, if approved. | Cards Squad / Operations review | Open question |

## Published Events

Planned events, subject to event catalog and consumer impact review:

| Event | Purpose | Producer | Known Consumers | Status |
| --- | --- | --- | --- | --- |
| `CardReplacementRequested` | Records accepted card replacement request. | `card-management-service` | Operations, audit, notification | Assumption |
| `CardReplacementCompleted` | Records completed replacement lifecycle. | `card-management-service` | Notification, operations, reporting | Assumption |
| `CardStatusChanged` | Records material lifecycle status change. | `card-management-service` | Fraud, notification, operations, audit | Assumption |
| `CardControlChanged` | Records material card control change. | `card-management-service` | Fraud, audit, notification | Open question |

## Consumed Events

| Event | Purpose | Producer | Cards Usage | Status |
| --- | --- | --- | --- | --- |
| `CustomerProfileUpdated` | Customer profile or contact changes. | Customer Profile / Onboarding | Keep cardholder contact and notification context current. | Assumption |
| `FraudCaseCreated` | Fraud signal or case impacting card controls. | Fraud Platform | Support card block or review workflows. | Open question |
| `AccountStatusChanged` | Deposit account status changes. | Deposits | Determine whether card controls must change when linked account changes. | Open question |

## Integrations

| Integration | Responsibility | Owner / Reviewer | Status |
| --- | --- | --- | --- |
| Card Processor | Execute card replacement, activation, block, unblock, and control actions. | Cards Squad / Card Processor owner | Assumption |
| Customer Profile | Resolve customer and contact context. | Customer Profile owner | Assumption |
| Core Banking | Validate linked account relationships where card lifecycle depends on account state. | Deposits / Core Banking owner | Open question |
| Fraud Platform | Consume or provide fraud-related card status/control signals. | Fraud / Security owner | Open question |
| Notification Service | Send customer-safe card lifecycle notifications. | Channel Platform / Notification owner | Assumption |
| Audit Store | Persist immutable material card events. | Audit platform owner | Assumption |
| Operations Portal | Operations visibility and privileged actions. | Operations owner | Open question |

## Ownership

| Area | Owner | Notes |
| --- | --- | --- |
| Domain context | Cards Domain Owner | Open question until named by stakeholders. |
| Primary squad | Cards Squad | Assumed for initial onboarding. |
| Solution architecture | Cards Architect | Open question until assigned. |
| Frontend feature module | Cards Squad | Requires Channel Platform review for shell/shared changes. |
| Backend service | Cards Squad | Planned `card-management-service`. |
| API ownership | Cards Squad | API changes require architecture, QA, security, and consumer review. |
| Event ownership | Cards Squad as producer; impacted consumers as reviewers | Event changes require producer and consumer review. |

## Frontend Placement Assumptions

| Field | Value |
| --- | --- |
| `target_app` | `mobile-banking-app` |
| `target_frontend_module` | `apps/mobile-banking-app/features/cards/` |
| Shell owner | Channel Platform Squad |
| Shared component owner | Channel Platform Squad |
| Feature owner squad | Cards Squad |
| Allowed paths | `apps/mobile-banking-app/features/cards/**` |
| Restricted paths | app shell, shared components, other domain feature modules |
| Required approvals | Cards Squad; Channel Platform for shell/shared impact |

The frontend folders are placement assumptions only. This onboarding does not create app folders.

## Backend Service Placement Assumptions

| Field | Value |
| --- | --- |
| `target_service` | `card-management-service` |
| Service path | `services/cards/card-management-service/` |
| Owning squad | Cards Squad |
| Capabilities served | Card Lifecycle Management, Card Controls |
| Card Lifecycle Management features | Card Replacement, Card Activation, Card Renewal, Card Closure, Card Status Inquiry |
| Card Controls features | Block Card, Unblock Card, Usage Controls, Limit Controls |
| Allowed paths | `services/cards/card-management-service/**` |
| Restricted paths | payments, deposits, lending, onboarding, operations services; shared libraries without approval |
| Required approvers | Cards Squad, Cards Architect, QA Lead, Security/Risk where controls or fraud impact exist |
| Regression scope | unit, API contract, card processor integration, event contract, cards regression |

The service folder is a placement assumption only. This onboarding does not create service folders.

## Shared Asset Impacts

| Shared Asset | Potential Impact | Required Review |
| --- | --- | --- |
| design-system | Card screens may need shared card display, status, or controls components. | Channel Platform |
| audit-library | Card lifecycle events require immutable audit evidence. | Platform Engineering / Audit owner |
| error-model | Card APIs need stable actor-safe error responses. | API Platform |
| observability-library | Card lifecycle metrics, logs, traces, and alerts. | DevSecOps Platform |
| kafka-event-template | Card events may need schema templates and compatibility checks. | Event Platform |

Shared asset changes require owner and impacted consumer approval before implementation.

## NFR Considerations

| NFR | Consideration | Status |
| --- | --- | --- |
| Security | Card data must be masked; no full PAN or sensitive card data in logs, APIs, events, or evidence. | Required |
| Privacy | Customer/cardholder data must be exposed only to authorized actors. | Required |
| Audit | Material lifecycle and control changes require immutable audit evidence. | Required |
| Availability | Card status and controls may require high availability; target pending approval. | Open question |
| Performance | Card status and control actions need approved response targets. | Open question |
| Idempotency | Lifecycle and control commands should be duplicate-safe. | Required for command APIs |
| Observability | Metrics, logs, traces, and alerts are needed for processor failures and stuck workflows. | Required |
| Compatibility | API and event changes require consumer impact review. | Required |

## Out Of Scope

- Capability-specific intent, requirements, architecture, tests, validation, release, and workflow state.
- Source code.
- App, service, library, or platform folder creation.
- Card processor implementation internals.
- Fraud decisioning internals.
- Core banking account lifecycle.
- Payments execution.
- Operations case management workflow.

## Open Questions

| Question | Owner | Impact |
| --- | --- | --- |
| Who is the named Cards Domain Owner? | Product / Technology leadership | Required before approval. |
| Who is the Cards Architect? | Architecture leadership | Required before architecture approval. |
| Which card processor integration is in scope for Card Lifecycle Management? | Cards Domain Owner | Affects API, integration, and test design. |
| Which card controls are in scope for MVP? | Product / Risk / Security | Affects API and event scope. |
| Which operations actions are allowed for Cards? | Operations / Security | Affects frontend, API, entitlement, and audit design. |
| Are card events published through Kafka or another event platform? | Event Platform | Affects event catalog and compatibility checks. |
| What availability and performance targets apply? | Product / SRE / QA | Blocks final NFR validation planning. |

## Next Steps

1. Review this Cards domain context.
2. Resolve or accept open questions.
3. Confirm domain owner, Cards Squad, Cards Architect, and required approvers.
4. Approve domain onboarding.
5. Use `Card Lifecycle Management` as the parent capability for Card Replacement, Card Activation, Card Renewal, Card Closure, and Card Status Inquiry feature delivery.
6. Use `Card Controls` as the parent capability for Block Card, Unblock Card, Usage Controls, and Limit Controls feature delivery.
