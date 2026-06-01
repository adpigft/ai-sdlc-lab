# AI SDLC Operating Model

## Purpose

This page is the Confluence-ready operating model for AI-assisted software delivery in this repository. The repository remains the versioned source of truth; Confluence is the stakeholder-facing publication channel.

## Lifecycle

| Stage | Primary Artifact | Human Gate | System Of Record |
| --- | --- | --- | --- |
| Intent | Intent document | Product owner approval | Jira and repository |
| Specification | Spec, context, API contract | Product, architecture, QA, security review | Jira and repository |
| Build readiness | Implementation plan and story breakdown | Engineering approval | Jira |
| Validation | Test evidence and validation report | QA and risk review | GitHub, SonarCloud, Jira, repository |
| Release | Release notes and change record | Release approval | Jira or change system |
| Feedback | Feedback log and backlog updates | Triage owner decision | Jira and repository |

## Source Of Truth

- Jira owns work status, assignment, approvals, and backlog state.
- This repository owns versioned SDLC artifacts, templates, standards, workflows, traceability, and ADRs.
- GitHub owns pull requests, reviews, commits, and CI evidence.
- SonarCloud owns static analysis and quality gate evidence.
- Confluence publishes approved operating-model content for broader consumption.

## AI Responsibilities

AI may:

- Draft intent, specs, tests, review notes, and release notes.
- Compare artifacts for inconsistency.
- Suggest missing acceptance criteria, risks, and tests.
- Summarize Jira, GitHub, validation, and feedback evidence when supplied.

AI must not:

- Approve scope, risk, architecture, security exceptions, or release.
- Invent evidence, Jira approvals, test results, or SonarCloud outcomes.
- Handle production customer data, secrets, credentials, or private keys in prompts.
- Add application code before build readiness is approved.

## Human Gates

Human approval is required for:

- Product intent approval.
- Specification approval.
- Architecture decisions and ADRs.
- Security risk acceptance.
- Build readiness.
- Pull request review.
- Release approval.
- Post-release risk or incident closure.

## Tooling Model

| Tool | Role |
| --- | --- |
| Jira | Epics, stories, defects, risks, approvals, release scope |
| Confluence | Stakeholder publication of approved operating model and release summaries |
| GitHub | Repository, pull requests, code review, branch protection, CI evidence |
| GitHub Actions | Automated checks for tests, quality, security, traceability, and release evidence |
| SonarCloud | Static analysis, maintainability, reliability, security, coverage, quality gate |

## Payment Example

For KHQR payment initiation, the SDLC must prove:

- The customer can initiate a valid payment.
- Duplicate submissions cannot create duplicate payments.
- Pending, failed, rejected, and completed states are visible and reconcilable.
- Sensitive customer and transaction data is protected.
- Operational teams can monitor, support, and reconcile the flow.
- Release evidence links Jira, GitHub Actions, SonarCloud, validation, and release notes.

## Audit Expectations

An auditor should be able to start from a Jira epic and locate:

- Business intent.
- Approved specification.
- Architecture and risk decisions.
- API contract.
- Test evidence.
- Pull request and review evidence.
- SonarCloud quality gate result.
- Release approval.
- Feedback and post-release actions.
