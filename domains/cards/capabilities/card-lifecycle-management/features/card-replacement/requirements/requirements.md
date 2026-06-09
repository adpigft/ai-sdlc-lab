# Card Replacement Requirements

## Metadata

| Field | Value |
| --- | --- |
| Requirements ID | REQ-CARDREP-001 |
| Intent ID | INT-CARDREP-001 |
| Jira Epic | TBD |
| Domain | Cards |
| Capability | Card Lifecycle Management |
| Feature | Card Replacement |
| Owner | Cards Squad |
| Status | Draft for PO / BA review |
| Source Intent | `domains/cards/capabilities/card-lifecycle-management/features/card-replacement/intent/intent.md` |

## Overview

Card Replacement enables eligible customers and operations users to request replacement of lost, stolen, or damaged cards through approved digital channels. The pilot supports Mobile App and Operations Portal journeys, requires address confirmation, blocks Lost and Stolen cards, preserves audit and traceability evidence, and provides replacement status visibility.

This requirements artifact defines requirements only. It does not create design, API contracts, tests, implementation, validation, release artifacts, or source code.

## Requirement Gaps Carried Forward

These gaps do not block draft requirements creation, but they must be resolved before the downstream stage indicated.

| Gap ID | Gap | Required Resolution |
| --- | --- | --- |
| GAP-CARDREP-001 | Product Owner and Business Analyst names are unresolved. | Required before requirements approval. |
| GAP-CARDREP-002 | Cards Domain Owner is unresolved. | Required before final domain approval and owner escalation. |
| GAP-CARDREP-003 | Cards Architect is unresolved. | Architect assignment is required for design approval, not for design creation. |
| GAP-CARDREP-004 | Euronet Card Processor is the assumed pilot processor. Card Replacement owns the pilot replacement journey and directly coordinates required processor blocking for Lost and Stolen replacement reasons. | Design must confirm Euronet integration details, error handling, and evidence requirements. |
| GAP-CARDREP-005 | Notification expectations for Lost, Stolen, and Damaged replacement are unresolved. | Required before notification requirements, design, or tests are approved. |
| GAP-CARDREP-006 | Customer-safe and operations-only status values are approved for requirements baseline. | Design must map internal transitions to these approved status values. |

## Actors

| Actor | Description |
| --- | --- |
| Customer | Authenticated cardholder using the Mobile App to request replacement for their own eligible card. |
| Operations User | Authorized bank operations user using the Operations Portal to request replacement on behalf of a customer. |
| Support / Operations Viewer | Authorized user who can view replacement status and safe operational details. |
| Cards Squad | Capability owner responsible for Card Replacement behavior and coordination. |

## Functional Requirements

