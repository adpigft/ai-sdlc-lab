# AI-SDLC-LAB

## Overview

AI-SDLC-LAB is a specification-driven AI-native delivery framework.

The framework enables teams to deliver software using:

- Specifications as the source of truth
- Human ownership and approvals
- AI-assisted execution
- Continuous validation and traceability
- Git-based delivery artifacts
- Automated governance

The framework is designed for:

- Digital Banking
- Core Banking
- Payments
- Deposits
- Cards
- Lending
- Onboarding
- Operations Portals
- Event-Driven Architectures
- API and Integration Platforms

---

# Core Principles

1. Specifications are the primary delivery artifact. In this framework, specification means requirements.
2. Human roles own decisions and approvals.
3. AI assists execution but does not replace accountability.
4. Every change must be traceable.
5. Validation happens continuously.
6. Git is the source of truth.

---

# Repository Structure

```text
.ai-sdlc-lab
├── .agents
├── .codex
├── .github
├── decisions
├── docs
├── domains
├── feedback
├── framework
├── scripts
├── src
├── traceability
├── AGENTS.md
├── README.md
└── sonar-project.properties
```

---

# Framework Structure

```text
framework
├── 00-navigation
├── 01-lifecycle
├── 02-context-control
├── 03-delivery-governance
├── 04-engineering-standards
├── 05-platform-bootstrap
├── 06-tool-integrations
└── 07-templates
```

---

# Key Folders

## domains/

Contains domain, capability, and feature delivery knowledge.

Example:

```text
domains/
└── payments/
    └── capabilities/
        └── payment-reversal/
            ├── capability-context.md
            └── features/
                └── khqr-payment-reversal/
```

Each parent capability contains `capability-context.md` and one or more feature delivery folders.

Each feature contains:

```text
intent/
specification/
design/
contracts/
tests/
implementation/
pr-review/
validation/
release/
workflow-state.yaml
```

Canonical feature artifact paths are `intent/intent.md`, `specification/specification.md`, `design/design.md`, `contracts/openapi.yaml`, `tests/acceptance.feature`, `implementation/implementation-plan.md`, `pr-review/pr-review-report.md`, `validation/validation-report.md`, `release/release-notes.md`, and `workflow-state.yaml`.

---

## src/

Contains executable source code.

Example:

```text
src/main/java/
src/test/java/
```

Source code is created only after specification, design, test-design, traceability, and implementation slice approval are complete.

---

# Domain, Capability, and Feature Model

The current pilot framework uses three delivery levels:

- Domain = architecture boundary
- Capability = business function boundary
- Feature = delivery boundary

## Domain

A domain owns domain context, domain architecture, ownership, core services, core integrations, core events, and frontend/backend ownership assumptions.

Example: `Cards`

## Capability

A capability owns a business function boundary and shared context for related features.

The capability folder contains:

- `capability-context.md`
- shared business flow, APIs, events, integrations, and state model when applicable
- `features/<feature>/` delivery folders

## Feature

A feature owns the AI-SDLC delivery lifecycle: intent, specification, design, test-design, implementation, pr-review, validation, release, and feedback.

Example capability and features:

```text
Cards
└── Card Lifecycle Management
    ├── Card Replacement
    ├── Card Activation
    ├── Card Renewal
    └── Card Closure
```

The AI-SDLC lifecycle runs at feature level. Domain and capability context guide the feature. Feature implementation can be delivered in smaller implementation slices. Slices are not features; they are implementation increments inside a feature.

Example:

```text
domains/cards/
└── capabilities/
    └── card-lifecycle-management/
        ├── capability-context.md
        └── features/
            └── card-replacement/
                ├── intent/intent.md
                ├── specification/specification.md
                ├── design/design.md
                ├── contracts/openapi.yaml
                ├── tests/acceptance.feature
                ├── implementation/implementation-plan.md
                ├── pr-review/pr-review-report.md
                ├── validation/validation-report.md
                ├── release/release-notes.md
                └── workflow-state.yaml
```

---

# Specification = Requirements

`specification/specification.md` contains functional requirements, non-functional requirements, acceptance criteria, business rules, and edge cases.

The framework calls this artifact `specification`, but it is equivalent to the requirements artifact in frameworks such as Kiro. Do not create a separate `requirements/` folder.

---

# Artifact Ownership

