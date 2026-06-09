# Integration Configuration Guide

## Purpose

This guide defines the configuration values required before enabling Jira, Confluence, GitHub Actions, and Sonar integrations for the AI SDLC framework.

It does not implement API calls, enable write mode, change lifecycle order, or add skills. Git remains the source of truth. Jira and Confluence are synchronized views. GitHub Actions enforces validation. Sonar provides code quality and security evidence.

## Configuration Principles

- Store secrets only in the approved secret store for the runtime, such as GitHub Actions secrets or a managed CI secret vault.
- Store non-secret environment values in repository variables, CI variables, or local shell environment.
- Do not commit tokens, passwords, API keys, customer data, or production-sensitive evidence.
- Keep API write mode disabled until generated payloads and summaries are reviewed against Git-owned artifacts.
- Treat generated Jira payloads and Confluence summaries as drafts until a human approves publishing.

## Jira Configuration

### Required Secrets

| Secret | Purpose |
| --- | --- |
| `JIRA_API_TOKEN` | API token or OAuth client secret for future Jira API calls. |
| `JIRA_USER_EMAIL` | Service account email when the Jira API requires basic auth style credentials. |

Use a dedicated service account with least privilege. Do not use a personal administrator token.

### Required Environment Variables

| Variable | Purpose | Example |
| --- | --- | --- |
| `JIRA_BASE_URL` | Jira site URL. | `https://example-bank.atlassian.net` |
| `JIRA_PROJECT_KEY` | Target project key for generated issues. | `PAY` |
| `JIRA_DEFAULT_ISSUE_SECURITY` | Optional issue security level for generated work items. | `Internal Delivery` |
| `JIRA_WRITE_MODE` | Must remain disabled until API publishing is approved. | `disabled` |

### Required Jira Mappings

| AI SDLC Concept | Jira Mapping |
| --- | --- |
| Capability | Epic |
| Feature | Story |
| Implementation Slice | Task |
| Optional engineering work | Sub-task |
| Defect / RCA finding | Defect |
| Architecture or delivery decision | Decision |
| Release package | Release or change issue type |

Required fields or custom-field mappings:

- Domain name
- Capability ID
- Feature ID
- Workflow state
- Workflow skill
- Parent Epic key
- Parent Story key for Tasks
- Parent Task key for Sub-tasks
- Requirement IDs
- Acceptance scenario IDs
- Implementation slice IDs
- Git source artifact links
- Approval reference
- Blocker status
- Release readiness status

Required source links on payloads:

- `domain-context.md`
- `capability-context.md`
- `workflow-state.yaml`
- `intent/intent.md`
- `requirements/requirements.md`
- `design/design.md`
- `tests/acceptance.feature`
- `implementation/implementation-plan.md`
- `validation/validation-report.md`
- `release/release-notes.md`

## Confluence Configuration

### Required Secrets

| Secret | Purpose |
| --- | --- |
| `CONFLUENCE_API_TOKEN` | API token or OAuth client secret for future Confluence publishing. |
| `CONFLUENCE_USER_EMAIL` | Service account email when the Confluence API requires basic auth style credentials. |

Use a service account with permission only to the approved AI SDLC publishing space.

### Required Environment Variables

| Variable | Purpose | Example |
| --- | --- | --- |
| `CONFLUENCE_BASE_URL` | Confluence site URL. | `https://example-bank.atlassian.net/wiki` |
| `CONFLUENCE_SPACE_KEY` | Publishing space key. | `AISDLC` |
| `CONFLUENCE_PARENT_PAGE_ID` | Parent page for generated summaries. | `123456789` |
| `CONFLUENCE_WRITE_MODE` | Must remain disabled until API publishing is approved. | `disabled` |

### Required Confluence Page Structure

Recommended structure:

```text
AI SDLC
└── Domains
    └── <Domain>
        └── Capabilities
            └── <Capability>
                ├── Capability Summary
                └── Features
                    └── <Feature>
                        ├── Feature Summary
                        ├── Design Summary
                        ├── Validation Summary
                        └── Release Summary
```

Each generated page must:

- State that it is a published view only.
- Link back to Git-owned source artifacts.
- Include the Jira Epic or Story reference when available.
- Avoid becoming the canonical source for requirements, design, tests, validation, or release evidence.
- Avoid storing secrets, credentials, sensitive customer data, or production incident details.

## GitHub Actions Configuration

### Required Secrets

| Secret | Purpose |
| --- | --- |
| `SONAR_TOKEN` | Runs Sonar scan and quality gate when Sonar configuration is non-placeholder. |
| `JIRA_API_TOKEN` | Reserved for future Jira publishing workflows. Keep unused until write mode is approved. |
| `CONFLUENCE_API_TOKEN` | Reserved for future Confluence publishing workflows. Keep unused until write mode is approved. |

### Required Repository Variables

