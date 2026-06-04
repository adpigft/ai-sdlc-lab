# Stage Context Packs

## Purpose

Define lightweight required, optional, forbidden, and escalation reads by lifecycle stage.

These packs reduce token usage and make Codex behavior predictable without adding heavy indexing.

These packs are framework adapter guidance. Generic skills should not duplicate this file; they should reference `framework/02-context-control/context/skill-context-adapter.md` when used inside this repository.

## Domain Onboarding

Purpose: create new domain context before capabilities exist.

Required reads:

- `.codex/skills/domain-onboarding/SKILL.md`
- `framework/03-delivery-governance/service-architecture/domain-onboarding-model.md`
- `framework/03-delivery-governance/multi-squad/domain-ownership-model.md`
- `framework/03-delivery-governance/service-architecture/service-catalog-template.md`
- `framework/03-delivery-governance/frontend/frontend-catalog-template.md`
- `framework/03-delivery-governance/multi-squad/shared-asset-ownership-model.md`
- `framework/03-delivery-governance/service-architecture/implementation-placement-model.md`

Optional reads:

- `README.md`
- `AGENTS.md`
- related existing domain contexts for style only

Forbidden reads:

- source code
- capability context and feature artifacts
- traceability and feedback unless the user asks for framework impact
- app, service, library, or platform folders

Expected outputs:

- `domains/<domain>/domain-context.md`
- `domains/<domain>/README.md`

Stop conditions:

- domain already exists and user has not approved updates
- missing domain owner or placement assumptions cannot be recorded as open questions
- user asks to create capabilities or code during onboarding

## Intent

Purpose: discover and draft business intent for a capability.

Required reads:

- `.codex/skills/intent/SKILL.md`
- `domains/<domain>/domain-context.md`
- `framework/01-lifecycle/workflow/workflow-state-guide.md`

Optional reads:

- `framework/07-templates/intent-template.md`
- Jira model docs when Jira mapping is needed
- existing feature artifacts in the same domain for style only

Forbidden reads:

- source code
- implementation plans from unrelated capabilities
- validation or release artifacts
- unrelated domains

Expected outputs:

- discovery summary
- approved `intent/intent.md` only after PO / BA approval
- `workflow-state.yaml` only after intent artifact creation

Stop conditions:

- domain context missing for a new domain
- insufficient intent discovery
- missing PO / BA approval

## Specification

Purpose: convert approved intent into requirements, rules, NFRs, and acceptance criteria.

Required reads:

- `.codex/skills/specification/SKILL.md`
- approved `intent/intent.md`
- `domains/<domain>/domain-context.md`
- `workflow-state.yaml`
- `framework/07-templates/spec-template.md`

Optional reads:

- `framework/04-engineering-standards/standards/api-standards.md`
- `framework/04-engineering-standards/standards/security-standards.md`
- similar approved specs in the same domain

Forbidden reads:

- source code
- implementation plans
- release artifacts
- unrelated domains

Expected outputs:

- `specification/specification.md`
- updated workflow state after approval gates where applicable

Stop conditions:

- intent is not approved
- open questions block requirements
- required approver is missing

## Design

Purpose: define boundaries, APIs, integrations, data, security, ADRs, and placement.

Required reads:

- `.codex/skills/design/SKILL.md`
- approved intent
- approved specification
- `domains/<domain>/domain-context.md`
- `workflow-state.yaml`
- `framework/03-delivery-governance/service-architecture/implementation-placement-model.md`

Optional reads:

- `framework/03-delivery-governance/service-architecture/service-catalog-template.md`
- `framework/03-delivery-governance/frontend/frontend-catalog-template.md`
- `framework/03-delivery-governance/multi-squad/shared-asset-ownership-model.md`
- `framework/04-engineering-standards/standards/api-standards.md`
- `framework/04-engineering-standards/standards/security-standards.md`
- event guidance if events are impacted

Forbidden reads:

- source code unless design is reviewing an existing implementation by explicit request
- unrelated domains unless cross-domain impact is identified
- validation and release artifacts unless checking existing drift

Expected outputs:

- `design/design.md`
- API guidance or `contracts/openapi.yaml` when needed
- ADR candidates
- implementation slice and placement guidance

Stop conditions:

- specification is not approved
- material decisions are unresolved
- target placement cannot be defined or explicitly deferred

## Test Design

Purpose: define acceptance, negative, integration, security, and NFR scenarios.

Required reads:

- `.codex/skills/test-design/SKILL.md`
- approved specification
- architecture context
- API contract when available
- `domains/<domain>/domain-context.md`
- `workflow-state.yaml`

Optional reads:

- `framework/04-engineering-standards/standards/testing-standards.md`
- `framework/04-engineering-standards/standards/security-standards.md`
- traceability matrix when coverage is being checked

Forbidden reads:

- source code unless designing regression from existing code by explicit request
- release artifacts
- unrelated domains

Expected outputs:

- `tests/acceptance.feature`
- test coverage notes

Stop conditions:

- architecture or API contract is not approved where required
- requirements lack acceptance basis
- NFR targets are missing and cannot be recorded as open questions

## Implementation

Purpose: implement one approved slice at a time.

Required reads:

- `.codex/skills/implementation/SKILL.md`
- `workflow-state.yaml`
- `domains/<domain>/domain-context.md`
- approved intent
- approved specification
- approved design
- approved API contract when applicable
- approved tests
- approved implementation plan
- placement metadata and allowed paths
- coding, testing, and security standards

Optional reads:

- existing source and tests only inside `allowed_paths`
- traceability matrix when mapping implementation evidence
- service, frontend, or shared asset docs referenced by placement metadata

Forbidden reads:

- source outside `allowed_paths`
- restricted paths
- unrelated domains or services
- release artifacts unless implementation is preparing release evidence

