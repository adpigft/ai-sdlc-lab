# Skill Inventory Analysis

## Scope

This analysis covers every current skill under `.codex/skills/` in the repository as of the date of review.

The analysis is inventory-first. It does not modify skills and it does not recommend merges or removals until the inventory is complete.

## 1. Full Skill Inventory

| Skill | Purpose | Inputs | Outputs | Typical Artifacts Produced | Greenfield Applicability | Brownfield Applicability | Wynxx Applicability | Dependencies | Similar / Overlapping Skills | Recommended Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `artifact-review` | Review AI-generated artifact quality before approval | Artifact, artifact type, upstream artifacts, checklist, criteria | Strengths, weaknesses, risks, recommendations, go/no-go, readiness score | Review notes, readiness assessment, approval request | Yes | Yes | No | Lifecycle adapter, context adapter, upstream artifacts | `pr-review`, `validation`, `test-design`, `traceability-review` | Keep |
| `capability-onboarding` | Create/update capability boundary and parent context | Domain context, capability name, purpose, features, owner, assumptions | Capability context, review summary, candidate capability structure | capability-context.md, onboarding summary | Yes | Yes | No | Domain context, artifact placement, ownership model | `domain-onboarding`, `intent` | Keep |
| `change-request` | Controlled change analysis and targeted updates | Change ID, summary, affected scope, constraints, evidence | Change impact summary, affected artifacts, correction plan | change impact summary, targeted update plan | Yes | Yes | No | Impact analysis, placement model, approvals | `impact-analysis`, `defect-fix`, `feedback-capture` | Keep |
| `decision` | Record material design/delivery decisions | Topic, context, options, recommendation, tradeoffs, owners | Decision record, status, impacted items, blocker/approval recommendation | ADR / decision record | Yes | Yes | No | Lifecycle adapter, context/placement rules, approvals | `design`, `change-request`, `artifact-review` | Keep |
| `defect-fix` | Analyze and resolve defects with targeted correction | Defect ID, expected vs observed behavior, environment, evidence, owner, scope | Defect summary, root cause, fix plan, regression and validation needs | defect analysis, fix plan, regression scope | Yes | Yes | No | Impact analysis, implementation placement, approvals, validation | `change-request`, `feedback-capture`, `impact-analysis`, `validation` | Keep |
| `design` | Translate approved requirements into solution design | Approved intent/specification, system context, constraints, standards, ownership | Design artifact/update, design guidance, decisions, placement metadata | design.md, APIs/events/integration guidance, ADRs | Yes | Yes | No | Specification, placement model, implementation placement model | `solution-design`, `decision`, `implementation` | Keep |
| `discovery-engineering` | Read-only current-state application analysis | Source app/repo, scope, tech hints, outputs, constraints | Discovery summary, quick scan, inventory artifacts, evidence | quick-scan, inventory docs, discovery evidence | Limited | Yes | No | Lifecycle adapter, context adapter, artifact placement, discovery model | `repo-discovery`, `source-ingestion`, `solution-design` | Rename |
| `domain-onboarding` | Establish domain-level context and ownership | Domain name, owner, scope, candidate capabilities, integrations, assumptions | Domain context artifact, onboarding summary, review request | domain-context.md, onboarding summary | Yes | Yes | No | Artifact placement, service/frontend catalogs, ownership models | `capability-onboarding`, `repo-discovery` | Keep |
| `feedback-capture` | Capture feedback and convert it to follow-up work | Feedback source/date, summary, affected scope, severity, owner | Feedback entry, classification, follow-up plan, traceability impact | feedback log entry, follow-up plan | Yes | Yes | No | Context adapter, placement model, approvals, traceability | `change-request`, `defect-fix`, `artifact-review` | Keep |
| `gap-analysis` | Compare current-state evidence to target design/spec | Discovery, approved intent, approved spec, solution design, evidence | Gap analysis, capability/architecture/data/API/business-rule/operational gaps, traceability | gap analysis docs, risk register, readiness gaps | No | Yes | No | Discovery, intent, spec, design, impact context | `impact-analysis`, `change-request`, `design` | Keep |
| `impact-analysis` | Assess change impact and sequencing | Current/target artifacts, traceability, change description, affected systems, owners | Impact assessment, impacted components/data/APIs/integrations/tests/ops, sequencing, risk summary | impact assessment docs, sequencing notes | Yes | Yes | No | Gap analysis, lifecycle adapter, placement model, traceability | `change-request`, `defect-fix`, `pr-review` | Keep |
| `implementation` | Build approved delivery slice | Approved upstream artifacts, slice scope, standards, code/test base, placement constraints | Source changes, tests, refactors, evidence, PR readiness summary | code changes, tests, implementation evidence | Yes | Yes | No | Design, test design, traceability, implementation architecture, placement metadata | `defect-fix`, `pr-review`, `validation` | Keep |
| `intent-definition` | Define target business state for brownfield modernization | Discovery findings, current-state summary, docs, stakeholder refs, pain points | Intent summary, target-state vision, scope, operating model, policy decisions, confidence | intent artifact, target-state summary | No | Yes | Potentially (as input) | Discovery-engineering, modern readiness, approvals, artifact placement | `intent`, `specification-definition`, `solution-design` | Merge |
| `intent` | Capture why work is needed and what outcome it should produce | Business problem, users, outcomes, scope, exclusions, constraints, references | Intent artifact, discovery summary, review request | intent.md | Yes | Yes | Yes (as candidate input) | Domain context, artifact placement, lifecycle adapter, optional source ingestion | `intent-definition`, `source-ingestion`, `wynxx-backlog-ingestion` | Keep |
| `pr-review` | Review implemented slice or PR before validation | PR/slice ref, changed files, approved scope, tests, traceability, placement constraints | PR review findings, scope assessment, recommendation, evidence artifact | PR review report | Yes | Yes | No | Implementation, validation, placement model, approvals, traceability | `artifact-review`, `validation`, `implementation` | Keep |
| `release` | Prepare and assess release readiness | Release scope, validation, CI/security evidence, risks, rollback/monitoring notes, approvals | Release readiness summary, release notes, rollback/monitoring plan, blockers | release notes, release readiness package | Yes | Yes | No | Validation, PR review, traceability, release governance | `validation`, `pr-review`, `change-request` | Keep |
| `repo-discovery` | Extract repository conventions and standards | Repository path, tech stack, scope, areas, known standards | Repo discovery summary, standards updates, reusable notes, gaps/risks | repo standards summary, reusable notes | Yes | Yes | No | Repo access, standards docs, optional framework governance | `discovery-engineering`, `source-ingestion` | Keep |
| `solution-design` | Brownfield target solution design with dynamic artifact selection | Approved intent/spec, discovery/context, integrations, constraints, ownership | Design-input review, design-artifact plan, architecture summary, ADR candidates, placement metadata | design-input review, design plan, architecture summary | No | Yes | No | Design, implementation placement, discovery model, brownfield flow | `design`, `gap-analysis`, `impact-analysis` | Merge |
| `source-ingestion` | Convert external docs into structured AI-readable input | External docs, source type, owner, target artifact, extraction goal | Ingestion summary, extracted notes, gaps/conflicts, recommended artifacts | ingestion summary, extracted notes, target artifact suggestions | Yes | Yes | Possible (docs pulled from Wynxx exports) | Document parsing, lifecycle/context adapters | `wynxx-backlog-ingestion`, `repo-discovery` | Keep |
| `specification-definition` | Brownfield requirements definition from approved intent | Approved intent, current-state discovery/context, policies, validation evidence | Requirements summary, business capabilities, state-machine reqs, traceability, placeholders | requirements doc, traceability-ready spec | No | Yes | Possible as candidate input | Discovery, intent, approvals, artifact placement | `specification`, `solution-design`, `gap-analysis` | Merge |
| `specification` | Turn approved intent into clear, testable requirements | Approved intent, policies, clarifications, standards, open questions | Specification artifact, requirement IDs, review request | specification.md, requirement set | Yes | Yes | Yes (as candidate output target) | Intent, domain context, approvals, artifact placement | `specification-definition`, `test-design`, `traceability-review` | Keep |
| `test-design` | Define QA-owned scenarios and coverage | Approved intent/spec, design context, rules, risk constraints, existing tests | Acceptance scenarios, negative/integration/security/regression/NFR coverage, gaps | acceptance/test design artifacts | Yes | Yes | No | Specification, design, traceability, QA approvals | `validation`, `artifact-review`, `pr-review` | Keep |
| `traceability-review` | Maintain auditable end-to-end traceability | Intent, requirements, design, tests, implementation, validation, release, external refs | Traceability assessment, matrix/update, gap/blocker list, review request | traceability matrix/update | Yes | Yes | No | Lifecycle artifacts, workflow state, external references | `artifact-review`, `change-request`, `pr-review` | Keep |
| `validation` | Execute/review validation evidence | Approved reqs/design/tests, implementation evidence, test results, CI/security outputs, defects | Validation report, evidence summary, release readiness recommendation | validation report, evidence summary | Yes | Yes | No | Implementation, PR review, test design, traceability | `pr-review`, `release`, `test-design` | Keep |
| `wynxx-backlog-ingestion` | Ingest Wynxx Story Creator backlog via MCP | MCP connection, project/backlog criteria, domain/capability, framework context, ingestion goal | Backlog summary, hierarchy mapping, candidate inputs, overlap warnings, next-skill recommendation | backlog summary, hierarchy mapping, candidate intent/spec/test/impl inputs | No | No | Yes | MCP tools, backlog hierarchy, Git context, framework mapping | `source-ingestion`, `intent`, `specification`, `test-design` | Merge |

