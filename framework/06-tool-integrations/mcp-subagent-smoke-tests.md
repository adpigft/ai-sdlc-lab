# MCP Subagent Smoke Tests

## Test Purpose

Validate that each MCP-specialist subagent can connect to its assigned tool and return a compact, read-only response without destructive actions.

These smoke tests verify connectivity, permissions, filtering, compact response formatting, and non-destructive behavior for:

- `wynxx-backlog-agent`
- `jira-lifecycle-agent`
- `confluence-publisher-agent`
- `github-evidence-agent`

## Preconditions

- MCP servers are configured for `wynxx`, `jira`, `confluence`, and `github`.
- Demo credentials are loaded through local environment variables or approved secret handling.
- The user has permission to read the demo Wynxx project, Jira project, Confluence space, and GitHub repository.
- Write scopes are disabled or unused for smoke testing.
- The main Codex agent remains the orchestrator.
- Subagents return compact summaries only.

## Environment Variables Required

Use `.env.mcp.example` as the token-free template.

| Variable | Purpose |
| --- | --- |
| `WYNXX_MCP_URL` | Wynxx MCP endpoint or server URL. |
| `WYNXX_API_TOKEN` | Wynxx demo API token. |
| `ATLASSIAN_SITE_URL` | Atlassian site URL for Jira and Confluence. |
| `ATLASSIAN_EMAIL` | Atlassian demo service account email. |
| `ATLASSIAN_API_TOKEN` | Atlassian demo API token. |
| `JIRA_PROJECT_KEY` | Jira demo project key. |
| `CONFLUENCE_SPACE_KEY` | Confluence demo space key. |
| `GITHUB_TOKEN` | GitHub demo token. |
| `GITHUB_OWNER` | GitHub owner or organization. |
| `GITHUB_REPO` | GitHub repository name. |

Do not print token values in smoke-test output.

## Expected Compact Output Format

Each subagent must return only:

```text
source_system:
object_id:
title:
status:
link:
summary:
errors:
recommended_next_action:
```

The response must not include full MCP payloads, full issue descriptions, full Confluence page bodies, full backlog exports, full workflow logs, secrets, credentials, or production data.

## Smoke Test Commands / Prompts

If automated MCP invocation is unavailable, run:

```bash
bash scripts/smoke-test-mcp-subagents.sh
```

The script prints the manual Codex prompts below.

### 1. `wynxx-backlog-agent`

Action:

- List available Wynxx projects or fetch one small backlog sample.
- Use demo project or status filters when available.
- Do not fetch the entire backlog.

Prompt:

```text
Use wynxx-backlog-agent in read-only mode.
List available Wynxx projects, or fetch one small backlog sample using demo filters if a project is already configured.
Return only compact output:
- source_system
- object_id
- title
- status
- link
- summary with project/backlog ID, title, and count of Epics/Features/Stories if available
- errors
- recommended_next_action
Do not create AI-SDLC artifacts.
Do not fetch the entire backlog.
Do not return full MCP payloads.
```

Expected result:

- Project or backlog ID.
- Title.
- Count of Epics, Features, and Stories if available.
- Connection status.

### 2. `jira-lifecycle-agent`

Action:

- Read Jira project metadata for `JIRA_PROJECT_KEY`.
- Search maximum 3 issues.
- Do not create or update tickets.

Prompt:

```text
Use jira-lifecycle-agent in read-only mode.
Read Jira project metadata for the configured demo project key.
Search maximum 3 issues using the demo project filter.
Return only compact output:
- source_system
- object_id
- title
- status
- link
- summary with project key, project name, issue keys, issue titles, and current statuses
- errors
- recommended_next_action
Do not create tickets.
Do not update Jira status.
Do not fetch full issue descriptions unless required to identify duplicates.
Do not return full MCP payloads.
```

Expected result:

- Project key.
- Project name.
- Up to 3 issue keys.
- Issue titles.
- Current statuses.

### 3. `confluence-publisher-agent`

Action:

- Read Confluence demo space metadata for `CONFLUENCE_SPACE_KEY`.
- Search maximum 3 pages.
- Do not create or update pages.