| Variable | Purpose |
| --- | --- |
| `JIRA_BASE_URL` | Future Jira API target. |
| `JIRA_PROJECT_KEY` | Future Jira project target. |
| `CONFLUENCE_BASE_URL` | Future Confluence API target. |
| `CONFLUENCE_SPACE_KEY` | Future Confluence publishing space. |
| `SONAR_ORGANIZATION` | Sonar organization when project configuration is finalized. |
| `SONAR_PROJECT_KEY` | Sonar project key when project configuration is finalized. |

### Required Workflows

`.github/workflows/ai-sdlc-validate.yml` must run:

- `scripts/validate-workflow-state.sh`
- `scripts/validate-artifacts.sh`
- `scripts/validate-traceability.sh`
- `scripts/validate-openapi.sh`
- `scripts/validate-java.sh`
- `scripts/validate-release-readiness.sh`
- `scripts/validate-workflow-consistency.sh`
- Sonar scan and quality gate when non-placeholder Sonar configuration and `SONAR_TOKEN` are available

### Branch Protection Rules

Protect `main` with:

- Require pull request before merge.
- Require at least one approving review.
- Require review from CODEOWNERS when CODEOWNERS is adopted.
- Require status checks from `AI SDLC Validation`.
- Require branch to be up to date before merge.
- Block force pushes.
- Block deletion.
- Restrict who can bypass required pull requests and status checks.
- Require conversation resolution before merge.

Recommended for regulated delivery:

- Require signed commits or verified provenance where supported.
- Require security review for changes affecting `.github/workflows/`, `scripts/`, `framework/`, authentication, authorization, payment movement, ledger, audit, or release paths.
- Require administrator enforcement unless the platform team has an approved emergency process.

## Sonar Configuration

### Required Secrets

| Secret | Purpose |
| --- | --- |
| `SONAR_TOKEN` | Authenticates Sonar scan and quality gate actions. |

### Required Environment Variables Or Properties

Sonar can be configured through `sonar-project.properties` and CI variables.

Required values:

- `sonar.organization`
- `sonar.projectKey`
- `sonar.projectName`
- `sonar.sources`
- `sonar.exclusions`
- `sonar.sourceEncoding`

Add language-specific values when application code and test tooling are approved:

- Java binaries path
- Java test binaries path
- coverage report paths
- test report paths
- source exclusions
- coverage exclusions

Do not enable quality-gate enforcement until the placeholder organization and project key are replaced with approved project values.

## Running Generators Locally

Generate Jira payload drafts:

```bash
python3 scripts/jira/generate-jira-payloads.py \
  --workflow-state domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/workflow-state.yaml \
  --output-dir /tmp/jira-payloads
```

Print Jira payload drafts to stdout:

```bash
python3 scripts/jira/generate-jira-payloads.py \
  --workflow-state domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/workflow-state.yaml
```

Generate Confluence summary drafts:

```bash
python3 scripts/confluence/generate-summary.py \
  --workflow-state domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/workflow-state.yaml \
  --output-dir /tmp/confluence-summaries
```

Print Confluence summary drafts to stdout:

```bash
python3 scripts/confluence/generate-summary.py \
  --workflow-state domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/workflow-state.yaml
```

Review generated files before any future publisher sends data to external systems.

## Validation Before API Write Mode

Before enabling Jira or Confluence API write mode:

1. Confirm `JIRA_WRITE_MODE=disabled` and `CONFLUENCE_WRITE_MODE=disabled` while validating configuration.
2. Generate Jira payloads and Confluence summaries locally.
3. Review generated output for correct parent-child mapping, source artifact links, page placement, labels, and missing values.
4. Confirm generated output contains no secrets, credentials, customer data, or sensitive operational details.
5. Run local validations:

```bash
git diff --check
bash scripts/validate-workflow-state.sh
bash scripts/validate-artifacts.sh
bash scripts/validate-traceability.sh
bash scripts/validate-openapi.sh
bash scripts/validate-java.sh
bash scripts/validate-release-readiness.sh
bash scripts/validate-workflow-consistency.sh
```

6. Confirm GitHub Actions validation passes on a pull request.
7. Confirm Sonar scan and quality gate pass if Sonar is enabled for the project.
8. Obtain approval from the framework owner, DevSecOps owner, and affected delivery owners.
9. Enable API write mode only through a separate approved change that adds the publisher, dry-run evidence, rollback behavior, audit logging, and failure handling.

API write mode must not be enabled by changing generator scripts alone.

## Readiness Checklist

| Area | Ready When |
| --- | --- |
| Jira | Service account, project key, issue type mappings, custom fields, parent-child rules, and disabled write mode are configured. |
| Confluence | Service account, space key, parent page, page structure, and disabled write mode are configured. |
| GitHub Actions | Required validation workflow and branch protection are active. |
| Sonar | Non-placeholder project configuration, token, and quality gate are approved. |
| Evidence | Local generators, local validations, pull request checks, and human review all pass. |
