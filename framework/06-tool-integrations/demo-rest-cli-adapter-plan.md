# Demo REST/CLI Adapter Plan

## Purpose

Provide the demo execution path for Jira, Confluence, and GitHub Actions evidence without enabling MCP writes.

Git remains the source of truth. Jira, Confluence, and GitHub remain synchronized views or evidence channels. The REST/CLI adapters are the demo-time execution path until a later MCP spike is approved.

## Scope

This plan covers:

- Jira REST validation, story creation, remote links, and status transitions.
- Confluence REST validation, page publish, and update-by-title.
- GitHub Actions evidence retrieval through the `gh` CLI.

This plan does not enable Atlassian Remote MCP, and it does not modify live Jira or Confluence content unless a user explicitly approves write mode and supplies `--apply`.

## Environment Variables

Required:

- `JIRA_BASE_URL`
- `JIRA_EMAIL`
- `JIRA_API_TOKEN`
- `JIRA_PROJECT_KEY`
- `CONFLUENCE_SPACE_KEY`
- `GITHUB_OWNER`
- `GITHUB_REPO`

Optional:

- `CONFLUENCE_BASE_URL`
- `GITHUB_TOKEN`
- `GH_TOKEN`

## Adapter Entry Points

| Adapter | Script | Purpose |
| --- | --- | --- |
| Jira | `scripts/jira/rest_cli.py` | Validate connection/project, create a demo story from approved intent, add Git and Confluence remote links, and transition Jira status. |
| Confluence | `scripts/confluence/rest_cli.py` | Validate the target space, publish an approved Git artifact page, and update an existing page by title. |
| GitHub Actions | `scripts/github/evidence.py` | List latest workflow runs and read the latest validation result through `gh`. |

## Demo Controls

- Default behavior is read-only or dry-run.
- Write operations require `--apply`.
- No secrets are committed in repository files.
- REST/CLI writes should only use reviewed Git-owned artifacts.
- Jira, Confluence, and GitHub remain synchronized views or evidence channels; Git remains canonical.

## Comparison

| Option | Strengths | Limits | Demo Fit |
| --- | --- | --- | --- |
| Local Docker `mcp-atlassian` | Single server for Jira and Confluence, good for later MCP-based automation, easy to keep read-only. | Requires MCP runtime configuration and tool exposure, adds moving parts before the demo path is validated. | Good later; not the immediate demo path. |
| Atlassian Remote MCP / Rovo MCP | Managed Atlassian-hosted remote protocol, likely less local server management once approved. | Needs OAuth, Atlassian admin allowlists, and extra operational validation. | Future spike only. |
| REST/CLI fallback | Direct, explicit, scriptable, easy to keep dry-run by default, matches the current demo need. | More manual than MCP for coordinated workflows. | Primary demo path. |

## Next Step

Use the REST/CLI adapters for demo execution. Keep the Atlassian Remote MCP / Rovo MCP investigation deferred until the demo-critical workflow is stable and reviewed.
