# AI SDLC Portal MVP

## Purpose

The AI SDLC Portal MVP provides a lightweight GUI for viewing framework status, editing Git-owned framework artifacts, and approving lifecycle stages while keeping Git as the source of truth.

The portal is a workflow interface over Git, not a replacement repository, document store, Jira workflow, Confluence publishing space, or lifecycle engine. Every material edit and approval must create a Git commit or pull request and must remain reviewable through normal Git history and GitHub Actions validation.

## User Roles

| Role | Portal Responsibility |
| --- | --- |
| Product Owner | Review intent, business scope, exclusions, success measures, and approve business gates. |
| Business Analyst | Edit and review intent, specification, acceptance criteria, business rules, and open questions. |
| Solution Architect | Review and approve design, API, event, integration, placement, and architecture decisions. |
| QA Lead | Review and approve test design, validation evidence, defects, and release-quality recommendations. |
| Developer Lead | Review implementation plans, code-impact summaries, PR evidence, and technical readiness. |
| DevSecOps / Platform | Review CI/CD, quality gates, release evidence, branch protection, Sonar, and operational readiness. |
| Delivery Lead | Monitor workflow state, blockers, approvals, traceability, and cross-tool synchronization. |
| Read-only Stakeholder | View current Git-backed status and published summaries without editing or approving. |

Role permissions in the portal must map to repository permissions and approval expectations. The portal must not grant approval authority that the repository, branch protection, or organization policy does not grant.

## Authentication Approach

MVP authentication should use the enterprise identity provider through OIDC.

Authentication requirements:

- Use OIDC single sign-on for portal access.
- Map identity claims to portal roles and GitHub organization or repository permissions.
- Require GitHub identity linkage for users who create commits, branches, pull requests, or approvals.
- Use least-privilege service credentials for GitHub API access.
- Store tokens only in approved secret storage.
- Use short-lived user sessions.
- Record actor identity in portal audit logs and Git commit metadata where applicable.

Authorization requirements:

- Read access allows viewing Git-backed artifacts and workflow state.
- Edit access allows proposing changes through branches or pull requests.
- Approval access is role-bound and stage-bound.
- Administrative access is limited to portal configuration, integration setup, and permission mapping.

## Screens

| Screen | Purpose |
| --- | --- |
| Dashboard | Show domains, capabilities, features, workflow stage, blockers, pending approvals, validation status, and recent Git activity. |
| Domain / Capability Explorer | Browse Git-owned domain, capability, and feature artifacts by hierarchy. |
| Feature Workspace | Show current feature lifecycle artifacts, workflow-state summary, traceability links, Jira references, Confluence summaries, and validation evidence. |
| Artifact Editor | Edit markdown, YAML, OpenAPI, test, release, and traceability artifacts with diff preview before saving. |
| Approval Center | Show pending approvals by stage, approver role, required evidence, validation status, and approval history. |
| Validation Results | Show latest local or GitHub Actions validation results, failed checks, and links to logs. |
| Control Tower Dashboard | Show read-only feature status, approval gates, traceability, quality gates, Jira links, Confluence links, and GitHub validation evidence from Git-owned artifacts. |
| Git Activity | Show commits, branches, pull requests, file diffs, merge status, and branch protection state. |
| Integration Status | Show GitHub, Jira, Confluence, Sonar, and Wynxx synchronization status and last generated payloads or summaries. |
| Backlog Ingestion | Show Wynxx storycreator-imported backlog candidates and allow conversion into Git-backed discovery inputs after human review. |
| Settings | Configure repositories, branch model, role mappings, integration endpoints, write-mode flags, and template locations. |

## Artifact Edit Workflow

All artifact edits must be Git-backed.

1. User opens a Git-owned artifact from the portal.
2. Portal loads the current branch version and records the source commit SHA.
3. User edits the artifact through a structured editor or markdown/YAML editor.
4. Portal shows a diff preview before save.
5. Portal checks whether the source commit SHA is still current.
6. If the file changed remotely, portal stops and requires the user to rebase, reload, or manually merge.
7. User saves the proposal.
8. Portal creates either:
   - a direct commit only where branch policy allows it, or
   - a branch and pull request where review or protected branch policy applies.
9. Portal triggers or links GitHub Actions validation.
10. Merge occurs only after required checks and reviews pass.

No silent overwrite is allowed. The portal must never write a file without showing the diff and verifying the base commit.

## Git Traceability Model

Git remains the source of truth for:

- framework standards
- lifecycle artifacts
- workflow-state files
- traceability matrix
- feedback log
- decisions
- validation evidence
- release notes
- source code

Portal traceability records must link:

- actor identity
- Git commit SHA
- branch or pull request
- changed artifact paths
- workflow stage
- requirement, design, test, validation, or release IDs where available
- Jira issue key where available
- Confluence page reference where available
- validation run URL where available
- approval decision where applicable

The portal may maintain an index or cache for performance, but cached data must be rebuildable from Git and must not become the source of truth.

## Approval Workflow

All approvals must update `workflow-state.yaml` and commit evidence.

Approval flow:

