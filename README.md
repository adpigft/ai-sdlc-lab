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

1. Specifications are the primary delivery artifact.
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
├── events
├── frontend
├── jira
├── libraries
├── multi-squad
├── service-architecture
├── standards
├── templates
├── workflow
├── workflow-state
└── workflows
```

---

# Key Folders

## domains/

Contains business delivery artifacts.

Example:

```text
domains/
└── payments/
    └── capabilities/
        └── khqr-payment-reversal/
```

Each capability contains:

```text
intent/
specs/
context/
contracts/
tests/
design/
validation/
release/
workflow-state.yaml
```

---

## src/

Contains executable source code.

Example:

```text
src/main/java/
src/test/java/
```

Source code is created only after specifications, architecture, tests, traceability, and implementation slice approval are complete.

---

# Enterprise Multi-Squad Placement

Current lab implementation may use `src/`. Enterprise delivery should place code under `apps/`, `services/`, and `libraries/` according to approved ownership and path catalogs.

Target placement must be decided during architecture and implementation planning before `$implementation`. The service catalog and frontend catalog remove guesswork by defining owning squads, allowed paths, restricted paths, approvers, and regression scope.

Use:

- `framework/multi-squad/domain-ownership-model.md`
- `framework/service-architecture/service-catalog-template.md`
- `framework/frontend/frontend-catalog-template.md`
- `framework/multi-squad/shared-asset-ownership-model.md`
- `framework/service-architecture/implementation-placement-model.md`
- `framework/service-architecture/domain-onboarding-model.md`
- `framework/multi-squad/path-governance-model.md`
- `framework/workflows/review-approval-flow.md`

---

## Context Management

Use `framework/context/context-pack-model.md` and `framework/context/stage-context-packs.md` to keep reads stage-specific and token usage controlled. Optional lightweight indexes are defined in `framework/context/context-index-template.md`.

Use `framework/indexing/indexing-model.md` for lightweight navigation indexes; indexes are optional in the lab, recommended for 3+ squads, and generated/validated aids rather than sources of truth.

Use `framework/prompt-patterns/` for lightweight stage prompt patterns that improve repeatability, stop conditions, and response consistency without replacing source artifacts.

---

## framework/

Contains reusable framework assets.

Examples:

- Standards
- Templates
- Event definitions
- Frontend standards
- Service architecture patterns
- Jira integration patterns
- Workflow definitions

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

Every capability follows the same lifecycle.

```text
Intent
→ Specification
→ Architecture
→ Test Design
→ Implementation
→ Validation
→ Release
→ Feedback
```

---

# Commands

| Command | Purpose |
|----------|----------|
| $domain-onboarding | Create new domain context before capability creation |
| $new | Create new capability |
| $change-request | Create change request |
| $defect-fix | Create defect fix |
| Status. | Navigate current workflow state and next action |
| Review. | Run quality review |
| Approved. | Approve current stage |
| $specification | Create or update specification |
| $architecture | Create or update architecture |
| $test-design | Create or update test design |
| $implementation | Create or update implementation |
| $validation | Execute validation |
| $release | Prepare release |
| $traceability-review | Verify traceability |
| $feedback-capture | Capture lessons learned |

---

# Status Command

## Purpose

```text
Status.
```

`Status.` is the main navigation command. Use it to understand where the active capability is, whether work can continue, and what command should be run next.

Status output must show:

- domain
- capability
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
Capability: Card Replacement
Current State: intent_review
Current Skill: $new
Active Artifact: domains/cards/capabilities/card-replacement/intent/intent.md
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

Every capability contains:

```text
workflow-state.yaml
```

This file controls delivery progress.

Example:

```yaml
current_skill: specification

current_state: specification_draft

next_skill: architecture
```

After approval:

```yaml
current_skill: architecture

current_state: specification_approved

next_skill: architecture
```

---

# New Capability Workflow

```text
$new

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

$architecture

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

Workflow:

```text
.github/workflows/ai-sdlc-validate.yml
```

---

# Jira Integration

Current state:

Offline payload generation.

Location:

```text
scripts/jira/
```

Purpose:

Generate:

- Epics
- Stories
- Tasks
- Defects
- Decisions
- Releases

Future:

- Jira API integration
- Automatic ticket creation
- Workflow synchronization

---

# Confluence Integration

Current state:

Offline summary generation.

Location:

```text
scripts/confluence/
```

Purpose:

Generate:

- Capability summaries
- Architecture summaries
- Validation summaries
- Release summaries

Future:

- Confluence API publishing

---

# Definition of Ready (DoR)

Before implementation:

- Intent approved
- Specification approved
- Architecture approved
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
domains/payments/capabilities/khqr-payment-reversal/
```

Run:

```text
Status.
```

Review:

```text
intent/
specs/
context/
contracts/
tests/
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
