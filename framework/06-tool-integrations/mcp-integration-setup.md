# MCP Integration Setup

## Purpose

This guide defines MCP connectivity for the AI-SDLC demo tools: Wynxx, Jira, Confluence, and GitHub.

MCP integrations help Codex read backlog, workflow, publishing, repository, pull request, validation, and release evidence during AI-SDLC workflows. They do not replace Git-owned framework artifacts or human approval gates.

## Source-Of-Truth Rules

- Git remains the source of truth for framework guidance, lifecycle artifacts, traceability, validation evidence, release evidence, and source code.
- Wynxx is a synchronized backlog-candidate input, not source of truth.
- AI-SDLC may create Jira tickets for the demo only after explicit approval.
- Jira is a synchronized workflow-tracking view.
- Confluence is a synchronized published-document view.
- GitHub is a synchronized repository, pull request, validation, and release-evidence view.
- Do not create or update real Jira tickets, Confluence pages, or GitHub repository content unless explicitly instructed.
- Start with read-only MCP validation wherever the MCP server supports it.

## Required MCP Servers

| Server | Purpose | Initial Mode |
| --- | --- | --- |
| `wynxx` | Read Wynxx Story Creator projects, backlogs, hierarchy, work items, acceptance criteria, tasks, and test cases. | Read-only |
| `jira` | Read Jira workflow tracking and, after approval, create/update demo Epic, Story, Task, Sub-task, status, and links. | Read-only first |
| `confluence` | Read publishing space and, after approval, publish generated summaries from Git-owned artifacts. | Read-only first |
| `github` | Read repository, branches, PRs, Actions status, validation evidence, commits, and releases; create PRs only after approval. | Read-only first |

## MCP Subagent Architecture

For token efficiency, the main Codex agent should not load all MCP tool context or full external payloads into the main session.

Use MCP-specialist subagents for bounded external-system operations:

| Subagent | MCP Server | Responsibility |
| --- | --- | --- |
| `wynxx-backlog-agent` | `wynxx` | Read backlog candidates and return normalized Epic, Feature, Story, Task, and Test Case summaries. |
| `jira-lifecycle-agent` | `jira` | Create/update approved demo tickets, lifecycle status, and Git/Confluence links while preventing duplicates. |
| `confluence-publisher-agent` | `confluence` | Publish or update approved Git artifact summaries without making Confluence the source of truth. |
| `github-evidence-agent` | `github` | Read PR, Actions, validation, and release evidence and return compact status summaries. |

Subagents return only source system, object ID, title, status, link, summary, errors, and recommended next action unless the user explicitly requests full payloads.

See `framework/06-tool-integrations/mcp-subagent-architecture.md` for the detailed subagent contract and token-control rules.

## Environment Variables

Use `.env.mcp.example` as the local template. Copy it to a local untracked environment file or export the variables in the shell.

Required values:

- `WYNXX_MCP_URL`
- `WYNXX_API_TOKEN`
- `ATLASSIAN_SITE_URL`
- `ATLASSIAN_EMAIL`
- `ATLASSIAN_API_TOKEN`
- `JIRA_PROJECT_KEY`
- `CONFLUENCE_SPACE_KEY`
- `GITHUB_TOKEN`
- `GITHUB_OWNER`
- `GITHUB_REPO`

Never commit real tokens or private URLs.

## Example Codex MCP Configuration

Codex MCP configuration can be added to `~/.codex/config.toml`. Server commands and arguments depend on the approved MCP server packages used in the demo environment.

```toml
[mcp_servers.wynxx]
command = "wynxx-mcp-server"
args = []

[mcp_servers.wynxx.env]
WYNXX_MCP_URL = "${WYNXX_MCP_URL}"
WYNXX_API_TOKEN = "${WYNXX_API_TOKEN}"

[mcp_servers.jira]
command = "jira-mcp-server"
args = []

[mcp_servers.jira.env]
ATLASSIAN_SITE_URL = "${ATLASSIAN_SITE_URL}"
ATLASSIAN_EMAIL = "${ATLASSIAN_EMAIL}"
ATLASSIAN_API_TOKEN = "${ATLASSIAN_API_TOKEN}"
JIRA_PROJECT_KEY = "${JIRA_PROJECT_KEY}"

[mcp_servers.confluence]
command = "confluence-mcp-server"
args = []

[mcp_servers.confluence.env]
ATLASSIAN_SITE_URL = "${ATLASSIAN_SITE_URL}"
ATLASSIAN_EMAIL = "${ATLASSIAN_EMAIL}"
ATLASSIAN_API_TOKEN = "${ATLASSIAN_API_TOKEN}"
CONFLUENCE_SPACE_KEY = "${CONFLUENCE_SPACE_KEY}"

[mcp_servers.github]
command = "github-mcp-server"
args = []

[mcp_servers.github.env]
GITHUB_TOKEN = "${GITHUB_TOKEN}"
GITHUB_OWNER = "${GITHUB_OWNER}"
GITHUB_REPO = "${GITHUB_REPO}"
```

