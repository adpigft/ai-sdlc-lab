window.__CONTROL_TOWER_DATA__ = {
  "generatedAt": "2026-06-07T04:01:41.459657+00:00",
  "summary": {
    "totalFeatures": 4,
    "blockedFeatures": 1,
    "validationPassed": 0,
    "validationFailed": 1,
    "traceabilityCoveragePercent": 100.0,
    "releaseReadyFeatures": 0,
    "featuresByState": {
      "Architecture context approved for API contract design": 1,
      "Blocked": 1,
      "Design Ready": 1,
      "Draft for Architect Review": 1
    }
  },
  "approvalQueue": {
    "PO / BA review": 1,
    "QA review": 0,
    "SA review": 2,
    "Dev review": 1,
    "DevOps / release review": 0
  },
  "features": [
    {
      "domain": "Cards",
      "capability": "Card Lifecycle Management",
      "feature": "Card Replacement",
      "featureId": "FEAT-CARDREP-001",
      "intentId": "INT-CARDREP-001",
      "specId": "SPEC-CARDREP-001",
      "designId": "DES-CARDREP-001",
      "testId": "TEST-CARDREP-001",
      "state": "Draft for Architect Review",
      "ownerRole": "Cards Squad",
      "daysInState": 1,
      "blocked": false,
      "blockedReason": "",
      "nextGate": "Architect Review",
      "workflow": {
        "state": "Draft for Architect Review",
        "owner_role": "Cards Squad",
        "approver_role": "Solution Architect",
        "next_gate": "Architect Review",
        "blocked_reason": "",
        "days_in_state": 1,
        "last_updated": "2026-06-05T15:24:44+00:00",
        "expected_max_days": 2,
        "pm_intervention_trigger": false
      },
      "jiraKey": "SCRUM-1",
      "confluencePageId": "688129",
      "traceabilityId": "TRACE-CARDREP-DEMO-001",
      "focus": true,
      "quality": {
        "intentPresent": true,
        "specificationPresent": true,
        "designPresent": true,
        "testsPresent": false,
        "openapiPresent": false,
        "traceabilityPresent": true,
        "validationStatus": "Not available",
        "validationSummary": "",
        "releaseReadinessStatus": "Not ready"
      },
      "links": {
        "gitIntentPath": "domains/cards/capabilities/card-lifecycle-management/features/card-replacement/intent/intent.md",
        "gitSpecificationPath": "domains/cards/capabilities/card-lifecycle-management/features/card-replacement/specification/specification.md",
        "gitDesignPath": "domains/cards/capabilities/card-lifecycle-management/features/card-replacement/design/design.md",
        "gitTestsPath": "",
        "gitValidationPath": "",
        "gitReleasePath": "",
        "jiraUrl": "",
        "confluenceUrl": "https://adpi04.atlassian.net/wiki/spaces/AISDLC/pages/688129"
      },
      "interventions": [],
      "paths": {
        "intent": "domains/cards/capabilities/card-lifecycle-management/features/card-replacement/intent/intent.md",
        "specification": "domains/cards/capabilities/card-lifecycle-management/features/card-replacement/specification/specification.md",
        "design": "domains/cards/capabilities/card-lifecycle-management/features/card-replacement/design/design.md",
        "tests": "",
        "validation": "",
        "release": "",
        "workflowState": "",
        "openapi": ""
      },
      "evidence": {
        "validationReport": "",
        "validationStatus": "Not available",
        "validationSummary": "",
        "githubValidationEvidence": ""
      }
    },
    {
      "domain": "Payments",
      "capability": "KHQR Payment Reversal",
      "feature": "KHQR Payment Reversal",
      "featureId": "FEAT-KHQRREV-001",
      "intentId": "INT-KHQRREV-001",
      "specId": "SPEC-KHQRREV-001",
      "designId": "",
      "testId": "TEST-KHQRREV-001",
      "state": "Blocked",
      "ownerRole": "Digital Payments Product Owner",
      "daysInState": 3,
      "blocked": true,
      "blockedReason": "Release is blocked because only Slice 1 is validated; remaining slices, release notes, CI evidence, and release approval are not complete.",
      "nextGate": "remaining_slice_implementation",
      "workflow": {
        "state": "Blocked",
        "owner_role": "Digital Payments Product Owner",
        "approver_role": "Developer Lead",
        "next_gate": "remaining_slice_implementation",
        "blocked_reason": "Release is blocked because only Slice 1 is validated; remaining slices, release notes, CI evidence, and release approval are not complete.",
        "days_in_state": 3,
        "last_updated": "2026-06-04T02:57:01+00:00",
        "expected_max_days": 5,
        "pm_intervention_trigger": true
      },
      "jiraKey": "JIRA-KHQRREV-001",
      "confluencePageId": "CONF-PAY-KHQRREV-SPEC",
      "traceabilityId": "TRACE-KHQRREV-001",
      "focus": false,
      "quality": {
        "intentPresent": true,
        "specificationPresent": true,
        "designPresent": true,
        "testsPresent": true,
        "openapiPresent": true,
        "traceabilityPresent": true,
        "validationStatus": "Partial validation complete; release not ready",
        "validationSummary": "Not ready for release.",
        "releaseReadinessStatus": "Not ready"
      },
      "links": {
        "gitIntentPath": "domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/intent/intent.md",
        "gitSpecificationPath": "domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/specification/specification.md",
        "gitDesignPath": "domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/design/design.md",
        "gitTestsPath": "domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/tests/acceptance.feature",
        "gitValidationPath": "domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/validation/validation-report.md",
        "gitReleasePath": "",
        "jiraUrl": "",
        "confluenceUrl": "https://adpi04.atlassian.net/wiki/spaces/AISDLC/pages/CONF-PAY-KHQRREV-SPEC"
      },
      "interventions": [
        "blocked",
        "failed-validation"
      ],
      "paths": {
        "intent": "domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/intent/intent.md",
        "specification": "domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/specification/specification.md",
        "design": "domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/design/design.md",
        "tests": "domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/tests/acceptance.feature",
        "validation": "domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/validation/validation-report.md",
        "release": "",
        "workflowState": "domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/workflow-state.yaml",
        "openapi": "domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/contracts/openapi.yaml"
      },
      "evidence": {
        "validationReport": "domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/validation/validation-report.md",
        "validationStatus": "Partial validation complete; release not ready",
        "validationSummary": "Not ready for release.",
        "githubValidationEvidence": ""
      }
    },
    {
      "domain": "Payments",
      "capability": "KHQR payment initiation",
      "feature": "KHQR Payment",
      "featureId": "FEAT-KHQR-001",
      "intentId": "INT-KHQR-001",
      "specId": "SPEC-KHQR-001",
      "designId": "",
      "testId": "TEST-KHQR-001",
      "state": "Design Ready",
      "ownerRole": "Digital Payments Product Owner",
      "daysInState": 3,
      "blocked": false,
      "blockedReason": "",
      "nextGate": "Architect Review",
      "workflow": {
        "state": "Design Ready",
        "owner_role": "Digital Payments Product Owner",
        "approver_role": "DevSecOps / Platform",
        "next_gate": "Architect Review",
        "blocked_reason": "",
        "days_in_state": 3,
        "last_updated": "2026-06-04T02:57:01+00:00",
        "expected_max_days": 2,
        "pm_intervention_trigger": true
      },
      "jiraKey": "JIRA-KHQR-010",
      "confluencePageId": "CONF-PAY-KHQR-SPEC",
      "traceabilityId": "TRACE-KHQR-001",
      "focus": false,
      "quality": {
        "intentPresent": true,
        "specificationPresent": true,
        "designPresent": true,
        "testsPresent": true,
        "openapiPresent": true,
        "traceabilityPresent": true,
        "validationStatus": "Draft pending implementation and test execution",
        "validationSummary": "GitHub evidence: Pending: GHA-KHQR-001",
        "releaseReadinessStatus": "Not ready"
      },
      "links": {
        "gitIntentPath": "domains/payments/capabilities/payment-initiation/features/khqr-payment/intent/intent.md",
        "gitSpecificationPath": "domains/payments/capabilities/payment-initiation/features/khqr-payment/specification/specification.md",
        "gitDesignPath": "domains/payments/capabilities/payment-initiation/features/khqr-payment/design/design.md",
        "gitTestsPath": "domains/payments/capabilities/payment-initiation/features/khqr-payment/tests/acceptance.feature",
        "gitValidationPath": "domains/payments/capabilities/payment-initiation/features/khqr-payment/validation/validation-report.md",
        "gitReleasePath": "domains/payments/capabilities/payment-initiation/features/khqr-payment/release/release-notes.md",
        "jiraUrl": "",
        "confluenceUrl": "https://adpi04.atlassian.net/wiki/spaces/AISDLC/pages/CONF-PAY-KHQR-SPEC"
      },
      "interventions": [
        "stale-state"
      ],
      "paths": {
        "intent": "domains/payments/capabilities/payment-initiation/features/khqr-payment/intent/intent.md",
        "specification": "domains/payments/capabilities/payment-initiation/features/khqr-payment/specification/specification.md",
        "design": "domains/payments/capabilities/payment-initiation/features/khqr-payment/design/design.md",
        "tests": "domains/payments/capabilities/payment-initiation/features/khqr-payment/tests/acceptance.feature",
        "validation": "domains/payments/capabilities/payment-initiation/features/khqr-payment/validation/validation-report.md",
        "release": "domains/payments/capabilities/payment-initiation/features/khqr-payment/release/release-notes.md",
        "workflowState": "",
        "openapi": "domains/payments/capabilities/payment-initiation/features/khqr-payment/contracts/openapi.yaml"
      },
      "evidence": {
        "validationReport": "domains/payments/capabilities/payment-initiation/features/khqr-payment/validation/validation-report.md",
        "validationStatus": "Draft pending implementation and test execution",
        "validationSummary": "GitHub evidence: Pending: GHA-KHQR-001",
        "githubValidationEvidence": "Pending: GHA-KHQR-001"
      }
    },
    {
      "domain": "Payments",
      "capability": "QR Refund",
      "feature": "QR Refund",
      "featureId": "FEAT-QRREF-001",
      "intentId": "INT-QRREF-001",
      "specId": "SPEC-QRREF-001",
      "designId": "",
      "testId": "TEST-QRREF-001",
      "state": "Architecture context approved for API contract design",
      "ownerRole": "Digital Payments Product Owner",
      "daysInState": 3,
      "blocked": false,
      "blockedReason": "",
      "nextGate": "Validation Review",
      "workflow": {
        "state": "Architecture context approved for API contract design",
        "owner_role": "Digital Payments Product Owner",
        "approver_role": "Developer Lead",
        "next_gate": "Validation Review",
        "blocked_reason": "",
        "days_in_state": 3,
        "last_updated": "2026-06-04T02:57:01+00:00",
        "expected_max_days": 5,
        "pm_intervention_trigger": true
      },
      "jiraKey": "JIRA-QRREF-001",
      "confluencePageId": "",
      "traceabilityId": "TRACE-QRREF-001",
      "focus": false,
      "quality": {
        "intentPresent": true,
        "specificationPresent": true,
        "designPresent": true,
        "testsPresent": true,
        "openapiPresent": true,
        "traceabilityPresent": true,
        "validationStatus": "Not available",
        "validationSummary": "",
        "releaseReadinessStatus": "Not ready"
      },
      "links": {
        "gitIntentPath": "domains/payments/capabilities/payment-refund/features/qr-refund/intent/intent.md",
        "gitSpecificationPath": "domains/payments/capabilities/payment-refund/features/qr-refund/specification/specification.md",
        "gitDesignPath": "domains/payments/capabilities/payment-refund/features/qr-refund/design/design.md",
        "gitTestsPath": "domains/payments/capabilities/payment-refund/features/qr-refund/tests/acceptance.feature",
        "gitValidationPath": "",
        "gitReleasePath": "",
        "jiraUrl": "",
        "confluenceUrl": ""
      },
      "interventions": [
        "sync-missing"
      ],
      "paths": {
        "intent": "domains/payments/capabilities/payment-refund/features/qr-refund/intent/intent.md",
        "specification": "domains/payments/capabilities/payment-refund/features/qr-refund/specification/specification.md",
        "design": "domains/payments/capabilities/payment-refund/features/qr-refund/design/design.md",
        "tests": "domains/payments/capabilities/payment-refund/features/qr-refund/tests/acceptance.feature",
        "validation": "",
        "release": "",
        "workflowState": "",
        "openapi": "domains/payments/capabilities/payment-refund/features/qr-refund/contracts/openapi.yaml"
      },
      "evidence": {
        "validationReport": "",
        "validationStatus": "Not available",
        "validationSummary": "",
        "githubValidationEvidence": ""
      }
    }
  ]
};
