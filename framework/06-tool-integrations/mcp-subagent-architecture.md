# MCP Subagent Architecture

## Purpose

Define a token-efficient MCP integration architecture for AI-SDLC demo tooling. The main Codex agent remains the orchestrator, while MCP-specialist subagents perform bounded tool-specific operations for Wynxx, Jira, Confluence, and GitHub.

This architecture avoids loading all MCP tool schemas, external payloads, and tool-specific context into the main Codex session. Subagents return compact, normalized summaries that the main Codex agent can use for AI-SDLC decisions and Git-owned artifact updates.

## Principles

- Git remains the source of truth.
- The main Codex agent decides what must happen.
- MCP subagents execute bounded tool-specific operations.
- MCP subagents are not lifecycle stages, approval authorities, or source-of-truth systems.
- Subagents must not bypass workflow-state, branch protection, GitHub Actions, or human approval gates.
- Subagents must not expose full MCP payloads unless the user explicitly requests them.
- External IDs and traceability links must be stored in Git-owned traceability artifacts.

## Main Orchestration Rule

The main Codex agent is responsible for:

- interpreting the user request
- selecting the active AI-SDLC skill or support skill
- deciding whether an MCP operation is needed
- assigning one bounded operation to the relevant MCP subagent
- reviewing the compact subagent result
- deciding whether Git artifacts need updates
- enforcing approval gates before write operations
- reporting final status and next actions to the user

MCP subagents are responsible only for the assigned external-system operation and compact result.

## Required Subagent Return Shape

Every MCP subagent must return only:

| Field | Purpose |
| --- | --- |
| `source_system` | Wynxx, Jira, Confluence, or GitHub. |
| `object_id` | External ID, issue key, page ID, PR number, run ID, backlog item ID, or equivalent. |
| `title` | Short object title. |
| `status` | Current external-system status. |
| `link` | Stable URL when available. |
| `summary` | Compact human-readable summary. |
| `errors` | Errors, missing permissions, conflicts, or unavailable data. |
| `recommended_next_action` | Suggested next action for the main Codex agent. |

Subagents must not return full raw payloads, long descriptions, full Confluence bodies, full Jira descriptions, complete backlog exports, or full GitHub logs unless explicitly requested.

## Subagents

### `wynxx-backlog-agent`

Purpose:

- Read Wynxx backlog candidates.
- Return normalized Epic, Feature, Story, Task, and Test Case summaries.
- Support `$wynxx-backlog-ingestion` without creating AI-SDLC artifacts directly.

Allowed operations:

- list projects using filters
- list backlogs using project and status filters
- read selected backlog hierarchy
- read selected work item details
- extract acceptance criteria where available
- summarize Epics, Features, User Stories, Tasks, and Test Cases
- return candidate hierarchy mapping for review

Not allowed:

- create intent automatically
- create specification automatically
- modify Git artifacts
- create Jira tickets
- fetch the entire Wynxx backlog by default
- treat Wynxx as source of truth

Compact output focus:

- candidate capability or Jira Epic
- candidate feature or feature group
- requirement candidates
- implementation slice candidates
- test design candidates
- duplicate or overlap warnings
- missing acceptance criteria

### `jira-lifecycle-agent`

Purpose:

- Create Jira tickets after approved Intent.
- Update Jira workflow status.
- Add Git and Confluence links.
- Prevent duplicate Jira ticket creation using external IDs and traceability metadata.

Allowed operations:

- read project metadata and issue type mappings
- search for existing issues by external ID, Git path, feature ID, or traceability metadata
- create Jira Epic, Story, Task, or Sub-task only after explicit approval
- update Jira workflow status only after explicit approval
- add Git artifact links, PR links, validation links, and Confluence links
- return issue key, status, link, and duplicate-detection outcome

Not allowed:

- create duplicate tickets when an external ID or traceability mapping already exists
- treat Jira descriptions as canonical requirements
- update Jira status without approval
- override missing Git evidence
- fetch full issue descriptions unless required for duplicate detection or conflict review

Duplicate prevention keys:

- Wynxx item ID
- Git artifact path
- workflow-state feature ID
- capability ID
- feature ID
- Jira issue key already stored in Git traceability artifacts

### `confluence-publisher-agent`

