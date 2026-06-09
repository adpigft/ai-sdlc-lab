# Skill Refactoring Plan

## Scope

This plan converts the skill inventory analysis into an actionable refactoring proposal before any skill files are modified.

It reflects the requested target direction:

- rename `discovery-engineering` -> `discovery`
- rename `specification` -> `requirements-definition`
- rename `wynxx-backlog-ingestion` -> `backlog-ingestion`
- merge `intent-definition` -> `intent`
- merge `specification-definition` -> `requirements-definition`
- merge `solution-design` -> `design`

It also incorporates the requested new framework concepts:

- `modernization-readiness`
- `implementation-readiness`
- `implementation-planning`
- `vertical-slice-planning`
- `implementation-architecture`
- decision management
- ADR management
- assumption management

## 1. Final Canonical Skill Catalog

### Core lifecycle

- `intent`
- `requirements-definition`
- `design`
- `test-design`
- `implementation-readiness`
- `implementation-planning`
- `vertical-slice-planning`
- `implementation-architecture`
- `implementation`
- `pr-review`
- `validation`
- `release`

### Discovery and intake

- `discovery`
- `backlog-ingestion`
- `source-ingestion`
- `repo-discovery`

### Domain and capability onboarding

- `domain-onboarding`
- `capability-onboarding`

### Governance and quality

- `artifact-review`
- `traceability-review`
- `decision`
- `change-request`
- `defect-fix`
- `feedback-capture`
- `gap-analysis`
- `impact-analysis`

### Status of current wrappers during transition

- `intent-definition` becomes a brownfield mode or migration wrapper inside `intent`
- `specification-definition` becomes a brownfield mode or migration wrapper inside `requirements-definition`
- `solution-design` becomes a brownfield mode or migration wrapper inside `design`

## 2. Skills to Keep

Keep unchanged as canonical skills:

- `artifact-review`
- `capability-onboarding`
- `change-request`
- `decision`
- `defect-fix`
- `feedback-capture`
- `gap-analysis`
- `impact-analysis`
- `implementation`
- `pr-review`
- `release`
- `repo-discovery`
- `source-ingestion`
- `test-design`
- `traceability-review`
- `validation`
- `domain-onboarding`

Keep with renaming or merging as noted elsewhere:

- `intent`
- `requirements-definition`
- `design`
- `discovery`
- `backlog-ingestion`

## 3. Skills to Rename

| Current Skill | Target Name | Change Type | Notes |
| --- | --- | --- | --- |
| `discovery-engineering` | `discovery` | Rename | Removes unnecessary `engineering` and aligns with generic current-state discovery naming |
| `specification` | `requirements-definition` | Rename | Makes intent clearer and matches the framework meaning of specification |
| `wynxx-backlog-ingestion` | `backlog-ingestion` | Rename | Moves source system into input mode rather than canonical name |

## 4. Skills to Merge

| Source Skill | Merge Target | Reason |
| --- | --- | --- |
| `intent-definition` | `intent` | Brownfield intent is a mode of intent, not a separate canonical capability |
| `specification-definition` | `requirements-definition` | Brownfield requirements are a mode of requirements definition, not a separate canonical capability |
| `solution-design` | `design` | Brownfield solution design is a mode of design, not a separate canonical capability |

### Merge intent

The merged target skill should:

- preserve greenfield behavior
- add brownfield mode flags or input selectors
- support mode-specific artifact structures
- keep outputs and approvals consistent across modes

## 5. Skills to Deprecate

Deprecate after the merge/rename transition is complete:

- `intent-definition`
- `specification-definition`
- `solution-design`
- `discovery-engineering`
- `wynxx-backlog-ingestion`

Deprecation should be temporary if migration wrappers are retained for one release cycle.

## 6. New Skills Required

The inventory shows gaps between the documented framework phases and the current skill catalog. The following should be added as separate skills if the framework wants explicit phase coverage rather than folded modes:

- `modernization-readiness`
- `implementation-readiness`
- `implementation-planning`
- `vertical-slice-planning`
- `implementation-architecture`

### Notes on new skills

- `modernization-readiness` should decide whether discovery is sufficient to begin target-state work.
- `implementation-readiness` should classify blockers into `must close`, `can proceed with assumptions`, and `can defer`.
- `implementation-planning` should produce the delivery plan, dependencies, risks, and traceability placeholders.
- `vertical-slice-planning` should define vertically deliverable slices and split horizontal foundation work where needed.
- `implementation-architecture` should define module/package structure, migration strategy, API/domain standards, transaction boundaries, outbox strategy, testing strategy, and CI/CD strategy.

## 7. Workflow Impact

### Greenfield workflow

Current canonical flow:

```text
intent -> specification -> design -> test-design -> implementation -> pr-review -> validation -> release
```

Target flow after refactoring:

```text
intent -> requirements-definition -> design -> test-design -> implementation-readiness -> implementation-planning -> vertical-slice-planning -> implementation-architecture -> implementation -> pr-review -> validation -> release
```

Impact:

- greenfield remains the default lifecycle
- implementation gets stronger planning gates before code
- `specification` is replaced by `requirements-definition`
- planning phases become explicit skills instead of implicit steps

### Brownfield workflow

Current brownfield flow:

```text
discovery-engineering -> intent-definition -> specification-definition -> solution-design -> gap-analysis -> impact-analysis -> implementation -> pr-review -> validation -> release
```

Target flow after refactoring:

```text
discovery -> modernization-readiness -> intent -> requirements-definition -> design -> gap-analysis -> impact-analysis -> implementation-readiness -> implementation-planning -> vertical-slice-planning -> implementation-architecture -> implementation -> pr-review -> validation -> release
```

Impact:

- brownfield becomes a mode-aware flow instead of a parallel wrapper catalog
- readiness and planning become explicit gates
- the output sequence becomes easier to reason about across discovery, intent, requirements, design, and build

### Wynxx backlog flow

Current Wynxx flow:

```text
wynxx-backlog-ingestion -> candidate inputs -> intent/specification/test-design/implementation
```

Target Wynxx flow after refactoring:

```text
backlog-ingestion -> candidate review -> intent -> requirements-definition -> test-design -> implementation-planning -> implementation
```

Impact:

- Wynxx becomes an input mode of backlog ingestion, not a special skill name
- candidate inputs remain advisory until reviewed
- the delivery flow is consistent with the rest of the catalog

## 8. Documentation Impact

The following documentation must be updated after the skill refactor:

- `README.md`
- `.codex/skills/README.md`
- `framework/01-lifecycle/skill-orchestration-adapter.md`
- `framework/01-lifecycle/workflows/skill-prerequisite-validation.md`
- `framework/01-lifecycle/workflows/review-approval-flow.md`
- `framework/01-lifecycle/workflows/03-spec-to-build.md`
- `framework/01-lifecycle/prompt-patterns/*.md`
- `framework/00-navigation/document-map.md`
- `framework/24-discovery-engineering/brownfield-modernization-flow.md`
- `framework/24-discovery-engineering/discovery-engineering-model.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/03-delivery-governance/service-architecture/implementation-placement-model.md`
- `framework/12-impact-analysis/impact-analysis-model.md`
- `framework/12-impact-analysis/change-impact-workflow.md`
- `framework/11-smoke-tests/skill-quality-review.md`

Additional documentation should be created or updated for new skills:

- readiness and planning prompt patterns
- lifecycle navigation references for the new planning gates
- artifact placement guidance for implementation-readiness, implementation-planning, vertical-slice-planning, and implementation-architecture
- concept guidance for decision management, ADR management, and assumption management

## 9. Migration Plan

### Phase 1: Additive preparation

- Create new skills for readiness and planning if they are to remain separate.
- Update documentation to describe the target catalog and flows.
- Add mode guidance to generic skills before renaming wrappers away.
- Introduce or update decision/ADR/assumption management guidance without changing delivery behavior yet.

### Phase 2: Rename canonical skills

- Rename `discovery-engineering` -> `discovery`
- Rename `specification` -> `requirements-definition`
- Rename `wynxx-backlog-ingestion` -> `backlog-ingestion`

### Phase 3: Merge brownfield wrappers

- Merge `intent-definition` into `intent`
- Merge `specification-definition` into `requirements-definition`
- Merge `solution-design` into `design`

### Phase 4: Deprecate wrappers

- Remove migration wrappers after one transition cycle, if approved
- Update all references in lifecycle docs, prompts, indexes, and examples

### Phase 5: Verify and normalize

- run markdown and link checks
- run `git diff --check`
- search for old names and remove stale references
- validate workflow-state guidance against the new catalog

## 10. Risks

- Renaming `specification` to `requirements-definition` introduces broad documentation churn because `specification` is already used across lifecycle docs.
- Merging brownfield wrappers too early may collapse useful mode distinctions before the canonical skills are mode-aware.
- Adding readiness/planning skills without clear artifact ownership could create overlap with `design`, `gap-analysis`, and `impact-analysis`.
- The new concept set for decision management, ADR management, and assumption management may require additional framework terminology and templates before it is operationally useful.
- Wynxx flow changes could create confusion if backlog candidates are treated as delivery artifacts instead of review inputs.

## Change Impact Summary

- The final catalog becomes smaller and more mode-aware.
- Brownfield and greenfield behavior should converge into fewer canonical skills with explicit modes.
- Planning and readiness become first-class phases instead of implicit handoffs.
- Wynxx becomes an input mode rather than a skill namespace.
- The documentation footprint is significant and should be updated in the same migration window as the skill files.

