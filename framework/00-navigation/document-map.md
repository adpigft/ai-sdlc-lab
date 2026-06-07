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
| Context quality foundation | `framework/08-context-quality/context-quality-model.md` | `framework/08-context-quality/skill-review-rubric.md`, `framework/08-context-quality/llm-judge-rubrics.md`, `framework/08-context-quality/task-eval-model.md` |
| Context packaging foundation | `framework/09-context-packaging/context-package-model.md` | `framework/09-context-packaging/context-registry-model.md`, `framework/09-context-packaging/context-versioning-policy.md`, `framework/09-context-packaging/context-manifest-model.md`, `scripts/context/README.md` |
| Context observability foundation | `framework/10-context-observability/context-observability-model.md` | `framework/10-context-observability/context-drift-model.md`, `framework/10-context-observability/context-drift-detection-policy.md`, `framework/10-context-observability/context-flywheel.md` |
| Impact analysis foundation | `framework/12-impact-analysis/impact-analysis-model.md` | `framework/12-impact-analysis/change-impact-workflow.md` |
| Spec-aware PR review foundation | `framework/13-pr-review/spec-aware-pr-review-model.md` | `framework/13-pr-review/pr-review-rubric.md`, `framework/13-pr-review/pr-review-feedback-loop.md` |
| Harness catalog | `framework/14-harness-catalog/harness-catalog.md` | `framework/14-harness-catalog/harness-selection-model.md` |
| AgentOps foundation | `framework/15-agentops/agentops-model.md` | `framework/15-agentops/agent-run-log-schema.md`, `scripts/agentops/README.md` |
| Enterprise AI governance | `framework/16-ai-governance/ai-governance-model.md` | `framework/16-ai-governance/model-risk-management.md` |
| Enterprise rollout model | `framework/17-enterprise-rollout/enterprise-rollout-model.md` | `framework/17-enterprise-rollout/squad-adoption-playbook.md` |
| Operating model | `framework/18-operating-model/operating-model.md` | `framework/18-operating-model/change-management-model.md` |
| Cost management | `framework/19-cost-management/token-economics-model.md` | `framework/19-cost-management/model-routing-strategy.md` |
| Access control | `framework/20-access-control/rbac-model.md` | `framework/20-access-control/` |
| Platform architecture | `framework/21-platform-architecture/platform-reference-architecture.md` | `framework/21-platform-architecture/context-registry-architecture.md` |
| Compliance | `framework/22-compliance/compliance-evidence-model.md` | `framework/22-compliance/audit-trail-model.md` |
| Adoption and training | `framework/23-adoption-training/training-curriculum.md` | `framework/23-adoption-training/certification-model.md` |
| Knowledge management | `framework/24-knowledge-management/knowledge-management-model.md` | `framework/24-knowledge-management/knowledge-registry-model.md`, `framework/24-knowledge-management/enterprise-memory-model.md` |
| Accelerator catalog | `framework/25-accelerator-catalog/accelerator-catalog-model.md` | `framework/25-accelerator-catalog/reuse-maturity-model.md` |
| Portfolio management | `framework/26-portfolio-management/portfolio-governance-model.md` | `framework/26-portfolio-management/control-tower-scaling-model.md`, `framework/26-portfolio-management/squad-operating-model.md` |
| Dependency management | `framework/27-dependency-management/dependency-model.md` | `framework/27-dependency-management/dependency-graph-model.md`, `framework/27-dependency-management/dependency-risk-model.md` |
| Multi-agent collaboration | `framework/28-multi-agent-collaboration/agent-collaboration-model.md` | `framework/28-multi-agent-collaboration/context-handoff-model.md`, `framework/28-multi-agent-collaboration/conflict-resolution-model.md` |
| AI evaluation framework | `framework/29-ai-evaluation/evaluation-framework.md` | `framework/29-ai-evaluation/quality-score-model.md`, `framework/29-ai-evaluation/eval-catalog.md`, `framework/29-ai-evaluation/continuous-improvement-flywheel.md` |
| Tool adapter layer | `framework/30-tool-adapters/tool-adapter-model.md` | `framework/30-tool-adapters/tool-change-resilience.md` |
| GUI authoring | `framework/31-gui-authoring/gui-authoring-model.md` | `framework/31-gui-authoring/artifact-editing-workflow.md` |
| Support skills | `.codex/skills/capability-onboarding/SKILL.md`, `.codex/skills/source-ingestion/SKILL.md`, `.codex/skills/repo-discovery/SKILL.md`, `.codex/skills/artifact-review/SKILL.md`, `.codex/skills/wynxx-backlog-ingestion/SKILL.md` | `framework/01-lifecycle/skill-orchestration-adapter.md`, `framework/02-context-control/context/skill-context-adapter.md`, `framework/03-delivery-governance/artifact-placement-model.md` |
| Workflow state | `framework/01-lifecycle/workflow/workflow-state-guide.md` | `framework/01-lifecycle/workflow-state/state-machine.md`, `framework/01-lifecycle/workflow/workflow-state-template.yaml` |
| Capability artifact naming | `README.md` | `AGENTS.md`, `framework/01-lifecycle/workflow/workflow-state-guide.md`, `framework/07-templates/` |
| `Review.`, `Approved.`, `Status.` | `framework/01-lifecycle/workflows/review-approval-flow.md` | `framework/01-lifecycle/workflow/workflow-state-guide.md`, `framework/01-lifecycle/workflow-state/approval-events.md` |
| PR review | `framework/01-lifecycle/workflows/pr-review-flow.md` | `.codex/skills/pr-review/SKILL.md`, `framework/01-lifecycle/prompt-patterns/pr-review-pattern.md` |
| Skill prerequisite validation | `framework/01-lifecycle/workflows/skill-prerequisite-validation.md` | `framework/02-context-control/context/stage-context-packs.md`, `framework/01-lifecycle/prompt-patterns/standard-response-format.md` |
| Domain, capability, and feature model | `README.md` | `framework/03-delivery-governance/multi-squad/domain-ownership-model.md` |
| Context routing and token discipline | `framework/02-context-control/context/context-pack-model.md` | `framework/02-context-control/context/stage-context-packs.md`, `framework/02-context-control/context/context-index-template.md` |
| Context packages and quality | `framework/08-context-quality/context-quality-model.md`, `framework/09-context-packaging/context-package-model.md`, `framework/10-context-observability/context-observability-model.md` | `framework/02-context-control/context/context-pack-model.md`, `framework/08-context-quality/task-eval-model.md`, `framework/10-context-observability/context-drift-model.md` |
| Lightweight indexing | `framework/00-navigation/indexing/indexing-model.md` | `framework/00-navigation/indexing/framework-index-template.md`, `framework/00-navigation/indexing/domain-index-template.md`, `framework/00-navigation/indexing/capability-index-template.md` |
| Capability summaries | `framework/00-navigation/capability-summary/capability-summary-model.md` | `framework/00-navigation/capability-summary/capability-summary-template.md` |
| Prompt patterns | `framework/01-lifecycle/prompt-patterns/prompt-pattern-model.md` | `framework/01-lifecycle/prompt-patterns/*-pattern.md`, `framework/01-lifecycle/prompt-patterns/standard-response-format.md`, `framework/01-lifecycle/prompt-patterns/README.md` |
| Implementation placement | `framework/03-delivery-governance/service-architecture/implementation-placement-model.md` | `framework/03-delivery-governance/multi-squad/path-governance-model.md` |
| Service ownership | `framework/03-delivery-governance/service-architecture/service-catalog-template.md` | `framework/03-delivery-governance/multi-squad/domain-ownership-model.md` |
| Frontend ownership | `framework/03-delivery-governance/frontend/frontend-catalog-template.md` | `framework/03-delivery-governance/frontend/shared-frontend-ownership.md`, `framework/03-delivery-governance/frontend/app-catalog-template.md` |
| Shared asset ownership | `framework/03-delivery-governance/multi-squad/shared-asset-ownership-model.md` | `framework/03-delivery-governance/libraries/shared-library-governance.md`, `framework/03-delivery-governance/libraries/library-catalog-template.md` |
| Path governance | `framework/03-delivery-governance/multi-squad/path-governance-model.md` | `framework/03-delivery-governance/multi-squad/codeowners-guidelines.md`, `framework/03-delivery-governance/multi-squad/branch-and-pr-model.md` |
| Integration foundation | `framework/06-tool-integrations/integration-foundation.md` | `framework/06-tool-integrations/integration-configuration-guide.md`, `.github/workflows/ai-sdlc-validate.yml`, `scripts/jira/README.md`, `scripts/confluence/README.md`, `sonar-project.properties` |
| Integration configuration | `framework/06-tool-integrations/integration-configuration-guide.md` | `framework/06-tool-integrations/integration-foundation.md`, `.github/workflows/ai-sdlc-validate.yml`, `scripts/jira/README.md`, `scripts/confluence/README.md`, `sonar-project.properties` |
| Demo REST/CLI adapters | `framework/06-tool-integrations/demo-rest-cli-adapter-plan.md` | `scripts/jira/rest_cli.py`, `scripts/confluence/rest_cli.py`, `scripts/github/evidence.py`, `scripts/jira/README.md`, `scripts/confluence/README.md`, `scripts/github/README.md` |
| Control Tower dashboard | `framework/07-control-tower/control-tower-data-model.md` | `scripts/dashboard/README.md`, `scripts/dashboard/generate-control-tower.py`, `scripts/dashboard/run-control-tower.sh`, `dashboard/control-tower.html`, `dashboard/control-tower.css`, `dashboard/control-tower.js` |
| MCP integration setup | `framework/06-tool-integrations/mcp-integration-setup.md` | `framework/06-tool-integrations/mcp-runtime-troubleshooting.md`, `framework/06-tool-integrations/mcp-subagent-architecture.md`, `framework/06-tool-integrations/mcp-subagent-smoke-tests.md`, `.env.mcp.example`, `.codex/config.toml`, `framework/06-tool-integrations/ai-sdlc-portal-mvp.md`, `.codex/skills/wynxx-backlog-ingestion/SKILL.md` |
| Jira model | `framework/06-tool-integrations/jira/jira-operating-model.md` | `framework/06-tool-integrations/jira/jira-issue-hierarchy.md`, `framework/06-tool-integrations/jira/jira-state-mapping.md`, `scripts/jira/README.md`, `scripts/jira/templates/*.json` |
| Confluence model | `scripts/confluence/README.md` | `scripts/confluence/templates/*.md`, `scripts/confluence/generate-summary.py` |
| Automation scripts | `scripts/` | `.github/workflows/ai-sdlc-validate.yml`, `sonar-project.properties` |
| Traceability | `traceability/traceability-matrix.md` | `framework/07-templates/traceability-row-template.md`, `.codex/skills/traceability-review/SKILL.md` |
| Feedback | `feedback/feedback-log.md` | `framework/07-templates/feedback-entry-template.md`, `.codex/skills/feedback-capture/SKILL.md` |
| Engineering standards | `framework/04-engineering-standards/standards-index.md` | `framework/04-engineering-standards/java-spring-boot-bootstrap.md`, `framework/04-engineering-standards/flutter-bootstrap.md`, `framework/04-engineering-standards/openapi-generation-standard.md`, `framework/04-engineering-standards/api-security-standard.md`, `framework/04-engineering-standards/database-design-standard.md`, `framework/04-engineering-standards/event-design-standard.md`, `framework/04-engineering-standards/testing-standard.md`, `framework/04-engineering-standards/security-quality-gates.md`, `framework/04-engineering-standards/ai-code-review-standard.md`, `framework/04-engineering-standards/microservice-decomposition-standard.md`, `framework/04-engineering-standards/reference-architecture-standard.md`, `framework/04-engineering-standards/system-modeling-standard.md`, `framework/04-engineering-standards/observability-standard.md`, `framework/04-engineering-standards/shared-library-gradle-standard.md`, `framework/04-engineering-standards/change-management-standard.md` |
| Legacy standards | `framework/04-engineering-standards/standards/` | `framework/04-engineering-standards/standards-index.md`, capability context and feature artifacts and validation reports |
| Testing strategy | `framework/04-engineering-standards/testing-strategy.md` | `framework/04-engineering-standards/testing-standard.md`, `$test-design`, `$implementation`, `$pr-review`, `$validation` |

