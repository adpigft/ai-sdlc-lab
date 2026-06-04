Feature: KHQR payment initiation
  Mobile banking customers need to initiate KHQR merchant payments safely,
  with clear status and no duplicate execution.

  Background:
    Given customer "CUST-001" is authenticated in mobile banking
    And customer "CUST-001" has an eligible funding account "acct_tok_12345"
    And the KHQR payment capability is enabled

  @JIRA-KHQR-010 @FR-KHQR-001
  Scenario: Reject malformed KHQR payload before payment creation
    Given the customer scans a malformed KHQR payload
    When the customer submits the KHQR payment for validation
    Then the payment request is rejected
    And no payment instruction is created
    And an audit event is recorded with masked payload details

  @JIRA-KHQR-011 @FR-KHQR-002
  Scenario: Display confirmation details before payment submission
    Given the customer scans a valid KHQR payload for merchant "Synthetic Market"
    And the QR payload contains amount "25.50" and currency "USD"
    When the payment confirmation screen is displayed
    Then the customer sees merchant "Synthetic Market"
    And the customer sees amount "25.50" and currency "USD"
    And the customer sees funding account "acct_tok_12345" in masked form

  @JIRA-KHQR-012 @FR-KHQR-003
  Scenario: Reject payment from an unauthorized funding account
    Given the customer selects funding account "acct_tok_not_owned"
    And the customer has a valid KHQR payload
    When the customer confirms the payment
    Then the payment request is rejected as unauthorized
    And no payment instruction is created

  @JIRA-KHQR-013 @FR-KHQR-004
  Scenario: Reject payment that breaches transaction limit
    Given the customer has a valid KHQR payload
    And the payment amount exceeds the configured transaction limit
    When the customer confirms the payment
    Then the payment request is rejected for limit breach
    And the rejection is visible to audit and operations

  @JIRA-KHQR-014 @FR-KHQR-005
  Scenario: Require idempotency key for initiation
    Given the customer has confirmed a valid KHQR payment
    When the mobile channel submits the payment without an idempotency key
    Then the payment request is rejected
    And no payment instruction is created

  @JIRA-KHQR-015 @FR-KHQR-006
  Scenario: Return original payment for duplicate request with same idempotency key
    Given the customer has submitted a valid KHQR payment with idempotency key "idem-synthetic-001"
    And the bank created payment reference "pay_synth_20260601"
    When the same request is submitted again with idempotency key "idem-synthetic-001"
    Then the response contains payment reference "pay_synth_20260601"
    And no second payment instruction is created
    And a duplicate request audit event is recorded

  @JIRA-KHQR-016 @FR-KHQR-007
  Scenario: Reject duplicate idempotency key with conflicting payload
    Given the customer has submitted a valid KHQR payment with idempotency key "idem-synthetic-002"
    When a different amount is submitted with idempotency key "idem-synthetic-002"
    Then the payment request is rejected with duplicate conflict
    And no second payment instruction is created

  @JIRA-KHQR-017 @FR-KHQR-008
  Scenario: Hold payment when fraud screening requires review
    Given the customer has confirmed a valid KHQR payment
    And fraud screening returns a hold decision
    When the payment is processed
    Then the payment status is "pending_screening"
    And the payment is not submitted to the processor
    And operations can view the masked hold reason category

  @JIRA-KHQR-018 @FR-KHQR-009
  Scenario: Return pending status when processor outcome is delayed
    Given the customer has confirmed a valid KHQR payment
    And the processor does not return a final outcome within the timeout window
    When the payment is submitted
    Then the payment status is "pending_processor"
    And the customer is not told the payment failed
    And the payment remains available for status inquiry

  @JIRA-KHQR-019 @FR-KHQR-010
  Scenario: Customer retrieves status for own KHQR payment
    Given customer "CUST-001" has payment reference "pay_synth_20260601"
    When the customer requests payment status for "pay_synth_20260601"
    Then the current payment status is returned
    And the response contains no unmasked account number

  @JIRA-KHQR-019 @FR-KHQR-010
  Scenario: Customer cannot retrieve another customer's payment status
    Given customer "CUST-002" has payment reference "pay_synth_other"
    When customer "CUST-001" requests payment status for "pay_synth_other"
    Then the request is rejected as forbidden
    And an access denial audit event is recorded

  @JIRA-KHQR-021 @FR-KHQR-012
  Scenario: Audit all terminal payment outcomes
    Given a KHQR payment reaches terminal status "completed"
    When the status is persisted
    Then an audit event is recorded
    And the event contains a correlation ID
    And the event contains masked customer, account, merchant, and payment identifiers