## 2. Naming Consistency Review

- The catalog currently mixes short generic names (`intent`, `design`, `validation`) with phase-specific wrappers (`intent-definition`, `specification-definition`, `solution-design`, `discovery-engineering`, `wynxx-backlog-ingestion`).
- `engineering` is only used in `discovery-engineering` and adds little value relative to `discovery`.
- `extraction` has already been eliminated from the current brownfield names in favor of definition/design language.
- Source-system names should not normally be part of canonical skill names.
- The most consistent naming pattern across the catalog is already the noun/action style used by `intent`, `specification`, `design`, `review`, `planning`, and `validation` concepts.

## 3. Duplicate Responsibility Analysis

- `intent` and `intent-definition` both define intent; the only meaningful difference is greenfield vs brownfield mode.
- `specification` and `specification-definition` both define requirements; the only meaningful difference is greenfield vs brownfield mode.
- `design` and `solution-design` both produce solution design; the only meaningful difference is greenfield vs brownfield mode and artifact selection depth.
- `discovery-engineering` overlaps with `repo-discovery` on repository analysis, but one is application current-state discovery while the other is repository standards discovery.
- `wynxx-backlog-ingestion` overlaps with `source-ingestion` on document intake, but it is a specific MCP source plus hierarchy mapping flow.
- `change-request`, `defect-fix`, `feedback-capture`, and `impact-analysis` all touch change intake, but at different control points and with different outputs.

