# Workflow 05: Release

## Purpose

Package, approve, and communicate a release with complete traceability and support readiness.

## Inputs

- Approved validation report.
- Release Jira ticket or change record.
- Pull requests, commits, build artifacts, and SonarCloud result.
- Operational readiness evidence.

## Steps

1. Confirm scope, release version, deployment window, and impacted customer journeys.
2. Confirm unresolved defects and risks have explicit acceptance.
3. Confirm rollback plan, monitoring, alerting, support contacts, and customer communication.
4. Prepare release notes using `framework/templates/release-notes-template.md`.
5. Update Confluence-facing release or operating pages where needed.
6. Capture production approval in Jira or the change-management system.
7. After release, collect feedback and update `feedback/feedback-log.md`.

## Outputs

- Release notes.
- Change approval reference.
- Production validation notes.
- Feedback entries.

## Human Gate

No production release may proceed on AI recommendation alone. A named human release approver must be recorded.
