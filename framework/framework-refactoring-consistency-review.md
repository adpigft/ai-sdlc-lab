# Framework Refactoring Consistency Review

## Pass / Fail Summary

- Pass for live execution paths.
- The remaining `specification` / `requirements-definition` / old-skill-name hits are historical analysis docs, legacy folder references, or adapter references to the preserved `framework/24-discovery-engineering/` path.
- Safe to commit: Yes, if you intentionally keep the historical framework path names and analysis notes unchanged.

## Files Updated

- [`.codex/skills/requirements/SKILL.md`](/Users/adpi/Documents/ai-sdlc-lab/.codex/skills/requirements/SKILL.md)
- [`framework/01-lifecycle/workflows/01-intent-to-requirements.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/01-lifecycle/workflows/01-intent-to-requirements.md)
- [`framework/01-lifecycle/workflows/02-requirements-review.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/01-lifecycle/workflows/02-requirements-review.md)
- [`framework/02-context-control/context/stage-context-packs.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/02-context-control/context/stage-context-packs.md)
- [`framework/06-tool-integrations/backlog-ingestion.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/06-tool-integrations/backlog-ingestion.md)
- [`framework/06-tool-integrations/jira/jira-example-capability.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/06-tool-integrations/jira/jira-example-capability.md)
- [`framework/07-templates/requirements-template.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/07-templates/requirements-template.md)
- [`framework/07-templates/traceability-row-template.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/07-templates/traceability-row-template.md)
- [`framework/07-templates/change-request-template.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/07-templates/change-request-template.md)
- [`framework/07-templates/defect-rca-template.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/07-templates/defect-rca-template.md)
- [`framework/07-control-tower/control-tower-data-model.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/07-control-tower/control-tower-data-model.md)
- [`framework/07-control-tower/workflow-ownership-matrix.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/07-control-tower/workflow-ownership-matrix.md)
- [`framework/08-context-quality/llm-judge-rubrics.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/08-context-quality/llm-judge-rubrics.md)
- [`framework/09-context-packaging/context-manifest-model.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/09-context-packaging/context-manifest-model.md)
- [`framework/11-smoke-tests/demo-scope-guide.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/11-smoke-tests/demo-scope-guide.md)
- [`framework/11-smoke-tests/end-to-end-smoke-test-report.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/11-smoke-tests/end-to-end-smoke-test-report.md)
- [`framework/11-smoke-tests/skill-quality-review.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/11-smoke-tests/skill-quality-review.md)
- [`framework/11-smoke-tests/wynxx-read-only-smoke-test.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/11-smoke-tests/wynxx-read-only-smoke-test.md)
- [`framework/12-impact-analysis/change-impact-workflow.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/12-impact-analysis/change-impact-workflow.md)
- [`framework/15-agentops/agent-run-log-schema.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/15-agentops/agent-run-log-schema.md)
- [`framework/16-ai-governance/model-risk-management.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/16-ai-governance/model-risk-management.md)
- [`framework/31-gui-authoring/gui-authoring-model.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/31-gui-authoring/gui-authoring-model.md)
- [`traceability/traceability-matrix.md`](/Users/adpi/Documents/ai-sdlc-lab/traceability/traceability-matrix.md)
- [`framework/00-navigation/document-map.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/00-navigation/document-map.md)

## Remaining Old-Name Hits

### Acceptable Historical References

| Path | Hit | Classification | Reason |
| --- | --- | --- | --- |
| [`README.md`](/Users/adpi/Documents/ai-sdlc-lab/README.md) | `24-discovery-engineering` | Acceptable historical reference | Repository tree still documents the preserved historical folder name. |
| [`.codex/skills/discovery/SKILL.md`](/Users/adpi/Documents/ai-sdlc-lab/.codex/skills/discovery/SKILL.md) | `framework/24-discovery-engineering/discovery-engineering-model.md` | Acceptable historical reference | Skill adapter points to preserved historical framework material. |
| [`.codex/skills/gap-analysis/SKILL.md`](/Users/adpi/Documents/ai-sdlc-lab/.codex/skills/gap-analysis/SKILL.md) | `framework/24-discovery-engineering/brownfield-modernization-flow.md` | Acceptable historical reference | Historical brownfield framework path retained for context. |
| [`.codex/skills/modernization-readiness/SKILL.md`](/Users/adpi/Documents/ai-sdlc-lab/.codex/skills/modernization-readiness/SKILL.md) | `framework/24-discovery-engineering/modernization-readiness-review.md` | Acceptable historical reference | Historical path reference only. |
| [`.codex/skills/requirements/SKILL.md`](/Users/adpi/Documents/ai-sdlc-lab/.codex/skills/requirements/SKILL.md) | `framework/24-discovery-engineering/current-state-extraction-model.md` | Acceptable historical reference | Adapter doc references the old brownfield framework location. |
| [`framework/00-navigation/document-map.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/00-navigation/document-map.md) | `framework/24-discovery-engineering/...` | Acceptable historical reference | Navigation map intentionally preserves the historical discovery folder path. |
| [`framework/01-lifecycle/prompt-patterns/design-input-review-pattern.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/01-lifecycle/prompt-patterns/design-input-review-pattern.md) | `framework/24-discovery-engineering/brownfield-modernization-flow.md` | Acceptable historical reference | Prompt pattern points at preserved historical framework material. |
| [`framework/01-lifecycle/prompt-patterns/modernization-readiness-review-pattern.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/01-lifecycle/prompt-patterns/modernization-readiness-review-pattern.md) | `framework/24-discovery-engineering/discovery-engineering-model.md`, `framework/24-discovery-engineering/modernization-readiness-review.md` | Acceptable historical reference | Historical discovery framework references only. |
| [`framework/framework-refactoring-summary.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/framework-refactoring-summary.md) | `requirements-definition`, `specification`, `wynxx-backlog-ingestion` | Acceptable historical reference | Prior refactoring summary documents the earlier naming decision. |
| [`framework/skill-inventory-analysis.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/skill-inventory-analysis.md) | `discovery-engineering`, `intent-definition`, `specification-definition`, `solution-design`, `wynxx-backlog-ingestion`, `specification` | Acceptable historical reference | Inventory analysis intentionally documents the pre-refactor catalog. |
| [`framework/skill-name-consistency-review.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/skill-name-consistency-review.md) | `discovery-engineering`, `intent-definition`, `specification-definition`, `solution-design`, `wynxx-backlog-ingestion`, `specification`, `requirements-definition` | Acceptable historical reference | Review artifact intentionally records earlier naming recommendations. |
| [`framework/skill-refactoring-plan.md`](/Users/adpi/Documents/ai-sdlc-lab/framework/skill-refactoring-plan.md) | `discovery-engineering`, `specification`, `requirements-definition`, `wynxx-backlog-ingestion`, `intent-definition`, `specification-definition`, `solution-design` | Acceptable historical reference | Refactoring plan intentionally captures prior target state and migration rationale. |

### Live References Requiring Fix

- None found in the live execution path scanned for this pass.

## Recommended Corrections

- Keep the canonical live names as `discovery`, `backlog-ingestion`, `intent`, `requirements`, and `design`.
- Keep historical analysis docs unchanged unless you want a separate documentation-only cleanup pass.
- If you want zero legacy references anywhere in the repository, do a second pass over the historical refactoring docs and the preserved `framework/24-discovery-engineering/` folder names.

## Validation

- `git diff --check` passed.
- A local markdown/link checker was not available in this environment.
- The reference scan found no live execution docs still using the retired skill names or `specification/` artifact path conventions.
