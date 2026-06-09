# Skill Name Consistency Review

## Scope

Reviewed all canonical skill folders under `.codex/skills/` and the current lifecycle, brownfield, and Wynxx backlog flow documentation.

This is a review-only document. No skill files were modified.

## Current Skill Set

### Core lifecycle

- `intent`
- `specification`
- `design`
- `test-design`
- `implementation`
- `pr-review`
- `validation`
- `release`

### Brownfield and discovery support

- `discovery-engineering`
- `intent-definition`
- `specification-definition`
- `solution-design`
- `gap-analysis`
- `impact-analysis`
- `artifact-review`

### Delivery, governance, and change support

- `domain-onboarding`
- `capability-onboarding`
- `change-request`
- `decision`
- `defect-fix`
- `feedback-capture`
- `traceability-review`

### Repository, ingestion, and backlog support

- `repo-discovery`
- `source-ingestion`
- `wynxx-backlog-ingestion`

## Review Findings

### 1. Duplicate Or Overlapping Skills

- `intent` and `intent-definition` overlap heavily.
- `specification` and `specification-definition` overlap heavily.
- `design` and `solution-design` overlap heavily.
- `discovery-engineering` and `repo-discovery` are both discovery-oriented, but they target different inputs and are not direct duplicates.
- `change-request`, `defect-fix`, `feedback-capture`, and `impact-analysis` all touch change intake and downstream correction, but they serve different control points.

### 2. Inconsistent Naming Patterns

- The catalog mixes plain nouns (`decision`, `validation`), noun phrases (`gap-analysis`, `impact-analysis`), and workflow-specific compound names (`intent-definition`, `specification-definition`, `solution-design`, `wynxx-backlog-ingestion`).
- `engineering` appears in `discovery-engineering` even though the skill is analysis and review, not engineering.
- `extraction` has already been removed from the current brownfield naming set, which is directionally correct for target-state artifact creation.
- Some skills encode the source system in the skill name (`wynxx-backlog-ingestion`) instead of treating the source as input mode.

### 3. Skills That Are Too Workflow-Specific

- `intent-definition`
- `specification-definition`
- `solution-design`
- `wynxx-backlog-ingestion`
- `discovery-engineering`

These names encode a specific delivery phase or source instead of a durable capability.

### 4. Skills That Should Be Generic

- `intent` should be the generic business-intent skill, with greenfield and brownfield as modes.
- `specification` should become the generic requirements-definition skill, with greenfield and brownfield as modes.
- `design` should become the generic solution-design skill, with implementation-placement and brownfield/greenfield mode handling inside the skill.
- `backlog-ingestion` should be the generic backlog intake skill, with Wynxx as one input mode.
- `discovery` should be the generic current-state discovery skill, with repository/application scope mode handled internally.

### 5. Skills That Should Remain Unchanged

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

These names are already short, durable, and understandable.

### 6. Skills That Should Be Merged

- Merge `intent-definition` into `intent`.
- Merge `specification-definition` into `specification`, but rename the canonical skill to `requirements-definition`.
- Merge `solution-design` into `design`.
- Merge `discovery-engineering` into `discovery`.
- Merge `wynxx-backlog-ingestion` into `backlog-ingestion`.

### 7. Skills That Should Be Renamed

- `discovery-engineering` -> `discovery`
- `specification` -> `requirements-definition`
- `wynxx-backlog-ingestion` -> `backlog-ingestion`

Recommended, but only if the project is willing to collapse the brownfield wrappers into the generic lifecycle skills:

- `intent-definition` -> `intent` mode
- `specification-definition` -> `requirements-definition` mode
- `solution-design` -> `design` mode

### 8. Skills That Should Be Deprecated

- `intent-definition` as a separate canonical skill
- `specification-definition` as a separate canonical skill
- `solution-design` as a separate canonical skill
- `discovery-engineering` as a separate canonical skill
- `wynxx-backlog-ingestion` as a separate canonical skill

Keep them only as migration aliases if the team wants a staged transition.

## Naming Recommendations

- Use simple noun or action names.
- Avoid `engineering` unless it adds a distinct delivery meaning.
- Avoid `extraction` when the skill defines or refines target-state artifacts.
- Use `definition` for intent and requirements only if the canonical name stays clear and durable.
- Use `design` for solution and architecture.
- Use `planning` for delivery and implementation planning.
- Use `review` for quality gates.
- Keep greenfield and brownfield behavior as modes inside skills where possible.
- Do not create duplicate skills just because the input source differs.