| File | Purpose | Owner |
|---|---|---|
| `domains/<domain>/domain-context.md` | Domain boundary, ownership, core services, integrations, events | Domain Owner / Solution Architect |
| `domains/<domain>/capabilities/<capability>/capability-context.md` | Capability purpose, owned features, shared flows/APIs/events/integrations | Capability Owner / Solution Architect |
| `intent/intent.md` | Why we are building this; business outcome, scope, exclusions | PO / BA |
| `specification/specification.md` | What must be built; FRs, NFRs, acceptance criteria, business rules, edge cases | BA / PO |
| `design/design.md` | Feature design; APIs, events, integrations, state model, placement metadata | Solution Architect |
| `contracts/openapi.yaml` | API contract owned by the feature/service design | Solution Architect / Developer Lead |
| `tests/acceptance.feature` | Behaviour scenarios and acceptance tests | QA / BA |
| `implementation/implementation-plan.md` | Implementation slices, target paths, technical approach, test plan | Developer Lead / Solution Architect |
| `pr-review/pr-review-report.md` | Code review findings, standards checks, path checks, approval outcome | Developer Lead / Reviewer |
| `validation/validation-report.md` | Evidence that implementation meets approved requirements | QA Lead |
| `release/release-notes.md` | Release scope, evidence, approvals, risks | Release Manager / DevSecOps |
| `workflow-state.yaml` | Current state, gates, blockers, approvals, artifact paths | Delivery Lead / AI Workflow |

---

# Framework Guidance Ownership

| File | Purpose | Owner |
|---|---|---|
| `framework/00-navigation/document-map.md` | Navigation map for framework documents | Framework Owner |
| `framework/01-lifecycle/skill-orchestration-adapter.md` | How generic skills map to this framework lifecycle, gates, workflow-state, and navigation commands | Framework Owner |
| `framework/02-context-control/context/skill-context-adapter.md` | How generic skills load context in this framework | Framework Owner |
| `framework/03-delivery-governance/artifact-placement-model.md` | Where framework artifacts are stored | Framework Owner / Delivery Lead |
| `framework/02-context-control/context/stage-context-packs.md` | Required/optional/forbidden reads by lifecycle stage | Framework Owner |
| `framework/01-lifecycle/prompt-patterns/<stage>-pattern.md` | Standard prompt shape for each stage | Framework Owner |
| `framework/01-lifecycle/workflows/skill-prerequisite-validation.md` | Rules for when a skill may proceed or must stop | Framework Owner |
| `framework/01-lifecycle/prompt-patterns/standard-response-format.md` | Standard response format for skills | Framework Owner |
| `framework/03-delivery-governance/service-architecture/implementation-placement-model.md` | Where code should go; app/service/library targeting | Solution Architect / Platform Architect |
| `framework/03-delivery-governance/multi-squad/path-governance-model.md` | Allowed/restricted paths by squad/domain | Platform Architect / Delivery Lead |
| `framework/03-delivery-governance/multi-squad/domain-ownership-model.md` | Domain and squad ownership | Delivery Lead / Domain Owner |
| `framework/03-delivery-governance/service-architecture/service-catalog-template.md` | Backend service ownership template | Solution Architect |
| `framework/03-delivery-governance/frontend/frontend-catalog-template.md` | Frontend module ownership template | Frontend Lead |
| `framework/05-platform-bootstrap/README.md` | One-time bootstrap guidance for frontend, microservice templates, shared libraries, packaging, Helm, CI/CD | Platform Architect / DevSecOps Lead |

---

# Enterprise Multi-Squad Placement

Current lab implementation may use `src/`. Enterprise delivery should place code under `apps/`, `services/`, and `libraries/` according to approved ownership and path catalogs.

Target placement must be decided during design and implementation planning before `$implementation`. The service catalog and frontend catalog remove guesswork by defining owning squads, allowed paths, restricted paths, approvers, and regression scope.

Use:

- `framework/03-delivery-governance/multi-squad/domain-ownership-model.md`
- `framework/03-delivery-governance/service-architecture/service-catalog-template.md`
- `framework/03-delivery-governance/frontend/frontend-catalog-template.md`
- `framework/03-delivery-governance/multi-squad/shared-asset-ownership-model.md`
- `framework/03-delivery-governance/service-architecture/implementation-placement-model.md`
- `framework/03-delivery-governance/service-architecture/domain-onboarding-model.md`
- `framework/03-delivery-governance/multi-squad/path-governance-model.md`
- `framework/01-lifecycle/workflows/review-approval-flow.md`

---

## Context Management

Skills are reusable procedures. The framework adapters decide repository-specific context loading, artifact placement, workflow-state updates, approval gates, and next-stage routing.

