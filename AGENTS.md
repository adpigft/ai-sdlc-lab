# AI SDLC Lab - Codex Project Instructions

## Repository Purpose

This repository demonstrates an AI-native SDLC for banking delivery using Codex, skills, Jira, Confluence, GitHub, GitHub Actions, SonarCloud, traceability, feedback-capture, optional MCP integrations, and human approval gates.

## Important Directories

- `.codex/skills/`: the only canonical Codex-native project skill path. Each skill is a folder with `SKILL.md`.
- `.codex/archive/skills/`: archived skills retained for future reuse. They are not recommended for normal use.
- `framework/`: AI SDLC governance, standards, templates, and lifecycle orchestration.
- `framework/00-navigation/`: document map, indexes, and capability summary guidance.
- `framework/01-lifecycle/`: lifecycle workflows, workflow state, review flow, and prompt patterns.
- `framework/02-context-control/`: context packs, token discipline, and context index guidance.
- `framework/03-delivery-governance/`: ownership, placement, frontend, service, event, and shared asset governance.
- `framework/04-engineering-standards/`: engineering, API, security, and testing standards.
- `framework/05-platform-bootstrap/`: platform bootstrap guidance and templates.
- `framework/06-tool-integrations/`: Jira and other tool integration guidance.
- `framework/07-templates/`: reusable artifact templates.
- `.codex/config.toml`: optional enterprise MCP placeholders. Environment variables only; no tokens in files.
- `docs/automation/`: automation and MCP setup notes.
- `docs/subagents/`: subagent review workflow notes.
- `domains/`: business domains, capabilities, specs, contracts, tests, validation, and release artifacts.
- `traceability/`: end-to-end traceability matrix.
- `feedback/`: review findings, corrections, defects, and change requests.
- `.github/workflows/`: GitHub Actions validation and CI placeholders.
- `src/`: application code. Do not generate code until approved.

## Source Of Truth

- Git is the source of truth for specs, tests, code, traceability, release artifacts, standards, workflows, and ADRs.
- GitHub Actions is the system of record for CI gates.
- Jira and Confluence MCP integrations are optional collaboration aids, not source-of-truth replacements.
- GitHub MCP may assist repository collaboration, but GitHub Actions remains authoritative for CI gate results.

## Default AI SDLC Flow

Do not jump directly to code.

Skills are reusable procedures. Framework-specific lifecycle routing, artifact placement, context loading, workflow-state updates, and governance are defined by:

- `framework/01-lifecycle/skill-orchestration-adapter.md`
- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`

Normal users should use these orchestration skills:

- `$domain-onboarding` for a new banking domain before creating capabilities.
- `$intent` for a new capability or new feature flow.
- `$specification` for requirements.
- `$design` for feature design, API, event, integration, placement, and ADR discovery.
- `$test-design` for acceptance, negative, integration, security, and NFR scenarios.
- `$implementation` for approved implementation slices.
- `$pr-review` for implementation slice / PR readiness review.
- `$validation` for QA validation evidence.
- `$change-request` for change requests.
- `$defect-fix` for bugs and defects.
- `$traceability-review` for end-to-end traceability.
- `$feedback-capture` for findings, corrections, and lessons learned.
- `$decision` for architecture decisions and ADRs.
- `$release` for release readiness and release management.

Support skills are reusable procedures, not lifecycle stages:

- `$capability-onboarding` for capability context creation under an existing domain.
- `$source-ingestion` for converting external source documents into AI-readable summaries.
- `$repo-discovery` for extracting repository standards and conventions.
- `$artifact-review` for reviewing AI-generated artifacts before human approval.

Archived skills under `.codex/archive/skills/` are retained for future reuse, but they are not recommended for normal use.

For any new feature, the framework lifecycle order is:

1. `$intent`
2. `$specification`
3. `$design`
4. `$test-design`
5. `$implementation`
6. `$pr-review`
7. `$validation`
8. `$release`

Use `$traceability-review`, `$feedback-capture`, and `$decision` where the orchestration adapter or active evidence requires them.

## Interaction Rule

When the user says `Start new feature: <feature name>`:

1. Use `$intent` first.
2. Create or reference a lightweight Jira Epic shell if Jira is available.
3. Begin with intent discovery using `$intent`.
4. Ask discovery questions.
5. Do not create Git artifacts until sufficient intent is captured.
6. Summarize understanding.
7. Ask for approval.
8. Create or update only the artifact owned by the active skill.
9. Move to the next skill only after human approval.

Jira lifecycle:

Jira Epic (Capability) -> Jira Story (Feature) -> Intent -> Specification -> Design/API/Tests -> Implementation Slices / Jira Tasks -> PR Review -> Validation -> Release

- Jira Epic is the capability container.
- Jira Story is the feature delivery container.
- Intent is created in Git after discovery.
- Specification is created after intent approval.
- Jira Story scope is refined after specification approval.
- Jira Tasks/Subtasks are created after implementation slices are defined.
- Git remains source of truth for intent/spec/design/tests/code/traceability.
- Jira is work management and approval tracking.

## Human Approval Gates

- Intent requires PO / BA approval.
- Specification requires BA / PO approval.
- Design context requires Architect approval.
- API contract requires Architect approval.
- Tests require QA approval.
- Traceability requires BA, Architect, and QA review.
- Implementation requires Developer and Architect review.
- PR review requires Developer Lead, Architect, and impacted owner review where paths, APIs, events, or shared assets are affected.
- Validation requires QA approval.
- Release requires PO, QA, Architect, and DevSecOps approval.

Approval evidence:

- For lab work in this repository, explicit user confirmation in chat is acceptable approval evidence.
- For real delivery, approval must be backed by Jira status, pull request approval, or signed artifact approval.

## Subagents

Subagents are for parallel review only. They are not the normal sequential workflow.

Use subagents only to review existing artifacts from a specific angle, such as security, QA coverage, architecture consistency, release readiness, or documentation consistency. Do not use subagents to skip discovery, bypass approvals, create implementation early, or override GitHub Actions, SonarCloud, Jira, or signed artifact gates.

## File Ownership

- Intent: `domains/**/features/**/intent/intent.md`
- Specification: `domains/**/features/**/specification/specification.md`
- Design: `domains/**/features/**/design/design.md`
- API contract: `domains/**/features/**/contracts/openapi.yaml`
- Acceptance tests: `domains/**/features/**/tests/acceptance.feature`
- Implementation plan: `domains/**/features/**/implementation/implementation-plan.md`
- PR review: `domains/**/features/**/pr-review/pr-review-report.md`
- Validation: `domains/**/features/**/validation/validation-report.md`
- Release: `domains/**/features/**/release/release-notes.md`
- Traceability: `traceability/traceability-matrix.md`
- Feedback: `feedback/feedback-log.md`

Existing capability-level artifacts may still use `domains/**/specs/spec.md`, `domains/**/context/context.md`, and `domains/**/design/implementation-plan.md` for one migration cycle. New framework guidance and templates should use the canonical feature-level paths above.

## Safety Rules

- Never modify unrelated files.
- Never hardcode tokens, passwords, API keys, or MCP credentials.
- Use environment variables for enterprise integrations.
- Never generate code before approved intent, specification, design, API, tests, and traceability.
- If an approved artifact has a gap, stop and report it instead of coding around it.
- Keep changes small and reviewable.
- Always summarize impacted files.
