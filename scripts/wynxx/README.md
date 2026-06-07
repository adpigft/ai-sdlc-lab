# Wynxx Story Creator MCP Smoke Test

This folder documents the read-only Wynxx Story Creator backlog ingestion setup for Codex.

## Codex Setup

The Codex MCP entry uses the Wynxx package published in the Azure registry:

```toml
[mcp_servers.wynxx]
enabled = true
command = "npx"
args = [
  "-y",
  "@wynxx/mcp",
  "--instance",
  "playground.gft.aid.services.gft.com"
]

[mcp_servers.wynxx.env]
"npm_config_@wynxx:registry" = "https://pkgs.dev.azure.com/gft-assets/ai-impact-feed/_packaging/ai-impact-feed/npm/registry/"
```

## How To Smoke Test

Use Codex with the Wynxx Story Creator MCP server enabled and run read-only discovery only:

1. List available Wynxx Story Creator MCP tools.
2. List available projects.
3. Read one small backlog sample.
4. Normalize the candidate hierarchy into AI-SDLC concepts.
5. Stop before any Jira, Confluence, or Git writes.

## Expected Output

The smoke test should produce a compact summary with:

- project id
- project name
- epic count
- feature count
- user story count
- task count if available
- test case count if available
- one sample item title
- preserved source IDs

If the smoke test succeeds, write the normalized ingestion output to:

```text
build/wynxx/ingestion-result.json
```

## Troubleshooting

- If the MCP handshake stalls, refresh the Wynxx Story Creator OAuth session or token and retry.
- If the server never returns `tools/list`, treat the session as blocked and do not fabricate backlog content.
- Do not create Jira or Confluence writes from the smoke test.
- Do not create Intent, Specification, or Design artifacts automatically from Wynxx data.

## Rules

- Read-only only.
- Wynxx Story Creator is a candidate backlog source only.
- Git remains the source of truth.
- Jira and Confluence remain synchronized views, not Wynxx outputs.
