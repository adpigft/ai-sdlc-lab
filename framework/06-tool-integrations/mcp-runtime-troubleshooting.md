# MCP Runtime Troubleshooting

## Purpose

Document the local MCP runtime setup for read-only AI-SDLC validation.

This note does not modify credentials, create tickets, publish pages, create GitHub issues, open pull requests, commit changes, rerun workflows, or change repositories.

## Current MCP Server Status

Observed local configuration: `.codex/config.toml`

| Server | Configured | Enabled | Command / Image | Environment Variables | Runtime Status |
| --- | --- | --- | --- | --- | --- |
| Atlassian | Yes | `enabled = false` | `sh -lc` wrapper around `docker run --rm -i ghcr.io/sooperset/mcp-atlassian:latest` | Standard local variables plus server-native aliases derived from them; `READ_ONLY_MODE=true`; explicit `TOOLSETS=jira_issues,jira_fields,jira_transitions,confluence_pages,confluence_comments` | Disabled pending review. This remains the local Jira and Confluence MCP option when re-enabled. |
| GitHub | Yes | `enabled = false` | `docker run -i --rm ghcr.io/github/github-mcp-server --read-only` | `GITHUB_TOKEN`, `GITHUB_OWNER`, `GITHUB_REPO`; token is mapped to the server-required `GITHUB_PERSONAL_ACCESS_TOKEN` | Disabled pending review. This remains the local GitHub MCP option when re-enabled. |
| Wynxx | No | No | Not configured | Not configured in `.codex/config.toml` | Kept disabled until a real Wynxx MCP command or URL is available. |

## Current Decision

MCP remains a post-demo technical spike. Do not add more MCP variants before the existing local Atlassian MCP, GitHub MCP, and REST/CLI fallback paths are validated.

For demo execution, use REST/CLI adapters as the primary path for Jira ticket creation and Confluence publishing. Keep near-term implementation focus on:

- Wynxx Story Creator ingestion.
- Jira ticket creation.
- Confluence publishing.
- Portal MVP.

TODO: Investigate Atlassian Remote MCP / Rovo MCP after demo-critical paths are stable. The investigation should compare Codex streamable HTTP OAuth support, Atlassian admin allowlists, IP allowlists, read-only tool policy, audit logging, and operational complexity against the current local Docker `mcp-atlassian` option and REST/CLI fallback. Do not add an Atlassian Remote MCP entry to `.codex/config.toml` until that spike is reviewed and approved.

Current operational mode: Jira, Confluence, and GitHub MCP are disabled in `.codex/config.toml`. Use REST/CLI adapters for demo work until a review explicitly re-enables MCP.

## Placeholder Commands Replaced

The following placeholder commands were removed from `.codex/config.toml`:

| Placeholder | Replacement |
| --- | --- |
| `jira-mcp-server` | Single `atlassian` MCP entry using `ghcr.io/sooperset/mcp-atlassian:latest`. |
| `confluence-mcp-server` | Single `atlassian` MCP entry using `ghcr.io/sooperset/mcp-atlassian:latest`. |
| `github-mcp-server` | Docker-backed official GitHub MCP server image `ghcr.io/github/github-mcp-server`. |

Jira and Confluence are intentionally configured through the same Atlassian MCP server. The server-native variables are derived from the standardized local variables so secrets remain outside Git.

The upstream `mcp-atlassian` configuration uses `TOOLSETS` for group-level tool exposure. For this repository, do not use `TOOLSETS=default` while troubleshooting missing Codex tool exposure. Use explicit Jira and Confluence toolsets:

```text
TOOLSETS=jira_issues,jira_fields,jira_transitions,confluence_pages,confluence_comments
READ_ONLY_MODE=true
```

`READ_ONLY_MODE=true` must remain enabled. The selected toolsets expose the required read-only smoke-test tools, including `jira_search`, `jira_get_project_issues`, `jira_get_transitions`, and `confluence_search`; server-level read-only mode disables create, update, and delete operations.

## Required Environment Variables

Use read-only demo credentials first.

| Server | Required Variables |
| --- | --- |
| Atlassian | `ATLASSIAN_SITE_URL`, `ATLASSIAN_EMAIL`, `ATLASSIAN_API_TOKEN`, `JIRA_PROJECT_KEY`, `CONFLUENCE_SPACE_KEY` |
| GitHub | `GITHUB_TOKEN`, `GITHUB_OWNER`, `GITHUB_REPO` |
| Wynxx | None until a real Wynxx MCP command or URL is approved. |

