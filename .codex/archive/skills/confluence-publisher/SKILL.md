---
name: confluence-publisher
description: Publish approved summaries to Confluence using manual content or MCP/API integration when available. Use when approved content needs publishing, while Git remains source of truth.
---

# Confluence Publisher Skill

## Purpose
Publish approved summaries to Confluence using manual content or MCP/API integration when available.

## When to use
Use when approved content needs publishing to Confluence while Git remains the source of truth.

## Inputs
- approved summary
- source-controlled artifacts
- Confluence target page details

## Process
1. Prepare the approved summary.
2. Publish or update the page when integration is available.
3. Keep Git as the source of truth.
4. Record the published location.

## Outputs
- Confluence page content
- publishing record

## Quality checks
- approved content only
- source of truth remains in Git
- publishing is traceable

## Human gate
Human approval is required before publishing.

## Next skill
sprint-planning

