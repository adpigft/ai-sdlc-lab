# AI SDLC Lab - Codex Project Instructions

## Repository Purpose

This repository demonstrates an AI-native SDLC for banking delivery using Codex, skills, Jira, Confluence, GitHub, GitHub Actions, SonarCloud, traceability, feedback-capture, optional MCP integrations, and human approval gates.

## Important Directories

- `.codex/skills/`: the only canonical Codex-native project skill path. Each skill is a folder with `SKILL.md`.
- `.codex/archive/skills/`: archived skills retained for future reuse. They are not recommended for normal use.
- `framework/`: AI SDLC governance, standards, templates, and lifecycle orchestration. Legacy role skill files were removed after migration to canonical `.codex/skills/`.
- `framework/workflows/`: lifecycle workflows and orchestration notes.
- `framework/standards/`: engineering, API, security, and testing standards.
- `framework/templates/`: reusable artifact templates.
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

Normal users should use these orchestration skills:

- `$domain-onboarding` for a new banking domain before creating capabilities.
- `$new` for a new capability or new feature flow.
- `$change-request` for change requests.
- `$defect-fix` for bugs and defects.
- `$decision` for architecture decisions and ADRs.
- `$release` for release readiness and release management.

Temporary aliases remain available for one migration cycle:

- `$change`
- `$defect`
- `$traceability`
- `$feedback`

Specialists can use these stage-level entry points:

- `$intent`
- `$specification`
- `$architecture`
- `$test-design`
- `$implementation`
- `$validation`

Expert users may still invoke existing specialist skills directly.

Core specialist skills are internal building blocks used by the user-facing and stage-level skills:

- `ba-intent`
- `ba-specification`
- `architect-context`
- `developer-implementation`
- `qa-test-design`
- `qa-validation`
- `traceability-review`
- `feedback-capture`
- `devsecops-release`

Archived skills under `.codex/archive/skills/` are retained for future reuse, but they are not recommended for normal use.

For any new feature, follow this order:

1. `.codex/skills/new/SKILL.md`
2. `.codex/skills/intent/SKILL.md`
3. `.codex/skills/specification/SKILL.md`
4. `.codex/skills/architecture/SKILL.md`
5. `.codex/skills/test-design/SKILL.md`
6. `.codex/skills/traceability-review/SKILL.md`
7. `.codex/skills/implementation/SKILL.md`
8. `.codex/skills/validation/SKILL.md`
9. `.codex/skills/release/SKILL.md`
10. `.codex/skills/feedback-capture/SKILL.md`

The stage-level orchestration skills wrap the specialist skills:

- `$intent` uses `ba-intent`.
- `$specification` uses `ba-specification`.
- `$architecture` uses `architect-context` and identifies any decision or API work through the active orchestration flow.
- `$test-design` uses `qa-test-design`.
- `$implementation` uses `developer-implementation`.
- `$validation` uses `qa-validation`.

## Interaction Rule

When the user says `Start new feature: <feature name>`:

1. Use `$new` first.
2. Create or reference a lightweight Jira Epic shell if Jira is available.
3. Begin with intent discovery using `$intent` / `ba-intent`.
4. Ask discovery questions.
5. Do not create Git artifacts until sufficient intent is captured.
6. Summarize understanding.
7. Ask for approval.
8. Create or update only the artifact owned by the active skill.
9. Move to the next skill only after human approval.

Jira lifecycle:

Jira Epic -> Intent -> Specification -> Jira Stories -> Architecture/API/Tests -> Implementation Slices -> PR/Validation/Release

- Jira Epic can exist before intent as a lightweight discovery container.
- Intent is created in Git after discovery.
- Specification is created after intent approval.
- Jira Stories are created after specification approval.
- Jira Tasks/Subtasks are created after implementation slices are defined.
- Git remains source of truth for intent/spec/design/tests/code/traceability.
- Jira is work management and approval tracking.

## Human Approval Gates

- Intent requires PO / BA approval.
- Specification requires BA / PO approval.
- Architecture context requires Architect approval.
- API contract requires Architect approval.
- Tests require QA approval.
- Traceability requires BA, Architect, and QA review.
- Implementation requires Developer and Architect review.
- Validation requires QA approval.
- Release requires PO, QA, Architect, and DevSecOps approval.

Approval evidence:

- For lab work in this repository, explicit user confirmation in chat is acceptable approval evidence.
- For real delivery, approval must be backed by Jira status, pull request approval, or signed artifact approval.

## Subagents

Subagents are for parallel review only. They are not the normal sequential workflow.

Use subagents only to review existing artifacts from a specific angle, such as security, QA coverage, architecture consistency, release readiness, or documentation consistency. Do not use subagents to skip discovery, bypass approvals, create implementation early, or override GitHub Actions, SonarCloud, Jira, or signed artifact gates.

## File Ownership

- Intent: `domains/**/intent/intent.md`
- Specification: `domains/**/specs/spec.md`
- Context/design: `domains/**/context/context.md`
- API contract: `domains/**/contracts/openapi.yaml`
- Acceptance tests: `domains/**/tests/acceptance.feature`
- Validation: `domains/**/validation/validation-report.md`
- Release: `domains/**/release/release-notes.md`
- Traceability: `traceability/traceability-matrix.md`
- Feedback: `feedback/feedback-log.md`

## Safety Rules

- Never modify unrelated files.
- Never hardcode tokens, passwords, API keys, or MCP credentials.
- Use environment variables for enterprise integrations.
- Never generate code before approved intent, specification, architecture, API, tests, and traceability.
- If an approved artifact has a gap, stop and report it instead of coding around it.
- Keep changes small and reviewable.
- Always summarize impacted files.
