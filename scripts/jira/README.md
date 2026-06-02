# Jira Integration Foundation

This folder contains offline helpers for preparing Jira issue payloads from Git-owned AI SDLC artifacts.

The generator does not call Jira APIs. It reads approved artifact files, applies local JSON templates, and emits draft payload JSON that can be reviewed before any future integration posts to Jira.

## Issue Mapping

| Jira Issue Type | AI SDLC Source |
| --- | --- |
| Epic | Capability |
| Story | Requirement group |
| Task | Implementation slice |
| Defect | Defect / RCA finding |
| Decision | ADR |
| Release | Validation / release package |

## Usage

Generate payloads for a capability workflow state:

```bash
python3 scripts/jira/generate-jira-payloads.py \
  --workflow-state domains/payments/capabilities/khqr-payment-reversal/workflow-state.yaml \
  --output-dir /tmp/jira-payloads
```

Print the payload bundle to stdout without writing files:

```bash
python3 scripts/jira/generate-jira-payloads.py \
  --workflow-state domains/payments/capabilities/khqr-payment-reversal/workflow-state.yaml
```

## Inputs

The generator resolves artifact paths from `workflow-state.yaml`:

- `artifacts.intent`
- `artifacts.specification`
- `artifacts.implementation_plan`
- `artifacts.validation_report`
- `artifacts.release_notes`, when present

It also scans `decisions/ADR-*.md` for local decision payloads.

## Outputs

When `--output-dir` is supplied, the generator writes:

- `epic.json`
- `stories/*.json`
- `tasks/*.json`
- `defects/*.json`
- `decisions/*.json`
- `release.json`
- `payload-bundle.json`

Review the generated payloads before wiring any Jira API caller.