| Req ID | Requirement | Priority | Acceptance Criteria | Jira |
| --- | --- | --- | --- | --- |
| FR-CARDREP-001 | The system shall allow an authenticated eligible customer to request card replacement through the Mobile App. | Must | Given an authenticated eligible customer and an eligible card, when the customer submits a valid replacement request through Mobile App, then a replacement request is created with a trackable status. | TBD |
| FR-CARDREP-002 | The system shall allow an authorized operations user to request card replacement through the Operations Portal. | Must | Given an authorized operations user and an eligible customer card, when the operations user submits a valid replacement request through Operations Portal, then a replacement request is created with a trackable status. | TBD |
| FR-CARDREP-003 | The system shall reject replacement requests from unsupported channels. | Must | Given a request from Web Banking, Branch Channel, or any unapproved channel, when submitted, then the request is rejected and no replacement request is created. | TBD |
| FR-CARDREP-004 | The system shall support Lost Card, Stolen Card, and Damaged Card as pilot replacement reasons. | Must | Given a replacement request with Lost Card, Stolen Card, or Damaged Card reason, when all other eligibility checks pass, then the reason is accepted. | TBD |
| FR-CARDREP-005 | The system shall reject replacement reasons outside pilot scope. | Must | Given a request for Expired Card, Fraud Reissue, Name Change, Product Upgrade/Downgrade, Card Renewal, or other unsupported reason, when submitted, then the request is rejected with an actor-safe reason. | TBD |
| FR-CARDREP-006 | The system shall require address confirmation before replacement request submission. | Must | Given a customer or operations user has not confirmed the delivery address, when they attempt to submit a replacement request, then submission is blocked until address confirmation is completed. | TBD |
| FR-CARDREP-007 | The system shall preserve the confirmed address reference used for replacement request traceability. | Must | Given a replacement request is submitted after address confirmation, when the request is stored, then the confirmed address source or reference is retained for audit and support evidence. | TBD |
| FR-CARDREP-008 | The system shall directly coordinate Card Processor blocking for Lost Card replacement requests. | Must | Given a Lost Card replacement request, when submitted, then Card Replacement invokes the Card Processor to block the existing card and the request must not proceed to successful submission unless blocking succeeds. | TBD |
| FR-CARDREP-009 | The system shall directly coordinate Card Processor blocking for Stolen Card replacement requests. | Must | Given a Stolen Card replacement request, when submitted, then Card Replacement invokes the Card Processor to block the existing card and the request must not proceed to successful submission unless blocking succeeds. | TBD |
| FR-CARDREP-010 | The system shall not require card blocking for Damaged Card replacement requests in the pilot unless Card Processor rules require it. | Must | Given a Damaged Card replacement request, when submitted, then replacement can proceed without mandatory card blocking unless the Card Processor requires blocking for that card or product. | TBD |
| FR-CARDREP-011 | The system shall charge no replacement fee for pilot replacement requests. | Must | Given any in-scope pilot replacement request, when submitted, then no fee is charged or assessed. | TBD |
| FR-CARDREP-012 | The system shall not require maker-checker approval for pilot replacement requests. | Must | Given an in-scope pilot replacement request, when submitted by an authorized actor, then no maker-checker approval step is required before request creation. | TBD |
| FR-CARDREP-013 | The system shall enforce authorization for customer and operations replacement journeys. | Must | Given an unauthorized actor, when they attempt to submit or view a replacement request, then the action is rejected and no unauthorized request or status disclosure occurs. | TBD |
| FR-CARDREP-014 | The system shall prevent customers from requesting replacement for cards they are not authorized to manage. | Must | Given a customer attempts to replace a card not linked to them or not available for customer self-service, when submitted, then the request is rejected. | TBD |
| FR-CARDREP-015 | The system shall validate that the card is eligible for replacement. | Must | Given a card is closed, already replaced, not found, or otherwise ineligible, when replacement is requested, then the request is rejected with an actor-safe reason. | TBD |
| FR-CARDREP-016 | The system shall create a unique replacement request reference for every accepted replacement request. | Must | Given a valid replacement request, when accepted, then the system returns and stores a unique replacement request reference. | TBD |
| FR-CARDREP-017 | The system shall provide replacement status tracking for customers and authorized operations users. | Must | Given an authorized actor, when they request replacement status, then the system returns the current status and actor-appropriate safe details. | TBD |
| FR-CARDREP-018 | The system shall preserve end-to-end traceability for replacement requests. | Must | Given a replacement request is created or updated, when the record is stored, then actor, channel, card reference, reason, address confirmation, blocking requirement, processor reference where available, status, timestamps, and correlation ID are traceable. | TBD |
| FR-CARDREP-019 | The system shall create audit evidence for material replacement actions. | Must | Given replacement request submission, rejection, card blocking outcome, status change, processor coordination, or unauthorized attempt, when the event occurs, then audit evidence is captured with masked sensitive details. | TBD |
| FR-CARDREP-020 | The system shall coordinate directly with the Card Processor for pilot replacement lifecycle actions, including required Lost and Stolen card blocking. | Must | Given a replacement request that requires Card Processor coordination, when the processor action is initiated or updated, then processor references and outcomes are captured for status and audit evidence. | TBD |
| FR-CARDREP-021 | The system shall not provide instant digital card issuance as part of pilot replacement. | Must | Given a replacement request is accepted, when the response or status is shown, then it does not create or imply an instant digital card. | TBD |
| FR-CARDREP-022 | The system shall not provide manufacturing, logistics, or external courier tracking status as part of pilot replacement. | Must | Given a replacement request is accepted, when status is shown, then manufacturing, logistics, and external courier tracking details are not exposed as feature-owned status. | TBD |
| FR-CARDREP-023 | The system shall support customer-safe and operations-safe replacement status visibility. | Must | Given customer and operations users request the same replacement status, when details differ by actor, then each actor sees only information approved for that actor type. | TBD |
| FR-CARDREP-024 | The system shall consume Customer Profile context only for replacement eligibility and address confirmation purposes. | Must | Given customer profile data is needed, when the replacement journey uses it, then the feature consumes only approved profile and address context and does not manage customer profile records. | TBD |
| FR-CARDREP-025 | The system shall consume Notification Capability only where notification expectations are approved. | Should | Given notification expectations are approved, when a notifiable replacement event occurs, then the feature requests notification through the Notification Capability without owning notification implementation. | TBD |
| FR-CARDREP-026 | The system shall not provide standalone card controls, usage restrictions, or manual block/unblock journeys as part of Card Replacement. | Must | Given an actor attempts a standalone block, unblock, usage-control, or limit-control action through Card Replacement, when submitted, then the action is rejected or routed outside this feature according to approved channel behavior. | TBD |