Purpose:

- Publish approved Git artifacts to Confluence.
- Update existing pages when Git artifact version changes.
- Preserve Confluence as a published view only.

Allowed operations:

- read target space and parent page
- search for existing pages by Git artifact path, feature ID, title, or traceability metadata
- publish approved summaries generated from Git artifacts after approval
- update existing pages when source Git artifact version changes
- add Git commit, PR, workflow-state, Jira, and validation links
- return page ID, title, status, link, and publish/update summary

Not allowed:

- treat Confluence page body as source of truth
- publish unapproved artifacts
- fetch full page bodies unless publishing or comparing
- overwrite a page without version comparison
- store secrets, production customer data, or sensitive operational details

Version comparison keys:

- Git artifact path
- Git commit SHA
- artifact ID
- workflow-state stage
- prior Confluence page ID

### `github-evidence-agent`

Purpose:

- Read GitHub Actions status.
- Read PR status.
- Capture validation and release evidence.
- Return compact evidence summary.

Allowed operations:

- read repository metadata
- read branch and pull request status
- read GitHub Actions workflow run status
- read required check status
- read release references
- return validation evidence links and status

Not allowed:

- create branches, commits, PRs, or releases without explicit approval
- fetch full workflow logs unless required for failure diagnosis
- bypass branch protection
- treat GitHub issue text as source-of-truth requirements

Compact output focus:

- PR number and status
- workflow run ID and status
- failed check names
- validation URL
- release tag or release URL where available
- recommended next action

## Token-Control Rules

- Do not fetch full Jira issue descriptions unless required.
- Do not fetch full Confluence page bodies unless publishing or comparing.
- Do not fetch entire Wynxx backlog by default.
- Do not fetch full GitHub Actions logs unless diagnosing a failed check.
- Use project, capability, feature, issue type, status, branch, PR, or date filters.
- Limit responses to the active demo scope.
- Return summarized external objects, not raw payloads.
- Store traceability IDs in Git artifacts.
- Cache retrieved external IDs in the Git-owned traceability artifact. Use `traceability.md` where a project has adopted that filename; in this repository, use the canonical `traceability/traceability-matrix.md`.
- Prefer stable external links over copied external content.

## External ID Traceability

Each external-system write or accepted mapping should record:

- source system
- external object ID
- object title
- source Git artifact path
- source Git commit SHA or PR
- workflow stage
- approval reference
- last synchronized timestamp
- link

This metadata prevents duplicate Jira ticket creation, supports Confluence page updates, and gives GitHub validation evidence a stable Git-owned reference.

## Bounded Operation Pattern

Use this pattern when the main Codex agent delegates work:

```text
Main Codex Agent
  -> chooses operation and filters
  -> invokes one MCP specialist subagent
  -> receives compact normalized result
  -> decides next AI-SDLC action
  -> updates Git artifacts only when the user requested or approved it
```

Example delegated requests:

- "Read Wynxx backlog `CARDS-123` and return candidate feature summaries only."
- "Check whether Jira already has a Story for Git artifact path `domains/cards/.../intent.md`."
- "Publish this approved validation summary to the existing Confluence page and return page ID plus link."
- "Read PR 42 and latest AI SDLC Validation workflow status."

## Error Handling

Subagents must report:

- missing MCP server
- authentication failure
- insufficient permission
- object not found
- duplicate found
- write blocked by missing approval
- payload too large and filtered
- source-system rate limit or outage

The main Codex agent decides whether to retry, narrow scope, ask the user, or stop for review.

## Review And Approval Boundaries

MCP subagent results are evidence or candidates. They are not approvals.

Human approval is still required before:

- creating Jira tickets
- updating Jira lifecycle status
- publishing Confluence pages
- creating GitHub branches, commits, PRs, or releases
- creating or updating AI-SDLC intent, specification, design, tests, implementation plan, validation, release, or workflow-state artifacts

## Related Documents

- `framework/06-tool-integrations/mcp-integration-setup.md`
- `framework/06-tool-integrations/integration-foundation.md`
- `framework/06-tool-integrations/ai-sdlc-portal-mvp.md`
- `.codex/skills/wynxx-backlog-ingestion/SKILL.md`
- `docs/subagents/subagent-workflows.md`
