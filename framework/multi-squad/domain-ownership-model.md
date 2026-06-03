# Domain Ownership Model

## Purpose

Define how business domains own delivery knowledge, capability artifacts, cross-domain changes, and implementation placement decisions in a multi-squad banking delivery model.

Domain ownership gives each capability a clear accountable business and technology boundary before architecture, implementation planning, or code changes begin.

## Domain, Capability, And Feature Hierarchy

The current pilot framework hierarchy is:

- Domain = architecture boundary
- Capability = delivery unit

Domains own domain context, domain architecture, ownership, core services, core integrations, core events, and frontend/backend ownership assumptions.

Capabilities own the smallest independently deliverable business outcome for the pilot implementation.

The capability folder currently contains:

- intent
- specification
- design
- tests
- validation
- release

Capabilities own the AI-SDLC delivery lifecycle: intent, specification, design, test-design, implementation, pr-review, validation, release, and feedback.

Example:

```text
Cards
├── Card Replacement
├── Card Activation
├── Card Renewal
└── Card Closure
```

The AI-SDLC lifecycle runs at capability level for the pilot. Domain context guides the capability. Capability implementation can be delivered in smaller implementation slices. Slices are implementation increments inside a capability; they are not capabilities.

The capability folder represents the smallest independently deliverable business outcome for the pilot implementation. A future framework version may introduce an explicit feature layer if required.

## Domain Owner Responsibilities

The domain owner is accountable for:

- maintaining `domains/<domain>/domain-context.md`
- approving domain language, glossary, and business boundaries
- confirming which capabilities belong inside the domain
- identifying impacted services, frontend modules, APIs, events, and shared assets
- reviewing cross-domain impacts
- confirming owner delegation for capabilities or service/module areas
- ensuring traceability stays aligned to domain rules and approvals

The domain owner may delegate capability ownership to a product squad, but the domain owner remains accountable for domain-level consistency.

## Domain Context Ownership

`domains/<domain>/domain-context.md` is owned by the domain owner.

The domain context should define:

- glossary and domain language
- business boundaries
- shared rules
- reusable patterns
- APIs and integrations
- event ownership
- data ownership
- security and risk constraints
- operational expectations

Capability artifacts inherit the domain language and rules from this file.

## Capability Ownership

Capabilities inherit domain ownership unless explicitly delegated.

Delegation should identify:

- capability owner
- owning squad
- impacted service owner
- impacted frontend module owner
- API/event owners
- required approvers
- allowed and restricted implementation paths

If delegation is unclear, the domain owner is the default approver and must resolve ownership before implementation planning.

## Cross-Domain Change Rules

Cross-domain changes require impacted domain owner review.

Examples of cross-domain impact:

- a payments feature needs card status or card controls
- an onboarding feature creates deposit account state
- a lending feature consumes deposit or cards transaction data
- operations case management changes investigation flows for payments, cards, deposits, or lending
- a shared event schema affects producer and consumer domains

Rules:

- Identify impacted domains during architecture or change impact analysis.
- Do not update another domain's artifacts, service, app module, event, or API without owner approval.
- Record impacted owners in the implementation plan or change/defect analysis.
- Add consumer impact review when APIs or events change.

## Domain Examples

| Domain | Domain Owner | Example Capabilities | Typical Services | Typical Frontend Module |
| --- | --- | --- | --- | --- |
| onboarding | Onboarding Domain Owner | Digital Onboarding, KYC Capture | `services/onboarding/onboarding-service/` | `apps/mobile-banking-app/features/onboarding/` |
| deposits | Deposits Domain Owner | Account Opening, Account Profile | `services/deposits/account-service/` | `apps/mobile-banking-app/features/deposits/` |
| payments | Payments Domain Owner | KHQR Payment Reversal, QR Refund, Remittance | `services/payments/local-payment-service/`, `services/payments/remittance-service/` | `apps/mobile-banking-app/features/payments/` |
| cards | Cards Domain Owner | Card Replacement, Card Controls | `services/cards/card-management-service/` | `apps/mobile-banking-app/features/cards/` |
| lending | Lending Domain Owner | Loan Application, Loan Status | `services/lending/loan-service/` | `apps/mobile-banking-app/features/lending/` |
| operations | Operations Domain Owner | Case Management, Exception Queue | `services/operations/case-management-service/` | `apps/mobile-banking-app/features/operations/` |

## Review Checklist

Before `$intent` in a new domain:

- `domains/<domain>/domain-context.md` exists
- domain owner is known
- initial service ownership is known
- frontend feature module ownership is known
- API/event/integration ownership is known

Before `$implementation`:

- capability ownership is clear
- target service/app/library ownership is clear
- cross-domain impacts are reviewed
- allowed and restricted paths are recorded
