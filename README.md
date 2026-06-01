# AI SDLC Lab

This repository defines a baseline operating model for using AI across a banking and digital payments software delivery lifecycle. It is intentionally documentation-first: no application code is included yet.

The baseline shows how a payment capability moves from business intent to specification, implementation readiness, validation, release, and feedback while preserving human accountability, traceability, and audit evidence.

## Repository Map

| Path | Purpose |
| --- | --- |
| `skills/` | The only canonical Codex project skill path. Each skill is a folder with `SKILL.md`. |
| `.ai/skills/` | Legacy/reference role instructions only. Do not use for active skill execution. |
| `.ai/skills-legacy/` | Legacy/reference role instructions only. Do not use for active skill execution. |
| `.ai/standards/` | Delivery standards that AI and humans must apply when creating specs, APIs, tests, secure designs, and code. |
| `.ai/templates/` | Reusable artifact templates for intent, specs, review gates, validation, release, feedback, and traceability. |
| `.ai/workflows/` | Step-by-step lifecycle workflows from intent capture through release. |
| `.codex/config.toml` | Optional enterprise MCP integration placeholders using environment variables only. |
| `domains/` | Domain-oriented product artifacts. The current scaffold contains a `payments/khqr-payment` capability. |
| `traceability/` | Cross-artifact mapping from business intent to Jira, specs, tests, controls, and release evidence. |
| `feedback/` | Feedback loop for defects, user validation, production observations, and prompt/process improvements. |
| `docs/automation/` | MCP and automation setup documentation. |
| `docs/subagents/` | Parallel review guidance for subagents. |
| `docs/confluence/` | Source-controlled Confluence-ready operating-model documents. |
| `decisions/` | Architecture Decision Records for SDLC governance decisions. |
| `.github/workflows/` | GitHub Actions governance automation. Artifact validation exists; CI jobs are placeholders until application code exists. |
| `sonar-project.properties` | SonarCloud placeholder configuration. Complete it when application code, binaries, and coverage paths exist. |
| `src/` | Intentionally empty. Do not add application code until specs, tests, traceability, and human gates are approved. |

## Operating Principles

1. Business intent is captured before solution design.
2. Jira is the delivery system of record for work items and approvals.
3. Git is the source of truth for specs, tests, code, traceability, release artifacts, standards, workflows, and ADRs.
4. Confluence mirrors approved operating-model content for stakeholder consumption, but it is not the source of truth.
5. AI may draft, compare, summarize, and validate artifacts, but humans approve risk, scope, architecture, release, and customer-impacting decisions.
6. Every material requirement must trace to acceptance criteria, tests, validation evidence, and release notes.
7. GitHub Actions is the system of record for CI gates.
8. Jira, Confluence, and GitHub MCP integrations are optional enterprise collaboration aids.
9. `skills/` is the only canonical Codex skill location for this repository.
10. Subagents are for parallel review only, not the normal sequential workflow.

## Example Capability

The sample capability is `domains/payments/capabilities/khqr-payment`, representing a digital payment feature that allows customers to initiate KHQR payments from a mobile banking channel.

Use this capability to exercise the lifecycle:

1. Capture payment intent and risk boundaries.
2. Produce a reviewed functional and non-functional specification.
3. Define an API contract and acceptance tests.
4. Validate against banking controls, QA standards, security standards, and traceability.
5. Record feedback after human review, test execution, and pilot release.

## Minimum Gate Expectations

Before implementation starts:

- Jira epic, story, risk, and approval references are present.
- Intent, context, specification, API contract, and acceptance criteria are complete.
- Architect, QA, security, and product owner review gates are recorded.
- Traceability matrix has no unlinked mandatory requirement.

Before release:

- Current repository state: GitHub Actions artifact validation must pass.
- Current repository state: build, test, security, and SonarCloud jobs are placeholders until application code exists.
- Future application release state: GitHub Actions must pass build, test, lint, security, and traceability checks.
- Future application release state: SonarCloud quality gate must pass.
- Release notes identify scope, risks, rollback, monitoring, and known limitations.
- Human release approval is recorded in Jira and referenced in this repository.

## Enterprise MCP

Optional MCP placeholders are documented in `.codex/config.toml` and `docs/automation/mcp-setup.md` for Jira, Confluence, and GitHub.

Rules:

- Do not hardcode tokens.
- Use environment variables only.
- Jira and Confluence MCP are for collaboration and publication workflows, not source-of-truth replacement.
- GitHub MCP may assist pull request and issue collaboration, but GitHub Actions remains authoritative for CI gate results.

## Subagents

Subagent guidance is documented in `docs/subagents/subagent-workflows.md`. Subagents may be used for parallel review of existing artifacts, such as security review, QA coverage review, architecture consistency review, release readiness review, or documentation consistency review.

Subagents must not skip the sequential AI SDLC workflow, bypass human approval gates, create application code early, or override GitHub Actions and SonarCloud evidence.

## Current Status

This is a baseline AI SDLC governance repository. The current focus is AI SDLC governance artifacts and the KHQR feature specification package.

Already set up:

- Codex project instructions in `AGENTS.md`.
- Canonical Codex skills under `skills/`.
- Legacy/reference role notes under `.ai/skills/` and `.ai/skills-legacy/`.
- AI SDLC standards, templates, and workflows under `.ai/`.
- Optional MCP placeholders for Jira, Confluence, and GitHub.
- Subagent review workflow guidance.
- KHQR payment intent, context, specification, OpenAPI contract, acceptance tests, validation report, and release notes under `domains/payments/capabilities/khqr-payment/`.
- Traceability and feedback artifacts.
- GitHub Actions workflows for AI SDLC artifact validation and placeholder CI.
- SonarCloud placeholder configuration in `sonar-project.properties`.

Application code is intentionally not created yet. The `src/` folder must remain empty until approved specifications, tests, traceability, and human gates are in place.

Jira automation and Confluence publishing automation are not implemented yet.
