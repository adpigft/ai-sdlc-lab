# Confluence Publishing Foundation

This folder contains offline helpers for generating stakeholder-ready Confluence summary drafts from Git-owned AI SDLC artifacts.

The generator does not call Confluence APIs. Git remains the source of truth for intent, requirements, architecture, validation, release evidence, and traceability. Confluence pages are a published view only.

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
