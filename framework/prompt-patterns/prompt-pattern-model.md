# Prompt Pattern Model

## Purpose

Define the common shape for lightweight prompt patterns used across the AI-SDLC lifecycle.

## Principles

- Patterns guide execution; source artifacts remain authoritative.
- Patterns should reduce ambiguity without forcing unnecessary artifacts.
- Reads must be stage-specific and token-aware.
- The AI must stop when approvals, required inputs, or placement metadata are missing.
- Full framework reads are allowed only for framework assessment or framework changes.
- Skill outputs should end with the standard response footer defined in `framework/prompt-patterns/standard-response-format.md`.

## Pattern Fields

Each pattern should include:

- role
- purpose
- required inputs
- required reads
- optional reads
- forbidden reads
- constraints
- expected outputs
- validation checks
- stop conditions
- standard response format

## Context Discipline

Use `framework/context/stage-context-packs.md` to decide what to read for each stage. Use optional indexes only as routing aids. Indexes do not replace source artifacts.

Before implementation, source code reads must be limited to approved `allowed_paths`. Change-request and defect-fix work may read impacted paths only after impact analysis or RCA identifies them.

## Standard Response Format

Use `framework/prompt-patterns/standard-response-format.md` as the canonical response footer guidance.

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
