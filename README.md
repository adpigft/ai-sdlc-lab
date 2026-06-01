# AI SDLC Lab

This repository defines a baseline operating model for using AI across a banking and digital payments software delivery lifecycle. It is intentionally documentation-first: no application code is included yet.

The baseline shows how a payment capability moves from business intent to specification, implementation readiness, validation, release, and feedback while preserving human accountability, traceability, and audit evidence.

## Repository Map

| Path | Purpose |
| --- | --- |
| `.codex/skills/` | Canonical active execution skills for Codex. Each skill is a folder with `SKILL.md`. |
| `.codex/archive/skills/` | Archived skills retained for future reuse. They are not recommended for normal use. |
| `framework/` | AI SDLC governance, standards, templates, and lifecycle orchestration. Legacy role skill files were removed after migration to canonical `.codex/skills/`. |
| `framework/standards/` | Delivery standards that AI and humans must apply when creating specs, APIs, tests, secure designs, and code. |
| `framework/templates/` | Reusable artifact templates for intent, specs, review gates, validation, release, feedback, and traceability. |
| `framework/workflows/` | Step-by-step lifecycle workflows from intent capture through release. |
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

## AI-Native SDLC Skill Library

The repository keeps the active skill library intentionally small. Normal users use the orchestration skills, specialists use stage-level entry points, and core specialist skills remain as internal building blocks.

### Normal User Skills

Normal users use:

- `$new` for a new capability or feature flow
- `$change` for change requests
- `$defect` for bugs and defects
- `$decision` for architecture decisions and ADRs
- `$release` for release readiness and release management

### Specialist Skills

Specialists use:

- `$intent`
- `$specification`
- `$architecture`
- `$test-design`
- `$implementation`
- `$validation`

### Core Specialist Building Blocks

Core specialist skills are internal building blocks used by the user-facing and specialist entry points:

- `ba-intent`
- `ba-specification`
- `architect-context`
- `developer-implementation`
- `qa-test-design`
- `qa-validation`
- `traceability`
- `feedback`
- `devsecops-release`

Archived skills are retained under `.codex/archive/skills/` for future reuse, but they are not recommended for normal use.

## Using Skills in Codex

- Run `/skills` to view the available repository skills.
- Type `$` to mention or invoke a skill in chat.
- Examples:
  - `$new Start new feature: QR Refund`
  - `$change Analyze CR: Support partial refunds`
  - `$defect Analyze defect: duplicate refund`
  - `$decision Create ADR for refund idempotency`
  - `$release Prepare release readiness for QR Refund`

## Supported Delivery Flows

### New Feature Flow

Jira Epic -> Intent -> Specification -> Jira Stories -> Architecture/API/Tests -> Implementation Slices -> PR/Validation/Release

Detailed flow:

Intent -> Specification -> Architecture -> ADR -> API Contract -> Acceptance Tests -> Traceability -> Validation Plan -> Implementation Plan -> Controlled Slice Delivery -> Validation -> Release -> Feedback

Jira lifecycle guidance:

- A Jira Epic can exist before intent as a lightweight discovery container.
- Intent is created in Git after discovery.
- Specification is created after intent approval.
- Jira Stories are created after specification approval.
- Jira Tasks and Subtasks are created after implementation slices are defined.
- Git remains the source of truth for intent, specification, design, tests, code, traceability, and release artifacts.
- Jira is used for work management and approval tracking.

### Change Request Flow

Feedback -> Change Impact Analysis -> Impacted Artifact Update -> Targeted Implementation -> Validation -> Release

### Defect Flow

Defect Analysis -> Root Cause Analysis -> Targeted Fix -> Validation -> Release

### Production Incident Flow

Incident Analysis -> Root Cause Analysis -> Corrective Action -> Preventive Action

### ADR Flow

ADR Creation -> ADR Review -> ADR Approval -> Architecture Update

## Human Approval Gates

Required approvals:

- Intent
- Specification
- Architecture
- API Contract
- Test Design
- Implementation Plan
- Validation
- Release

Principle:

AI drafts and validates. Humans approve.

## Operating Principles

1. Business intent is captured before solution design.
2. Jira is the work management and approval tracking system, not the source of truth for delivery artifacts.
3. Git is the source of truth for specs, tests, code, traceability, release artifacts, standards, workflows, and ADRs.
4. Confluence mirrors approved operating-model content for stakeholder consumption, but it is not the source of truth.
5. AI may draft, compare, summarize, and validate artifacts, but humans approve risk, scope, architecture, release, and customer-impacting decisions.
6. Every material requirement must trace to acceptance criteria, tests, validation evidence, and release notes.
7. GitHub Actions is the system of record for CI gates.
8. Jira, Confluence, and GitHub MCP integrations are optional enterprise collaboration aids.
9. `.codex/skills/` is the active Codex skill location for this repository.
10. Subagents are for parallel review only, not the normal sequential workflow.
11. `.codex/archive/skills/` retains old or advanced skills for future reuse, but normal users should not start there.

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

Git is the source of truth. Jira is for work management. Confluence is for publishing. GitHub is for source control and CI/CD.

Optional MCP placeholders are documented in `.codex/config.toml` and `docs/automation/mcp-setup.md` for Jira, Confluence, and GitHub.

Rules:

- Do not hardcode tokens.
- Use environment variables only.
- Jira and Confluence MCP are for collaboration and publication workflows, not source-of-truth replacement.
- GitHub MCP may assist pull request and issue collaboration, but GitHub Actions remains authoritative for CI gate results.

## Subagents

Subagents are used only for parallel review.

Examples:

- Architecture Review
- Security Review
- QA Review
- Release Readiness Review

Subagents must not:

- bypass approval gates
- generate production code independently
- override CI/CD evidence

## Enterprise Automation Roadmap

### Phase 1

- Skills
- Workflows
- Traceability
- Validation

### Phase 2

- Jira MCP
- Confluence Publishing
- GitHub Actions Enforcement
- SonarCloud Gates

### Phase 3

- Automated Jira Lifecycle
- Governance Reporting
- Release Reporting

## Current Status

This is a baseline AI SDLC governance repository. The current focus is the AI-native SDLC validation workflow, the slice-based implementation model, ADR-driven architecture governance, and the change-request and defect workflows planned for the next phase.

Already set up:

- Codex project instructions in `AGENTS.md`.
- Canonical Codex skills under `.codex/skills/`.
- Legacy role skill files were removed after migration to canonical `.codex/skills/`.
- AI SDLC standards, templates, and workflows under `framework/`.
- Optional MCP placeholders for Jira, Confluence, and GitHub.
- Subagent review workflow guidance.
- KHQR payment intent, context, specification, OpenAPI contract, acceptance tests, validation report, and release notes under `domains/payments/capabilities/khqr-payment/`.
- Traceability and feedback artifacts.
- GitHub Actions workflows for AI SDLC artifact validation and placeholder CI.
- SonarCloud placeholder configuration in `sonar-project.properties`.

Application code is intentionally not created yet. The `src/` folder must remain empty until approved specifications, tests, traceability, and human gates are in place.

Jira automation and Confluence publishing automation are not implemented yet.
