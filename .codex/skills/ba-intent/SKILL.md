---
name: ba-intent
description: Ask discovery questions, capture business intent, and create or update intent.md for a feature.
---

# BA Intent Skill

## Purpose
Capture business intent before requirements, design, tests, or code are created, after first checking the repository for existing domain and capability patterns that may be reused.

## When to use
Use when the user starts a new feature or changes business intent.

## Inputs
- User business request
- Existing intent.md if available
- Domain/capability context if available
- Jira/Confluence references if available
- Repository capability inventory from `domains/*/capabilities/*`

## Process
1. Scan `domains/*/capabilities/*` before asking questions.
2. Identify existing capabilities, existing intent artifacts, and artifact patterns in nearby domains.
3. Note likely reuse candidates and similar capabilities that may already solve part of the request.
4. Detect the domain naming, capability naming, metadata, and approval patterns already used in the repository.
5. Ask discovery questions only after the repository scan is complete.
6. Capture users, problem, outcome, scope, out of scope, assumptions, constraints, and success metrics.
7. Identify missing information.
8. Summarize understanding, including reuse candidates and any domain pattern observations that matter to intent.
9. Ask for approval.
10. Create or update intent.md only after approval.

## Output
- domains/<domain>/capabilities/<capability>/features/<feature>/intent/intent.md
- A reuse recommendation or nearest-match capability if an existing capability is materially similar

## Quality checks
- Problem is clear.
- Outcome is measurable.
- Users/stakeholders are identified.
- Scope and out of scope are explicit.
- Assumptions and constraints are listed.
- Existing capabilities and intent artifacts were scanned before discovery questions were asked.
- Similar capabilities and reuse opportunities were identified and reported.
- Domain and capability naming patterns in the repository were considered.
- Human approval section exists.

## Human gate
PO / BA approval is required before specification starts.

## Next skill
ba-specification