Use `framework/02-context-control/context/context-pack-model.md` and `framework/02-context-control/context/stage-context-packs.md` to keep reads stage-specific and token usage controlled. Optional lightweight indexes are defined in `framework/02-context-control/context/context-index-template.md`.

Do not load the entire `framework/` folder during normal feature delivery. Use the active skill, `workflow-state.yaml`, `framework/02-context-control/context/skill-context-adapter.md`, and the stage context pack to decide what to read.

Framework docs are a library. Context packs decide which pages are loaded for a lifecycle stage. One-time platform bootstrap docs are not loaded during normal feature work unless creating or changing baselines.

Use `framework/01-lifecycle/workflows/skill-prerequisite-validation.md` to check whether a skill may proceed before reading broad context or creating artifacts.

Use `framework/00-navigation/indexing/indexing-model.md` for lightweight navigation indexes; indexes are optional in the lab, recommended for 3+ squads, and generated/validated aids rather than sources of truth.

Use `framework/00-navigation/capability-summary/capability-summary-model.md` for optional single-page capability summaries that aid navigation without replacing source artifacts.

Use `framework/01-lifecycle/prompt-patterns/` for lightweight stage prompt patterns that improve repeatability, stop conditions, and response consistency without replacing source artifacts.

Use `framework/01-lifecycle/prompt-patterns/standard-response-format.md` for the standard skill response footer.

---

## framework/

Contains reusable framework assets.

Examples:

- `00-navigation/`: document map, indexes, and capability summary guidance.
- `01-lifecycle/`: workflow state, lifecycle workflows, review flow, and prompt patterns.
- `02-context-control/`: context packs, token discipline, and context index guidance.
- `03-delivery-governance/`: ownership, placement, frontend, service, event, and shared asset governance.
- `04-engineering-standards/`: Java-first backend, Flutter channel, API, database, event, testing, security, AI review, decomposition, reference architecture, change-management, and testing strategy standards. Start with `framework/04-engineering-standards/standards-index.md`.
- `05-platform-bootstrap/`: reserved for platform bootstrap guidance and templates.
- `06-tool-integrations/`: Jira and other tool integration guidance.
- `07-templates/`: reusable delivery artifact templates.

---

## traceability/

Contains traceability evidence.

Example:

```text
traceability/
└── traceability-matrix.md
```

---

## feedback/

Contains lessons learned and production feedback.

Example:

```text
feedback/
└── feedback-log.md
```

---

# Lifecycle

Every feature follows the same lifecycle.

```text
Intent
→ Specification
→ Design
→ Test Design
→ Implementation
→ PR Review
→ Validation
→ Release
→ Feedback
```

---

# Commands

| Command | Purpose |
|----------|----------|
| $domain-onboarding | Create new domain context before capability creation |
| $intent | Create or update feature intent |
| $change-request | Create change request |
| $defect-fix | Create defect fix |
| $decision | Create or review architecture decisions and ADRs |
| Status. | Navigate current workflow state and next action |
| Review. | Run quality review |
| Approved. | Approve current stage |
| $specification | Create or update specification |
| $design | Create or update design |
| $test-design | Create or update test design |
| $implementation | Create or update implementation |
| $pr-review | Review implementation changes before validation |
| $validation | Execute validation |
| $release | Prepare release |
| $traceability-review | Verify traceability |
| $feedback-capture | Capture lessons learned |
| $capability-onboarding | Create or update capability context under an existing domain |
| $source-ingestion | Convert external source material into AI-readable summaries |
| $repo-discovery | Extract repository standards and conventions |
| $artifact-review | Review AI-generated artifacts before human approval |
| $wynxx-backlog-ingestion | Ingest Wynxx Story Creator backlogs into reviewable AI SDLC candidate inputs |

## Support Skills

These skills support the lifecycle but are not lifecycle stages:

- `$capability-onboarding` for creating or updating capability context under an existing domain.
- `$source-ingestion` for converting external source material into AI-readable summaries.
- `$repo-discovery` for extracting standards and conventions from an existing repository.
- `$artifact-review` for reviewing AI-generated artifacts before human approval.
- `$wynxx-backlog-ingestion` for ingesting Wynxx Story Creator backlogs into candidate intent, specification, implementation slice, and test design inputs without making Wynxx the source of truth.

---

## PR Review

Use `$pr-review` after implementation and before `$validation`. PR review checks changed files, `allowed_paths`, coding standards, design adherence, API/event compatibility, test coverage, validation scripts, and traceability. It can recommend readiness, changes, or blockers, but human PR approval remains mandatory.

Intent, specification, design, test-design, validation, and release are feature-level. Implementation may be delivered in one or more slices. PR review is normally per slice or PR. Feature validation and release happen after required slices are complete.