## Specific Evaluations

### Should `intent-definition` remain separate?

No, not as a permanent canonical skill. It should become a mode of `intent`.

Reason:
- It duplicates the business-intent capability.
- Greenfield and brownfield differ by mode, not by the core intent function.
- The catalog is simpler if intent remains one skill with explicit scope mode.

### Should `specification-definition` be renamed to `requirements-definition`?

Yes.

Reason:
- `specification` is vague outside the framework.
- `requirements-definition` is more explicit and consistent with the content it produces.
- This also keeps the noun/action naming principle clearer.

### Should `context-extraction` be renamed to `solution-design`?

Yes, but only as a transition step.

Reason:
- `solution-design` is the right meaning for the work.
- The long-term cleaner state is to absorb it into `design` as a mode rather than keep a separate brownfield-only wrapper.

### Should `wynxx-backlog-ingestion` become `backlog-ingestion` with Wynxx as an input mode?

Yes.

Reason:
- The skill is backlog ingestion, not Wynxx-specific ingestion.
- Wynxx is one source system among potentially several backlog sources.
- The source system belongs in inputs, not the canonical skill name.

### Should `implementation-planning` become `delivery-planning` or remain `implementation-planning`?

It should remain `implementation-planning`.

Reason:
- `delivery-planning` is too broad and could overlap release planning, change management, and portfolio planning.
- `implementation-planning` is specific, clear, and aligned to the work it prepares.

## Recommended Final Skill Catalog

### Canonical lifecycle and governance

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
- `artifact-review`
- `traceability-review`
- `decision`
- `change-request`
- `defect-fix`
- `feedback-capture`

### Discovery and intake

- `discovery`
- `repo-discovery`
- `source-ingestion`
- `backlog-ingestion`

### Domain onboarding

- `domain-onboarding`
- `capability-onboarding`

### Brownfield review and analysis modes

- `modernization-readiness-review`
- `design-input-review`
- `gap-analysis`
- `impact-analysis`

## Old Name -> New Name Mapping

| Old Name | Recommended New Name | Action |
| --- | --- | --- |
| `intent-definition` | `intent` | Merge into generic skill with mode support |
| `specification-definition` | `requirements-definition` | Merge and rename canonical skill |
| `solution-design` | `design` | Merge into generic skill with mode support |
| `discovery-engineering` | `discovery` | Rename and merge |
| `wynxx-backlog-ingestion` | `backlog-ingestion` | Rename and merge |
| `specification` | `requirements-definition` | Canonical rename |

## Skills To Keep

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
- `modernization-readiness-review`
- `design-input-review`
- `implementation-readiness`
- `implementation-planning`
- `vertical-slice-planning`
- `implementation-architecture`

## Skills To Delete Or Deprecate

- `intent-definition`
- `specification-definition`
- `solution-design`
- `discovery-engineering`
- `wynxx-backlog-ingestion`

Keep these only as temporary migration wrappers if a staged migration is required.

## Updated Greenfield Flow

```text
intent
-> requirements-definition
-> design
-> test-design
-> implementation-readiness
-> implementation-planning
-> vertical-slice-planning
-> implementation-architecture
-> implementation
-> pr-review
-> validation
-> release
```

## Updated Brownfield Flow

```text
discovery
-> modernization-readiness-review
-> intent
-> requirements-definition
-> design-input-review
-> design
-> gap-analysis
-> impact-analysis
-> implementation-readiness
-> implementation-planning
-> vertical-slice-planning
-> implementation-architecture
-> implementation
-> pr-review
-> validation
-> release
```

## Updated Wynxx Backlog Flow

```text
backlog-ingestion
-> review candidate inputs
-> intent
-> requirements-definition
-> design
-> implementation-planning
-> implementation
```

## Recommendation Summary

The cleanest long-term catalog is smaller and mode-aware:

- one intent skill
- one requirements-definition skill
- one design skill
- one discovery skill
- one backlog-ingestion skill

The brownfield-specific phases should remain as review/planning modes and bridge steps, not as separate copies of the same core lifecycle skills.

