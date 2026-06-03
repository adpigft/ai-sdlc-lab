---
name: new
description: Temporary compatibility alias for the canonical `intent` skill during the migration cycle.
---

# New Alias Skill

## Purpose
Preserve `$new` for one migration cycle while the canonical procedure-oriented command becomes `$intent`.

## When to use
Use `$intent` for new capability intent discovery. If the user invokes `$new`, route to `.codex/skills/intent/SKILL.md`.

## Behavior
This alias must not define separate behavior. It delegates to `$intent`.

## Next skill or next workflow step
Use `$intent`.