## 4. Greenfield Workflow Mapping

Current greenfield lifecycle support is strong and should remain centered on:

```text
intent -> specification -> design -> test-design -> implementation -> pr-review -> validation -> release
```

Supporting skills for greenfield delivery:

- `domain-onboarding`
- `capability-onboarding`
- `source-ingestion`
- `repo-discovery`
- `artifact-review`
- `decision`
- `change-request`
- `defect-fix`
- `feedback-capture`
- `traceability-review`

Greenfield mode does not need separate wrapper skills for intent/spec/design unless the framework wants explicit brownfield-vs-greenfield modes inside the same canonical skill.

## 5. Brownfield Workflow Mapping

Current brownfield support is best represented as a mode-aware extension of the greenfield flow:

```text
discovery-engineering -> intent-definition -> specification-definition -> solution-design -> gap-analysis -> impact-analysis -> implementation -> pr-review -> validation -> release
```

Important note:

- The framework docs already describe readiness and planning phases, but those phases are not currently separate skills under `.codex/skills/`.
- Brownfield work should be mode-aware inside the canonical skills where possible, instead of spawning a separate canonical skill for each intermediate phase.

Brownfield-supporting skills:

- `discovery-engineering`
- `intent-definition`
- `specification-definition`
- `solution-design`
- `gap-analysis`
- `impact-analysis`

Cross-cutting support:

- `artifact-review`
- `change-request`
- `decision`
- `defect-fix`
- `feedback-capture`
- `traceability-review`

## 6. Wynxx Workflow Mapping

Current Wynxx flow is a source-to-candidate flow, not a delivery lifecycle:

```text
wynxx-backlog-ingestion -> review candidate inputs -> intent/specification/test-design/implementation candidates
```

