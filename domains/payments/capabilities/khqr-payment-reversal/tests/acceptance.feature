Feature: KHQR Payment Reversal
  Operations users need to reverse completed KHQR payments before final
  settlement when a processor, ledger, or bank system error requires a
  controlled operational correction.

  Background:
    Given the KHQR Payment Reversal capability is enabled
    And original KHQR payment "pay_khqrrev_20260601" has status "Completed"
    And original KHQR payment "pay_khqrrev_20260601" is not finally settled
    And original KHQR payment "pay_khqrrev_20260601" has amount "100.00" and currency "USD"
    And the Merchant Settlement Service cutoff status is fresh within 60 seconds
    And operations maker "ops-maker-001" has reversal-maker entitlement
    And operations checker "ops-checker-001" has reversal-checker entitlement
    And operations checker "ops-checker-001" is different from operations maker "ops-maker-001"

  @JIRA-KHQRREV-020 @FR-KHQRREV-001 @BR-KHQRREV-001
  Scenario: Operations maker creates reversal request for eligible completed payment
    Given the reversal request includes reason code "PROCESSOR_STATUS_CORRECTION"
    And the request includes evidence reference "evidence-khqrrev-001"
    And the request includes idempotency key "idem-khqrrev-request-001"
    And the request includes correlation ID "corr-khqrrev-request-001"
    When operations maker "ops-maker-001" requests a full reversal for original payment "pay_khqrrev_20260601"
    Then a reversal request is created for checker approval
    And the reversal amount equals the full original payment amount
    And processor and ledger reversal execution has not started
    And an immutable audit event is recorded for the reversal request

  @JIRA-KHQRREV-021 @FR-KHQRREV-002 @security
  Scenario: Reject reversal request without operations reversal entitlement
    Given operations user "ops-user-no-entitlement" does not have reversal-maker entitlement
    When operations user "ops-user-no-entitlement" requests a full reversal for original payment "pay_khqrrev_20260601"
    Then the reversal request is rejected as forbidden
    And no reversal request is created
    And no processor or ledger reversal execution occurs
    And an authorization failure audit event is recorded

  @JIRA-KHQRREV-022 @FR-KHQRREV-003 @BR-KHQRREV-002
  Scenario: Processor and ledger execution does not start before checker approval
    Given operations maker "ops-maker-001" created reversal request "revreq-khqrrev-001"
    When checker approval is still missing
    Then reversal request "revreq-khqrrev-001" remains awaiting checker approval
    And no processor reversal command is submitted
    And no ledger reversal command is submitted

  @JIRA-KHQRREV-023 @FR-KHQRREV-004 @BR-KHQRREV-003 @security
  Scenario: Reject maker self-approval
    Given operations maker "ops-maker-001" created reversal request "revreq-khqrrev-001"
    When operations maker "ops-maker-001" attempts to approve reversal request "revreq-khqrrev-001"
    Then the approval is rejected for maker-checker violation
    And reversal request "revreq-khqrrev-001" remains unexecuted
    And a maker-checker violation audit event is recorded

  @JIRA-KHQRREV-024 @FR-KHQRREV-005
  Scenario: Checker rejects reversal request
    Given operations maker "ops-maker-001" created reversal request "revreq-khqrrev-002"
    When operations checker "ops-checker-001" rejects reversal request "revreq-khqrrev-002" with reason code "CHECKER_REJECTED_INSUFFICIENT_EVIDENCE"
    Then reversal request "revreq-khqrrev-002" is marked "Reversal Rejected"
    And no processor or ledger reversal execution occurs
    And an immutable audit event is recorded for the checker rejection

  @JIRA-KHQRREV-024 @JIRA-KHQRREV-033 @FR-KHQRREV-005 @FR-KHQRREV-014
  Scenario: Checker approval starts controlled reversal execution
    Given operations maker "ops-maker-001" created reversal request "revreq-khqrrev-003"
    And the Merchant Settlement Service still returns "not_finally_settled" immediately before execution
    When operations checker "ops-checker-001" approves reversal request "revreq-khqrrev-003" with reason code "PROCESSOR_STATUS_CORRECTION"
    Then reversal request "revreq-khqrrev-003" is accepted for execution
    And the reversal status is "Reversal Pending"
    And processor reversal and ledger reversal actions are attempted
    And both downstream attempts record correlation and reversal references

  @JIRA-KHQRREV-025 @FR-KHQRREV-006
  Scenario Outline: Reject reversal when original payment is not completed
    Given original KHQR payment "pay_khqrrev_non_completed" has status "<paymentStatus>"
    When operations maker "ops-maker-001" requests a full reversal for original payment "pay_khqrrev_non_completed"
    Then the reversal request is rejected for original payment not completed
    And no reversal request is created
    And no processor or ledger reversal execution occurs

    Examples:
      | paymentStatus |
      | Pending       |
      | Failed        |
      | Rejected      |
      | Expired       |
      | Cancelled     |

  @JIRA-KHQRREV-026 @FR-KHQRREV-007
  Scenario Outline: Reject reversal request when request-time settlement cutoff is not eligible
    Given original KHQR payment "pay_khqrrev_settlement" has status "Completed"
    And the Merchant Settlement Service cutoff status is "<cutoffStatus>"
    And the cutoff evidence freshness is "<freshness>"
    When operations maker "ops-maker-001" requests a full reversal for original payment "pay_khqrrev_settlement"
    Then the reversal request is rejected before checker approval
    And no executable reversal request is created
    And no processor reversal command is submitted
    And no ledger reversal command is submitted
    And the settlement-cutoff outcome is visible to operations
    And the outcome is audited with settlement-cutoff evidence

    Examples:
      | cutoffStatus        | freshness        |
      | finally_settled     | fresh            |
      | unknown             | fresh            |
      | unavailable         | fresh            |
      | not_finally_settled | older_60_seconds |
      | contradictory       | fresh            |

  @JIRA-KHQRREV-026 @FR-KHQRREV-007
  Scenario: Re-check settlement cutoff immediately before execution
    Given operations maker "ops-maker-001" created reversal request "revreq-khqrrev-004"
    And operations checker "ops-checker-001" approves reversal request "revreq-khqrrev-004"
    And the Merchant Settlement Service returns "finally_settled" immediately before execution
    When execution eligibility is evaluated
    Then reversal request "revreq-khqrrev-004" must not execute
    And no processor reversal command is submitted
    And no ledger reversal command is submitted
    And the non-executed outcome is visible to operations

  @JIRA-KHQRREV-027 @FR-KHQRREV-008
  Scenario: Reject partial reversal request in MVP
    Given original KHQR payment "pay_khqrrev_20260601" has amount "100.00" and currency "USD"
    When operations maker "ops-maker-001" requests a reversal for amount "40.00" and currency "USD"
    Then the reversal request is rejected for partial amount not supported
    And no reversal request is created
    And no processor or ledger reversal execution occurs

  @JIRA-KHQRREV-028 @FR-KHQRREV-009
  Scenario Outline: Reject missing or invalid reversal request reason code
    Given the reversal request includes idempotency key "idem-khqrrev-reason-001"
    And the reversal request includes reason code "<reasonCode>"
    When operations maker "ops-maker-001" requests a full reversal for original payment "pay_khqrrev_20260601"
    Then the reversal request is rejected for invalid reason code
    And no reversal request is created
    And the rejection is audited

    Examples:
      | reasonCode                         |
      |                                    |
      | CUSTOMER_RETURN                    |
      | CHECKER_REJECTED_NOT_ELIGIBLE      |
      | free_text_processor_error          |

  @JIRA-KHQRREV-028 @FR-KHQRREV-009
  Scenario Outline: Reject checker decision with missing or invalid decision reason code
    Given operations maker "ops-maker-001" created reversal request "revreq-khqrrev-reason-002"
    When operations checker "ops-checker-001" submits checker decision "<decision>" with reason code "<reasonCode>"
    Then the checker decision is rejected for invalid reason code
    And reversal request "revreq-khqrrev-reason-002" remains unexecuted
    And no processor reversal command is submitted
    And no ledger reversal command is submitted
    And the rejected checker decision is audited

    Examples:
      | decision | reasonCode                    |
      | approve  |                               |
      | approve  | CUSTOMER_RETURN               |
      | reject   |                               |
      | reject   | PROCESSOR_STATUS_CORRECTION   |
      | reject   | free_text_rejection_reason    |

  @JIRA-KHQRREV-029 @FR-KHQRREV-010
  Scenario: Reject reversal command without idempotency key
    Given the reversal request includes reason code "LEDGER_POSTING_ERROR"
    And the reversal request includes correlation ID "corr-khqrrev-no-idem-001"
    When operations maker "ops-maker-001" requests a full reversal without an idempotency key for original payment "pay_khqrrev_20260601"
    Then the reversal request is rejected for missing idempotency key
    And no reversal request is created
    And the rejection is audited

  @JIRA-KHQRREV-030 @FR-KHQRREV-011 @NFR-KHQRREV-002
  Scenario: Prevent duplicate reversal for same original payment
    Given reversal "rev-khqrrev-existing-001" already exists with status "Reversal Pending" for original payment "pay_khqrrev_20260601"
    When operations maker "ops-maker-001" requests another full reversal for original payment "pay_khqrrev_20260601"
    Then no second reversal execution is created
    And the duplicate attempt is rejected or mapped to the existing reversal according to idempotency rules
    And a duplicate reversal attempt audit event is recorded

  @JIRA-KHQRREV-031 @FR-KHQRREV-012
  Scenario: Same idempotency key and same payload returns existing reversal
    Given operations maker "ops-maker-001" submitted a reversal request with idempotency key "idem-khqrrev-replay-001"
    And the system created reversal request "revreq-khqrrev-replay-001"
    When the same reversal payload is submitted again with idempotency key "idem-khqrrev-replay-001"
    Then the response contains reversal request "revreq-khqrrev-replay-001"
    And the response contains the current reversal status
    And no second reversal request or execution path is created

  @JIRA-KHQRREV-032 @FR-KHQRREV-013
  Scenario: Same idempotency key and different payload is rejected
    Given operations maker "ops-maker-001" submitted a reversal request with idempotency key "idem-khqrrev-conflict-001"
    When a different original payment ID is submitted with idempotency key "idem-khqrrev-conflict-001"
    Then the command is rejected with idempotency conflict
    And no reversal request is created for the conflicting payload
    And the conflict is audited

  @JIRA-KHQRREV-030 @JIRA-KHQRREV-051 @FR-KHQRREV-011 @NFR-KHQRREV-002
  Scenario: Concurrent reversal submissions do not create duplicate execution
    Given original KHQR payment "pay_khqrrev_20260601" has no existing reversal
    When two operations makers submit reversal requests for original payment "pay_khqrrev_20260601" at the same time with different idempotency keys
    Then only one reversal request or execution path is created
    And the other request is rejected as duplicate or mapped to the existing reversal according to idempotency rules
    And both attempts are traceable by correlation ID
    And duplicate-prevention audit events are recorded

  @JIRA-KHQRREV-033 @JIRA-KHQRREV-034 @FR-KHQRREV-014 @FR-KHQRREV-015 @integration
  Scenario: Processor and ledger success marks reversal reversed
    Given reversal request "revreq-khqrrev-005" is checker-approved
    When processor reversal succeeds with reference "proc-rev-001"
    And ledger reversal succeeds with reference "ledger-rev-001"
    And reconciliation references are available
    Then reversal request "revreq-khqrrev-005" is marked "Reversed"
    And processor and ledger references are preserved
    And completion and reconciliation evidence are published

  @JIRA-KHQRREV-035 @FR-KHQRREV-016 @ADR-KHQRREV-004 @integration
  Scenario: Processor success and ledger unknown remains pending
    Given reversal request "revreq-khqrrev-006" is checker-approved
    When processor reversal succeeds with reference "proc-rev-002"
    And ledger reversal outcome is unknown
    Then reversal request "revreq-khqrrev-006" remains "Reversal Pending"
    And processor reversal is not blindly resubmitted
    And pending-age details are visible to operations
    And the split outcome is auditable and traceable

  @JIRA-KHQRREV-035 @FR-KHQRREV-016 @ADR-KHQRREV-004 @integration
  Scenario: Ledger success and processor unknown remains pending
    Given reversal request "revreq-khqrrev-007" is checker-approved
    When ledger reversal succeeds with reference "ledger-rev-002"
    And processor reversal outcome is unknown
    Then reversal request "revreq-khqrrev-007" remains "Reversal Pending"
    And ledger reversal is not blindly resubmitted
    And pending-age details are visible to operations
    And the split outcome is auditable and traceable

  @JIRA-KHQRREV-036 @FR-KHQRREV-017 @ADR-KHQRREV-004 @integration
  Scenario Outline: Terminal processor or ledger failure marks reversal failed
    Given reversal request "revreq-khqrrev-failure" is checker-approved
    When processor reversal outcome is "<processorOutcome>"
    And ledger reversal outcome is "<ledgerOutcome>"
    Then reversal request "revreq-khqrrev-failure" is marked "Reversal Failed"
    And no automatic compensating command is attempted
    And an exception case is visible to operations
    And failure evidence is available for finance investigation

    Examples:
      | processorOutcome | ledgerOutcome |
      | Success          | Failed        |
      | Failed           | Success       |
      | Failed           | Failed        |
      | Failed           | Pending       |
      | Failed           | Unknown       |
      | Pending          | Failed        |
      | Unknown          | Failed        |

  @JIRA-KHQRREV-035 @JIRA-KHQRREV-036 @FR-KHQRREV-016 @FR-KHQRREV-017 @NFR-KHQRREV-008
  Scenario Outline: Pending reversal threshold handling
    Given reversal request "revreq-khqrrev-pending" is checker-approved
    And processor or ledger outcome is not terminal
    When the reversal has been pending for "<elapsedTime>"
    Then the reversal status is "<expectedStatus>"
    And operations handling includes "<expectedHandling>"
    And pending or failed evidence is audited

    Examples:
      | elapsedTime | expectedStatus   | expectedHandling         |
      | 5 minutes   | Reversal Pending | alert                    |
      | 15 minutes  | Reversal Pending | exception queue case     |
      | 60 minutes  | Reversal Failed  | finance operations owner |

  @JIRA-KHQRREV-037 @FR-KHQRREV-018 @security
  Scenario: Authorized operations user views reversal status
    Given reversal "rev-khqrrev-status-001" exists with status "Reversal Pending"
    And operations user "ops-status-001" has reversal-status-view entitlement
    When operations user "ops-status-001" requests reversal status for "rev-khqrrev-status-001"
    Then the system returns current reversal status and safe operational details
    And sensitive customer, merchant, processor, and ledger identifiers are masked unless explicitly authorized

  @JIRA-KHQRREV-037 @FR-KHQRREV-018 @security
  Scenario: Reject reversal status view without entitlement
    Given reversal "rev-khqrrev-status-001" exists with status "Reversal Pending"
    And operations user "ops-status-denied-001" does not have reversal-status-view entitlement
    When operations user "ops-status-denied-001" requests reversal status for "rev-khqrrev-status-001"
    Then the request is rejected as forbidden
    And no sensitive reversal details are returned
    And an authorization failure audit event is recorded

  @JIRA-KHQRREV-038 @FR-KHQRREV-019 @NFR-KHQRREV-003
  Scenario: Preserve references needed for reconciliation
    Given reversal request "revreq-khqrrev-008" is checker-approved
    When processor, ledger, settlement, and audit references become available
    Then the reversal record preserves original payment ID, reversal ID, processor reference, ledger reference, settlement reference, amount, currency, timestamps, actor, approval, and correlation ID
    And the references are available for reconciliation evidence

  @JIRA-KHQRREV-039 @FR-KHQRREV-020 @NFR-KHQRREV-004
  Scenario Outline: Audit material reversal events
    When material reversal event "<eventType>" occurs
    Then an immutable audit event is recorded
    And required sensitive fields are masked
    And the audit event includes reversal reference, actor when applicable, reason code when applicable, outcome, timestamp, and correlation ID

    Examples:
      | eventType                 |
      | request_created           |
      | checker_approved          |
      | checker_rejected          |
      | execution_started         |
      | processor_outcome_recorded |
      | ledger_outcome_recorded    |
      | reversal_reversed         |
      | reversal_failed           |
      | duplicate_attempt         |
      | settlement_cutoff_blocked |

  @JIRA-KHQRREV-039 @FR-KHQRREV-020 @NFR-KHQRREV-004
  Scenario: Do not complete material state change when audit persistence fails
    Given reversal request "revreq-khqrrev-009" is ready for a material state change
    When immutable audit persistence fails
    Then the material state change is not completed unless approved durable audit buffering exists
    And the failure is visible to operations support
    And no untraceable reversal state is produced

  @JIRA-KHQRREV-040 @FR-KHQRREV-021
  Scenario: Reversal is not reported as refund
    Given reversal "rev-khqrrev-reporting-001" exists for original KHQR payment "pay_khqrrev_20260601"
    When the reversal is displayed, exported, audited, or reconciled
    Then the record is identified as a bank or system operational correction
    And the record is not identified as a merchant or business refund
    And QR Refund records remain separate from KHQR Payment Reversal records

  @JIRA-KHQRREV-041 @FR-KHQRREV-022 @NFR-KHQRREV-003 @integration
  Scenario Outline: Reconciliation identifies reversal outcomes
    Given reconciliation receives reversal evidence for reversal "rev-khqrrev-recon-001"
    And the reversal has outcome "<reversalOutcome>"
    And the reconciliation match result is "<matchResult>"
    When reconciliation matching runs
    Then the reversal outcome is identifiable as "<reconciliationClassification>"
    And operations and finance can trace original payment, reversal, processor, ledger, and settlement references

    Examples:
      | reversalOutcome   | matchResult            | reconciliationClassification |
      | Reversed          | references_match       | matched                      |
      | Reversal Pending  | outcome_not_final      | pending                      |
      | Reversal Failed   | terminal_failure       | failed                       |
      | Reversal Rejected | control_rejection      | rejected                     |
      | Reversed          | references_do_not_match | mismatched                   |

  @JIRA-KHQRREV-042 @FR-KHQRREV-023 @ADR-KHQRREV-005
  Scenario: Retry is disabled until retry policy is approved
    Given reversal "rev-khqrrev-retry-001" has status "Reversal Pending"
    And no retry policy has been approved
    When operations user "ops-maker-001" attempts to retry reversal "rev-khqrrev-retry-001"
    Then the retry command is rejected or unavailable
    And no processor or ledger command is resubmitted
    And the retry attempt is audited if the command reaches the system

  @JIRA-KHQRREV-043 @FR-KHQRREV-024 @ADR-KHQRREV-006
  Scenario: Notifications are not required for MVP until scope is approved
    Given reversal "rev-khqrrev-notify-001" reaches outcome "Reversed"
    And customer or merchant notification scope is not approved
    When release readiness evidence is reviewed
    Then notification delivery evidence is not required for MVP reversal acceptance
    And no customer or merchant notification is sent by the reversal capability

  @JIRA-KHQRREV-050 @NFR-KHQRREV-001 @nfr
  Scenario: Reversal completion time target requires approved threshold before validation
    Given the reversal completion-time target is not yet approved
    When QA prepares validation planning
    Then completion-time validation remains conditional
    And Product, Finance, Operations, and QA approval is required before release validation can claim success against a target

  @JIRA-KHQRREV-051 @JIRA-KHQRREV-054 @NFR-KHQRREV-002 @NFR-KHQRREV-005 @security
  Scenario: Reversal command evidence protects sensitive data and replay controls
    Given reversal command evidence is captured for validation
    When logs, reports, operations views, audit events, and test evidence are inspected
    Then customer, account, merchant, processor, and ledger identifiers are masked unless explicitly authorized
    And idempotency keys and request fingerprints prevent replay from creating duplicate reversal execution

  @JIRA-KHQRREV-056 @JIRA-KHQRREV-057 @JIRA-KHQRREV-058 @NFR-KHQRREV-006 @NFR-KHQRREV-007 @NFR-KHQRREV-008 @operational
  Scenario: Operational observability exists for reversal lifecycle
    Given reversal requests, approvals, rejections, duplicate attempts, settlement cutoff outcomes, processor outcomes, ledger outcomes, pending states, failed states, and reversed outcomes occur
    When operational evidence is reviewed
    Then metrics, logs, traces, alerts, and operations-visible queues exist for each lifecycle outcome
    And unknown or partial downstream outcomes do not create duplicate execution, untraceable state, or hidden financial inconsistency
