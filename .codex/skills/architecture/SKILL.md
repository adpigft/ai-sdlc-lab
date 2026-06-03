---
name: architecture
description: Temporary compatibility alias for the canonical `design` skill during the migration cycle.
---

# Architecture Alias Skill

## Purpose
Preserve `$architecture` for one migration cycle while the canonical procedure-oriented command becomes `$design`.

## When to use
Use `$design` for the design stage. If the user invokes `$architecture`, route to `.codex/skills/design/SKILL.md`.

## Behavior
This alias must not define separate behavior. It delegates to `$design`.

## Next skill or next workflow step
Use `$design`.
