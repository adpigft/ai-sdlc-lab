# GitHub Actions Evidence

This folder contains the demo REST/CLI adapter for reading GitHub Actions evidence through the `gh` CLI.

The adapter does not write to GitHub. It reads workflow run history and the latest validation result for the configured repository.

## Environment Variables

- `GITHUB_OWNER`
- `GITHUB_REPO`
- Optional: `GITHUB_TOKEN` or `GH_TOKEN`

## Usage

List the latest workflow runs:

```bash
python3 scripts/github/evidence.py list-latest-workflow-runs
```

Read the latest validation workflow result:

```bash
python3 scripts/github/evidence.py latest-validation-result
```

The default validation workflow name is `AI SDLC Validation`.
