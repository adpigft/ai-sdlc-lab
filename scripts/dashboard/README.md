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

For the best experience, serve the repo locally and open the dashboard through HTTP:

```bash
python3 -m http.server 8080
```

Then open:

```text
http://localhost:8080/dashboard/control-tower.html
```

Local HTTP mode enables 30-second auto-refresh from `build/dashboard/control-tower.json`.
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
- Use the delivery pipeline to see status, owner, next gate, and Jira / Confluence references.
- Use the approval queue to see where work is waiting.
- Use the traceability view to confirm the end-to-end artifact chain.
- Use the quality gate view to spot missing artifacts.
- Use the PM intervention view to identify stalled or incomplete work.

## Known Limitations

- The dashboard is static and read-only.
- It does not call Jira, Confluence, or GitHub APIs.
- It relies on locally generated JSON and Git-owned artifacts.
- Features without workflow-state files derive state from artifact metadata.
- GitHub validation evidence is summarized from local validation reports when available.
- No approval or write-back actions are available yet.
- The UI intentionally stays separate from Wynxx branding and assets.