Prompt:

```text
Use confluence-publisher-agent in read-only mode.
Read Confluence demo space metadata for the configured space key.
Search maximum 3 pages in that space.
Return only compact output:
- source_system
- object_id
- title
- status
- link
- summary with space key, space name, page titles, and page links
- errors
- recommended_next_action
Do not publish pages.
Do not update pages.
Do not fetch full page bodies.
Do not return full MCP payloads.
```

Expected result:

- Space key.
- Space name.
- Up to 3 page titles.
- Page links.

### 4. `github-evidence-agent`

Action:

- Read repository metadata for `GITHUB_OWNER` / `GITHUB_REPO`.
- Read latest GitHub Actions workflow runs.
- Do not create branches, commits, PRs, releases, or repository changes.

Prompt:

```text
Use github-evidence-agent in read-only mode.
Read repository metadata for the configured GitHub owner and repository.
Read latest GitHub Actions workflow runs.
Return only compact output:
- source_system
- object_id
- title
- status
- link
- summary with repository, default branch, latest workflow name, latest workflow status, and conclusion
- errors
- recommended_next_action
Do not create branches, commits, pull requests, releases, or repository changes.
Do not fetch full workflow logs unless required for failure diagnosis.
Do not return full MCP payloads.
```

Expected result:

- Repository.
- Default branch.
- Latest workflow name.
- Latest workflow status and conclusion.

## Pass / Fail Criteria

| Result | Criteria |
| --- | --- |
| Pass | Subagent connects, performs read-only action, returns compact output, and avoids full payloads. |
| Partial Pass | Subagent connects but lacks permission for part of the read-only scope, or no demo objects exist. |
| Fail | Subagent cannot connect, returns full payloads, attempts a write, exposes secrets, or ignores filters. |
| Blocked | MCP server is not configured or required environment variables are missing. |

## Troubleshooting Notes

- If a server is missing, verify `~/.codex/config.toml` and `framework/06-tool-integrations/mcp-integration-setup.md`.
- If credentials fail, verify demo tokens are loaded and not expired.
- If Jira returns no issues, confirm `JIRA_PROJECT_KEY` and project permissions.
- If Confluence returns no pages, confirm `CONFLUENCE_SPACE_KEY`, page permissions, and whether the space is empty.
- If GitHub Actions cannot be read, confirm `GITHUB_TOKEN` scopes and repository access.
- If Wynxx returns too much data, add project, backlog, status, or item-type filters.
- If output is too large, rerun with stricter limits and request only IDs, titles, status, links, errors, and next action.

## Review Notes

Smoke-test results should be copied into the review conversation or a future validation artifact only after human review. Do not commit secrets, raw MCP payloads, or production data.

## Execution Results

### 2026-06-06 Manual Subagent Smoke Test

| Field | Value |
| --- | --- |
| Execution date | 2026-06-06 |
| Environment used | Local Codex session for `ai-sdlc-lab`; no live MCP tool namespaces were exposed to the main session or specialist subagents. |
| Credential handling | No token values were printed or committed. Demo credentials were not available to the session. |
| Execution mode | Read-only specialist subagent prompts. |
| Destructive actions | None. No Jira tickets, Confluence pages, GitHub repository changes, or AI-SDLC artifacts were created through MCP. |

| Subagent | Source System | Pass / Fail | Returned Object IDs Only | Errors | Remediation Steps |
| --- | --- | --- | --- | --- | --- |
| `wynxx-backlog-agent` | Wynxx | Blocked | None | Wynxx MCP resources, templates, or callable tools were not exposed. No active `mcp_servers.wynxx` entry was available in local config. | Configure a read-only Wynxx MCP server with `WYNXX_MCP_URL` and `WYNXX_API_TOKEN`, then rerun with demo project or backlog filters. |
| `jira-lifecycle-agent` | Jira | Blocked | `JIRA_PROJECT_KEY` placeholder only | Jira MCP resources, templates, or callable tools were not exposed. Local Jira MCP placeholder is disabled. | Enable/configure Jira MCP with read-only Atlassian credentials and `JIRA_PROJECT_KEY`, then rerun project metadata and max 3 issue search. |
| `confluence-publisher-agent` | Confluence | Blocked | None | Confluence MCP resources, templates, or callable tools were not exposed. | Enable/configure Confluence MCP with read-only Atlassian credentials and `CONFLUENCE_SPACE_KEY`, then rerun space metadata and max 3 page search. |
| `github-evidence-agent` | GitHub | Blocked | None | GitHub MCP resources, templates, or callable tools were not exposed. | Enable/configure GitHub MCP with read-only repository and Actions permissions, then rerun repository metadata and latest workflow run read. |

