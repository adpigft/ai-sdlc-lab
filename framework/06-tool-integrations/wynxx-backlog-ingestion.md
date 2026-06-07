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

`codex mcp list` shows `wynxx` is registered and enabled in Codex:

- Command: `npx`
- Args: `-y @wynxx/mcp --instance playground.gft.aid.services.gft.com`
- Auth status in Codex registry: `Unsupported`
- Enabled tools in Codex registry: not enumerated

The installed `@wynxx/mcp` package exposes these tools in the server code path:

### Safe read-only tools

- `list_doc_prompts`
- `list_audiences`
- `list_projects`
- `get_project`
- `list_backlogs`
- `get_backlog`
- `get_work_item`
- `list_test_prompts`
- `list_llms`
- `list_jobs`
- `list_jobs_by_type`
- `list_job_types`
- `list_sast`
- `list_sast_by_type`
- `list_sast_types`

### Authentication tools

- `authenticate`

### Write / mutation tools

- `set_llm`
- `set_repo`
- `set_pull_request`
- `set_doc_prompt`
- `set_audience`
- `set_test_prompt`
- `refresh_settings`

### Job-starting / long-running tools

- `run_review`
- `start_review`
- `run_full_review`
- `start_fixer`
- `run_fixer`
- `start_tester`
- `run_tester`
- `start_repo_documenter`
- `run_repo_documenter`
- `monitor_job`
- `monitor_fixer`
- `get_fixer_status`
- `monitor_tester`
- `get_tester_status`

## Expected Notes Compared To Actual Surface

| Expected note | Actual Wynxx tool surface |
| --- | --- |
| `authenticate` | Present as `authenticate` and required by many job / AI tools. |
| `list_use_cases` | Not exposed. Closest actual read tools are `list_projects`, `list_backlogs`, and `get_project`. |
| `get_use_case` | Not exposed. Closest actual read tools are `get_project`, `get_backlog`, and `get_work_item`. |
| `get_backlog_item` | Not exposed. Closest actual read tool is `get_work_item`. |
| `edit_backlog_item` | Not exposed. No direct backlog edit tool is exported. |
| `delete_backlog_item` | Not exposed. No direct backlog delete tool is exported. |
| `create_child_item` | Not exposed. No direct child-item creation tool is exported. |
| `refresh_settings` | Present as `refresh_settings`, but it refreshes server-side cache and should be treated as mutation / non-demo. |

Observed runtime result in this session:

- The package resolves from the configured Azure registry.
- The server binary is `wynxx-mcp`.
- OAuth-backed authentication is required for runtime access.
- A usable read-only `tools/list` result was not obtained in this session.
- No backlog project or backlog sample was returned.

Minimal auth smoke test in this session:

- Authentication status: ok
- `list_llms` result count: 1
- First LLM name: `GPT4-o`
- No backlog data was fetched
- No write or job-starting tool was called

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

## Forbidden For Demo

- `authenticate`
- `set_llm`
- `set_repo`
- `set_pull_request`
- `set_doc_prompt`
- `set_audience`
- `set_test_prompt`
- `run_review`
- `start_review`
- `run_full_review`
- `start_fixer`
- `run_fixer`
- `start_tester`
- `run_tester`
- `start_repo_documenter`
- `run_repo_documenter`
- `monitor_job`
- `monitor_fixer`
- `get_fixer_status`
- `monitor_tester`
- `get_tester_status`
- `refresh_settings`

## Next Recommended Smoke Test

After Wynxx OAuth is refreshed, run a read-only discovery sequence only:

1. `list_projects`
2. `get_project`
3. `list_backlogs`
4. `get_backlog`
5. `get_work_item`

Stop before any mutation or job-starting tool.
