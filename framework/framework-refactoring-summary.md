# Framework Refactoring Summary

## Scope

Implemented the approved skill refactoring across the AI-SDLC framework without modifying application source code.

## Canonical Skill Changes

- Renamed `discovery-engineering` to `discovery`
- Renamed `specification` to `requirements-definition`
- Renamed `wynxx-backlog-ingestion` to `backlog-ingestion`
- Merged the brownfield wrapper skills into the canonical lifecycle skills:
  - `intent-definition` -> `intent`
  - `specification-definition` -> `requirements-definition`
  - `solution-design` -> `design`
- Removed the deprecated wrapper skills and the legacy `specification` skill from `.codex/skills/`
- Added the separate bridge skills requested by the refactoring plan:
  - `modernization-readiness`
  - `implementation-readiness`
  - `implementation-planning`
  - `vertical-slice-planning`
  - `implementation-architecture`

## Decision Skill

Extended `decision` to support:

- ADR management
- assumption management
- architecture decisions
- business decisions

## Framework Documentation Updated

- Skill catalog and orchestration docs
- Lifecycle and workflow-state docs
- Prompt patterns
- Brownfield modernization flow docs
- Wynxx backlog integration docs
- Jira lifecycle integration docs
- Navigation and smoke-test docs
- Generated skill-quality summary
- README examples and lifecycle references

## Files Changed

- `.codex/skills/README.md`
- `.codex/skills/artifact-review/SKILL.md`
- `.codex/skills/decision/SKILL.md`
- `.codex/skills/design/SKILL.md`
- `.codex/skills/discovery/SKILL.md`
- `.codex/skills/gap-analysis/SKILL.md`
- `.codex/skills/impact-analysis/SKILL.md`
- `.codex/skills/implementation/SKILL.md`
- `.codex/skills/intent/SKILL.md`
- `.codex/skills/backlog-ingestion/SKILL.md`
- `.codex/skills/implementation-architecture/SKILL.md`
- `.codex/skills/implementation-planning/SKILL.md`
- `.codex/skills/implementation-readiness/SKILL.md`
- `.codex/skills/modernization-readiness/SKILL.md`
- `.codex/skills/requirements-definition/SKILL.md`
- `.codex/skills/vertical-slice-planning/SKILL.md`
- `README.md`
- `build/skills/skill-quality-summary.json`
- `framework/00-navigation/document-map.md`
- `framework/01-lifecycle/canonical-workflow-state-model.md`
- `framework/01-lifecycle/prompt-patterns/README.md`
- `framework/01-lifecycle/prompt-patterns/design-input-review-pattern.md`
- `framework/01-lifecycle/prompt-patterns/design-pattern.md`
- `framework/01-lifecycle/prompt-patterns/implementation-architecture-pattern.md`
- `framework/01-lifecycle/prompt-patterns/implementation-pattern.md`
- `framework/01-lifecycle/prompt-patterns/implementation-planning-pattern.md`
- `framework/01-lifecycle/prompt-patterns/implementation-readiness-pattern.md`
- `framework/01-lifecycle/prompt-patterns/intent-pattern.md`
- `framework/01-lifecycle/prompt-patterns/modernization-readiness-review-pattern.md`
- `framework/01-lifecycle/prompt-patterns/specification-pattern.md`
- `framework/01-lifecycle/prompt-patterns/vertical-slice-planning-pattern.md`
- `framework/01-lifecycle/skill-orchestration-adapter.md`
- `framework/01-lifecycle/workflow/workflow-state-guide.md`
- `framework/01-lifecycle/workflows/03-spec-to-build.md`
- `framework/01-lifecycle/workflows/review-approval-flow.md`
- `framework/01-lifecycle/workflows/skill-prerequisite-validation.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/03-delivery-governance/service-architecture/implementation-placement-model.md`
- `framework/06-tool-integrations/jira/jira-git-lifecycle-integration.md`
- `framework/06-tool-integrations/mcp-integration-setup.md`
- `framework/06-tool-integrations/mcp-subagent-architecture.md`
- `framework/11-smoke-tests/skill-quality-review.md`
- `framework/12-impact-analysis/change-impact-workflow.md`
- `framework/12-impact-analysis/impact-analysis-model.md`
- `framework/24-discovery-engineering/brownfield-modernization-flow.md`
- `framework/24-discovery-engineering/current-state-extraction-model.md`
- `framework/24-discovery-engineering/discovery-engineering-model.md`
- `framework/24-discovery-engineering/modernization-readiness-review.md`
- `framework/24-discovery-engineering/recovered-artifact-confidence-model.md`
- `framework/framework-refactoring-summary.md`

## Validation

- `git diff --check` passed
- Old skill-name search returned no active skill-name hits in the canonical catalog
- Deprecated wrapper folders were removed from `.codex/skills/`

## Notes

- I did not modify any lending-app source files.
- I did not commit any changes.
- Legacy framework folder names such as `framework/24-discovery-engineering/` remain in place as historical framework paths, but the skill catalog now uses the new canonical names.
