---
name: jira-lifecycle
description: Manage Jira lifecycle using manual content or MCP/API integration when available. Use when issues, statuses, comments, or links need to be created or updated.
---

# Jira Lifecycle Skill

## Purpose
Manage Jira lifecycle using manual content or MCP/API integration when available.

## When to use
Use when Jira issues, statuses, comments, or links need to be created or updated.

## Inputs
- Jira issue content
- manual updates or MCP/API context
- related artifacts

## Process
1. Prepare issue content.
2. Create or update issue records when integration is available.
3. Link related work items.
4. Record the outcome in source-controlled artifacts when required.

## Outputs
- Jira updates
- issue links
- lifecycle notes

## Quality checks
- no hardcoded credentials
- issue content is traceable
- status changes are explicit

## Human gate
Human approval is required before lifecycle changes are published.

## Next skill
confluence-publisher

