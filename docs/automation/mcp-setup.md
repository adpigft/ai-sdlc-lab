# MCP Setup

## Purpose

Model Context Protocol integrations are optional enterprise collaboration helpers for this AI SDLC lab. They can help Codex read or update Jira, Confluence, and GitHub context when an enterprise environment provides approved MCP servers.

MCP does not replace repository governance.

## Source Of Truth Rules

- Git is the source of truth for specs, tests, code, traceability, release artifacts, standards, workflows, and ADRs.
- GitHub Actions is the system of record for CI gates.
- Jira MCP is for collaboration with Jira work items, approvals, and status. Jira remains a delivery tracking system, not the canonical artifact store.
- Confluence MCP is for collaboration and publication. Confluence is not the source of truth for SDLC artifacts in this repository.
- GitHub MCP is optional assistance for repository and pull request collaboration. GitHub Actions remains authoritative for CI results.

## Configuration

The placeholder configuration lives in `.codex/config.toml`.

Do not hardcode tokens in repository files. Use environment variables only.

Expected environment variables:

| Integration | Variables |
| --- | --- |
| Jira | `JIRA_BASE_URL`, `JIRA_EMAIL`, `JIRA_API_TOKEN` |
| Confluence | `CONFLUENCE_BASE_URL`, `CONFLUENCE_EMAIL`, `CONFLUENCE_API_TOKEN` |
| GitHub | `GITHUB_TOKEN`, `GITHUB_OWNER`, `GITHUB_REPO` |

## Enablement Checklist

1. Confirm the MCP server package or binary is approved by enterprise security.
2. Configure credentials through approved environment variables or secret management.
3. Keep `.codex/config.toml` free of secrets.
4. Verify MCP access is read-limited unless write access is explicitly approved.
5. Record any workflow change in `AGENTS.md` and relevant operating documentation.

## Safety Rules

- Do not paste production customer data, secrets, payment credentials, or private keys into MCP prompts.
- Do not treat MCP output as approved evidence unless it links to the authoritative source.
- Do not let MCP-generated Jira or Confluence content bypass human gates.
- Do not use MCP to override GitHub Actions CI gates.
