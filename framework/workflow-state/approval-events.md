# Approval Events

## Purpose

Define the approval events that drive workflow-state transitions after human approval. Approval events let Codex continue the lifecycle automatically while preserving explicit human gates.

## Event Contract

Approval events should capture enough information to prove who approved what, for which capability, and what transition is allowed.

```yaml
event_type: approval_granted
capability: payments/qr-refund
current_state: intent_review
approval_gate: intent_approval
approved_artifact: domains/payments/capabilities/qr-refund/intent/intent.md
approver_role: Product Owner
approver: ""
approval_reference: JIRA-QRREF-001
decision: approved
conditions: []
timestamp: "2026-06-01T00:00:00Z"
next_state: specification_review
next_skill: specification
```

## Supported Decisions

| Decision | Meaning | State Result |
| --- | --- | --- |
| `approved` | Gate is approved with no blocking conditions. | Move to next state. |
| `approved_with_conditions` | Gate is approved, but conditions must be checked. | Move only if conditions are non-blocking; otherwise `blocked`. |
| `changes_required` | Artifact must be revised before proceeding. | Remain in current review state. |
| `rejected` | Artifact or scope is not accepted. | Move to `blocked` or return to earlier lifecycle state. |

## Approval Event To State Transition Mapping

| Approval Gate | Approved Artifact | From State | Next State | Next Skill |
| --- | --- | --- | --- | --- |
| `intent_approval` | Intent | `intent_review` | `specification_review` | `specification` |
| `specification_approval` | Specification | `specification_review` | `architecture_review` | `design` |
| `architecture_approval` | Architecture context, API guidance, ADR status, implementation plan | `architecture_review` | `test_review` | `test-design` |
| `test_design_approval` | Acceptance and QA test design | `test_review` | `implementation_ready` | `implementation` |
| `implementation_start_approval` | Implementation plan and first approved slice | `implementation_ready` | `implementation_in_progress` | `implementation` |
| `implementation_slice_approval` | Implemented slice, PR, unit tests, review evidence | `implementation_in_progress` | `validation_ready` | `validation` |
| `validation_approval` | Validation report and evidence | `validation_ready` | `release_ready` | `release` |
| `release_approval` | Release notes, rollback, risk acceptance, deployment approval | `release_ready` | `released` | `feedback-capture` |

## Required Approval Evidence

| Gate | Minimum Evidence |
| --- | --- |
| `intent_approval` | PO / BA approval reference and approved intent path. |
| `specification_approval` | PO / BA approval reference and approved specification path. |
| `architecture_approval` | Architect approval reference and approved architecture path. |
| `test_design_approval` | QA approval reference and approved test design path. |
| `implementation_start_approval` | Product, architecture, QA, and engineering readiness approval. |
| `implementation_slice_approval` | PR reference, reviewer approval, test result reference, and slice ID. |
| `validation_approval` | QA validation report, defect status, and release readiness recommendation. |
| `release_approval` | PO, QA, Architect, DevSecOps, and Release Manager approval evidence. |

## Automatic Continuation Rule

When `decision` is `approved` and no blocking condition exists, Codex should continue with `next_skill` without asking the user to choose a skill.

When `decision` is `approved_with_conditions`, Codex should classify each condition:

- Non-blocking condition: record the condition and continue.
- Blocking condition: set state to `blocked`, record the condition, and ask for resolution.

## User-Facing Approval Phrases

Codex should treat these as approval events when the capability and artifact can be inferred:

- `Approved intent`
- `Approve specification`
- `Architecture approved`
- `QA approves test design`
- `Implementation slice approved`
- `Validation approved`
- `Release approved`

If the capability or artifact cannot be inferred, Codex should ask one concise clarification question instead of guessing.
