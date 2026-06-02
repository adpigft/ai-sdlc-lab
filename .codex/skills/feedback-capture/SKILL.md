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
