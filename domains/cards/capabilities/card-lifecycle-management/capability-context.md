# Card Lifecycle Management Capability Context

## Capability Purpose

Card Lifecycle Management owns customer card lifecycle changes in the Cards domain, including replacement, activation, renewal, closure, and card status visibility.

The capability provides a parent business-function boundary for lifecycle features that coordinate card profile state, card processor instructions, customer-safe notifications, customer profile lookups, audit evidence, and operations/customer visibility.

## Business Boundary

Card Lifecycle Management owns:

- card lifecycle state changes for issued customer cards
- lifecycle workflow coordination for replacement, activation, renewal, and closure
- lifecycle status visibility for customer and operations channels
- lifecycle API behavior exposed by the Cards domain
- lifecycle events produced by the Cards domain
- card processor coordination for lifecycle operations
- lifecycle audit and traceability evidence

Card Lifecycle Management does not own:

- card control preferences or usage restrictions
- card transaction processing
- card authorization decisions
- card settlement
- fraud management
- rewards
- notification implementation
- customer profile management

## Owned Features

| Feature | Status | Notes |
| --- | --- | --- |
| Card Replacement | Initial | Feature-level delivery artifact not yet created. |
| Card Activation | Future | Activates newly issued or replaced cards after required verification. |
| Card Renewal | Future | Supports lifecycle renewal for expiring cards. |
| Card Closure | Future | Supports controlled card closure where approved. |
| Card Status Inquiry | Future | Provides customer-safe and operations-safe lifecycle status visibility. |

## Shared Flows

Shared lifecycle flow assumptions:

1. A customer, channel, branch, operations user, or scheduled lifecycle process initiates a lifecycle action.
2. The capability validates actor authorization, card eligibility, card status, and linked customer/account context.
3. The capability coordinates with the card processor when the lifecycle action requires processor execution.
4. The capability records durable lifecycle state and processor references.
5. The capability emits lifecycle events for downstream consumers.
6. The capability triggers customer-safe notification requests where notification is in scope for the feature.
7. The capability records audit evidence for material lifecycle actions.

Feature-level intent, specification, design, tests, validation, and release artifacts will define each flow in detail.

## Shared APIs

| API | Purpose | Ownership | Status |
| --- | --- | --- | --- |
| Card Lifecycle API | Expose lifecycle operations and lifecycle status for Cards features. | Cards Squad | Assumption |

The Card Lifecycle API is the capability-level API boundary. Feature-level contracts will define concrete resources, commands, responses, errors, and compatibility expectations.

## Shared Events

| Event | Purpose | Producer | Status |
| --- | --- | --- | --- |
| `CardReplaced` | Records completed card replacement lifecycle outcome. | Card Lifecycle Management | Assumption |
| `CardActivated` | Records card activation lifecycle outcome. | Card Lifecycle Management | Assumption |
| `CardRenewed` | Records card renewal lifecycle outcome. | Card Lifecycle Management | Assumption |
| `CardClosed` | Records card closure lifecycle outcome. | Card Lifecycle Management | Assumption |

Event schemas, consumers, compatibility rules, and audit requirements must be confirmed during feature design.

## Shared Integrations

| Integration | Direction | Capability Responsibility | Ownership |
| --- | --- | --- | --- |
| Card Processor | Outbound command / inbound status | Coordinate lifecycle execution and store processor references. | Card Processor owner review required. |
| Notification Capability | Outbound request or event | Request customer-safe lifecycle notifications when feature scope requires it. | Consumed dependency; not owned by this capability. |
| Customer Profile Capability | Outbound lookup | Resolve customer identity, contact, and profile context needed for lifecycle decisions. | Consumed dependency; not owned by this capability. |

## Shared State Model

Shared lifecycle state assumptions:

- Card profile lifecycle state is owned by Cards.
- Lifecycle features may introduce feature-specific workflow records, such as replacement request state or renewal state.
- Processor references must be traceable to the lifecycle action that created or changed them.
- Material lifecycle state changes require audit evidence.
- Sensitive card details must be masked in APIs, events, logs, summaries, and validation evidence.

Candidate lifecycle statuses include:

- Pending Activation
- Active
- Replacement Requested
- Replaced
- Renewed
- Closed

Final state names and transitions must be approved during feature design.

## Ownership

| Area | Owner | Status |
| --- | --- | --- |
| Capability owner | Cards Squad | Confirmed by user input. |
| Domain owner | TBD | Open question. |
| Architect | TBD | Open question. |
| API owner | Cards Squad | Assumption. |
| Event producer owner | Cards Squad | Assumption. |
| Card processor integration reviewer | Card Processor owner | Required for feature design. |
| Notification integration reviewer | Notification Capability owner | Required where notification is in scope. |
| Customer profile integration reviewer | Customer Profile Capability owner | Required where customer profile context is in scope. |

## Out Of Scope

- Card Controls
- Card Transaction Processing
- Card Authorization
- Card Settlement
- Fraud Management
- Rewards
- Notification implementation
- Customer Profile management
- Feature-level intent, specification, design, tests, validation, release, or workflow state
- Source code

## Open Questions

| Question | Owner | Impact |
| --- | --- | --- |
| Who is the named Cards Domain Owner? | Product / Technology leadership | Required before final capability approval. |
| Who is the named Cards Architect? | Architecture leadership | Required before feature design approval. |
| Which Card Processor implementation is in scope for the first feature? | Cards Squad / Card Processor owner | Affects integration design and test strategy. |
| Which channels can initiate Card Replacement? | Product / Cards Squad | Affects feature intent and API design. |
| Which actors can view lifecycle status? | Product / Operations / Security | Affects status inquiry and entitlement requirements. |
| Which notification events are required for Card Replacement? | Product / Notification Capability owner | Affects integration scope and out-of-scope boundaries. |

## Review Notes

This capability context is ready for Cards Squad and architect review. It should not be treated as approved until the capability owner and architect accept the boundary, ownership assumptions, dependencies, and open questions.
