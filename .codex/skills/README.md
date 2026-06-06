# Codex Skills

This folder contains the canonical project-local Codex skills under `.codex/skills/` for the AI SDLC.

Skills are reusable procedures. Repository-specific lifecycle behavior, artifact placement, context loading, approval handling, and governance are defined by the framework adapter documents:

- `framework/01-lifecycle/skill-orchestration-adapter.md`
- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`

Support skills are also reusable procedures. They assist the lifecycle but are not lifecycle stages:

- `capability-onboarding`
- `source-ingestion`
- `repo-discovery`
- `artifact-review`
- `wynxx-backlog-ingestion`
- `decision`
- `traceability-review`
- `feedback-capture`

Each skill follows the Codex folder-based structure:

```text
skill-name/
├── SKILL.md
├── references/
├── assets/
└── scripts/
