# Confluence Publishing Foundation

This folder contains offline helpers for generating stakeholder-ready Confluence summary drafts from Git-owned AI SDLC artifacts.

The generator does not call Confluence APIs. Git remains the source of truth for intent, requirements, architecture, validation, release evidence, and traceability. Confluence pages are a published view only.

The REST/CLI demo adapter in `scripts/confluence/rest_cli.py` is the execution path for demo-time validation and opt-in publishing. It validates a space, publishes an approved Git artifact page, and updates an existing page by title when `--apply` is supplied.

## Summary Templates

| Template | Source Artifacts |
| --- | --- |
| `capability-summary.md` | `workflow-state.yaml`, `intent.md`, `specification.md` |
| `feature-summary.md` | `workflow-state.yaml`, `intent.md`, `specification.md`, design path, traceability path |
| `design-summary.md` | `workflow-state.yaml`, `design.md`, OpenAPI path |
| `validation-summary.md` | `workflow-state.yaml`, `validation-report.md`, traceability path |
| `release-summary.md` | `workflow-state.yaml`, `validation-report.md`, optional release notes |

## Usage

Generate a combined summary bundle to stdout:

```bash
python3 scripts/confluence/generate-summary.py \
  --workflow-state domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/workflow-state.yaml
```

Write individual Markdown summary drafts for review:

```bash
python3 scripts/confluence/generate-summary.py \
  --workflow-state domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/workflow-state.yaml \
  --output-dir /tmp/confluence-summaries
```

## Output Files

When `--output-dir` is supplied, the generator writes:

- `capability-summary.md`
- `feature-summary.md`
- `design-summary.md`
- `validation-summary.md`
- `release-summary.md`

Review generated summaries before wiring any future Confluence publisher.

## REST / CLI Demo Adapter

Environment variables:

- `JIRA_BASE_URL`
- `JIRA_EMAIL`
- `JIRA_API_TOKEN`
- `CONFLUENCE_SPACE_KEY`

Commands:

```bash
python3 scripts/confluence/rest_cli.py validate-space
python3 scripts/confluence/rest_cli.py publish-approved-git-artifact-page --source framework/06-tool-integrations/demo-rest-cli-adapter-plan.md
python3 scripts/confluence/rest_cli.py update-page-by-title --title "Demo REST/CLI Adapter Plan" --source framework/06-tool-integrations/demo-rest-cli-adapter-plan.md
```

Add `--apply` only after the reviewed change is explicitly approved for write-back.
