# AI-Native SDLC Framework

This repository is a spec-driven AI-native SDLC framework for banking delivery. It shows how Product Owners, Business Analysts, Solution Architects, QA, Developers, DevSecOps, platform teams, and domain squads can move from business intent to controlled implementation, validation, release, and feedback without losing traceability or human approval.

The framework uses:

- Git as the source of truth for intent, specs, architecture, APIs, tests, code, traceability, validation, release evidence, standards, and ADRs.
- Jira as the workflow tracker for Epics, Stories, Tasks, defects, approvals, and work management.
- Confluence as a published view for stakeholder summaries and operating-model pages.
- GitHub Actions as the validation guardrail for workflow state, artifacts, traceability, OpenAPI, and test execution.

AI can draft, compare, validate, and summarize. Humans approve scope, risk, architecture, implementation readiness, validation, and release.

## Quick Start

1. Read this README once end to end.
2. Pick an existing capability to inspect, such as `domains/payments/capabilities/khqr-payment-reversal/`.
3. Run `Status.` in Codex to see the active lifecycle state from `workflow-state.yaml`.
4. Run the local validation scripts listed in [Validation Commands](#validation-commands).
5. For a new capability in an existing domain, start with `$new <Capability Name>`.
6. For a new domain, create `domains/<domain>/domain-context.md` before running `$new`.
7. Do not touch `src/` until an implementation slice has explicit approval.

Jira and Confluence are optional/offline foundations for now. The scripts generate draft payloads and summaries, but they do not call Jira or Confluence APIs.

## Prerequisites

Local tooling:

- Git
- Bash
- Python 3
- Ruby, for YAML/OpenAPI parsing in validation
- Java/JDK, for Java compilation and executable tests where applicable
- Codex with the repository skills available under `.codex/skills/`

Optional tooling:

- Jira access, when work tracking moves beyond offline payload review
- Confluence access, when summary publishing moves beyond offline draft review
- GitHub Actions access, for hosted CI validation
- SonarCloud access, once application code and quality gates are configured

No Jira or Confluence credentials are required for the current offline foundations.

## Repository Structure

| Path | Purpose |
| --- | --- |
| `domains/` | Delivery knowledge: domain-owned intent, requirements, architecture, contracts, tests, validation, release, and workflow state. |
| `domains/<domain>/domain-context.md` | Domain glossary, boundaries, shared rules, integrations, events, APIs, risks, and patterns. New domains must create this first. |
| `domains/<domain>/capabilities/<capability>/` | Capability lifecycle artifacts: intent, spec, context, contracts, tests, design, validation, release, and workflow state. |
| `apps/` | Channel or product applications, such as a shared Flutter mobile banking app. |
| `services/` | Backend services grouped by domain and service name. |
| `libraries/` | Shared libraries governed separately from application and service squads. |
| `platform/` | Platform templates, bootstrap assets, service templates, and platform enablement patterns. |
| `framework/` | SDLC governance, standards, workflows, templates, events, frontend, libraries, service architecture, and multi-squad guidance. |
| `.codex/skills/` | Canonical active Codex skills. These drive the AI-native lifecycle. |
| `traceability/` | End-to-end traceability matrix from intent to Jira, requirements, architecture, APIs, tests, validation, release, and feedback. |
| `feedback/` | Feedback log for findings, defects, change requests, stakeholder feedback, and corrections. |
| `scripts/` | Local automation foundations for validation, Jira payload generation, and Confluence summary generation. |
| `src/` | Implementation code and tests. This must not be touched before implementation slice approval. |

## How `src/` Is Used

`domains/` contains delivery knowledge. It describes what should be built, why it matters, which rules apply, which APIs and tests are approved, and what evidence is required.

`src/` contains implementation code. It is used only after the lifecycle has approved:

- intent
- specification
- architecture
- API contract where applicable
- test design
- traceability
- implementation plan
- implementation slice approval

Before slice approval, do not add, edit, or reorganize `src/`. If a gap appears in approved artifacts, stop and report the gap instead of coding around it.

## First Exercise For New Users

Use the existing payments example to learn the framework:

1. Inspect `domains/payments/domain-context.md`.
2. Inspect `domains/payments/capabilities/khqr-payment-reversal/workflow-state.yaml`.
3. Run `Status.` in Codex.
4. Read the intent, spec, context, OpenAPI contract, acceptance tests, implementation plan, validation report, and traceability rows for KHQR Payment Reversal.
5. Run the validation scripts locally.
6. Generate offline Jira payloads to `/tmp/jira-payloads-review`.
7. Generate offline Confluence summaries to `/tmp/confluence-summaries-review`.
8. Review the outputs and confirm Git artifacts remain the source of truth.

Suggested commands:

```bash
scripts/validate-workflow-state.sh
scripts/validate-artifacts.sh
scripts/validate-traceability.sh
scripts/validate-openapi.sh
scripts/validate-java.sh

python3 -B scripts/jira/generate-jira-payloads.py \
  --workflow-state domains/payments/capabilities/khqr-payment-reversal/workflow-state.yaml \
  --output-dir /tmp/jira-payloads-review

python3 -B scripts/confluence/generate-summary.py \
  --workflow-state domains/payments/capabilities/khqr-payment-reversal/workflow-state.yaml \
  --output-dir /tmp/confluence-summaries-review
```

## Existing Domain Usage

Example:

- Existing domain: `payments`
- New capability: `KHQR Payment Reversal`

Typical command flow:

```text
$new KHQR Payment Reversal
Review.
Approved.
$specification
Review.
Approved.
$architecture
Review.
Approved.
$test-design
Review.
Approved.
$implementation
Review.
$validation
$release
```

Use `Status.` at any time to inspect the active capability, workflow state, current artifact, pending gate, blockers, next state, and next skill.

Use `Review.` when an artifact is ready for gate review. Findings should be resolved before approval.

Use `Approved.` only when the current gate has human approval. Approval advances `workflow-state.yaml` to the next state.

Use `Resolve findings.` or equivalent instructions to correct targeted review findings. Then use `Review.` again.

Use `Proceed.` after the current gate is approved and the next lifecycle stage should begin.

## New Domain Usage

Example:

- New domain: `cards`
- First capability: `Card Replacement`

Before creating capabilities, create:

```text
domains/cards/domain-context.md
```

The domain context should define:

- glossary and domain language
- domain boundaries
- integrations and third parties
- events and ownership
- APIs and shared contracts
- shared business rules
- data and security patterns
- operational and observability patterns

Only after `domain-context.md` exists should you start the first capability:

```text
$new Card Replacement
```

New domains need a domain context first so capabilities reuse the same language, integration model, ownership rules, and constraints.

## New Feature Flow

The normal lifecycle for a new capability is:

1. Intent: capture the business problem, users, outcomes, scope, assumptions, risks, and approval gate.
2. Specification: define functional requirements, non-functional requirements, business rules, data needs, edge cases, and acceptance criteria.
3. Architecture: define system boundary, components, integrations, data ownership, security, observability, risks, and ADR needs.
4. API Contract: define `contracts/openapi.yaml` when APIs are needed.
5. Test Design: create QA-owned acceptance, negative, integration, security, and NFR scenarios.
6. Traceability: map intent to requirements, APIs, tests, implementation slices, validation, release, Jira, and Confluence.
7. Implementation Plan: define one or more approved implementation slices.
8. Implementation Slice: implement one approved slice at a time using TDD and focused changes.
9. Validation: capture QA evidence, test execution, CI evidence, defects, risks, and release readiness.
10. Release: prepare release notes, rollback plan, monitoring checks, known risks, and approval evidence.

Jira lifecycle:

```text
Epic -> Stories -> Tasks/Subtasks -> Validation/Release references
```

Git lifecycle:

```text
Intent -> Spec -> Architecture/API -> Tests -> Traceability -> Implementation -> Validation -> Release -> Feedback
```

Git remains authoritative. Jira tracks work. Confluence publishes stakeholder summaries.

## Change Request Flow

Example:

```text
$change-request Support Partial Refunds
```

Change requests use impact analysis before edits:

1. Assign or confirm a Change ID.
2. Read the relevant `domain-context.md`.
3. Identify impacted intent, spec, architecture, API, tests, code, traceability, validation, release, and feedback artifacts.
4. Identify impacted owners and approvals.
5. Ask for approval before updates.
6. Update only impacted files.
7. Do not regenerate the whole solution.
8. Update traceability and feedback after approved changes.
9. Route to `$specification`, `$architecture`, `$test-design`, `$implementation`, `$validation`, or `$release` only where impacted.

Change requests preserve existing approved content that is not affected by the change.

## Defect Flow

Example:

```text
$defect-fix Duplicate Reversal Under Concurrency
```

Defect handling is RCA-led:

1. Assign or confirm a Defect ID.
2. Capture observed behavior, expected behavior, environment, build, logs, tests, or reproduction evidence.
3. Read the relevant `domain-context.md`.
4. Classify root cause as requirement, architecture, design, code, test, or operational gap.
5. Identify impacted artifacts and missing approvals.
6. Propose a targeted correction path.
7. Ask for approval before artifact, test, code, validation, or release changes.
8. Apply only targeted fixes.
9. Capture regression and validation evidence.
10. Update traceability and feedback.

Do not use a defect fix to bypass missing requirements, architecture, tests, traceability, or approval gates.

## Frontend Model

One shared Flutter app can support multiple domains and features:

```text
apps/mobile-banking-app/
apps/mobile-banking-app/features/payments/
apps/mobile-banking-app/features/cards/
apps/mobile-banking-app/shared/
```

Ownership model:

- The shared app shell is owned by the channel or platform squad.
- Feature modules are owned by domain squads.
- Shared UI components, navigation, authentication shell, analytics, and platform behavior require channel/platform approval.
- Domain feature changes should stay within the owning feature module unless shared changes are explicitly approved.

## Backend Microservices Model

Backend services are organized by domain and service name:

```text
services/<domain>/<service-name>/
```

Examples:

- `services/payments/local-payment-service/`
- `services/payments/international-payment-service/`
- `services/payments/remittance-service/`
- `services/cards/card-management-service/`
- `services/onboarding/onboarding-service/`
- `services/lending/lending-service/`
- `services/operations/operations-service/`

An implementation slice identifies its target service through:

- service catalog entries
- implementation plan slice metadata
- slice ownership metadata
- `CODEOWNERS`
- allowed paths enforced by workflow validation
- architecture and API ownership decisions

Do not modify another squad's service without ownership approval.

## APIs, Events, And Integrations

APIs are captured in:

```text
domains/<domain>/capabilities/<capability>/contracts/openapi.yaml
```

Events should be captured under capability or framework event areas, such as:

```text
domains/<domain>/capabilities/<capability>/events/
framework/events/
```

Integration governance should identify:

- third-party systems
- internal producer and consumer ownership
- event schemas and compatibility rules
- API versioning and compatibility checks
- consumer impact review
- operational dependencies
- failure modes and rollback behavior

Event producer and consumer ownership must be explicit before implementation and release.

## Bootstrap And Templates

Platform teams can provide baseline templates:

```text
platform/templates/flutter-app-template/
platform/templates/spring-boot-service-template/
platform/templates/shared-library-template/
platform/templates/kafka-service-template/
```

Bootstrap rules:

- A frontend app is created once from a baseline, then feature modules are added under domain folders.
- Backend services are created from the approved microservice template.
- Kafka/event services are created from the event-enabled template.
- Shared libraries are governed separately and require library ownership, versioning, compatibility, and dependency review.

Templates accelerate setup. They do not replace lifecycle artifacts, ownership approval, or traceability.

## Standards

Standards live under `framework/standards/` and related framework areas. Teams should apply:

- coding standards
- API standards
- security standards
- testing standards
- architecture and design standards
- observability standards
- release standards

Standards apply to both human-authored and AI-generated work.

## Multi-Squad Governance

Every material artifact or code area needs an owner:

- domain owner
- service owner
- app owner
- library owner
- event owner
- API owner
- release owner

Governance controls:

- `CODEOWNERS` defines review ownership.
- PRs should stay within approved capability, service, app, or library boundaries.
- Dependency changes require review by affected owners.
- Shared frontend changes require platform/channel approval.
- Shared library changes require library owner approval.
- Event and API changes require producer, consumer, and compatibility review.
- Cross-squad impact should be reviewed before implementation.

## Automation

GitHub Actions validation foundation checks:

- `workflow-state.yaml` exists
- required artifacts exist
- traceability matrix exists
- OpenAPI contracts parse
- Java compiles/tests pass where applicable
- forbidden path changes are blocked by stage

GitHub Actions can be tested locally with the same scripts:

```bash
scripts/validate-workflow-state.sh
scripts/validate-artifacts.sh
scripts/validate-traceability.sh
scripts/validate-openapi.sh
scripts/validate-java.sh
```

Jira automation foundation:

- `scripts/jira/generate-jira-payloads.py` generates offline Jira payload JSON.
- Epic maps to capability.
- Story maps to business requirement group or business capability slice.
- Task maps to implementation slice.
- No Jira API is called yet.

Confluence automation foundation:

- `scripts/confluence/generate-summary.py` generates stakeholder Markdown summaries.
- Confluence is a published view only.
- No Confluence API is called yet.

Automation supports review. It does not replace Git, approvals, or GitHub Actions gate results.

## Validation Commands

Run all local validation guardrails:

```bash
scripts/validate-workflow-state.sh
scripts/validate-artifacts.sh
scripts/validate-traceability.sh
scripts/validate-openapi.sh
scripts/validate-java.sh
```

Generate Jira payloads offline:

```bash
python3 -B scripts/jira/generate-jira-payloads.py \
  --workflow-state domains/payments/capabilities/khqr-payment-reversal/workflow-state.yaml \
  --output-dir /tmp/jira-payloads-review
```

Generate Confluence summaries offline:

```bash
python3 -B scripts/confluence/generate-summary.py \
  --workflow-state domains/payments/capabilities/khqr-payment-reversal/workflow-state.yaml \
  --output-dir /tmp/confluence-summaries-review
```

Check Markdown and whitespace changes before review:

```bash
git diff --check
git status --short
```

## Definition Of Ready And Done

Implementation DoR:

- intent approved
- specification approved
- architecture approved
- API contract approved where applicable
- test design approved
- traceability reviewed
- implementation slice approved
- target app/service/library path identified
- owners and allowed paths confirmed
- open blockers documented or resolved

Implementation DoD:

- one approved slice implemented
- tests added and passing where runnable
- code maps to approved requirements and test design
- no secrets or credentials committed
- traceability updated where needed
- validation notes prepared
- developer and architect review completed

Release readiness is separate from implementation done. Release requires validation evidence, CI evidence, release notes, rollback plan, monitoring checks, known risks, and human release approval.

## Examples

Example capabilities by domain:

- Payments: KHQR Payment Reversal
- Payments: QR Refund
- Cards: Card Replacement
- Onboarding: Digital Onboarding
- Deposits: Account Opening
- Lending: Loan Application
- Operations: Case Management

Use these examples as naming and lifecycle patterns, not as permission to skip discovery or approval.

## Command Reference

User commands:

| Command | Purpose |
| --- | --- |
| `$new` | Start a new capability or feature with discovery, intent, and approval gates. |
| `$change-request` | Analyze and apply a scoped change without regenerating the whole solution. |
| `$defect-fix` | Analyze RCA and apply targeted defect corrections. |
| `Status.` | Show current capability, state, artifact, gate, blockers, next state, and next skill. |
| `Review.` | Review the current artifact against its pending gate. |
| `Approved.` | Record approval and move workflow state forward. |
| `Resolve findings.` | Correct targeted review findings. |
| `Proceed.` | Continue to the next approved lifecycle step. |

Lifecycle skills:

| Skill | Purpose |
| --- | --- |
| `$specification` | Turn approved intent into requirements, rules, NFRs, and acceptance criteria. |
| `$architecture` | Define context, boundaries, APIs, integrations, data, security, ADRs, and implementation planning. |
| `$test-design` | Create QA-owned acceptance, negative, integration, security, and NFR scenarios. |
| `$implementation` | Implement one approved slice at a time using TDD and focused changes. |
| `$validation` | Capture QA validation evidence, defects, risks, and release readiness evidence. |
| `$release` | Prepare release notes, rollback, monitoring, risks, and release approvals. |
| `$traceability-review` | Maintain end-to-end traceability across artifacts, Jira, Confluence, validation, and release. |
| `$feedback-capture` | Capture review findings, defects, changes, and stakeholder feedback. |

## Troubleshooting

`Status.` cannot find the active capability:

- Check that `domains/<domain>/capabilities/<capability>/workflow-state.yaml` exists.
- If multiple capabilities exist, name the capability explicitly.

Validation says `workflow-state.yaml` is missing:

- Create or update workflow state through the active lifecycle skill.
- Do not invent a state to bypass approval gates.

Artifact validation fails:

- Check the `artifacts` section in `workflow-state.yaml`.
- Confirm required files exist and are not empty.
- Keep artifact paths relative to the repository root.

OpenAPI validation fails:

- Confirm `contracts/openapi.yaml` is valid YAML.
- Confirm it declares `openapi` or `swagger`, `info.title`, `info.version`, and `paths`.

Java validation fails:

- Confirm a JDK is installed.
- If no Maven or Gradle project exists, the script uses `javac` and executable test mains.
- Fix compile or test failures only when the relevant implementation slice is approved.

Jira payload generation fails:

- Confirm `workflow-state.yaml` points to intent, specification, implementation plan, and validation report paths.
- Remember the Jira script is offline and does not call Jira APIs.

Confluence summary generation fails:

- Confirm `workflow-state.yaml` points to intent, specification, architecture context, and validation report paths.
- Remember the Confluence script is offline and does not call Confluence APIs.

You are unsure whether to edit `src/`:

- Do not edit it unless implementation slice approval exists.
- Use `Status.` and inspect `workflow-state.yaml`.
- If approval evidence is missing, stop and request the required approval.

## Golden Rules

- Do not generate code before approved specification, architecture, API, tests, traceability, and slice approval.
- Do not regenerate the whole solution for a change request or defect.
- Do not modify another squad's service without ownership approval.
- Do not touch `src/` before implementation slice approval.
- Treat `domains/` as delivery knowledge and `src/` as implementation code.
- Keep changes small, targeted, and reviewable.
- Git is the source of truth.
- Jira tracks workflow and approvals.
- Confluence publishes summaries.
- GitHub Actions is authoritative for validation guardrails.
- AI follows `workflow-state.yaml`.
- Human approval gates are mandatory.