Expected outputs:

- tests and code for one approved slice
- developer notes or PR readiness evidence

Stop conditions:

- upstream approvals are missing
- `allowed_paths` or `restricted_paths` are missing
- requested change needs restricted paths
- implementation scope expands beyond the approved slice

## PR Review

Purpose: review implementation changes before QA validation.

Required reads:

- `.codex/skills/pr-review/SKILL.md`
- `framework/01-lifecycle/workflows/pr-review-flow.md`
- `workflow-state.yaml` when available
- approved implementation plan
- placement metadata and allowed paths
- changed file list
- changed source and test files inside `allowed_paths`
- relevant coding, testing, security, API, event, and architecture standards
- traceability matrix when checking implementation links

Optional reads:

- CI or local validation output
- impacted API contracts or event schemas
- architecture context for the active capability

Forbidden reads:

- unrelated source files
- unrelated domains or capabilities
- restricted paths without explicit owner approval
- release artifacts unless the PR changes release evidence

Expected outputs:

- PR review findings
- allowed-path assessment
- standards and architecture assessment
- API/event compatibility assessment
- test coverage assessment
- validation script and traceability assessment

Stop conditions:

- changed files are unknown
- `allowed_paths` or `restricted_paths` are missing
- changed files include restricted or unapproved paths
- required implementation evidence is missing
- validation, traceability, API/event compatibility, or workflow evidence disagrees

## Validation

Purpose: validate implementation evidence against approved requirements, tests, traceability, and release blockers.

Required reads:

- `.codex/skills/validation/SKILL.md`
- `workflow-state.yaml`
- validation report
- approved tests
- implementation evidence
- traceability matrix
- approved requirements and architecture as needed

Optional reads:

- source and tests inside implemented paths
- CI logs or validation command output
- security, testing, and NFR standards

Forbidden reads:

- unrelated source paths
- unrelated capabilities unless regression scope requires them

Expected outputs:

- `validation/validation-report.md`
- validation findings
- release readiness position

Stop conditions:

- implementation evidence is missing
- tests cannot be mapped to requirements
- release readiness is claimed without required evidence

## Release

Purpose: prepare release readiness, notes, rollback, monitoring, and approval evidence.

Required reads:

- `.codex/skills/release/SKILL.md`
- `workflow-state.yaml`
- validation report
- traceability matrix
- release notes template
- CI and quality evidence when code exists

Optional reads:

- implementation plan
- feedback log
- operational standards
- Jira/Confluence generated summaries

Forbidden reads:

- source code unless needed to verify release evidence
- unrelated capabilities

Expected outputs:

- `release/release-notes.md`
- release readiness summary
- rollback and monitoring evidence

Stop conditions:

- validation says release is not ready
- release notes are missing
- CI, security, rollback, or NFR evidence is missing
- release approval is missing

## Change Request

Purpose: perform impact analysis and targeted updates for scoped changes.

Required reads:

- `.codex/skills/change-request/SKILL.md`
- `workflow-state.yaml` when capability exists
- active domain context
- impacted artifacts named by the change
- placement guidance for code-impacting changes

Optional reads:

- traceability matrix
- feedback log
- related domain contexts for cross-domain impact
- Jira model docs

Forbidden reads:

- unrelated feature artifacts
- source code before impact analysis and approval
- restricted paths without owner approval

Expected outputs:

- change impact summary
- impacted owners and artifacts
- targeted update plan
- feedback and traceability impact

Stop conditions:

- change ID is missing and cannot be assigned
- impacted owners cannot be identified
- approval is missing for artifact or code changes

## Defect Fix

Purpose: analyze defects, classify RCA, and plan targeted corrections.

Required reads:

- `.codex/skills/defect-fix/SKILL.md`
- defect report or user evidence
- active domain context
- impacted feature artifacts
- workflow state when capability exists
- placement guidance for code-impacting fixes

Optional reads:

- source and tests only after RCA indicates code impact and paths are approved
- traceability matrix
- validation report
- feedback log

Forbidden reads:

- unrelated source
- unrelated capabilities
- restricted paths without approval

Expected outputs:

- defect analysis summary
- root cause classification
- impacted artifacts and owners
- targeted correction path
- validation and regression needs

Stop conditions:

- defect evidence is insufficient for RCA
- owner or allowed paths are missing for code-impacting fixes
- upstream artifact gap must be resolved before code

## Traceability Review

Purpose: verify end-to-end coverage across intent, requirements, architecture, API, tests, validation, release, Jira, and Confluence.

Required reads:

- `.codex/skills/traceability-review/SKILL.md`
- active domain context
- capability context and feature artifacts
- `traceability/traceability-matrix.md`
- `workflow-state.yaml`

Optional reads:

- feedback log
- Jira and Confluence generated payloads
- validation report and release notes

Forbidden reads:

- source code unless implementation evidence must be mapped
- unrelated capabilities unless cross-capability impact exists

Expected outputs:

- traceability findings
- coverage gaps
- updated or recommended traceability rows after approval

Stop conditions:

- mandatory source artifact is missing
- traceability gap blocks implementation, validation, or release

## Feedback Capture

Purpose: capture learning from review, tests, defects, incidents, production, and stakeholders.

Required reads:

- `.codex/skills/feedback-capture/SKILL.md`
- `feedback/feedback-log.md`
- impacted capability or domain artifacts
- workflow state when capability exists

Optional reads:

- traceability matrix
- validation report
- release notes
- Jira and Confluence placeholders

Forbidden reads:

- unrelated source or domains
- code changes before impact analysis and approval

Expected outputs:

- feedback entry
- impacted artifact update plan
- traceability update recommendation

Stop conditions:

- feedback affects requirements, tests, code, or release but owner approval is missing
- customer-sensitive details are not masked
