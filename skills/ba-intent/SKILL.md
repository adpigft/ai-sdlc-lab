---
name: ba-intent
description: Ask discovery questions, capture business intent, and create or update intent.md for a feature.
---

# BA Intent Skill

## Purpose
Capture business intent before requirements, design, tests, or code are created.

## When to use
Use when the user starts a new feature or changes business intent.

## Inputs
- User business request
- Existing intent.md if available
- Domain/capability context if available
- Jira/Confluence references if available

## Process
1. Ask discovery questions first.
2. Capture users, problem, outcome, scope, out of scope, assumptions, constraints, and success metrics.
3. Identify missing information.
4. Summarize understanding.
5. Ask for approval.
6. Create or update intent.md only after approval.

## Output
- domains/<domain>/capabilities/<capability>/intent/intent.md

## Quality checks
- Problem is clear.
- Outcome is measurable.
- Users/stakeholders are identified.
- Scope and out of scope are explicit.
- Assumptions and constraints are listed.
- Human approval section exists.

## Human gate
PO / BA approval is required before specification starts.

## Next skill
ba-specification