Alternative CLI-style setup, if the local Codex version and MCP server packages support it:

```bash
codex mcp add wynxx --env WYNXX_MCP_URL --env WYNXX_API_TOKEN -- wynxx-mcp-server
codex mcp add jira --env ATLASSIAN_SITE_URL --env ATLASSIAN_EMAIL --env ATLASSIAN_API_TOKEN --env JIRA_PROJECT_KEY -- jira-mcp-server
codex mcp add confluence --env ATLASSIAN_SITE_URL --env ATLASSIAN_EMAIL --env ATLASSIAN_API_TOKEN --env CONFLUENCE_SPACE_KEY -- confluence-mcp-server
codex mcp add github --env GITHUB_TOKEN --env GITHUB_OWNER --env GITHUB_REPO -- github-mcp-server
```

Validate command names, server binaries, and required arguments against the approved MCP server documentation for the demo environment before use.

## MCP Validation Checklist

Read-only validation:

- Wynxx: can list projects.
- Wynxx: can list backlogs for a selected project.
- Wynxx: can read backlog hierarchy.
- Wynxx: can read work item details and acceptance criteria.
- Wynxx: can map backlog items to candidate AI-SDLC capability, feature, requirement, implementation slice, and test design inputs.
- Jira: can read project metadata and issue type mappings.
- Confluence: can read the target space and parent page.
- GitHub: can read repository metadata, branch status, pull requests, and GitHub Actions status.

Approval-gated write validation:

- Can create Jira Epic or Story only after approval.
- Can update Jira lifecycle status only after approval.
- Can publish a Confluence page generated from a Git-owned artifact only after approval.
- Can link Jira and Confluence back to the Git artifact path and commit or PR reference.
- Can log all write operations with actor, timestamp, target system, target ID, source Git artifact, and approval reference.

## Demo Integration Flow

```text
Wynxx Story Creator backlog candidate
→ AI-SDLC review
→ Intent approval
→ Create Jira ticket
→ Generate requirements/design
→ Publish Confluence
→ Run GitHub validation
→ Update Jira lifecycle
```

Detailed flow:

1. Use `wynxx` MCP to read a Wynxx Story Creator backlog candidate.
2. Use `wynxx-backlog-agent` to return compact candidate backlog summaries.
3. Use `$backlog-ingestion` to summarize and map the backlog to AI-SDLC candidate inputs.
4. Human reviews the candidate mapping.
5. Use `$intent` only after the user approves moving from candidate backlog input to Git-owned intent work.
6. After intent approval, use `jira-lifecycle-agent` to create or update the approved Jira demo ticket when explicitly instructed.
7. Continue with `$requirements`, `$design`, and later lifecycle stages using Git-owned artifacts.
8. Use `confluence-publisher-agent` to publish Confluence summaries only from reviewed Git artifacts and only after approval.
9. Use `github-evidence-agent` to read GitHub validation through GitHub Actions.
10. Use `jira-lifecycle-agent` to update Jira lifecycle tracking from Git-owned workflow state and validation evidence.

## Security Notes

- Never commit real tokens.
- Use least privilege API tokens.
- Prefer read-only MCP access first.
- Separate demo credentials from production credentials.
- Use dedicated demo service accounts where possible.
- Store credentials in local environment variables, GitHub secrets, or approved secret managers.
- Do not paste production customer data, secrets, credentials, or private keys into prompts.
- Log all write operations.
- Disable or omit write scopes until the demo explicitly needs them.
- Rotate demo tokens after public demonstrations or shared sessions.

## Write Guardrails

MCP tools must not:

- create Jira tickets before approval
- update Jira status before approval
- publish Confluence pages before approval
- create GitHub branches, commits, or PRs before approval
- overwrite Git-owned artifacts from Jira, Confluence, or Wynxx
- treat Wynxx, Jira, or Confluence as synchronized views or inputs rather than source of truth
- bypass GitHub Actions validation or branch protection

## Related Documents

- `framework/06-tool-integrations/integration-foundation.md`
- `framework/06-tool-integrations/integration-configuration-guide.md`
- `framework/06-tool-integrations/mcp-subagent-architecture.md`
- `framework/06-tool-integrations/ai-sdlc-portal-mvp.md`
- `.codex/skills/backlog-ingestion/SKILL.md`
- `.codex/config.toml`
