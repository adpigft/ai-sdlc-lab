# KHQR Payment Context

## Capability Boundary

The KHQR payment capability covers the customer-facing initiation and status inquiry flow for merchant QR payments in mobile banking. It does not own customer authentication, account master data, merchant onboarding, ledger posting, dispute management, or processor settlement.

## Domain Language

| Term | Meaning |
| --- | --- |
| KHQR | QR payment format used for Cambodian QR payments. |
| Funding account | Customer account selected to fund the payment. |
| Merchant | Recipient represented by the QR payload. |
| QR payload | Encoded payment data scanned by the customer. |
| Idempotency key | Client-supplied unique key used to prevent duplicate initiation. |
| Payment instruction | Bank-created request to execute a payment. |
| Pending | Payment outcome is not final. |
| Reconciliation | Operational matching of bank, processor, and ledger records. |

## System Context

| System | Role | Ownership |
| --- | --- | --- |
| Mobile Banking App | Scans QR, displays confirmation, submits payment, displays status. | Digital Channels |
| KHQR Payment API | Validates request, creates payment instruction, returns status. | Payments Platform |
| Customer Profile Service | Provides customer identity and risk attributes. | Customer Platform |
| Account Service | Confirms account eligibility, balance availability, and debit constraints. | Core Banking |
| Fraud Screening Service | Screens payment for fraud signals and risk holds. | Financial Crime |
| Sanctions Screening Service | Screens relevant beneficiary and merchant data where required. | Compliance |
| Payment Processor | Executes KHQR payment and returns status. | External or Payments Platform |
| Ledger or Core Banking | Records debit and payment accounting entries. | Core Banking |
| Notification Service | Sends customer payment notifications. | Digital Channels |
| Observability Platform | Stores metrics, logs, traces, and alerts. | SRE |
| Jira | Work items, approvals, risks, and defects. | Delivery Governance |
| Confluence | Published stakeholder documentation. | Delivery Governance |

## Data Classification

| Data | Classification | Handling |
| --- | --- | --- |
| Customer ID | Confidential | Use internal identifier; mask in logs. |
| Account reference | Restricted | Tokenize or mask outside trusted boundaries. |
| QR payload | Confidential | Store only if required; mask sensitive sections. |
| Amount and currency | Confidential | Display to customer and audit; protect in logs. |
| Merchant name or ID | Confidential | Display confirmation value; protect in analytics. |
| Idempotency key | Internal | Log correlation-safe value only. |
| Payment status | Confidential | Expose only to authorized customer and support roles. |

## Payment State Model

| State | Meaning | Terminal |
| --- | --- | --- |
| received | Request accepted by KHQR Payment API for processing. | No |
| pending_screening | Fraud or sanctions decision is not final. | No |
| pending_processor | Processor outcome is not final. | No |
| completed | Payment completed and recorded. | Yes |
| rejected | Payment rejected by validation, risk, sanctions, or processor. | Yes |
| failed | Payment failed due to technical or non-retryable processing error. | Yes |
| expired | Pending payment exceeded allowed status window. | Yes |

## Key Controls

- Customer must be authenticated and authorized for the funding account.
- QR payload must be parsed and validated before confirmation.
- Confirmed merchant, amount, currency, and funding account must be bound to the submitted request.
- Payment initiation must require an idempotency key.
- Duplicate idempotency key with same payload must return the original payment reference and status.
- Duplicate idempotency key with conflicting payload must be rejected.
- All payment attempts must produce audit events.
- Logs must not contain raw secrets, credentials, full account numbers, or unmasked sensitive QR data.

## Confluence Placeholders

- CONF-PAY-KHQR-CONTEXT: KHQR capability context.
- CONF-PAY-KHQR-RUNBOOK: Operations and support runbook.
- CONF-PAY-KHQR-CONTROLS: Risk and control summary.

## Open Context Questions

| Question | Owner | Jira | Status |
| --- | --- | --- | --- |
| Which exact KHQR payload version is approved for first release? | Payments Architect | JIRA-KHQR-002 | Open |
| Which fraud and sanctions decision outcomes are customer-displayable? | Security and Risk Lead | JIRA-KHQR-004 | Open |
| What is the maximum pending status duration before expiry? | Product Owner | JIRA-KHQR-001 | Open |
