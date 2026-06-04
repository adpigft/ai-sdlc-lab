# AI SDLC Canonical Document Map

## Purpose

This map tells users which framework document is authoritative for each topic and which documents are supporting references. It reduces duplication and helps PO, BA, SA, QA, Developer, DevSecOps, platform, and multi-squad users start in the right place.

Git remains the source of truth. Jira tracks workflow. Confluence publishes reviewed summaries.

## Canonical Documents By Topic

| Topic | Canonical Document | Supporting Documents |
| --- | --- | --- |
| User onboarding | `README.md` | `framework/00-navigation/document-map.md`, `AGENTS.md` |
| Codex operating rules | `AGENTS.md` | `.codex/skills/README.md`, `.codex/skills/*/SKILL.md` |
| Skill orchestration adapter | `framework/01-lifecycle/skill-orchestration-adapter.md` | `framework/01-lifecycle/workflow/workflow-state-guide.md`, `framework/01-lifecycle/workflows/review-approval-flow.md` |
| Skill context adapter | `framework/02-context-control/context/skill-context-adapter.md` | `framework/02-context-control/context/stage-context-packs.md`, `framework/02-context-control/context/context-pack-model.md` |
| Artifact placement adapter | `framework/03-delivery-governance/artifact-placement-model.md` | `README.md`, `AGENTS.md`, `framework/07-templates/` |
| Support skills | `.codex/skills/capability-onboarding/SKILL.md`, `.codex/skills/source-ingestion/SKILL.md`, `.codex/skills/repo-discovery/SKILL.md`, `.codex/skills/artifact-review/SKILL.md` | `framework/01-lifecycle/skill-orchestration-adapter.md`, `framework/02-context-control/context/skill-context-adapter.md`, `framework/03-delivery-governance/artifact-placement-model.md` |
| Workflow state | `framework/01-lifecycle/workflow/workflow-state-guide.md` | `framework/01-lifecycle/workflow-state/state-machine.md`, `framework/01-lifecycle/workflow/workflow-state-template.yaml` |
| Capability artifact naming | `README.md` | `AGENTS.md`, `framework/01-lifecycle/workflow/workflow-state-guide.md`, `framework/07-templates/` |
| `Review.`, `Approved.`, `Status.` | `framework/01-lifecycle/workflows/review-approval-flow.md` | `framework/01-lifecycle/workflow/workflow-state-guide.md`, `framework/01-lifecycle/workflow-state/approval-events.md` |
| PR review | `framework/01-lifecycle/workflows/pr-review-flow.md` | `.codex/skills/pr-review/SKILL.md`, `framework/01-lifecycle/prompt-patterns/pr-review-pattern.md` |
| Skill prerequisite validation | `framework/01-lifecycle/workflows/skill-prerequisite-validation.md` | `framework/02-context-control/context/stage-context-packs.md`, `framework/01-lifecycle/prompt-patterns/standard-response-format.md` |
| Domain, capability, and feature model | `README.md` | `framework/03-delivery-governance/multi-squad/domain-ownership-model.md` |
| Context routing and token discipline | `framework/02-context-control/context/context-pack-model.md` | `framework/02-context-control/context/stage-context-packs.md`, `framework/02-context-control/context/context-index-template.md` |
| Lightweight indexing | `framework/00-navigation/indexing/indexing-model.md` | `framework/00-navigation/indexing/framework-index-template.md`, `framework/00-navigation/indexing/domain-index-template.md`, `framework/00-navigation/indexing/capability-index-template.md` |
| Capability summaries | `framework/00-navigation/capability-summary/capability-summary-model.md` | `framework/00-navigation/capability-summary/capability-summary-template.md` |
| Prompt patterns | `framework/01-lifecycle/prompt-patterns/prompt-pattern-model.md` | `framework/01-lifecycle/prompt-patterns/*-pattern.md`, `framework/01-lifecycle/prompt-patterns/standard-response-format.md`, `framework/01-lifecycle/prompt-patterns/README.md` |
| Implementation placement | `framework/03-delivery-governance/service-architecture/implementation-placement-model.md` | `framework/03-delivery-governance/multi-squad/path-governance-model.md` |
| Service ownership | `framework/03-delivery-governance/service-architecture/service-catalog-template.md` | `framework/03-delivery-governance/multi-squad/domain-ownership-model.md` |
| Frontend ownership | `framework/03-delivery-governance/frontend/frontend-catalog-template.md` | `framework/03-delivery-governance/frontend/shared-frontend-ownership.md`, `framework/03-delivery-governance/frontend/app-catalog-template.md` |
| Shared asset ownership | `framework/03-delivery-governance/multi-squad/shared-asset-ownership-model.md` | `framework/03-delivery-governance/libraries/shared-library-governance.md`, `framework/03-delivery-governance/libraries/library-catalog-template.md` |
| Path governance | `framework/03-delivery-governance/multi-squad/path-governance-model.md` | `framework/03-delivery-governance/multi-squad/codeowners-guidelines.md`, `framework/03-delivery-governance/multi-squad/branch-and-pr-model.md` |
| Jira model | `framework/06-tool-integrations/jira/jira-operating-model.md` | `framework/06-tool-integrations/jira/jira-issue-hierarchy.md`, `framework/06-tool-integrations/jira/jira-state-mapping.md`, `scripts/jira/README.md` |
| Confluence model | `scripts/confluence/README.md` | `scripts/confluence/templates/*.md` |
| Automation scripts | `scripts/` | `.github/workflows/ai-sdlc-validate.yml` |
| Traceability | `traceability/traceability-matrix.md` | `framework/07-templates/traceability-row-template.md`, `.codex/skills/traceability-review/SKILL.md` |
| Feedback | `feedback/feedback-log.md` | `framework/07-templates/feedback-entry-template.md`, `.codex/skills/feedback-capture/SKILL.md` |
| Standards | `framework/04-engineering-standards/standards/` | capability context and feature artifacts and validation reports |

