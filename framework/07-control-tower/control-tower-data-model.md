# Control Tower Data Model

## Purpose

Define the static JSON shape used by the AI-SDLC Control Tower dashboard MVP.

The dashboard is read-only. It consumes Git-owned artifacts, local traceability, and locally generated validation evidence only.

## Source Inputs

- `domains/**/features/**/intent/intent.md`
- `domains/**/features/**/specification/specification.md`
- `domains/**/features/**/design/design.md`
- `domains/**/features/**/tests/acceptance.feature`
- `domains/**/features/**/contracts/openapi.yaml`
- `domains/**/features/**/validation/validation-report.md`
- `domains/**/features/**/release/release-notes.md`
- `domains/**/features/**/workflow-state.yaml`
- `traceability/traceability-matrix.md`
- `framework/07-control-tower/workflow-ownership-matrix.md`
- `framework/08-context-quality/context-quality-model.md`
- `framework/09-context-packaging/context-package-model.md`
- `framework/10-context-observability/context-observability-model.md`
- `framework/10-context-observability/context-drift-model.md`
- `framework/12-impact-analysis/impact-analysis-model.md`
- `framework/13-pr-review/spec-aware-pr-review-model.md`
- `framework/14-harness-catalog/harness-catalog.md`
- `framework/15-agentops/agentops-model.md`
- `framework/24-knowledge-management/knowledge-management-model.md`
- `framework/25-accelerator-catalog/accelerator-catalog-model.md`
- `framework/26-portfolio-management/portfolio-governance-model.md`
- `framework/27-dependency-management/dependency-model.md`
- `framework/28-multi-agent-collaboration/agent-collaboration-model.md`
- `framework/29-ai-evaluation/evaluation-framework.md`

## JSON Schema Example

```json
{
  "generatedAt": "2026-06-06T12:00:00Z",
  "summary": {
    "totalFeatures": 0,
    "blockedFeatures": 0,
    "validationPassed": 0,
    "validationFailed": 0,
    "traceabilityCoveragePercent": 0,
    "releaseReadyFeatures": 0,
    "featuresByState": {
      "Draft for Architect Review": 0
    }
  },
  "approvalQueue": {
    "PO / BA review": 0,
    "QA review": 0,
    "SA review": 0,
    "Dev review": 0,
    "DevOps / release review": 0
  },
  "features": [
    {
      "domain": "cards",
      "capability": "card-lifecycle-management",
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
        "approver_role": null,
        "next_gate": "Architect Review",
        "blocked_reason": "",
        "days_in_state": 1,
        "last_updated": "2026-06-06T12:00:00Z",
        "expected_max_days": 2,
        "pm_intervention_trigger": true
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
      "evidence": {
        "validationReport": "",
        "validationStatus": "Not available",
        "validationSummary": "",
        "githubValidationEvidence": ""
      },
      "contextHealthScore": 0,
      "contextPackages": [],
      "contextDriftCount": 0,
      "staleContextPackages": 0,
      "contextSecurityFindings": 0,
      "contextEvalStatus": "Not available",
      "contextLastReviewed": "",
      "impactRisk": "Not available",
      "impactedArtifacts": [],
      "contextVersionStatus": "Not available",
      "driftStatus": "Not available",
      "prReviewStatus": "Not available",
      "harnessType": "Not available",
      "agentRunHealth": "Not available",
      "agentReworkCount": 0,
      "tokenBudgetStatus": "Not available",
      "portfolio": {
        "portfolioManager": "Not available",
        "program": "Not available"
      },
      "program": {
        "programManager": "Not available"
      },
      "dependencies": [],
      "knowledge": {
        "knowledgeScore": "Not available",
        "knowledgePackages": []
      },
      "accelerators": [],
      "agentCollaboration": {
        "pattern": "Not available",
        "confidence": "Not available"
      },
      "evaluation": {
        "specScore": "Not available",
        "contextScore": "Not available",
        "architectureScore": "Not available",
        "prScore": "Not available",
        "deliveryScore": "Not available"
      },
      "links": {
        "gitIntentPath": "domains/cards/capabilities/card-lifecycle-management/features/card-replacement/intent/intent.md",
        "gitSpecificationPath": "domains/cards/capabilities/card-lifecycle-management/features/card-replacement/specification/specification.md",
        "gitDesignPath": "domains/cards/capabilities/card-lifecycle-management/features/card-replacement/design/design.md",
        "gitTestsPath": "",
        "gitValidationPath": "",
        "gitReleasePath": "",
        "jiraUrl": "https://example.atlassian.net/browse/SCRUM-1",
        "confluenceUrl": "https://example.atlassian.net/wiki/spaces/AISDLC/pages/688129"
      },
      "interventions": [
        "missing-approval"
      ],
      "paths": {
        "intent": "domains/cards/capabilities/card-lifecycle-management/features/card-replacement/intent/intent.md",
        "specification": "domains/cards/capabilities/card-lifecycle-management/features/card-replacement/specification/specification.md",
        "design": "domains/cards/capabilities/card-lifecycle-management/features/card-replacement/design/design.md",
        "tests": "",
        "validation": "",
        "release": "",
        "workflowState": "",
        "openapi": ""
      }
    }
  ]
}
```

## Notes

- `featureId` is derived from the approved artifact identifiers where available.
- `state` and `nextGate` are derived from `workflow-state.yaml` when present; otherwise from approved artifact status metadata.
- `workflow` is the canonical governance object for consumers that prefer snake_case governance fields while retaining backward-compatible camelCase fields at the feature root.
- `workflow.approver_role` remains `null` unless the source workflow-state explicitly provides a reliable approver role.
- `workflow.last_updated` is derived from workflow-state or artifact timestamps, falling back to the dashboard generation time.
- `framework/07-control-tower/workflow-ownership-matrix.md` is the source of thresholds, owner-role defaults, approver-role defaults, and PM intervention rules when workflow-state data is incomplete.
- If the matrix cannot be parsed cleanly, the generator uses a small internal fallback mapping derived from the same matrix and preserves backward-compatible output.
- `workflow.expected_max_days` and `workflow.pm_intervention_trigger` are derived governance fields used by the dashboard for staleness and intervention surfacing.
- Future context health fields are reserved for the Control Tower dashboard and should remain additive:
  - `contextHealthScore`
  - `contextPackages`
  - `contextDriftCount`
  - `staleContextPackages`
  - `contextSecurityFindings`
  - `contextEvalStatus`
  - `contextLastReviewed`
- Future operational fields are also reserved and should remain additive:
  - `impactRisk`
  - `impactedArtifacts`
  - `contextVersionStatus`
  - `driftStatus`
  - `prReviewStatus`
  - `harnessType`
  - `agentRunHealth`
  - `agentReworkCount`
  - `tokenBudgetStatus`
- Future enterprise-scale fields are also reserved and should remain additive:
  - `portfolio`
  - `program`
  - `dependencies`
  - `knowledge`
  - `accelerators`
  - `agentCollaboration`
  - `evaluation`
- `traceabilityId`, `jiraKey`, and `confluencePageId` are read from the traceability matrix when available.
- `quality.validationStatus` is a summary of local validation evidence only.
- `interventions` is a convenience list for PM review and does not change workflow state.