Summary:

- Smoke-test prompts executed through specialist subagents.
- No full MCP payloads were returned.
- No write operations were attempted.
- No MCP connection could be validated because the required MCP servers/tools were unavailable in this session.

### 2026-06-06 GitHub MCP Enablement Smoke Test

| Field | Value |
| --- | --- |
| Execution timestamp | 2026-06-06 15:42:50 +08 |
| Environment used | Local Codex session for `ai-sdlc-lab`. |
| Configuration change | GitHub MCP enabled in `.codex/config.toml`; Jira and Confluence remain disabled; Wynxx remains unconfigured. |
| Credential validation | `GITHUB_TOKEN`, `GITHUB_OWNER`, and `GITHUB_REPO` were missing from the local shell environment. Values were not printed or modified. |
| MCP server start check | Blocked. `github-mcp-server` was not found on `PATH`; current Codex session did not expose GitHub MCP resources, templates, or callable tools. |
| Destructive actions | None. No commits, PRs, issues, workflow reruns, or repository modifications were made through MCP. |

| Subagent | Source System | Pass / Fail | Returned Object IDs Only | Returned Metadata | Issues Encountered | Remediation Steps |
| --- | --- | --- | --- | --- | --- | --- |
| `github-evidence-agent` | GitHub MCP | Blocked | `github-evidence-agent-smoke-test` | Repository metadata: not returned; workflow runs: not returned; latest commit: not returned. | GitHub MCP enabled in config but tools were not exposed; required GitHub environment variables were missing; `github-mcp-server` command was unavailable on `PATH`. | Install or approve the GitHub MCP server binary, export read-only `GITHUB_TOKEN`, `GITHUB_OWNER`, and `GITHUB_REPO`, restart Codex so MCP tools are loaded, then rerun the read-only smoke test. |

GitHub success criteria status:

- GitHub MCP visible to Codex: Not met.
- Read-only queries successful: Not met.
- No repository changes made through MCP: Met.

### 2026-06-06 Atlassian MCP Read-Only Smoke Test

| Field | Value |
| --- | --- |
| Execution date | 2026-06-06 |
| Environment used | Local Codex session for `ai-sdlc-lab`; Atlassian MCP tools exposed directly to the main session. |
| Execution mode | Read-only only. |
| Destructive actions | None. No Jira tickets were created or updated. No Confluence pages were created or updated. |
| Atlassian MCP pass/fail | Fail. Required Jira search, Jira transition lookup, Confluence page search, and Confluence page metadata checks did not all complete successfully. |

Available Atlassian tools:

- Jira: `jira_search`, `jira_get_project_issues`, `jira_get_issue`, `jira_get_transitions`, `jira_batch_get_changelogs`, `jira_search_fields`, `jira_get_field_options`.
- Confluence: `confluence_search`, `confluence_get_page`, `confluence_get_comments`, `confluence_get_page_children`, `confluence_get_page_diff`, `confluence_get_page_history`, `confluence_get_space_page_tree`.

Jira read-only results:

| Test | Result |
| --- | --- |
| Search project `SCRUM`, maximum 3 issues | Failed through `jira_search`; Atlassian client attempted to use literal `${ATLASSIAN_SITE_URL}` and rejected the URL before returning issues. |
| Alternate read of project `SCRUM`, maximum 3 issues | Completed through `jira_get_project_issues`; returned zero issues. |
| Returned issue object IDs | None. |
| Issue summaries | None returned. |
| Transition lookup | Not run because no issue key was returned. |

Confluence read-only results:

| Test | Result |
| --- | --- |
| Search configured Confluence content, maximum 3 pages | Completed through `confluence_search`; returned zero pages. |
| Returned page object IDs | None. |
| Page titles and links | None returned. |
| Page metadata lookup | Not run because no page ID was returned. |

Limitations:

- Read-only mode was maintained for all Atlassian MCP calls.
- Jira `jira_search` appears misconfigured because the site URL is still a literal `${ATLASSIAN_SITE_URL}` placeholder.
- Jira project `SCRUM` returned no issue IDs through the alternate project issue read, so transitions could not be inspected.
- Confluence search returned no page IDs, so metadata-only page retrieval could not be inspected.
- No secrets, credentials, full Jira payloads, or full Confluence page bodies were recorded.

### 2026-06-06 Atlassian MCP Environment Injection Fix Retest

| Field | Value |
| --- | --- |
| Execution date | 2026-06-06 |
| Environment used | Local Codex session for `ai-sdlc-lab`; Atlassian MCP tools exposed directly to the main session. |
| Execution mode | Read-only only. |
| Config inspected | `.codex/config.toml` Atlassian MCP block. |
| Config fix | Replaced literal TOML placeholder env mappings with a `sh -lc` Docker wrapper that expands local `ATLASSIAN_*`, `JIRA_PROJECT_KEY`, and `CONFLUENCE_SPACE_KEY` variables at MCP server startup. |
| Secret handling | No secret values were printed, recorded, or hardcoded. |
| Required local environment variables | `ATLASSIAN_SITE_URL`, `ATLASSIAN_EMAIL`, `ATLASSIAN_API_TOKEN`, `JIRA_PROJECT_KEY`, and `CONFLUENCE_SPACE_KEY` were present in the local shell. |
| Config syntax validation | Passed. `.codex/config.toml` parsed successfully with `tomllib`. |
| Restart status | Not completed inside this running Codex session. Active MCP tools continued using the old server process/config. |
| Atlassian MCP pass/fail | Partial pass for config remediation; fail for live MCP retest until Codex is restarted and the Atlassian MCP server reloads config. |

Available Atlassian tools:

- Jira: `jira_search`, `jira_get_project_issues`, `jira_get_issue`, `jira_get_transitions`, `jira_batch_get_changelogs`, `jira_search_fields`, `jira_get_field_options`.
- Confluence: `confluence_search`, `confluence_get_page`, `confluence_get_comments`, `confluence_get_page_children`, `confluence_get_page_diff`, `confluence_get_page_history`, `confluence_get_space_page_tree`.

Read-only retest results before Codex restart:

| Test | Result |
| --- | --- |
| Jira search project `SCRUM`, maximum 3 issues | Failed. The live MCP server still used literal `${ATLASSIAN_SITE_URL}`, indicating the running MCP process had not reloaded the fixed config. |
| Jira project issues for `SCRUM`, maximum 3 issues | Completed. Returned zero issues. |
| Confluence search, maximum 3 pages | Completed. Returned zero pages. |
| Returned Jira issue object IDs | None. |
| Returned Confluence page object IDs | None. |
| Jira transition lookup | Not run because no Jira issue key was returned. |
| Confluence page metadata lookup | Not run because no Confluence page ID was returned. |

Limitations:

- Read-only mode was maintained for all Atlassian MCP calls.
- Codex must be restarted before this fix can be fully validated through MCP tools.
- The post-restart smoke test should rerun `jira_search`, `jira_get_project_issues`, and `confluence_search` with maximum 3 objects each.
- No Jira tickets or Confluence pages were created or updated.

### 2026-06-06 Atlassian MCP Post-Restart Read-Only Smoke Test

| Field | Value |
| --- | --- |
| Execution timestamp | 2026-06-06 16:48:08 +0800 |
| Environment used | Local Codex session for `ai-sdlc-lab` after restart. |
| Requested scope | `jira_search` max 3 issues in project `SCRUM`; `jira_get_project_issues` max 3 for `SCRUM`; `confluence_search` max 3 pages in space `AISDLC`; if an issue is returned, `jira_get_transitions` only. |
| Execution mode | Read-only only. |
| Tool discovery result | Blocked. No callable Atlassian MCP tools were exposed in this session; discovery returned no `jira_*` or `confluence_*` tools. |
| Destructive actions | None. No Jira tickets were created or updated. No Confluence pages were created or updated. |
| Atlassian MCP pass/fail | Blocked. Required Atlassian tools were unavailable, so no live Jira or Confluence reads could be performed. |

