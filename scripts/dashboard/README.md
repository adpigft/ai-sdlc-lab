# Control Tower Dashboard

This folder contains the static AI-SDLC Control Tower dashboard MVP.

The dashboard is read-only. It does not edit Git artifacts, update Jira, or publish Confluence.

## Generate Dashboard Data

```bash
bash scripts/dashboard/run-control-tower.sh
```

This command:

1. Scans `domains/**` for feature artifacts.
2. Reads `traceability/traceability-matrix.md`.
3. Generates `build/dashboard/control-tower.json`.
4. Generates `build/dashboard/control-tower-data.js` for local browser loading.
5. Prints the dashboard file path to open.

## Open Locally

Open:

```text
dashboard/control-tower.html
```

The page reads the generated `build/dashboard/control-tower-data.js` wrapper when available and falls back to `build/dashboard/control-tower.json`.
The top of the page includes an executive KPI strip. Governance includes the workflow ownership matrix and the future context-health section.

For the best experience, serve the repo locally and open the dashboard through HTTP:

```bash
python3 -m http.server 8080
```

Then open:

```text
http://localhost:8080/dashboard/control-tower.html
```

Local HTTP mode enables 30-second auto-refresh from `build/dashboard/control-tower.json`.
Use the top-right `Refresh Dashboard` button for an immediate refresh.
If you open the page directly with `file://`, the dashboard still renders from the generated wrapper data, but auto-refresh is disabled.

## Files Scanned

- `domains/**/features/**/intent/intent.md`
- `domains/**/features/**/specification/specification.md`
- `domains/**/features/**/design/design.md`
- `domains/**/features/**/tests/acceptance.feature`
- `domains/**/features/**/contracts/openapi.yaml`
- `domains/**/features/**/validation/validation-report.md`
- `domains/**/features/**/release/release-notes.md`
- `domains/**/features/**/workflow-state.yaml`
- `traceability/traceability-matrix.md`

## How PM Should Use It

- Review the featured feature card and the intervention list first.
- Use the sticky left navigation to jump between sections during demos.
- Use the KPI strip for a quick executive readout before drilling into tables.
- Use the delivery pipeline to see status, owner, current gate, and Jira / Confluence references.
- Use the approval queue to see where work is waiting.
- Use the traceability view to confirm the end-to-end artifact chain.
- Use the quality gate view to spot missing artifacts.
- Use the PM intervention view to identify stalled or incomplete work.
- Use the governance section for read-only operating rules and the ownership matrix.
- Use the context-health section for the future context observability placeholder.

## Known Limitations

- The dashboard is static and read-only.
- It does not call Jira, Confluence, or GitHub APIs.
- It relies on locally generated JSON and Git-owned artifacts.
- Features without workflow-state files derive state from artifact metadata.
- GitHub validation evidence is summarized from local validation reports when available.
- No approval or write-back actions are available yet.
- The UI intentionally stays separate from Wynxx branding and assets.