## Documents That Should Not Be Duplicated

- Do not duplicate workflow-state rules outside `framework/01-lifecycle/workflow/workflow-state-guide.md`; link to it.
- Do not duplicate skill orchestration, context-loading, or artifact-placement rules inside `.codex/skills`; use the adapter documents.
- Do not duplicate capability artifact naming rules outside `README.md` and `AGENTS.md`; new guidance should use canonical paths and mention old paths only as migration aliases.
- Do not duplicate `Review.`, `Approved.`, and `Status.` behavior outside `framework/01-lifecycle/workflows/review-approval-flow.md`; link to it.
- Do not duplicate skill prerequisite rules outside `framework/01-lifecycle/workflows/skill-prerequisite-validation.md`; link to it.
- Do not redefine the domain/capability/feature hierarchy outside `README.md` and `framework/03-delivery-governance/multi-squad/domain-ownership-model.md`; link to it.
- Do not duplicate implementation placement rules outside `framework/03-delivery-governance/service-architecture/implementation-placement-model.md`; link to it.
- Do not duplicate context routing rules outside `framework/02-context-control/context/context-pack-model.md`; link to it.
- Do not duplicate context versioning, manifest, drift, impact analysis, PR review, harness, or AgentOps rules outside their canonical documents; link to them.
- Do not duplicate AI governance, enterprise rollout, operating model, cost management, access control, platform architecture, compliance, or adoption and training rules outside their canonical documents; link to them.
- Do not duplicate knowledge management, accelerator catalog, portfolio management, dependency management, multi-agent collaboration, or AI evaluation rules outside their canonical documents; link to them.
- Do not duplicate tool adapter or GUI authoring rules outside their canonical documents; link to them.
- Do not duplicate source artifact content in indexes; indexes are navigation aids only.
- Do not duplicate source artifact content in capability summaries; summaries are navigation aids only.
- Do not duplicate prompt pattern rules in skills or artifacts; link to `framework/01-lifecycle/prompt-patterns/` when execution structure is needed.
- Do not duplicate service, frontend, or shared asset ownership tables in capability context and feature artifacts; reference the approved catalog or template.
- Do not duplicate Jira or Confluence payload behavior in capability context and feature artifacts; use the scripts and their README files.
- Do not duplicate coding, API, security, testing, Java, Flutter, database, event, quality-gate, AI-review, decomposition, reference-architecture, change-management, or testing-strategy standards inside each capability unless a capability needs an approved exception.

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
14. Use `framework/06-tool-integrations/integration-foundation.md` and `framework/06-tool-integrations/integration-configuration-guide.md` to understand how GitHub Actions, Jira, Confluence, and Sonar support Git-owned evidence.
15. Keep capability truth in Git. Jira and Confluence outputs are generated views until API integrations are explicitly approved.

Canonical lifecycle skill names are `$intent`, `$specification`, `$design`, `$test-design`, `$implementation`, `$pr-review`, `$validation`, and `$release`.