---

# Status Command

## Purpose

```text
Status.
```

`Status.` is the main navigation command. Use it to understand where the active feature is, whether work can continue, and what command should be run next.

Status output must show:

- domain
- capability
- feature
- current_state
- current_skill
- active artifact
- pending gate
- required approvers
- blockers
- next command
- whether code changes are allowed
- whether release is blocked
- validation consistency status

If `workflow-state.yaml`, validation report, release notes, or traceability disagree, `Status.` must report the inconsistency and must not recommend moving forward.

Example:

```text
Domain: cards
Capability: Card Lifecycle Management
Feature: Card Replacement
Current State: intent_review
Current Skill: $intent
Active Artifact: domains/cards/capabilities/card-lifecycle-management/features/card-replacement/intent/intent.md
Pending Gate: intent_approval
Required Approvers: Product Owner, Business Analyst
Blockers: none
Code Changes Allowed: no
Release Blocked: not applicable
Validation Consistency: not applicable
Next Command: Review.
```

When blocked:

```text
Blockers:
- validation report says release is not ready
- release notes are missing

Next Command: Resolve findings.
```

---

# Review Command

## Purpose

```text
Review.
```

Runs a quality review of the current artifact.

Review checks:

- Completeness
- Correctness
- Traceability
- Standards compliance
- Missing requirements
- Missing validations
- Approval readiness

Example:

```text
$specification

Review.
```

Possible output:

```text
Finding 1:
Missing acceptance criteria

Finding 2:
Missing NFR

Recommendation:
Changes Required
```

Review does not approve anything.

Review does not advance workflow state.

---

# Approved Command

## Purpose

```text
Approved.
```

Confirms that a human accepts the current artifact.

Only humans approve.

AI may recommend approval but cannot approve itself.

Example:

```text
Review completed.

Approved.
```

When approved:

- Workflow state advances
- Next skill becomes active
- Delivery can continue

---

# Workflow State

Every feature contains:

```text
workflow-state.yaml
```

This file controls delivery progress.

Example:

```yaml
current_skill: specification

current_state: specification_draft

next_skill: design
```

After approval:

```yaml
current_skill: design

current_state: specification_approved

next_skill: design
```

---

# Intent Workflow

```text
$intent

Review.
Approved.

$specification

Review.
Approved.

$design

Review.
Approved.

$test-design

Review.
Approved.

$implementation

Review.
Approved.

$pr-review

Review.
Approved.

$validation

Review.
Approved.

$release

Approved.

$feedback-capture
```

---

# Change Request Workflow

```text
$change-request

Review.
Approved.

$specification

Review.
Approved.

$design

Review.
Approved.

$implementation

Review.
Approved.

$validation

Review.
Approved.

$release
```

Only impacted artifacts are updated.

Do not regenerate the entire solution.

---

# Defect Fix Workflow

```text
$defect-fix

Review.
Approved.

Root Cause Analysis

Review.
Approved.

$implementation

Review.
Approved.

$validation

Review.
Approved.

$release
```

Only impacted artifacts are updated.

---

# Validation

Run validations:

```bash
bash scripts/validate-workflow-state.sh
bash scripts/validate-workflow-consistency.sh
bash scripts/validate-artifacts.sh
bash scripts/validate-traceability.sh
bash scripts/validate-release-readiness.sh
bash scripts/validate-openapi.sh
bash scripts/validate-java.sh
```

Expected result:

```text
All validations passed
```

---

# GitHub Actions

Current capabilities:

- Workflow state validation
- Workflow consistency validation
- Artifact validation
- Traceability validation
- Release readiness validation
- OpenAPI validation
- Java compilation
- Test execution
- Optional Sonar scan and quality gate when non-placeholder `sonar-project.properties` and `SONAR_TOKEN` are available

Workflow:

```text
.github/workflows/ai-sdlc-validate.yml
```

---

# MCP Demo Integrations

MCP setup for Wynxx, Jira, Confluence, and GitHub is documented in:

```text
framework/06-tool-integrations/mcp-integration-setup.md
```

Token-efficient MCP specialist subagent routing is documented in:

```text
framework/06-tool-integrations/mcp-subagent-architecture.md
```

Read-only MCP subagent smoke tests are documented in:

```text
framework/06-tool-integrations/mcp-subagent-smoke-tests.md
```

To print manual smoke-test prompts:

```bash
bash scripts/smoke-test-mcp-subagents.sh
```

Use `.env.mcp.example` as the token-free environment template.

Rules:

