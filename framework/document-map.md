# AI SDLC Canonical Document Map

## Purpose

This map tells users which framework document is authoritative for each topic and which documents are supporting references. It reduces duplication and helps PO, BA, SA, QA, Developer, DevSecOps, platform, and multi-squad users start in the right place.

Git remains the source of truth. Jira tracks workflow. Confluence publishes reviewed summaries.

## Canonical Documents By Topic

| Topic | Canonical Document | Supporting Documents |
| --- | --- | --- |
| User onboarding | `README.md` | `framework/document-map.md`, `AGENTS.md` |
| Codex operating rules | `AGENTS.md` | `.codex/skills/README.md`, `.codex/skills/*/SKILL.md` |
| Workflow state | `framework/workflow/workflow-state-guide.md` | `framework/workflow-state/state-machine.md`, `framework/workflow/workflow-state-template.yaml` |
| `Review.`, `Approved.`, `Status.` | `framework/workflows/review-approval-flow.md` | `framework/workflow/workflow-state-guide.md`, `framework/workflow-state/approval-events.md` |
| Skill prerequisite validation | `framework/workflows/skill-prerequisite-validation.md` | `framework/context/stage-context-packs.md`, `framework/prompt-patterns/standard-response-format.md` |
| Context routing and token discipline | `framework/context/context-pack-model.md` | `framework/context/stage-context-packs.md`, `framework/context/context-index-template.md` |
| Lightweight indexing | `framework/indexing/indexing-model.md` | `framework/indexing/framework-index-template.md`, `framework/indexing/domain-index-template.md`, `framework/indexing/capability-index-template.md` |
| Prompt patterns | `framework/prompt-patterns/prompt-pattern-model.md` | `framework/prompt-patterns/*-pattern.md`, `framework/prompt-patterns/standard-response-format.md`, `framework/prompt-patterns/README.md` |
| Implementation placement | `framework/service-architecture/implementation-placement-model.md` | `framework/multi-squad/path-governance-model.md` |
| Service ownership | `framework/service-architecture/service-catalog-template.md` | `framework/multi-squad/domain-ownership-model.md` |
| Frontend ownership | `framework/frontend/frontend-catalog-template.md` | `framework/frontend/shared-frontend-ownership.md`, `framework/frontend/app-catalog-template.md` |
| Shared asset ownership | `framework/multi-squad/shared-asset-ownership-model.md` | `framework/libraries/shared-library-governance.md`, `framework/libraries/library-catalog-template.md` |
| Path governance | `framework/multi-squad/path-governance-model.md` | `framework/multi-squad/codeowners-guidelines.md`, `framework/multi-squad/branch-and-pr-model.md` |
| Jira model | `framework/jira/jira-operating-model.md` | `framework/jira/jira-issue-hierarchy.md`, `framework/jira/jira-state-mapping.md`, `scripts/jira/README.md` |
| Confluence model | `scripts/confluence/README.md` | `scripts/confluence/templates/*.md` |
| Automation scripts | `scripts/` | `.github/workflows/ai-sdlc-validate.yml` |
| Traceability | `traceability/traceability-matrix.md` | `framework/templates/traceability-row-template.md`, `.codex/skills/traceability-review/SKILL.md` |
| Feedback | `feedback/feedback-log.md` | `framework/templates/feedback-entry-template.md`, `.codex/skills/feedback-capture/SKILL.md` |
| Standards | `framework/standards/` | capability artifacts and validation reports |

## Documents That Should Not Be Duplicated

- Do not duplicate workflow-state rules outside `framework/workflow/workflow-state-guide.md`; link to it.
- Do not duplicate `Review.`, `Approved.`, and `Status.` behavior outside `framework/workflows/review-approval-flow.md`; link to it.
- Do not duplicate skill prerequisite rules outside `framework/workflows/skill-prerequisite-validation.md`; link to it.
- Do not duplicate implementation placement rules outside `framework/service-architecture/implementation-placement-model.md`; link to it.
- Do not duplicate context routing rules outside `framework/context/context-pack-model.md`; link to it.
- Do not duplicate source artifact content in indexes; indexes are navigation aids only.
- Do not duplicate prompt pattern rules in skills or artifacts; link to `framework/prompt-patterns/` when execution structure is needed.
- Do not duplicate service, frontend, or shared asset ownership tables in capability artifacts; reference the approved catalog or template.
- Do not duplicate Jira or Confluence payload behavior in capability artifacts; use the scripts and their README files.
- Do not duplicate coding, API, security, or testing standards inside each capability unless a capability needs an approved exception.

## Guidance For New Users

1. Start with `README.md` to understand the framework, repository structure, lifecycle, and commands.
2. Use `AGENTS.md` to understand how Codex must behave in this repository.
3. Use `framework/workflows/review-approval-flow.md` for `Status.`, `Review.`, `Approved.`, `Resolve findings.`, and `Proceed.`.
4. Use `framework/workflow/workflow-state-guide.md` when creating or updating `workflow-state.yaml`.
5. Use `framework/workflows/skill-prerequisite-validation.md` to check whether a skill may proceed before reading broad context or creating artifacts.
6. Use `framework/context/context-pack-model.md` and `framework/context/stage-context-packs.md` to decide what to read for each stage.
7. Use `framework/indexing/indexing-model.md` when lightweight indexes are needed for navigation at multi-squad scale.
8. Use `framework/prompt-patterns/` when a stage needs a repeatable response shape or execution checklist.
9. Before implementation, use `framework/service-architecture/implementation-placement-model.md` and the ownership catalogs to decide allowed paths and restricted paths.
10. Use `scripts/` and `.github/workflows/ai-sdlc-validate.yml` to validate the framework locally and in GitHub Actions.
11. Keep capability truth in Git. Jira and Confluence outputs are generated views until API integrations are explicitly approved.