Typical mapping:

- Epic -> capability candidate
- Feature -> feature candidate
- User Story -> intent or requirement candidate
- Task -> implementation hint only
- Test Case -> test-design hint only

`wynxx-backlog-ingestion` is the only Wynxx-specific canonical skill today, and it should eventually become a generic backlog-ingestion skill with Wynxx as one input mode.

## 7. Recommended Canonical Skill Catalog

Recommended long-term canonical catalog:

- `intent`
- `requirements-definition`
- `design`
- `test-design`
- `implementation`
- `pr-review`
- `validation`
- `release`
- `discovery`
- `backlog-ingestion`
- `domain-onboarding`
- `capability-onboarding`
- `repo-discovery`
- `source-ingestion`
- `artifact-review`
- `decision`
- `change-request`
- `defect-fix`
- `feedback-capture`
- `gap-analysis`
- `impact-analysis`
- `traceability-review`

Notes:

- `implementation-readiness`, `implementation-planning`, `vertical-slice-planning`, and `implementation-architecture` are valuable framework phases, but they are not currently represented as canonical skills in `.codex/skills/`.
- If these phases become skills later, they should be added as clearly named, mode-aware planning/review skills rather than duplicating existing capabilities.

## 8. Recommended Renames

| Current Skill | Recommended Name | Reason |
| --- | --- | --- |
| `discovery-engineering` | `discovery` | Removes unnecessary `engineering`; keeps meaning clear |
| `specification` | `requirements-definition` | Makes purpose explicit and consistent with content |
| `wynxx-backlog-ingestion` | `backlog-ingestion` | Moves source system out of canonical name |

Optional transition-only renames, if the team wants temporary wrappers before merging:

| Current Skill | Suggested Temporary Wrapper Name | End State |
| --- | --- | --- |
| `intent-definition` | `intent` mode | Merge into `intent` |
| `specification-definition` | `requirements-definition` mode | Merge into `requirements-definition` |
| `solution-design` | `design` mode | Merge into `design` |

## 9. Recommended Merges

- Merge `intent-definition` into `intent`.
- Merge `specification-definition` into `requirements-definition`.
- Merge `solution-design` into `design`.
- Merge `discovery-engineering` into `discovery`.
- Merge `wynxx-backlog-ingestion` into `backlog-ingestion`.

Rationale:

- The wrapper skills mostly encode input mode, not unique capability.
- The greenfield vs brownfield difference is better handled as a mode or context flag inside the canonical skill.
- Wynxx should remain a source/input mode, not a canonical delivery capability name.

## 10. Recommended Deprecations

- Deprecate `intent-definition` as a standalone canonical skill.
- Deprecate `specification-definition` as a standalone canonical skill.
- Deprecate `solution-design` as a standalone canonical skill.
- Deprecate `discovery-engineering` as a standalone canonical skill.
- Deprecate `wynxx-backlog-ingestion` as a standalone canonical skill.

Do not remove them before the catalog transition is complete if the team needs a migration path.

## 11. Impact Assessment

### What is stable

- The greenfield lifecycle is already well-formed and should remain the default path.
- `artifact-review`, `change-request`, `decision`, `defect-fix`, `feedback-capture`, `pr-review`, `release`, `repo-discovery`, `source-ingestion`, `test-design`, `traceability-review`, and `validation` are broadly durable and should stay independent.
- `domain-onboarding` and `capability-onboarding` are useful boundary-setting skills and should stay independent.

### What is redundant

- The three brownfield wrapper skills duplicate the intent/spec/design lifecycle with a different mode.
- The Wynxx ingestion skill duplicates generic backlog intake behavior with a source-specific wrapper.
- `discovery-engineering` duplicates current-state discovery behavior that can be expressed more simply as `discovery`.

### What is missing

- Dedicated skills for `implementation-readiness`, `implementation-planning`, `vertical-slice-planning`, and `implementation-architecture` do not currently exist in `.codex/skills/`.
- The framework docs describe these phases, but the skill catalog does not yet operationalize them as separate skills.

### What should happen next

- Collapse wrappers into canonical mode-aware skills where possible.
- Rename canonical skills to the simplest durable nouns/actions.
- Keep source-system names out of canonical skill names.
- Add any missing planning/review skills only if they represent truly distinct responsibilities.