- Git remains source of truth.
- Wynxx is backlog candidate ingestion only.
- Jira is workflow tracking.
- Confluence is published documentation.
- GitHub is repository, PR, validation, and release evidence.
- Start with read-only validation and enable writes only after explicit approval.

---

# REST / CLI Demo Integrations

Demo execution uses explicit REST/CLI adapters while MCP remains a later spike.

Locations:

```text
framework/06-tool-integrations/demo-rest-cli-adapter-plan.md
scripts/jira/rest_cli.py
scripts/confluence/rest_cli.py
scripts/github/evidence.py
```

Purpose:

- Validate Jira connectivity and project access.
- Create a demo Jira story from an approved intent.
- Add Git and Confluence remote links to Jira.
- Transition Jira status through explicit approvals.
- Validate Confluence space access.
- Publish approved Git artifact pages to Confluence.
- Update Confluence pages by title.
- Read GitHub Actions workflow history and the latest validation result.

Rules:

- Git remains source of truth.
- Jira and Confluence are synchronized views.
- Use environment variables only.
- Write operations require `--apply`.
- Do not create real Jira tickets or Confluence pages without explicit approval.

---

# Jira Integration

Current state:

REST/CLI demo adapters, plus offline payload generation.

Location:

```text
scripts/jira/
```

Purpose:

Generate:

- Epics for capabilities
- Stories for features
- Tasks for implementation slices
- Optional Sub-tasks for engineering tasks
- Defects
- Decisions
- Releases

Payloads link back to Git-owned domain context, capability context, workflow state, intent, specification, design, tests, implementation plan, validation report, and release notes where available.

Future:

- Jira automation via explicit REST adapter write mode
- Workflow synchronization

---

# Confluence Integration

Current state:

REST/CLI demo adapters, plus offline summary generation.

Location:

```text
scripts/confluence/
```

Purpose:

Generate:

- Capability summaries
- Feature summaries
- Design summaries
- Validation summaries
- Release summaries

Future:

- Confluence automation via explicit REST adapter write mode

---

# GitHub Actions Evidence

Current state:

CLI-based evidence retrieval.

Location:

```text
scripts/github/
```

Purpose:

- List latest workflow runs.
- Read latest validation result.

Future:

- Expand workflow evidence reporting if required by portal or release tooling

---

# Control Tower Dashboard

Current state:

Static read-only dashboard generated from Git-owned artifacts.

Locations:

```text
framework/07-control-tower/control-tower-data-model.md
scripts/dashboard/
dashboard/control-tower.html
dashboard/control-tower.css
dashboard/control-tower.js
build/dashboard/control-tower.json
```

Purpose:

- Show feature status, approval gates, traceability, and quality gates.
- Surface Jira and Confluence references where traceability provides them.
- Highlight PM intervention indicators without changing workflow state.
- Present GitHub validation evidence from local repository artifacts.

Usage:

```bash
bash scripts/dashboard/run-control-tower.sh
```

Rules:

- Read-only only.
- Git remains source of truth.
- Jira and Confluence remain synchronized views.
- No approvals, ticket updates, or page updates from the dashboard.

---

# Definition of Ready (DoR)

Before implementation:

- Intent approved
- Specification approved
- Design approved
- API contract approved
- Test design approved
- Traceability reviewed
- Required approvals completed

---

# Definition of Done (DoD)

Before release:

- Implementation completed
- Tests passed
- Validation completed
- Traceability updated
- Documentation updated
- Review completed
- Approval completed

---

# First Exercise

Review the sample capability:

```text
domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/
```

Run:

```text
Status.
```

Review:

```text
intent/
specification/
design/
contracts/
tests/
implementation/
pr-review/
validation/
release/
workflow-state.yaml
```

Run validations:

```bash
bash scripts/validate-workflow-state.sh
bash scripts/validate-artifacts.sh
bash scripts/validate-traceability.sh
bash scripts/validate-openapi.sh
bash scripts/validate-java.sh
```

This is the recommended starting point for all new users.

---

# Golden Rules

1. Git is the source of truth.
2. Jira manages workflow and approvals.
3. Confluence publishes stakeholder summaries.
4. Do not generate code before approvals.
5. Do not regenerate entire solutions for changes.
6. Keep changes small and traceable.
7. Human approvals are mandatory.
8. AI assists delivery but does not replace governance.
9. Every requirement must trace to implementation and validation.
10. Continuous validation is required before release.
11. Do not write code outside implementation-plan `allowed_paths`.
12. Do not modify shared libraries, events, platform code, or another squad's app/service without owner approval.
