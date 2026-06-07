# Wynxx Backlog Ingestion

## Purpose

Wynxx Story Creator is a backlog candidate source for the AI-SDLC lab.

It is not the source of truth. It provides candidate work items that must be reviewed before any Git-owned AI-SDLC artifact is created.

## Role In The Flow

- Wynxx supplies backlog candidates for discovery and review.
- Git remains the source of truth after human approval.
- Jira and Confluence are not created or updated automatically from Wynxx.
- AI-SDLC intent, specification, design, implementation, validation, and release artifacts are not created automatically from Wynxx.

## Mapping Model

| Wynxx Item | AI-SDLC Candidate Mapping |
| --- | --- |
| Epic | Capability Candidate |
| Feature | Feature Candidate |
| User Story | Intent Input |
| Task | Implementation Work Item Candidate |
| Test Case | Validation Input Candidate |

## Read-Only Smoke Test Status

The Codex session was configured with the Wynxx MCP server entry, but the live MCP handshake did not complete in this environment.

Observed result:

- `@wynxx/mcp` resolves from the configured Azure registry.
- The package exposes the `wynxx-mcp` binary.
- The server startup requires OAuth-backed interaction and did not produce a usable read-only `tools/list` response in this session.
- No backlog project or backlog sample was returned.

## Token And Auth Limitation

- If the Wynxx OAuth session is expired or unavailable, refresh the token or re-authenticate before retrying.
- Do not treat a stalled handshake as valid backlog data.
- Do not fabricate backlog items when MCP access is unavailable.

## Human Review Rule

AI-SDLC artifacts must not be created from Wynxx candidate input until a human approves the mapping and scope.

## Notes

- Preserve Wynxx source IDs in any future normalized ingestion output.
- Use read-only MCP operations only for backlog discovery.
- Do not create Jira tickets, Confluence pages, or Git artifacts automatically from Wynxx output.
