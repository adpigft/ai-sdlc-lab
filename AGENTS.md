# AI SDLC Lab - Codex Project Instructions

## Repository Purpose

This repository demonstrates an AI-native SDLC for banking delivery using Codex, skills, Jira, Confluence, GitHub, GitHub Actions, SonarCloud, traceability, feedback, optional MCP integrations, and human approval gates.

## Important Directories

- `skills/`: the only canonical Codex-native project skill path. Each skill is a folder with `SKILL.md`.
- `framework/`: AI SDLC governance, standards, templates, and lifecycle orchestration. Legacy role skill files were removed after migration to canonical `skills/`.
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

For any new feature, follow this order:

1. `skills/ba-intent/SKILL.md`
2. `skills/ba-specification/SKILL.md`
3. `skills/architect-context/SKILL.md`
4. `skills/architect-api/SKILL.md`
5. `skills/qa-test-design/SKILL.md`
6. `skills/traceability/SKILL.md`
7. `skills/developer-implementation/SKILL.md`
8. `skills/qa-validation/SKILL.md`
9. `skills/devsecops-release/SKILL.md`
10. `skills/feedback/SKILL.md`

## Interaction Rule

When the user says `Start new feature: <feature name>`:

1. Use `ba-intent` first.
2. Ask discovery questions.
3. Do not create artifacts until sufficient intent is captured.
4. Summarize understanding.
5. Ask for approval.
6. Create or update only the artifact owned by the active skill.
7. Move to the next skill only after human approval.

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
