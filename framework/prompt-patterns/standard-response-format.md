# Standard Response Format

## Purpose

Make skill outputs consistent, predictable, and easy for users to follow.

Every skill should end with the standard response footer unless the user explicitly asks for a different format.

## Standard Response Footer

```text
Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
```

## Optional Sections

Use these sections only when they add clarity:

```text
Findings:
- ...

Validation:
- ...

Assumptions:
- ...

Files Changed:
- ...

No Changes Made:
- No files changed.
```

## Rules

- Every skill should end with the standard response footer.
- If no files are changed, say `No files changed.`
- If review finds issues, use `Findings`, `Blockers`, and `Next`.
- If an artifact is ready, use `Pending Review` and `Next`.
- If blocked, make the blocker explicit.
- Do not claim approval unless the user explicitly approved.
- Do not recommend moving forward if validation, workflow-state, traceability, or release evidence disagree.
- Keep the footer factual; avoid repeating long analysis already shown above it.

