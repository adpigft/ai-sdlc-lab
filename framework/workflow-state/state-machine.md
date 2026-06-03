# Workflow State Machine

## Purpose

Define a lightweight workflow-state model that lets Codex move to the next AI SDLC skill after a human approval, without asking users to manually select the next skill.

## Scope

This state machine coordinates lifecycle progress only. It does not replace Git artifacts, Jira approvals, Confluence publication, traceability, or human gates.

## States

| State | Meaning | Primary Skill |
| --- | --- | --- |
| `idea` | Raw capability idea or intake exists. | `intent` |
| `intent_review` | Intent is being drafted or reviewed for approval. | `intent` |
| `specification_review` | Specification is being drafted or reviewed for approval. | `specification` |
| `architecture_review` | Architecture, API considerations, decisions, and implementation planning are being drafted or reviewed. | `design` |
| `test_review` | QA test design is being drafted or reviewed. | `test-design` |
| `implementation_ready` | Approved requirements, architecture, tests, and traceability are ready for implementation slicing. | `implementation` |
| `implementation_in_progress` | One approved implementation slice is active. | `implementation` |
| `validation_ready` | Implementation is ready for QA validation. | `validation` |
| `release_ready` | QA validation is approved and release readiness can start. | `release` |
| `released` | Release is approved and completed. | `feedback-capture` |
| `blocked` | Required approval, evidence, decision, dependency, or artifact is missing. | Current owner |

## Approval Transitions

| Approval Event | From State | To State | Next Skill |
| --- | --- | --- | --- |
| `intent_approval` | `intent_review` | `specification_review` | `specification` |
| `specification_approval` | `specification_review` | `architecture_review` | `design` |
| `architecture_approval` | `architecture_review` | `test_review` | `test-design` |
| `test_design_approval` | `test_review` | `implementation_ready` | `implementation` |
| `implementation_start_approval` | `implementation_ready` | `implementation_in_progress` | `implementation` |
| `implementation_slice_approval` | `implementation_in_progress` | `validation_ready` | `validation` |
| `validation_approval` | `validation_ready` | `release_ready` | `release` |
| `release_approval` | `release_ready` | `released` | `feedback-capture` |

## Runtime Behavior

When an approval is received, Codex should:

1. Identify the capability and current state.
2. Identify the approved artifact and approval gate.
3. Verify the approval event is valid for the current state.
4. Check for blocking conditions.
5. Set the next state and next skill.
6. Announce the transition.
7. Start the next skill automatically.

Example:

```text
Intent approval received for payments/qr-refund.
Transition: intent_review -> specification_review.
Next skill: specification.
```

## Blocking Rules

Transition to `blocked` instead of the next state when:

- Approval is conditional and the condition blocks downstream work.
- The required artifact is missing.
- Mandatory open questions remain unresolved.
- Traceability has mandatory gaps.
- Architecture has unresolved blocking decisions.
- The next step would create source code before all pre-build gates are approved.
- Required validation, CI, security, release, or rollback evidence is missing.

## Source Of Truth

The workflow-state file should be stored in Git beside the capability artifacts when adopted. Jira may mirror the state for work management, but Git remains the source of truth for lifecycle state history.

Recommended location:

```text
domains/<domain>/capabilities/<capability>/workflow-state.yaml
```

## Traceability Relationship

Workflow state records the lifecycle position, next skill, blockers, and approval history. Traceability records the requirement-to-artifact-to-evidence mapping. They should cross-check each other, but one should not replace the other.
