Feature: QR Refund for completed KHQR payments
  Merchants and bank operations users need to issue full refunds for completed
  KHQR payments with strong controls, traceability, audit, and reconciliation.

  Background:
    Given the QR Refund capability is enabled for KHQR payments
    And original KHQR payment "pay_synth_20260601" belongs to merchant "MERCH-001"
    And original KHQR payment "pay_synth_20260601" has status "Completed"
    And original KHQR payment "pay_synth_20260601" was created within 30 calendar days
    And original KHQR payment "pay_synth_20260601" has not been refunded
    And merchant "MERCH-001" is active

  @JIRA-QRREF-020 @JIRA-QRREF-027 @JIRA-QRREF-028 @FR-QRREF-001 @FR-QRREF-008 @FR-QRREF-009
  Scenario: Successful merchant full refund
    Given merchant user "merchant-user-001" is authenticated for merchant "MERCH-001"
    And the merchant user has refund permission
    And the refund request includes reason code "CUSTOMER_RETURN"
    And the request includes idempotency key "idem-qrref-001"
    And the request includes correlation ID "corr-qrref-001"
    When the merchant submits a full refund for original payment "pay_synth_20260601"
    Then the refund request is accepted
    And the refund response contains a refund ID beginning with "rfnd_"
    And the refund response status is "requested" or "processing"
    And the refund amount equals the full original payment amount
    And the refund is linked to original payment "pay_synth_20260601"
    And an audit event is recorded for the refund request

  @JIRA-QRREF-021 @JIRA-QRREF-027 @JIRA-QRREF-028 @FR-QRREF-002 @FR-QRREF-008 @FR-QRREF-009
  Scenario: Successful operations full refund creation
    Given operations user "ops-create-001" has refund create entitlement
    And original KHQR payment "pay_synth_20260601" is eligible for refund
    And the operations refund request includes reason code "MERCHANT_SUPPORT_REQUEST"
    And the request includes idempotency key "idem-qrref-ops-001"
    And the request includes correlation ID "corr-qrref-ops-001"
    When operations user "ops-create-001" creates a full refund for original payment "pay_synth_20260601"
    Then the refund request is accepted
    And the refund response contains a refund ID beginning with "rfnd_"
    And the refund amount equals the full original payment amount
    And the refund is linked to original payment "pay_synth_20260601"
    And an audit event is recorded for the operations refund request

  @JIRA-QRREF-021 @FR-QRREF-002
  Scenario: Reject operations full refund creation without entitlement
    Given operations user "ops-create-002" does not have refund create entitlement
    And original KHQR payment "pay_synth_20260601" is eligible for refund
    When operations user "ops-create-002" creates a full refund for original payment "pay_synth_20260601"
    Then the refund request is rejected as forbidden
    And no refund transaction is created
    And an authorization failure audit event is recorded

  @JIRA-QRREF-022 @FR-QRREF-003
  Scenario Outline: Reject refund when original payment is not completed
    Given original KHQR payment "pay_non_completed" belongs to merchant "MERCH-001"
    And original KHQR payment "pay_non_completed" has status "<paymentStatus>"
    And merchant user "merchant-user-001" is authenticated for merchant "MERCH-001"
    When the merchant submits a full refund for original payment "pay_non_completed"
    Then the refund request is rejected
    And no refund transaction is created
    And the rejection is audited with reason "PAYMENT_NOT_COMPLETED"

    Examples:
      | paymentStatus |
      | Received      |
      | Processing    |
      | Failed        |
      | Rejected      |
      | Expired       |

  @JIRA-QRREF-023 @JIRA-QRREF-028 @FR-QRREF-004 @FR-QRREF-009
  Scenario: Prevent duplicate refund for the same original payment
    Given refund "rfnd_synth_001" already exists for original payment "pay_synth_20260601"
    When merchant user "merchant-user-001" submits another refund for original payment "pay_synth_20260601"
    Then the refund request is rejected as already refunded
    And no second refund transaction is created
    And an audit event is recorded for the duplicate refund attempt

  @JIRA-QRREF-028 @JIRA-QRREF-029 @FR-QRREF-009 @FR-QRREF-010
  Scenario: Return existing refund for duplicate request with same idempotency key and payload
    Given merchant user "merchant-user-001" submitted a refund with idempotency key "idem-qrref-dup-001"
    And the bank created refund "rfnd_synth_dup_001"
    When the same refund payload is submitted again with idempotency key "idem-qrref-dup-001"
    Then the response contains refund ID "rfnd_synth_dup_001"
    And no second refund transaction is created

  @JIRA-QRREF-028 @FR-QRREF-009
  Scenario: Reject refund initiation without idempotency key
    Given merchant user "merchant-user-001" is authenticated for merchant "MERCH-001"
    And the refund request includes reason code "CUSTOMER_RETURN"
    And the request includes correlation ID "corr-qrref-missing-idem-001"
    When the merchant submits a full refund without an idempotency key for original payment "pay_synth_20260601"
    Then the refund request is rejected for missing idempotency key
    And no refund transaction is created
    And the rejection is audited

  @JIRA-QRREF-029 @FR-QRREF-010
  Scenario: Reject duplicate idempotency key with conflicting payload
    Given merchant user "merchant-user-001" submitted a refund with idempotency key "idem-qrref-conflict-001"
    When a different original payment ID is submitted with idempotency key "idem-qrref-conflict-001"
    Then the refund request is rejected with idempotency conflict
    And no refund transaction is created for the conflicting request
    And the conflict is audited

  @JIRA-QRREF-044 @NFR-QRREF-005
  Scenario: Concurrent refund submissions for the same payment do not create duplicate refunds
    Given merchant user "merchant-user-001" is authenticated for merchant "MERCH-001"
    And original KHQR payment "pay_synth_20260601" has not been refunded
    When two refund requests for original payment "pay_synth_20260601" are submitted at the same time with different idempotency keys
    Then only one refund transaction is created
    And the second refund request is rejected as already refunded or duplicate in progress
    And both attempts are traceable by correlation ID
    And duplicate-prevention audit events are recorded

  @JIRA-QRREF-024 @FR-QRREF-005
  Scenario: Reject refund outside the 30-day refund window
    Given original KHQR payment "pay_old_001" belongs to merchant "MERCH-001"
    And original KHQR payment "pay_old_001" has status "Completed"
    And original KHQR payment "pay_old_001" was created more than 30 calendar days ago
    When merchant user "merchant-user-001" submits a full refund for original payment "pay_old_001"
    Then the refund request is rejected for expired refund window
    And no refund transaction is created
    And the rejection is audited

  @JIRA-QRREF-025 @FR-QRREF-006
  Scenario: Allow refund after merchant settlement
    Given original KHQR payment "pay_settled_001" belongs to merchant "MERCH-001"
    And original KHQR payment "pay_settled_001" has status "Completed"
    And original KHQR payment "pay_settled_001" was created within 30 calendar days
    And original KHQR payment "pay_settled_001" has already settled to the merchant
    And original KHQR payment "pay_settled_001" has not been refunded
    And merchant user "merchant-user-001" is authenticated for merchant "MERCH-001"
    And the refund request includes reason code "CUSTOMER_RETURN"
    And the request includes idempotency key "idem-qrref-settled-001"
    When the merchant submits a full refund for original payment "pay_settled_001"
    Then the refund request is accepted
    And settlement state alone does not block refund eligibility
    And an audit event is recorded for the refund request

  @JIRA-QRREF-025 @FR-QRREF-006
  Scenario: Merchant balance availability is not required for MVP refund eligibility
    Given original KHQR payment "pay_balance_001" belongs to merchant "MERCH-001"
    And original KHQR payment "pay_balance_001" has status "Completed"
    And original KHQR payment "pay_balance_001" was created within 30 calendar days
    And merchant balance availability cannot be confirmed
    And original KHQR payment "pay_balance_001" has not been refunded
    And merchant user "merchant-user-001" is authenticated for merchant "MERCH-001"
    And the refund request includes reason code "CUSTOMER_RETURN"
    And the request includes idempotency key "idem-qrref-balance-001"
    When the merchant submits a full refund for original payment "pay_balance_001"
    Then the refund request is not rejected because of merchant balance availability
    And the refund remains eligible for normal refund processing
    And an audit event is recorded for the refund request

  @JIRA-QRREF-026 @FR-QRREF-007
  Scenario: Reject refund for suspended merchant
    Given merchant "MERCH-001" is suspended
    And merchant user "merchant-user-001" is authenticated for merchant "MERCH-001"
    When the merchant submits a full refund for original payment "pay_synth_20260601"
    Then the refund request is rejected for suspended merchant
    And no refund transaction is created
    And the rejection is audited

  @JIRA-QRREF-027 @FR-QRREF-008
  Scenario Outline: Reject refund request with missing or invalid reason code
    Given merchant user "merchant-user-001" is authenticated for merchant "MERCH-001"
    And the request includes idempotency key "<idempotencyKey>"
    And the request includes correlation ID "<correlationId>"
    When the merchant submits a full refund for original payment "pay_synth_20260601" with reason code "<reasonCode>"
    Then the refund request is rejected for invalid reason code
    And no refund transaction is created
    And the rejection is audited

    Examples:
      | reasonCode | idempotencyKey        | correlationId         |
      |            | idem-qrref-reason-001 | corr-qrref-reason-001 |
      | lowercase  | idem-qrref-reason-002 | corr-qrref-reason-002 |
      | X          | idem-qrref-reason-003 | corr-qrref-reason-003 |

  @JIRA-QRREF-030 @FR-QRREF-011
  Scenario: Route high-value refund to manual review
    Given original KHQR payment "pay_high_value_001" belongs to merchant "MERCH-001"
    And original KHQR payment "pay_high_value_001" has status "Completed"
    And the refund amount is above the configured high-value threshold
    When merchant user "merchant-user-001" submits a full refund for original payment "pay_high_value_001"
    Then the refund request is accepted for manual review
    And the refund does not proceed automatically to processor submission
    And the refund response includes review status "pending"
    And an audit event is recorded for manual review routing

  @JIRA-QRREF-031 @FR-QRREF-012
  Scenario: Operations override is requested with required controls
    Given operations user "ops-maker-001" has override-maker entitlement
    And refund "rfnd_window_001" is rejected for expired refund window
    When operations user "ops-maker-001" requests an override for control "refund_window"
    And the override request includes reason code "BANK_APPROVED_EXCEPTION"
    And the override request includes correlation ID "corr-override-001"
    Then an override request is created
    And the override status is "requested"
    And an immutable audit event is recorded for the override request

  @JIRA-QRREF-031 @FR-QRREF-012
  Scenario: Reject override for a control not approved for override
    Given operations user "ops-maker-001" has override-maker entitlement
    And refund "rfnd_non_overrideable_001" is rejected for a non-overrideable control
    When operations user "ops-maker-001" requests an override for the non-overrideable control
    And the override request includes reason code "BANK_APPROVED_EXCEPTION"
    Then the override request is rejected
    And the refund does not continue under override
    And the rejected override attempt is audited

  @JIRA-QRREF-031 @FR-QRREF-012
  Scenario: Maker-checker approval allows permitted override to continue
    Given operations user "ops-maker-001" requested override "ovr_synth_001"
    And operations user "ops-checker-001" has override-checker entitlement
    And operations user "ops-checker-001" is different from "ops-maker-001"
    When operations user "ops-checker-001" approves override "ovr_synth_001"
    Then the override status is "approved"
    And the refund is eligible to continue only for the approved control
    And the approval user is captured in the audit trail

  @JIRA-QRREF-031 @FR-QRREF-012
  Scenario: Reject override approval when maker and checker are the same user
    Given operations user "ops-maker-001" requested override "ovr_synth_002"
    When operations user "ops-maker-001" attempts to approve override "ovr_synth_002"
    Then the override decision is rejected
    And the refund does not continue under override
    And the rejected approval attempt is audited

  @JIRA-QRREF-032 @JIRA-QRREF-033 @FR-QRREF-013 @FR-QRREF-014
  Scenario: Retry failed refund from operations exception queue
    Given refund "rfnd_failed_001" has status "failed"
    And refund "rfnd_failed_001" is visible in the operations exception queue
    And operations user "ops-retry-001" has refund retry entitlement
    When operations user "ops-retry-001" retries refund "rfnd_failed_001" with reason code "PROCESSOR_TIMEOUT_RETRY"
    Then the retry request is accepted
    And the refund status becomes "processing"
    And retry metadata is captured
    And an audit event is recorded for the retry

  @JIRA-QRREF-047 @NFR-QRREF-008
  Scenario: Processor timeout keeps refund traceable and visible to operations
    Given a refund for original payment "pay_synth_20260601" has been accepted
    And the payment processor does not return a final outcome within the timeout window
    When refund processing evaluates the processor timeout
    Then the refund remains traceable by refund ID and correlation ID
    And no duplicate processor refund is submitted
    And the refund becomes visible to operations if unresolved
    And a processor timeout metric or alert is emitted

  @JIRA-QRREF-047 @NFR-QRREF-008
  Scenario: Ledger timeout keeps refund traceable and prevents unsafe duplicate posting
    Given a refund for original payment "pay_synth_20260601" has processor reference "proc_rfnd_001"
    And the ledger does not return a final posting outcome within the timeout window
    When refund processing evaluates the ledger timeout
    Then the refund remains traceable by refund ID and correlation ID
    And no duplicate ledger posting is submitted
    And the refund becomes visible to operations for investigation
    And a ledger timeout metric or alert is emitted

  @JIRA-QRREF-034 @FR-QRREF-015
  Scenario: Failed notification handling does not change authoritative refund outcome
    Given refund "rfnd_notify_001" has status "completed"
    And the notification service is unavailable
    When the system attempts to send the completed refund notification
    Then the refund status remains "completed"
    And the notification failure is recorded for recovery
    And a notification failure metric or alert is emitted
    And no sensitive customer information is written to logs

  @JIRA-QRREF-035 @FR-QRREF-016
  Scenario: Merchant retrieves refund status for own refund
    Given refund "rfnd_synth_001" belongs to merchant "MERCH-001"
    And merchant user "merchant-user-001" is authenticated for merchant "MERCH-001"
    When the merchant requests refund status for "rfnd_synth_001"
    Then the current refund status is returned
    And the response contains merchant-safe refund details
    And the response does not expose unmasked ledger or processor internals

  @JIRA-QRREF-035 @FR-QRREF-016
  Scenario: Merchant cannot retrieve another merchant's refund status
    Given refund "rfnd_other_001" belongs to merchant "MERCH-002"
    And merchant user "merchant-user-001" is authenticated for merchant "MERCH-001"
    When the merchant requests refund status for "rfnd_other_001"
    Then the request is rejected as forbidden
    And an authorization failure audit event is recorded

  @JIRA-QRREF-039 @JIRA-QRREF-045 @FR-QRREF-020 @NFR-QRREF-006
  Scenario Outline: Audit event is created for material refund event
    Given refund "rfnd_audit_001" exists
    When the refund event "<eventType>" occurs
    Then an immutable audit event is recorded
    And the audit event contains original payment ID, refund ID, initiator, user role, reason code, timestamp, and correlation ID
    And sensitive customer information is masked

    Examples:
      | eventType  |
      | request    |
      | approval   |
      | rejection  |
      | retry      |
      | completion |
      | failure    |
      | override   |

  @JIRA-QRREF-039 @JIRA-QRREF-047 @FR-QRREF-020 @NFR-QRREF-008
  Scenario: Audit failure prevents unaudited material refund state change
    Given a refund request for original payment "pay_synth_20260601" passed eligibility checks
    And the audit platform cannot confirm durable capture for the material state change
    When the system attempts to move the refund into processing
    Then the refund does not complete without audit evidence
    And the refund remains traceable by refund ID or correlation ID
    And the failure is visible to operations
    And an audit failure metric or alert is emitted

  @JIRA-QRREF-037 @FR-QRREF-018
  Scenario: End-of-day reconciliation identifies matched refund records
    Given refund "rfnd_recon_001" has status "completed"
    And refund "rfnd_recon_001" has original payment, processor, ledger, and merchant settlement references
    When end-of-day reconciliation runs
    Then the refund is matched across original payment, refund transaction, payment processor, ledger, and merchant settlement
    And the reconciliation result is available to operations and finance

  @JIRA-QRREF-037 @FR-QRREF-018
  Scenario: End-of-day reconciliation identifies mismatch for investigation
    Given refund "rfnd_recon_break_001" has status "completed"
    And the processor refund record does not match the ledger refund record
    When end-of-day reconciliation runs
    Then the mismatch is identified
    And the mismatch is visible to operations and finance
    And the mismatch is traceable by refund ID, original payment ID, processor reference, ledger reference, and correlation ID
