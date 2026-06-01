# AI SDLC Lab

This repository defines a baseline operating model for using AI across a banking and digital payments software delivery lifecycle. It is intentionally documentation-first: no application code is included yet.

The baseline shows how a payment capability moves from business intent to specification, implementation readiness, validation, release, and feedback while preserving human accountability, traceability, and audit evidence.

## Repository Map

| Path | Purpose |
| --- | --- |
| `.ai/skills/` | Role instructions for AI-assisted BA, architect, developer, QA, and DevSecOps work. |
| `.ai/standards/` | Delivery standards that AI and humans must apply when creating specs, APIs, tests, secure designs, and code. |
| `.ai/templates/` | Reusable artifact templates for intent, specs, review gates, validation, release, feedback, and traceability. |
| `.ai/workflows/` | Step-by-step lifecycle workflows from intent capture through release. |
| `domains/` | Domain-oriented product artifacts. The current scaffold contains a `payments/khqr-payment` capability. |
| `traceability/` | Cross-artifact mapping from business intent to Jira, specs, tests, controls, and release evidence. |
| `feedback/` | Feedback loop for defects, user validation, production observations, and prompt/process improvements. |
| `docs/confluence/` | Source-controlled Confluence-ready operating-model documents. |
| `decisions/` | Architecture Decision Records for SDLC governance decisions. |
| `.github/workflows/` | Reserved for GitHub Actions automation. No workflows are implemented in this baseline. |
| `src/` | Reserved for future application code. Do not use until an approved spec and build gate exist. |

## Operating Principles

1. Business intent is captured before solution design.
2. Jira is the delivery system of record for work items and approvals.
3. This repository is the source of truth for versioned SDLC artifacts.
4. Confluence mirrors approved operating-model content for stakeholder consumption.
5. AI may draft, compare, summarize, and validate artifacts, but humans approve risk, scope, architecture, release, and customer-impacting decisions.
6. Every material requirement must trace to acceptance criteria, tests, validation evidence, and release notes.
7. GitHub Actions and SonarCloud gates must be added before application code is introduced.

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

- GitHub Actions has passed build, test, lint, security, and traceability checks.
- SonarCloud quality gate has passed.
- Release notes identify scope, risks, rollback, monitoring, and known limitations.
- Human release approval is recorded in Jira and referenced in this repository.

## Current Status

This is a baseline AI SDLC repository. It contains operating content and templates only. Application code, CI workflow files, Jira automation, Confluence publishing automation, and SonarCloud scanner configuration are intentionally not yet implemented.