Do not commit real values. Keep credentials in the local shell environment, Codex user config, GitHub secrets, or approved enterprise secret management.

## Local Setup

### Install Commands

Docker-backed setup, matching `.codex/config.toml`:

```sh
docker pull ghcr.io/sooperset/mcp-atlassian:latest
docker pull ghcr.io/github/github-mcp-server
```

Optional GitHub MCP binary install if Docker is not available:

```sh
git clone https://github.com/github/github-mcp-server.git /tmp/github-mcp-server
cd /tmp/github-mcp-server
go build -o "$HOME/bin/github-mcp-server" ./cmd/github-mcp-server
```

Expected executable after the optional binary install:

```sh
command -v github-mcp-server
github-mcp-server stdio
```

The current repository config uses Docker because `github-mcp-server`, `mcp-atlassian`, and `uvx` were not installed on the local `PATH`, while `docker` was installed.

### PATH Checks

```sh
command -v docker
command -v github-mcp-server || true
command -v mcp-atlassian || true
command -v uvx || true
```

### Environment Variable Checks

Run this from a local shell. It reports only whether variables are set; it does not print secret values.

```sh
for v in \
  ATLASSIAN_SITE_URL \
  ATLASSIAN_EMAIL \
  ATLASSIAN_API_TOKEN \
  JIRA_PROJECT_KEY \
  CONFLUENCE_SPACE_KEY \
  GITHUB_TOKEN \
  GITHUB_OWNER \
  GITHUB_REPO
do
  eval "value=\${$v:-}"
  if [ -n "$value" ]; then
    printf '%s=set\n' "$v"
  else
    printf '%s=missing\n' "$v"
  fi
  unset value
done
```

### Codex MCP List Check

```sh
codex mcp list
```

Expected result:

- `atlassian` is listed as enabled with the `sh -lc` Docker wrapper and image `ghcr.io/sooperset/mcp-atlassian:latest`.
- The Atlassian command includes `READ_ONLY_MODE=true`.
- The Atlassian command includes `TOOLSETS=jira_issues,jira_fields,jira_transitions,confluence_pages,confluence_comments`.
- `github` is listed with command `docker` and image `ghcr.io/github/github-mcp-server`.
- Secrets are masked.
- Wynxx Story Creator is absent unless a real Wynxx Story Creator MCP server has been approved and configured.

## Read-Only Smoke Test Instructions

Run these only after the MCP tools are exposed in a restarted Codex session. Do not use them to create or update remote objects.

### Jira

```text
Use the Atlassian MCP server in read-only mode.
Run jira_search with JQL "project = SCRUM ORDER BY updated DESC" and limit 3.
Return only source system, object ID, title/name, status, link, summary, errors, and recommended next action.
Do not create tickets.
Do not update Jira status.
Do not fetch full issue descriptions.
```

### Confluence

```text
Use the Atlassian MCP server in read-only mode.
Run confluence_search with CQL "space = AISDLC AND type = page ORDER BY lastmodified DESC" and limit 3.
Return only source system, object ID, title/name, status, link, summary, errors, and recommended next action.
Do not publish pages.
Do not update pages.
Do not fetch full page bodies.
```

### GitHub

```text
Use the GitHub MCP server in read-only mode.
Read repository metadata for GITHUB_OWNER/GITHUB_REPO and, if available, the latest workflow run metadata.
Return only source system, object ID, title/name, status, link, summary, errors, and recommended next action.
Do not create branches, commits, pull requests, issues, releases, or repository changes.
Do not rerun workflows.
Do not fetch full workflow logs.
```

## Validation Notes

- `codex mcp list` validates that the local configuration parses and the Docker-backed MCP entries are registered.
- Smoke tests require MCP tools to be available in the active Codex tool surface. If they are not exposed, restart Codex after exporting the required environment variables and after confirming `TOOLSETS` is not `default`.
- A running Codex session does not reload MCP server configuration after `.codex/config.toml` changes. Restart Codex before expecting `jira_*` or `confluence_*` tools to appear.
- Docker image pull and remote smoke tests require network access and approved credentials. They should be performed only with read-only tokens.

## Related Documents

- `framework/06-tool-integrations/mcp-integration-setup.md`
- `framework/06-tool-integrations/mcp-subagent-architecture.md`
- `framework/06-tool-integrations/mcp-subagent-smoke-tests.md`
- `.env.mcp.example`
- `.codex/config.toml`
