# Centralized Dashboard Publishing

## Purpose

Define the publishing model for the AI-SDLC Control Tower dashboard so the local demo view stays separate from the official delivery view.

## Local Versus Central

- The local dashboard is for demo and developer preview only.
- The production dashboard must read from central Git, not from an individual laptop or a local working tree.
- Local generation is useful for iteration, but it is not authoritative.

## Publishing Model

- GitHub Actions generates `build/dashboard/control-tower.json` on pull requests and on the `main` branch.
- Pull request builds can show proposed feature state from the branch under review.
- `main` branch builds are the official delivery view.
- The PM dashboard should refresh from a published build artifact rather than from a local machine.

## Safe MVP Workflow

1. Repository changes update dashboard input artifacts in Git.
2. GitHub Actions runs the dashboard generator.
3. GitHub Actions validates the generated dashboard assets.
4. GitHub Actions uploads the dashboard build as an artifact.
5. No external dashboard publishing occurs yet.

## Future Hosting Options

- GitHub Pages
- S3 and CloudFront
- Internal portal backend

## Operational Rules

- Git remains the source of truth.
- The dashboard is read-only.
- The dashboard must not become a hidden write path.
- Dashboard publishing must never skip validation.
- PR and `main` outputs must remain distinguishable.

## Recommended Branch Behavior

- Pull request runs should publish the dashboard artifact only for review.
- Main branch runs should publish the dashboard artifact as the official delivery package.
- Any future hosted dashboard should point to the published artifact or a central Git-backed data source, not to a developer workspace.

## Notes

- This document defines the target control model for a future centralized dashboard service.
- It does not introduce authentication, RBAC, editing, approval actions, or external publishing.
