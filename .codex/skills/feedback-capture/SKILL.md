---
name: feedback-capture
description: Capture review findings, defects, change requests, and stakeholder feedback, then apply controlled corrections.
---

# Feedback Skill

## Purpose
Capture feedback and convert it into controlled corrections.

## When to use
Use whenever feedback, defect, review finding, or change request is received.

## Inputs
- Feedback source
- Affected artifacts
- Current traceability matrix
- Jira reference

## Context pack
Use the `Feedback Capture` pack in `framework/02-context-control/context/stage-context-packs.md`.

Required reads:
- This skill document.
- Feedback log.
- Impacted capability or domain artifacts.
- Active `workflow-state.yaml` when the capability exists.

Optional reads:
- Traceability, validation report, release notes, and Jira/Confluence placeholders.

Forbidden reads:
- Unrelated source and unrelated domains.
- Code changes before impact analysis and approval.

Escalation rule: Read additional artifacts only when the feedback item maps to them through impact analysis.

Token discipline rule: Keep context to the feedback item and impacted artifacts; full framework reads are allowed only for framework assessment or framework changes.

Stop conditions:
- Feedback affects requirements, tests, code, or release but owner approval is missing.
- Customer-sensitive details are not masked.

## Process
1. Record feedback.
2. Classify as clarification, defect, change request, risk, or improvement.
3. Identify affected artifacts.
4. Propose corrections.
5. Ask for approval.
6. Apply corrections only to affected files.
7. Update traceability.

## Outputs
- feedback/feedback-log.md
- Updated affected artifacts
- Updated traceability matrix

## Quality checks
- Feedback has owner and status.
- Affected artifacts are identified.
- Corrections are traceable.
- No unrelated rewrite is performed.

## Human gate
Artifact owner approval required before correction is applied.
