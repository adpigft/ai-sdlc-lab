---
name: source-ingestion
description: Convert external delivery documents into AI-readable summaries and extraction notes.
---

# Source Ingestion Skill

## Purpose

Convert external business, delivery, or workshop documents into structured AI-readable inputs for analysis and follow-up work.

## When To Use

Use `$source-ingestion` when inputs come from Word, Excel, PowerPoint, Confluence, Jira, email, workshop notes, diagrams, or test documents.

## Inputs Needed

- External source documents
- Source type
- Owner
- Target artifact type
- Known feature, capability, or domain
- Extraction goal

## Framework Adapter

When this skill is used inside this repository, context loading, source handling, and human review expectations are defined by:

- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/01-lifecycle/skill-orchestration-adapter.md`

## Procedure

1. Inventory the source documents and their types.
2. Extract the strongest available business intent, requirements, design inputs, and test inputs.
3. Record decisions, assumptions, conflicts, and missing information.
4. Identify recommended target artifacts for follow-up work.
5. Produce a reviewable summary rather than an approved delivery artifact.
6. Stop for human review when the extracted content is ambiguous or incomplete.

## Outputs Produced

- Source ingestion summary
- Extracted notes for business intent, requirements, design, and tests
- Conflict and gap list
- Recommended target artifact list
- Human review notes

## Artifact Structure

1. Source Inventory
2. Extracted Business Intent
3. Extracted Requirements
4. Extracted Design Inputs
5. Extracted Test Inputs
6. Decisions / Assumptions
7. Conflicts
8. Missing Information
9. Recommended Target Artifacts
10. Human Review Notes

## Quality Checks

- Source documents are inventoried clearly.
- Extraction preserves the original meaning as closely as possible.
- Conflicts and missing information are visible.
- The summary does not claim approval.
- Approved Git artifacts remain the source of truth.

## Stop Conditions

- The extraction goal is unclear.
- Source documents are missing or unreadable.
- The user asks for approval from the source-ingestion summary.

## Human Approval Expectations

Human review is required before source-ingested content is treated as delivery input.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
