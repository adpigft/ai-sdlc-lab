# Integration Foundation

## Purpose

This foundation defines how GitHub Actions, Jira, Confluence, and Sonar support the AI SDLC framework without changing lifecycle order, skills, artifact ownership, or source-of-truth rules.

Git remains the source of truth for framework guidance, delivery artifacts, traceability, validation, release evidence, and source code. Integrations publish, track, or enforce evidence that originates in Git.

## System Responsibilities

| System | Responsibility | Not Responsible For |
| --- | --- | --- |
| GitHub Actions | Run validation scripts, contract checks, build/test checks, and optional Sonar quality evidence on pull requests and protected branches. | Replacing human approvals or rewriting delivery artifacts. |
| Jira | Track workflow, ownership, blockers, approvals, sprint planning, implementation slices, defects, decisions, and releases. | Storing canonical requirements, design, tests, validation evidence, or release notes. |
| Confluence | Publish stakeholder-facing summaries generated from Git-owned artifacts. | Becoming the source of truth for capability or feature delivery artifacts. |
| Sonar | Provide code quality and security evidence when code and project configuration are available. | Approving architecture, business behavior, release readiness, or lifecycle progression. |

## GitHub Actions Foundation

The canonical validation workflow is `.github/workflows/ai-sdlc-validate.yml`.

It must run:

- `scripts/validate-workflow-state.sh`
- `scripts/validate-artifacts.sh`
- `scripts/validate-traceability.sh`
- `scripts/validate-openapi.sh`
- `scripts/validate-java.sh`
- `scripts/validate-release-readiness.sh`
- `scripts/validate-workflow-consistency.sh`

When a non-placeholder `sonar-project.properties` and `SONAR_TOKEN` are available, the workflow runs Sonar scan and quality gate steps. If Sonar is not configured for a run, the workflow reports the skip rather than failing framework validation.

## Jira Foundation

Jira issue hierarchy:

```text
Epic = Capability
Story = Feature
Task = Implementation Slice
Sub-task = optional engineering task
```

Jira payloads are generated offline by `scripts/jira/generate-jira-payloads.py`. The generator does not call Jira APIs.

Payloads must link to Git-owned source artifacts when available:

- `domain-context.md`
- `capability-context.md`
- `workflow-state.yaml`
- `intent/intent.md`
- `specification/specification.md`
- `design/design.md`
- `tests/acceptance.feature`
- `implementation/implementation-plan.md`
- `validation/validation-report.md`
- `release/release-notes.md`

## Confluence Foundation

Confluence summaries are generated offline by `scripts/confluence/generate-summary.py`. The generator does not call Confluence APIs.

Generated stakeholder summaries:

- capability summary
- feature summary
- design summary
- validation summary
- release summary

Each summary must identify itself as a published view and link back to Git-owned source artifacts.

## Sonar Foundation

Sonar is quality and security evidence for code-bearing changes. The baseline configuration is `sonar-project.properties`.

Sonar evidence should be used by `$pr-review`, `$validation`, and `$release` when code exists and the project has an approved Sonar organization, project key, token, and quality profile. Sonar does not override failed GitHub Actions checks, missing traceability, or missing human approvals.

## Guardrails

- Do not change lifecycle order through integration automation.
- Do not add skills for integration mechanics.
- Do not modify business domain artifacts only to satisfy Jira or Confluence publishing.
- Do not let Jira, Confluence, or Sonar override Git-owned artifacts.
- Do not store secrets, credentials, customer data, or production-sensitive evidence in generated payloads or summaries.