Read-only test results:

| Test | Result |
| --- | --- |
| `jira_search` project `SCRUM`, maximum 3 issues | Not run; `jira_search` was not exposed as a callable tool. |
| `jira_get_project_issues` for `SCRUM`, maximum 3 issues | Not run; `jira_get_project_issues` was not exposed as a callable tool. |
| `confluence_search` in space `AISDLC`, maximum 3 pages | Not run; `confluence_search` was not exposed as a callable tool. |
| Issue transition lookup | Not run because no Jira issue could be returned. |

Returned objects:

| Source | Object IDs | Compact summary |
| --- | --- | --- |
| Jira | None | No Jira results available; tools unavailable. |
| Confluence | None | No Confluence results available; tools unavailable. |

Limitations:

- The post-restart session did not expose the Atlassian MCP tool namespace needed for read-only validation.
- No secrets, credentials, raw Jira payloads, or raw Confluence payloads were recorded.
- Rerun after confirming the Atlassian MCP server is enabled and the session exposes `jira_search`, `jira_get_project_issues`, `jira_get_transitions`, and `confluence_search`.

### 2026-06-06 Atlassian MCP Explicit Toolsets Retest

| Field | Value |
| --- | --- |
| Execution timestamp | 2026-06-06 16:53:44 +0800 |
| Environment used | Local Codex session for `ai-sdlc-lab` before process restart. |
| Requested scope | Replace `TOOLSETS=default` with explicit Jira and Confluence tool exposure, keep `READ_ONLY_MODE=true`, then run `jira_search` max 3 for project `SCRUM` and `confluence_search` max 3 for space `AISDLC`. |
| Execution mode | Read-only only. |
| Config inspected | `.codex/config.toml`; upstream `mcp-atlassian` configuration documentation. |
| Config fix | Replaced `TOOLSETS=default` with `TOOLSETS=jira_issues,jira_fields,jira_transitions,confluence_pages,confluence_comments`. |
| Correct exposure variable | `TOOLSETS` is the server-supported group-level exposure variable. `ENABLED_TOOLS` is available for individual tool filtering, but was not used for this fix. |
| Read-only status | `READ_ONLY_MODE=true` remains configured. |
| Config syntax validation | Passed. `.codex/config.toml` parsed successfully with `tomllib`. |
| MCP list validation | Passed for config registration. `codex mcp list` shows `atlassian` enabled and includes the explicit `TOOLSETS` value. |
| Tool discovery result | Blocked in this still-running session. No callable `jira_search` or `confluence_search` tools are exposed until Codex reloads MCP server configuration. |
| Restart status | Not completed inside the active Codex process. Codex must be restarted by the operator before live smoke tests can run. |
| Destructive actions | None. No Jira tickets were created or updated. No Confluence pages were created or updated. |
| Atlassian MCP pass/fail | Partial pass for config remediation; blocked for live read-only smoke tests pending Codex restart and tool exposure. |

Read-only test results:

| Test | Result |
| --- | --- |
| `jira_search` project `SCRUM`, maximum 3 issues | Not run; `jira_search` is not exposed as a callable tool in the active session. |
| `confluence_search` in space `AISDLC`, maximum 3 pages | Not run; `confluence_search` is not exposed as a callable tool in the active session. |

Returned objects:

| Source | Object IDs | Compact summary |
| --- | --- | --- |
| Jira | None | No Jira results available; tools unavailable before restart. |
| Confluence | None | No Confluence results available; tools unavailable before restart. |

Limitations:

- This session confirmed configuration registration, not live Atlassian reads.
- The live smoke test must be rerun after restarting Codex and confirming the tool surface includes `jira_search` and `confluence_search`.
- No secrets, credentials, raw Jira payloads, or raw Confluence payloads were recorded.
