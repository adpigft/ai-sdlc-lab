# End-to-End AI-SDLC Framework Smoke Test Report

## Test Date

2026-06-07 05:00:11 UTC

## Scope

- Demo feature: Card Replacement
- Excluded: Wynxx Story Creator MCP
- Focus: framework artifacts, Jira REST adapter, Confluence REST adapter, GitHub Actions evidence script, traceability, validation scripts, and Control Tower dashboard

## Scenarios Executed

1. Happy path flow
2. Jira integration check
3. Confluence integration check
4. GitHub Actions evidence check
5. Dashboard check
6. Negative test: missing traceability
7. Negative test: failed validation
8. Negative test: stale state
9. Full validation suite

## Results Summary

| Scenario | Status | Evidence |
| --- | --- | --- |
| Happy path flow | Partial pass | Local artifacts for Card Replacement exist; traceability row exists; dashboard JSON generated and includes Card Replacement, SCRUM-1, and Confluence page 688129. Live Jira/Confluence reads were blocked by DNS connectivity in this session. |
| Jira integration check | Blocked | `python3 scripts/jira/rest_cli.py validate-connection-project` failed with DNS resolution error for `adpi04.atlassian.net`. Direct Jira GETs also failed. |
| Confluence integration check | Blocked | `python3 scripts/confluence/rest_cli.py validate-space` failed with DNS resolution error for `adpi04.atlassian.net`. Direct Confluence GETs also failed. |
| GitHub Actions evidence check | Blocked | `gh` CLI is installed, but both evidence script reads failed with `error connecting to api.github.com`. No workflow was triggered. |
| Dashboard check | Pass | `bash scripts/dashboard/run-control-tower.sh` generated `build/dashboard/control-tower.json` and `build/dashboard/control-tower-data.js`. The generated JSON contains Card Replacement, SCRUM-1, 688129, TRACE-CARDREP-DEMO-001, PM Intervention, Delivery Pipeline, Traceability, Quality Gates, Governance, and Context Health sections. |
| Missing traceability negative test | Pass | Simulated Card Replacement with empty traceability rows using the dashboard generator logic. Result: `missing-traceability`, `sync-missing`, `traceabilityPresent=false`, `pm_intervention_trigger=true`. |
| Failed validation negative test | Pass | Existing feature `FEAT-KHQRREV-001` shows `validationStatus=Partial validation complete; release not ready`, `releaseReadinessStatus=Not ready`, and PM intervention reasons `blocked,failed-validation`. |
| Stale state negative test | Pass | Existing feature `FEAT-KHQR-001` shows `daysInState=3`, `expectedMaxDays=2`, and PM intervention reason `stale-state`. |
| Full validation suite | Pass | `git diff --check`, workflow state, artifacts, traceability, OpenAPI, Java, release readiness, workflow consistency, `node --check dashboard/control-tower.js`, and `python3 -m py_compile scripts/dashboard/generate-control-tower.py scripts/jira/rest_cli.py scripts/confluence/rest_cli.py scripts/github/evidence.py` all passed. |

## Evidence Captured

- Dashboard generator output in `build/dashboard/control-tower.json`
- Dashboard wrapper output in `build/dashboard/control-tower-data.js`
- Local dashboard layout and section anchors in `dashboard/control-tower.html`
- Dashboard renderer logic in `dashboard/control-tower.js`
- Jira adapter read failure from DNS resolution
- Confluence adapter read failure from DNS resolution
- GitHub evidence script read failure from `api.github.com`
- Simulated missing-traceability result for Card Replacement
- Local validation script output

## Jira Result

- Read-only connection validation attempted
- Existing issue `SCRUM-1` is mapped in traceability and dashboard JSON
- Live Jira verification was blocked by DNS resolution failure in this environment
- No Jira write was attempted

## Confluence Result

- Read-only space validation attempted
- Existing page `688129` is mapped in traceability and dashboard JSON
- Live Confluence verification was blocked by DNS resolution failure in this environment
- No Confluence write was attempted

## Dashboard Result

- Card Replacement appears in the generated dashboard JSON
- `SCRUM-1`, `688129`, and `TRACE-CARDREP-DEMO-001` are present in generated dashboard data
- PM Intervention, Executive Summary, Delivery Pipeline, Approval Queue, Squad View, Traceability, Quality Gates, Governance, and Context Health sections are present
- Dashboard remains static and read-only

## Validation Result

Passed:
- `node --check dashboard/control-tower.js`
- `python3 -m py_compile scripts/dashboard/generate-control-tower.py scripts/jira/rest_cli.py scripts/confluence/rest_cli.py scripts/github/evidence.py`
- `bash scripts/dashboard/run-control-tower.sh`
- `git diff --check`
- `bash scripts/validate-workflow-state.sh`
- `bash scripts/validate-artifacts.sh`
- `bash scripts/validate-traceability.sh`
- `bash scripts/validate-openapi.sh`
- `bash scripts/validate-java.sh`
- `bash scripts/validate-release-readiness.sh`
- `bash scripts/validate-workflow-consistency.sh`

## Issues Found

1. Jira and Confluence DNS resolution failed for `adpi04.atlassian.net` in this environment.
2. GitHub API access failed for `api.github.com` in this environment.
3. End-to-end live integration verification could not be completed from this session.

## Recommended Improvements

1. Confirm network access and DNS resolution for Atlassian and GitHub APIs before demo validation.
2. Re-run the Jira, Confluence, and GitHub evidence checks from a network-enabled demo environment.
3. Keep the REST/CLI adapters as the demo execution path until live connectivity is validated end to end.

## Demo Readiness Assessment

The framework is locally demo-ready for artifacts, traceability, validation, and the Control Tower dashboard.

It is not fully demo-ready for live end-to-end Jira, Confluence, and GitHub evidence checks from this session because external API connectivity is blocked here.

## Addendum: Connectivity Retest

- Connectivity retest timestamp: 2026-06-07 05:00:11 UTC
- DNS/curl evidence from terminal:
  - `nslookup adpi04.atlassian.net` passed
  - `curl -I https://adpi04.atlassian.net` returned HTTP 302 login redirect
  - `nslookup api.github.com` passed
  - `curl -I https://api.github.com` returned HTTP 200
- Jira read result:
  - Project `SCRUM` validated successfully
  - Issue `SCRUM-1` read successfully
  - Summary: `[AI-SDLC DEMO] Card Replacement: create replacement story`
  - Status: `To Do`
  - AI-SDLC references present: yes
- Confluence read result:
  - Space `AISDLC` validated successfully
  - Page `688129` read successfully
  - Title: `[AI-SDLC DEMO] Card Replacement Specification`
  - Source references present: yes
- GitHub evidence result:
  - `gh auth status` succeeded for the active `adpigft` account
  - `gh run list --repo adpigft/ai-sdlc-lab --limit 3` returned the latest workflow runs
  - No workflow was triggered
- Revised demo readiness status:
  - Read-only end-to-end integration checks are now passing for Jira, Confluence, and GitHub evidence reads.
  - The framework is demo-ready for the requested smoke-test scope, with no writes performed.
