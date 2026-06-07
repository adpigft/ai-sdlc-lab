# Artifact Editing Workflow

## Purpose

This workflow defines how a GUI-based editor should interact with Git-owned artifacts.

## Workflow

1. view artifact
2. edit draft
3. validate
4. submit for approval
5. commit / PR
6. sync Jira / Confluence after approval

## Rules

- editing must happen against a draft
- validation must occur before approval submission
- Git commit or pull request is the source-of-truth transition
- Jira and Confluence sync happen only after approval

## Notes

- The workflow is future-state and optional.
- Silent overwrite is not allowed.
- The workflow should preserve auditability end to end.
