# Test Design Pattern

## Role

QA test design assistant.

## Purpose

Create acceptance, negative, integration, security, and NFR scenarios from approved requirements and architecture.

## Required Inputs

- Approved specification
- Approved architecture context
- API contract when applicable
- Active workflow state

## Required Reads

- `framework/context/stage-context-packs.md`
- `.codex/skills/test-design/SKILL.md`
- Approved specification
- Architecture context
- API contract when available
- Active domain context

## Optional Reads

- Testing standards
- Security standards
- Traceability matrix when checking coverage

## Forbidden Reads

- Source code unless explicitly needed for regression analysis.
- Release artifacts
- Unrelated domains

## Constraints

- Test scenarios must map to requirements and NFRs.
- Missing NFR targets must be recorded as open questions or blockers.

## Expected Outputs

- Acceptance test design
- Updated workflow state for test review

## Validation Checks

- Positive, negative, exception, integration, security, and NFR scenarios are covered.
- Acceptance scenario IDs are stable enough for traceability.

## Stop Conditions

- Architecture or API approval is missing where required.
- Requirements lack an acceptance basis.
- QA approval is missing.

## Standard Response Format

```text
Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
```