## Non-Functional Requirements

| Req ID | Requirement | Measure | Jira |
| --- | --- | --- | --- |
| NFR-CARDREP-001 | Replacement request submission shall be auditable. | 100% of accepted requests, rejected requests, unauthorized attempts, and material status changes have audit evidence. | TBD |
| NFR-CARDREP-002 | Sensitive card and customer data shall be protected. | Full PAN and sensitive customer data are not exposed in logs, events, summaries, validation evidence, or actor-visible responses unless explicitly authorized. | TBD |
| NFR-CARDREP-003 | Replacement request traceability shall be complete. | Each accepted request has a replacement reference, card reference, actor, channel, reason, confirmed address reference, status, timestamps, and correlation ID. | TBD |
| NFR-CARDREP-004 | Unauthorized replacement requests shall be prevented. | No accepted replacement request can be created by an unauthenticated actor, unauthorized customer, or operations user without required entitlement. | TBD |
| NFR-CARDREP-005 | Replacement status visibility shall be actor-safe. | Customer and operations status responses expose only approved fields for the requesting actor. | TBD |
| NFR-CARDREP-006 | The replacement journey shall be observable. | Metrics, logs, traces, and alerts exist for request submission, rejection, unauthorized attempts, blocking-required outcomes, processor coordination, and status changes. | TBD |
| NFR-CARDREP-007 | Card blocking for Lost and Stolen requests shall fail safely. | A Lost or Stolen replacement must not proceed to successful submission unless the required Card Processor blocking outcome succeeds. Failed or unavailable blocking produces a safe rejection or failure status with audit evidence. | TBD |
| NFR-CARDREP-008 | Pilot fee handling shall be deterministic. | No in-scope pilot replacement request creates a fee assessment, charge, waiver record, or customer-facing fee due. | TBD |
| NFR-CARDREP-009 | Delivery pipeline evidence shall be required before release once application code exists. | GitHub Actions, relevant tests, security checks, and quality evidence are linked in validation evidence. | TBD |

## Business Rules

| Rule ID | Rule | Source | Requirement Links |
| --- | --- | --- | --- |
| BR-CARDREP-001 | Pilot replacement reasons are Lost Card, Stolen Card, and Damaged Card only. | Approved intent | FR-CARDREP-004, FR-CARDREP-005 |
| BR-CARDREP-002 | Mobile App and Operations Portal are the only pilot channels. | Approved intent | FR-CARDREP-001, FR-CARDREP-002, FR-CARDREP-003 |
| BR-CARDREP-003 | Address confirmation is required before replacement request submission. | Approved intent | FR-CARDREP-006, FR-CARDREP-007 |
| BR-CARDREP-004 | Lost Card and Stolen Card replacement require Card Replacement to coordinate direct Card Processor blocking of the existing card. | Approved intent and requirements review decision | FR-CARDREP-008, FR-CARDREP-009, FR-CARDREP-020 |
| BR-CARDREP-005 | Damaged Card replacement does not require card blocking for the pilot unless Card Processor rules require it. | Approved intent and requirements review decision | FR-CARDREP-010 |
| BR-CARDREP-006 | No replacement fee applies during the pilot. | Approved intent | FR-CARDREP-011 |
| BR-CARDREP-007 | Maker-checker approval is not required during the pilot. | Approved intent | FR-CARDREP-012 |
| BR-CARDREP-008 | Branch-assisted replacement and Web Banking replacement are out of scope. | Approved intent | FR-CARDREP-003 |
| BR-CARDREP-009 | Card Renewal, Expired Card replacement, Fraud Reissue, Name Change, and Product Upgrade/Downgrade are out of pilot scope. | Approved intent | FR-CARDREP-005 |
| BR-CARDREP-010 | Notification implementation remains outside Card Replacement ownership. | Approved intent | FR-CARDREP-025 |
| BR-CARDREP-011 | Customer Profile management remains outside Card Replacement ownership. | Approved intent | FR-CARDREP-024 |
| BR-CARDREP-012 | Manufacturing, logistics, and external courier tracking are out of scope. | Approved intent | FR-CARDREP-022 |
| BR-CARDREP-013 | Card Controls remains out of scope; standalone block/unblock journeys, usage controls, and limit controls are not part of Card Replacement. | Specification review decision | FR-CARDREP-026 |

## Replacement Status Visibility

Approved customer-safe statuses:

