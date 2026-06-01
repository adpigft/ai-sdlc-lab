---
name: adr-review
description: Review ADRs.
---

# ADR Review Skill

## Purpose
Review ADRs.

## When to use
Use when an ADR draft is ready for review before acceptance.

## Inputs
- `ADR-*.md`

## Process
1. Review decision completeness.
2. Review risks and tradeoffs.
3. Review operational impacts.
4. Review security impacts.
5. Review testing impacts.
6. Return an approval recommendation.

## Output
- `approve`
- `approve with conditions`
- `reject`

## Checks
- decision completeness
- risks
- tradeoffs
- operational impacts
- security impacts
- testing impacts

## Rules
- do not modify artifacts
- review only

## Human gate
ADR approval is required before dependent work can proceed.
