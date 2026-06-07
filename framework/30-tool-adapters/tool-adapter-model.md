# Tool Adapter Model

## Purpose

Tool adapters let the framework work with external systems without making those systems the source of truth.

Git remains the system of record.

## Core Rule

- tools are synchronized views, not source of truth
- adapter output is derived from Git-owned artifacts and approved workflow state
- external systems may mirror reviewed state, but they do not own it

## Adapter Pattern

The framework should support adapters for:

- Jira
- Confluence
- GitHub
- GitLab
- Azure DevOps
- ServiceNow
- SharePoint
- Wynxx

## Generic External Reference Model

Each external reference should support:

- system
- type
- external_id
- url
- sync_status
- last_synced_at

## Notes

- This layer is future-state and optional.
- The adapter layer should preserve traceability even when tools change.
- The adapter layer should avoid encoding tool-specific truth into Git-owned artifacts.