| Status | Meaning | Actor Visibility |
| --- | --- | --- |
| Submitted | Replacement request is received and traceable. | Customer |
| In Progress | Replacement request is being processed. | Customer |
| Completed | Replacement request completed through approved pilot scope. | Customer |
| Rejected | Replacement request failed eligibility, authorization, address confirmation, processor blocking, or other approved checks. | Customer |

Approved operations-only statuses:

| Status | Meaning | Actor Visibility |
| --- | --- | --- |
| Pending Processor | Euronet Card Processor coordination is waiting or not final. | Operations |
| Processor Accepted | Euronet Card Processor accepted the replacement or blocking-related instruction. | Operations |
| Processor Failed | Euronet Card Processor rejected, failed, or could not complete the required instruction. | Operations |
| Awaiting Fulfilment | Replacement request is accepted and waiting for fulfilment activities outside detailed pilot tracking. | Operations |
| Fulfilment Completed | Fulfilment completion has been recorded at the approved pilot visibility level. | Operations |

Design must define internal transitions and API mapping without exposing operations-only statuses to customers.

## Acceptance Criteria

| AC ID | Requirement | Acceptance Criteria |
| --- | --- | --- |
| AC-CARDREP-001 | FR-CARDREP-001 | Customer can submit a valid Lost, Stolen, or Damaged replacement request through Mobile App. |
| AC-CARDREP-002 | FR-CARDREP-002 | Operations user with entitlement can submit a valid replacement request through Operations Portal. |
| AC-CARDREP-003 | FR-CARDREP-003 | Web Banking, Branch Channel, and unapproved channels cannot create pilot replacement requests. |
| AC-CARDREP-004 | FR-CARDREP-004, FR-CARDREP-005 | In-scope reasons are accepted and out-of-scope reasons are rejected. |
| AC-CARDREP-005 | FR-CARDREP-006, FR-CARDREP-007 | Request cannot be submitted until address is confirmed and address reference is traceable. |
| AC-CARDREP-006 | FR-CARDREP-008, FR-CARDREP-009 | Lost and Stolen requests invoke Card Processor blocking and cannot proceed to successful submission unless blocking succeeds. |
| AC-CARDREP-007 | FR-CARDREP-010 | Damaged replacement can proceed without mandatory card blocking unless Card Processor rules require blocking. |
| AC-CARDREP-008 | FR-CARDREP-011 | Pilot replacement does not charge or assess a replacement fee. |
| AC-CARDREP-009 | FR-CARDREP-012 | Pilot replacement does not require maker-checker approval. |
| AC-CARDREP-010 | FR-CARDREP-013, FR-CARDREP-014 | Unauthorized actors cannot create or view replacement requests. |
| AC-CARDREP-011 | FR-CARDREP-015 | Ineligible cards are rejected with actor-safe reason. |
| AC-CARDREP-012 | FR-CARDREP-016, FR-CARDREP-018 | Accepted requests receive a unique reference and preserve traceability fields. |
| AC-CARDREP-013 | FR-CARDREP-017, FR-CARDREP-023 | Customers and operations users can view approved replacement status details for their actor type. |
| AC-CARDREP-014 | FR-CARDREP-019 | Material replacement actions produce audit evidence. |
| AC-CARDREP-015 | FR-CARDREP-020 | Card Processor references and outcomes are captured when replacement coordination or required blocking occurs. |
| AC-CARDREP-016 | FR-CARDREP-021, FR-CARDREP-022 | Pilot status and responses do not include instant digital card, logistics, manufacturing, or courier-tracking capabilities. |
| AC-CARDREP-017 | FR-CARDREP-024 | Customer Profile data is consumed for approved replacement purposes only. |
| AC-CARDREP-018 | FR-CARDREP-025 | Notifications are requested only when notification expectations are approved. |
| AC-CARDREP-019 | FR-CARDREP-026 | Standalone block/unblock journeys, usage controls, and limit controls cannot be performed through Card Replacement. |

## Edge Cases