1. Portal displays the active stage, required approval role, source artifact, validation status, and open blockers.
2. Approver reviews the Git-backed artifact and diff.
3. Approver chooses Approve, Request Changes, or Block.
4. Portal updates `workflow-state.yaml` with approval reference, actor, timestamp, decision, and notes.
5. Portal creates a commit or pull request containing the workflow-state update.
6. GitHub Actions validates the repository state.
7. Approval is considered effective only after the workflow-state update is committed to the approved branch or merged through the required PR path.

The portal must not treat a button click as approval unless the Git evidence exists.

## Integration Model With GitHub, Jira, Confluence, Wynxx

| Integration | MVP Responsibility | Source-of-Truth Rule |
| --- | --- | --- |
| GitHub | Read and write Git artifacts, create branches and PRs, show commits, trigger or link Actions, enforce branch protection. | GitHub repository content and history are authoritative. |
| Jira | Display linked Epic, Story, Task, Sub-task, status, blockers, and approvals; generate or preview Jira payloads where configured. | Jira is workflow tracking, not the canonical source for artifacts. |
| Confluence | Display generated stakeholder summaries and publishing status. | Confluence is a synchronized publishing view, not the canonical source for artifacts. |
| Sonar | Display quality gate and security evidence for code-bearing changes. | Sonar is quality/security evidence, not approval authority. |
| Wynxx storycreator | Ingest backlog/story candidates and show source context for human review. | Wynxx storycreator is backlog ingestion only, not source of truth for requirements or artifacts. |

Synchronization rules:

- Git-to-Jira synchronization can update workflow tracking fields and links.
- Git-to-Confluence synchronization can publish reviewed summaries.
- Wynxx-to-portal ingestion creates draft backlog candidates only.
- Draft backlog candidates become Git-owned only after human review and a committed artifact or approved discovery record.
- Failed synchronization must be visible and retryable.
- No external system may silently overwrite Git-owned artifacts.

## MVP Architecture

```text
Browser
  |
  v
AI SDLC Portal Web UI
  |
  v
Portal Backend API
  |-- Auth Adapter -> Enterprise OIDC
  |-- Git Adapter -> GitHub Repository / Pull Requests / Actions
  |-- Artifact Service -> Markdown, YAML, OpenAPI, traceability readers/writers
  |-- Approval Service -> workflow-state.yaml update proposals
  |-- Validation Service -> local validation metadata and GitHub Actions links
  |-- Jira Adapter -> Jira read / payload preview
  |-- Confluence Adapter -> generated summary preview / publish status
  |-- Sonar Adapter -> quality gate read
  |-- Wynxx Adapter -> storycreator backlog candidate ingestion
  |
  v
Portal Cache / Index
```

MVP architecture principles:

- Git-backed writes only.
- Stateless portal backend where practical.
- Cache is rebuildable from Git and external APIs.
- All external writes are behind explicit write-mode flags.
- All secrets use approved secret storage.
- All artifact writes include optimistic concurrency checks using commit SHA.
- All validations use existing framework scripts or GitHub Actions results.

## What Is In Scope For Demo

The demo should prove the operating model, not a full enterprise platform.

In scope:

- Browse domains, capabilities, features, and framework documents from Git.
- View `workflow-state.yaml` summaries where available.
- View markdown artifacts with artifact metadata and source path.
- Edit a markdown artifact on a branch and show a diff before commit.
- Create a pull request for a portal-generated edit.
- Show GitHub Actions validation status for the PR.
- Approve a stage by updating `workflow-state.yaml` through a branch or PR.
- View the read-only Control Tower Dashboard for feature status, quality gates, and traceability.
- Display Jira issue links from Git-owned metadata where available.
- Display generated Confluence summary previews.
- Display Wynxx storycreator backlog candidates as draft ingestion items.
- Enforce no silent overwrite through source commit SHA checks.

## What Is Out Of Scope

Out of scope for MVP:

- Replacing Git, GitHub, Jira, Confluence, or Sonar.
- Bypassing branch protection or pull request review.
- Silent artifact overwrite.
- Direct lifecycle changes or new lifecycle stages.
- New Codex skills.
- Source-code generation or implementation.
- Domain business artifact creation without the active lifecycle skill and approval.
- Full Jira write synchronization.
- Full Confluence publish automation.
- Dashboard write actions, approvals, or lifecycle updates.
- Production-grade workflow engine.
- Enterprise-wide RBAC administration.
- Offline editing and merge resolution.
- Complex real-time collaborative editing.
- Production customer data handling.
- Deployment to production.

## Future Roadmap

| Phase | Capability |
| --- | --- |
| Phase 1 | Git-backed read views, artifact editor, diff preview, branch/PR creation, validation status, approval commits, and integration status. |
| Phase 2 | Structured artifact forms, stronger traceability visualization, Jira payload publishing after write-mode approval, and Confluence publish workflow. |
| Phase 3 | Role-based approval queues, CODEOWNERS-aware approver suggestions, signed approval evidence, and release readiness dashboard. |
| Phase 4 | Wynxx backlog ingestion enrichment, duplicate detection, backlog-to-intent handoff, and stakeholder review workflow. |
| Phase 5 | Enterprise audit dashboard, policy-as-code checks, cross-repository portfolio status, and operational evidence aggregation. |

Roadmap phases must preserve Git as source of truth and must not change the AI SDLC lifecycle without explicit framework approval.
