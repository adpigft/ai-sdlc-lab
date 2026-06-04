# Service Catalog Template

## Purpose

Define backend service ownership, deterministic implementation placement, API/event ownership, data ownership, integrations, allowed paths, restricted paths, approvers, and regression scope.

Architecture and implementation planning use the service catalog to decide where backend code belongs before `$implementation` starts.

## Service Catalog Entry Format

| Field | Description |
| --- | --- |
| `domain` | Business domain that owns the service. |
| `service_name` | Stable service name. |
| `service_path` | Planned or existing path, usually `services/<domain>/<service-name>/`. |
| `owning_squad` | Squad accountable for code, contracts, operations, and approvals. |
| `capabilities_served` | Capabilities implemented or supported by the service. |
| `APIs_owned` | Public or internal APIs owned by the service. |
| `events_published` | Events produced by the service. |
| `events_consumed` | Events consumed by the service. |
| `database_ownership` | Data stores and records owned by the service. |
| `integrations` | Third-party and internal integrations used by the service. |
| `allowed_paths` | Paths this service owner may modify for an approved slice. |
| `restricted_paths` | Paths that require other owner approval or must not be touched. |
| `required_approvers` | Required reviewers before implementation or merge. |
| `regression_scope` | Tests and checks required for service changes. |

## Example Service Catalog

| domain | service_name | service_path | owning_squad | capabilities_served | APIs_owned | events_published | events_consumed | database_ownership | integrations | allowed_paths | restricted_paths | required_approvers | regression_scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| payments | local-payment-service | `services/payments/local-payment-service/` | Payments Squad | KHQR Payment, QR Refund lookup support, KHQR Payment Reversal lookup support | `POST /khqr/payments`, `GET /khqr/payments/{paymentId}` | `PaymentInitiated`, `PaymentCompleted`, `PaymentFailed`, `PaymentPending` | processor status events, ledger posting events | Local payment records, payment idempotency records | Payment Processor, Ledger/Core Banking, Audit Store, Reconciliation Platform | `services/payments/local-payment-service/**` | other payment services, cards/deposits/lending services, shared libraries without approval | Payments Squad, Payments Architect, QA Lead | unit, API contract, event contract, payment regression |
| payments | remittance-service | `services/payments/remittance-service/` | Remittance Squad | Domestic remittance, international remittance | remittance command and status APIs | `RemittanceRequested`, `RemittanceCompleted`, `RemittanceFailed` | FX rate events, sanctions screening events, ledger posting events | Remittance records, quote references, remittance idempotency records | FX Provider, Sanctions Screening, Ledger/Core Banking, Notification Service | `services/payments/remittance-service/**` | local payment service, international payment service, non-payments services | Remittance Squad, Payments Architect, Compliance for screening changes | unit, integration, API contract, sanctions/FX regression |
| payments | international-payment-service | `services/payments/international-payment-service/` | International Payments Squad | Cross-border payment initiation and status | international payment command and status APIs | `InternationalPaymentInitiated`, `InternationalPaymentCompleted`, `InternationalPaymentFailed` | FX rate events, sanctions screening events, correspondent bank events | International payment records, FX quote linkage, payment idempotency records | FX Provider, Sanctions Screening, Correspondent Banking, Ledger/Core Banking | `services/payments/international-payment-service/**` | remittance service, local payment service, non-payments services | International Payments Squad, Payments Architect, Compliance | unit, API contract, integration, sanctions/FX regression |
| cards | card-management-service | `services/cards/card-management-service/` | Cards Squad | Card Replacement, Card Activation, Card Controls | card replacement, card activation, card controls APIs | `CardReplacementRequested`, `CardStatusChanged` | customer profile events, fraud events | Card profile, card replacement workflow records | Card Processor, Customer Profile, Fraud Platform, Notification Service | `services/cards/card-management-service/**` | payments/deposits/lending services | Cards Squad, Cards Architect, Security/Risk | unit, API contract, card processor integration, cards regression |
| deposits | account-service | `services/deposits/account-service/` | Deposits Squad | Account Opening, Account Profile, Account Status | account opening and account status APIs | `AccountOpened`, `AccountStatusChanged` | onboarding completed events, KYC decision events | Deposit account records, account lifecycle state | Core Banking, KYC Platform, Customer Profile | `services/deposits/account-service/**` | cards/lending/payments services | Deposits Squad, Deposits Architect, Compliance | unit, API contract, core banking integration, deposits regression |
| lending | loan-service | `services/lending/loan-service/` | Lending Squad | Loan Application, Loan Decisioning, Loan Status | loan application and loan status APIs | `LoanApplicationSubmitted`, `LoanDecisioned` | credit bureau response events, customer profile events | Loan application records, decision state, offer records | Credit Bureau, Decision Engine, Core Banking, Document Service | `services/lending/loan-service/**` | deposits/cards/payments services | Lending Squad, Lending Architect, Risk/Compliance | unit, API contract, decisioning, lending regression |
| onboarding | onboarding-service | `services/onboarding/onboarding-service/` | Onboarding Squad | Digital Onboarding, KYC Orchestration | onboarding application and KYC status APIs | `OnboardingStarted`, `KycCompleted`, `OnboardingCompleted` | identity verification events, document verification events | Onboarding application state, KYC workflow state | Identity Provider, KYC Platform, Document Service, Customer Profile | `services/onboarding/onboarding-service/**` | deposits/cards/lending services | Onboarding Squad, Security/Risk, Compliance | unit, API contract, KYC integration, onboarding regression |
| operations | case-management-service | `services/operations/case-management-service/` | Operations Squad | Case Management, Exception Queue, Investigations | case creation, assignment, investigation, resolution APIs | `CaseCreated`, `CaseAssigned`, `CaseResolved` | payment exception events, refund exception events, reversal exception events | Operations case records, investigation notes | Operations Portal, Audit Store, Notification Service | `services/operations/case-management-service/**` | domain services unless owner approval exists | Operations Squad, impacted domain squad, QA Lead | unit, API contract, case workflow, impacted-domain regression |

## Usage Rules

- Implementation plans must reference the service catalog for backend target placement.
- `allowed_paths` must be narrow enough for the approved slice.
- `restricted_paths` must list nearby paths that are easy to touch accidentally.
- API and event changes require contract and consumer impact review.
- Database ownership changes require service owner and architect approval.

If `target_service`, `allowed_paths`, or `required_approvers` are missing, implementation must not start.