| Scenario ID | Scenario | Expected Outcome |
| --- | --- | --- |
| EDGE-CARDREP-001 | Customer attempts replacement for a card not linked to the customer. | Request is rejected; no replacement request is created. |
| EDGE-CARDREP-002 | Operations user lacks replacement entitlement. | Request is rejected as unauthorized. |
| EDGE-CARDREP-003 | Replacement reason is Expired Card, Fraud Reissue, Name Change, Product Upgrade/Downgrade, or Renewal. | Request is rejected as out of scope. |
| EDGE-CARDREP-004 | Customer starts request but does not confirm address. | Submission is blocked until address confirmation is completed. |
| EDGE-CARDREP-005 | Address source is unavailable. | Submission is blocked or routed to an approved safe failure outcome; no unconfirmed address is used. |
| EDGE-CARDREP-006 | Lost or Stolen request cannot complete required Card Processor blocking. | Replacement does not proceed to successful submission; safe rejection or failure status is visible and audit evidence is captured. |
| EDGE-CARDREP-007 | Damaged request is submitted for a card already closed or replaced. | Request is rejected as ineligible. |
| EDGE-CARDREP-008 | Web Banking or Branch Channel submits request. | Request is rejected as unsupported channel. |
| EDGE-CARDREP-009 | Actor requests status for a replacement they are not authorized to view. | Status request is rejected and no sensitive details are exposed. |
| EDGE-CARDREP-010 | Card Processor coordination is unavailable. | Lost or Stolen replacement does not proceed to successful submission; Damaged replacement proceeds only if processor rules do not require blocking or other unavailable processor coordination. Traceability and audit evidence are preserved. |
| EDGE-CARDREP-011 | Audit evidence cannot be persisted. | Material state change must not complete without durable audit evidence or approved durable buffering. |
| EDGE-CARDREP-012 | Notification expectation is not approved. | Replacement processing continues without feature-owned notification implementation. |
| EDGE-CARDREP-013 | Actor attempts standalone block, unblock, usage-control, or limit-control action through Card Replacement. | Action is rejected or routed outside this feature; no Card Controls behavior is performed by Card Replacement. |

## Dependencies

| Dependency | Purpose | Status |
| --- | --- | --- |
| Euronet Card Processor | Direct processor blocking for Lost/Stolen replacement and replacement lifecycle coordination. | Assumed pilot processor; design input required for integration details. |
| Card Controls | Standalone block/unblock journeys, usage controls, and limit controls. | Out of scope; not consumed for pilot replacement blocking. |
| Customer Profile Capability | Customer profile and address context for confirmation. | Consumed dependency; ownership external. |
| Notification Capability | Customer-safe notifications where approved. | Expectations unresolved; consumed dependency only. |
| Mobile App | Customer replacement request channel. | In pilot scope. |
| Operations Portal | Operations-user replacement request channel. | In pilot scope. |
| Audit Store | Durable audit evidence for material events. | Required. |

## Assumptions

- Cards Squad owns Card Replacement under Card Lifecycle Management.
- Card Replacement owns the pilot replacement journey and directly coordinates required Card Processor blocking for Lost and Stolen replacement.
- Lost and Stolen replacement require successful Card Processor blocking before successful submission.
- Damaged replacement does not require card blocking for pilot unless Card Processor rules require it.
- Euronet Card Processor is the assumed pilot processor.
- Customer-safe replacement statuses are Submitted, In Progress, Completed, and Rejected.
- Operations-only statuses are Pending Processor, Processor Accepted, Processor Failed, Awaiting Fulfilment, and Fulfilment Completed.
- Card Controls remains out of scope because standalone block/unblock journeys and customer usage controls are not part of Card Replacement.
- Address confirmation is mandatory before request submission.
- No replacement fee applies during the pilot.
- Maker-checker approval is not required during the pilot.
- Mobile App and Operations Portal are the only pilot channels.
- Notification Capability and Customer Profile Capability are consumed dependencies and are not owned by this feature.
- Detailed Euronet Card Processor integration behavior is not decided in this requirements artifact.

## Open Questions

| Question | Owner | Due Date | Status |
| --- | --- | --- | --- |
| Who is the named Product Owner for Card Replacement? | Cards Squad / Product leadership | Before requirements approval | Open |
| Who is the named Business Analyst for Card Replacement? | Cards Squad / Product leadership | Before requirements approval | Open |
| Who is the named Cards Domain Owner? | Product / Technology leadership | Before final domain approval | Open |
| Who is the named Cards Architect? | Architecture leadership | Required for design approval, not design creation | Open |
| What Euronet Card Processor integration details, error mappings, and evidence fields are required for pilot replacement and blocking? | Cards Squad / Card Processor owner | Before design approval | Open |
| Which notifications are required for Lost, Stolen, and Damaged replacement? | Product / Notification Capability owner | Before notification requirements, design, or tests are approved | Open |
| What target should be used for reduced branch dependency? | Product Owner / BA | Before validation planning | Open |
| What target should be used for replacement status visibility accuracy? | Product Owner / QA | Before validation planning | Open |

## Review Gate

| Approval | Reference | Approver | Date | Decision |
| --- | --- | --- | --- | --- |
| Specification review | TBD | Product Owner / Business Analyst | TBD | Pending review. |
