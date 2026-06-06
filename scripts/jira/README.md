# Jira Integration Foundation

This folder contains offline helpers for preparing Jira issue payloads from Git-owned AI SDLC artifacts.

The generator does not call Jira APIs. It reads approved artifact files, applies local JSON templates, and emits draft payload JSON that can be reviewed before any future integration posts to Jira.

The REST/CLI demo adapter in `scripts/jira/rest_cli.py` is the execution path for demo-time Jira validation and opt-in writes. It validates a Jira project, drafts a story from an approved intent, adds Git and Confluence remote links, and transitions issue status when `--apply` is supplied.

## Issue Mapping

| Jira Issue Type | AI SDLC Source |
| --- | --- |
| Epic | Capability |
| Story | Feature |
| Task | Implementation slice |
| Sub-task | Optional engineering task under a Task |
| Defect | Defect / RCA finding |
| Decision | ADR |
| Release | Validation / release package |

## Usage

Generate payloads for a capability workflow state:

```bash
python3 scripts/jira/generate-jira-payloads.py \
  --workflow-state domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/workflow-state.yaml \
  --output-dir /tmp/jira-payloads
```

Print the payload bundle to stdout without writing files:

```bash
python3 scripts/jira/generate-jira-payloads.py \
  --workflow-state domains/payments/capabilities/payment-reversal/features/khqr-payment-reversal/workflow-state.yaml
```

## Inputs

The generator resolves artifact paths from `workflow-state.yaml`:

- `artifacts.intent`
- `artifacts.specification`
- `artifacts.architecture`
- `artifacts.test_design`
- `artifacts.implementation_plan`
- `artifacts.validation_report`
- `artifacts.release_notes`, when present
- `artifacts.traceability`

It also derives source links for:

- `domains/<domain>/domain-context.md`
- `domains/<domain>/capabilities/<capability>/capability-context.md`
- `workflow-state.yaml`

It also scans `decisions/ADR-*.md` for local decision payloads.

Functional and non-functional requirements are not generated as individual Stories. They are mapped into feature Story payload fields.

For KHQR Payment Reversal, the generated Story groups are:

1. Reversal Request Creation
2. Maker Checker Decision
3. Settlement Eligibility
4. Processor And Ledger Execution
5. Status Audit Reconciliation Observability
6. MVP Exclusions And Release Guards

Each Story includes:

- mapped FR/NFR IDs
- acceptance scenario IDs
- linked implementation slice IDs
- source artifacts

## Outputs

When `--output-dir` is supplied, the generator writes:

- `epic.json`
- `stories/*.json`
- `tasks/*.json`
- `subtasks/*.json`, reserved for optional engineering Sub-tasks
- `defects/*.json`
- `decisions/*.json`
- `release.json`
- `payload-bundle.json`

Every payload includes a `sourceArtifacts` field linking back to Git-owned domain context, capability context, workflow state, intent, specification, design, tests, implementation plan, validation report, and release notes when available.

Review the generated payloads before wiring any Jira API caller.

## REST / CLI Demo Adapter

Environment variables:

- `JIRA_BASE_URL`
- `JIRA_EMAIL`
- `JIRA_API_TOKEN`
- `JIRA_PROJECT_KEY`

Commands:

```bash
python3 scripts/jira/rest_cli.py validate-connection-project
python3 scripts/jira/rest_cli.py create-demo-story --intent domains/.../intent/intent.md
python3 scripts/jira/rest_cli.py add-links --issue-key PAY-123 --git-url https://github.com/... --confluence-url https://.../wiki/spaces/...
python3 scripts/jira/rest_cli.py transition-status --issue-key PAY-123 --to-status "In Progress"
```

Add `--apply` only after the reviewed change is explicitly approved for write-back.
