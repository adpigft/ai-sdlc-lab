---
name: adr-creation
description: Draft architecture decision records for unresolved design choices and approval routing.
---

# ADR Creation Skill

## Purpose
Create ADR drafts that capture context, options, recommendations, and approval conditions.

## When to use
Use when a design decision must be recorded before implementation can continue.

## Inputs
- approved intent
- approved specification
- approved context
- implementation plan
- open questions

## Process
1. Summarize the decision context.
2. List decision options and tradeoffs.
3. Recommend a decision.
4. Capture impacts and conditions.
5. Ask for ADR approval.

## Output
- decisions/ADR-*.md

## Human gate
ADR approval is required before dependent implementation work.

