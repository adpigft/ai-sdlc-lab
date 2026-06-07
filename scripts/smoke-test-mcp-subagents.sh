#!/usr/bin/env bash
set -euo pipefail

cat <<'EOF'
AI-SDLC MCP Subagent Smoke Test Prompts
======================================

These prompts are read-only. They must not create Jira tickets, publish Confluence pages,
change GitHub repository state, or create AI-SDLC artifacts.

Required environment variables:
- WYNXX_MCP_URL
- WYNXX_API_TOKEN
- ATLASSIAN_SITE_URL
- ATLASSIAN_EMAIL
- ATLASSIAN_API_TOKEN
- JIRA_PROJECT_KEY
- CONFLUENCE_SPACE_KEY
- GITHUB_TOKEN
- GITHUB_OWNER
- GITHUB_REPO

1. wynxx-backlog-agent
----------------------
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

2. jira-lifecycle-agent
-----------------------
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

3. confluence-publisher-agent
-----------------------------
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

4. github-evidence-agent
------------------------
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
EOF