## Documents That Should Not Be Duplicated

- Do not duplicate workflow-state rules outside `framework/01-lifecycle/workflow/workflow-state-guide.md`; link to it.
- Do not duplicate skill orchestration, context-loading, or artifact-placement rules inside `.codex/skills`; use the adapter documents.
- Do not duplicate capability artifact naming rules outside `README.md` and `AGENTS.md`; new guidance should use canonical paths and mention old paths only as migration aliases.
- Do not duplicate `Review.`, `Approved.`, and `Status.` behavior outside `framework/01-lifecycle/workflows/review-approval-flow.md`; link to it.
- Do not duplicate skill prerequisite rules outside `framework/01-lifecycle/workflows/skill-prerequisite-validation.md`; link to it.
- Do not redefine the domain/capability/feature hierarchy outside `README.md` and `framework/03-delivery-governance/multi-squad/domain-ownership-model.md`; link to it.
- Do not duplicate implementation placement rules outside `framework/03-delivery-governance/service-architecture/implementation-placement-model.md`; link to it.
- Do not duplicate context routing rules outside `framework/02-context-control/context/context-pack-model.md`; link to it.
- Do not duplicate source artifact content in indexes; indexes are navigation aids only.
- Do not duplicate source artifact content in capability summaries; summaries are navigation aids only.
- Do not duplicate prompt pattern rules in skills or artifacts; link to `framework/01-lifecycle/prompt-patterns/` when execution structure is needed.
- Do not duplicate service, frontend, or shared asset ownership tables in capability context and feature artifacts; reference the approved catalog or template.
- Do not duplicate Jira or Confluence payload behavior in capability context and feature artifacts; use the scripts and their README files.
- Do not duplicate coding, API, security, or testing standards inside each capability unless a capability needs an approved exception.

## Guidance For New Users

1. Start with `README.md` to understand the framework, repository structure, lifecycle, and commands.
2. Use `AGENTS.md` to understand how Codex must behave in this repository.
3. Use `.codex/skills/*/SKILL.md` for reusable procedures.
4. Use `framework/01-lifecycle/skill-orchestration-adapter.md`, `framework/02-context-control/context/skill-context-adapter.md`, and `framework/03-delivery-governance/artifact-placement-model.md` to adapt skills to this framework.
5. Use `framework/01-lifecycle/workflows/review-approval-flow.md` for `Status.`, `Review.`, `Approved.`, `Resolve findings.`, and `Proceed.`.
6. Use `framework/01-lifecycle/workflow/workflow-state-guide.md` when creating or updating `workflow-state.yaml`.
7. Use `framework/01-lifecycle/workflows/skill-prerequisite-validation.md` to check whether a skill may proceed before reading broad context or creating artifacts.
8. Use `framework/02-context-control/context/context-pack-model.md` and `framework/02-context-control/context/stage-context-packs.md` to decide what to read for each stage.
9. Use `framework/00-navigation/indexing/indexing-model.md` when lightweight indexes are needed for navigation at multi-squad scale.
10. Use `framework/00-navigation/capability-summary/capability-summary-model.md` when a single-page capability navigation aid is needed.
11. Use `framework/01-lifecycle/prompt-patterns/` when a stage needs a repeatable response shape or execution checklist.
12. Before implementation, use `framework/03-delivery-governance/service-architecture/implementation-placement-model.md` and the ownership catalogs to decide allowed paths and restricted paths.
13. Use `scripts/` and `.github/workflows/ai-sdlc-validate.yml` to validate the framework locally and in GitHub Actions.
14. Keep capability truth in Git. Jira and Confluence outputs are generated views until API integrations are explicitly approved.

Canonical lifecycle skill names are `$intent`, `$specification`, `$design`, `$test-design`, `$implementation`, `$pr-review`, `$validation`, and `$release`.
