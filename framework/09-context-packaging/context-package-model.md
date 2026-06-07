# Context Package Model

## Purpose

Define a context package as a versioned library of curated delivery context.

Packages help squads reuse approved context without copying raw project data into prompts.

## Package Types

- enterprise context
- domain context
- capability context
- project context
- squad context
- feature context
- operational context

## Package Rules

- Each package must have a stable ID and version.
- Each package must declare scope, ownership, and classification.
- Each package must include sources and provenance.
- Each package must include security scan status before distribution.
- Each package must declare a token budget target where relevant.
- Each package must be reviewable and reusable.

## Sample Metadata

```yaml
id: ctx-cap-cards-001
version: 1.0.0
owner: Cards Squad
scope: capability
classification: internal
dependencies:
  - ctx-enterprise-001
  - ctx-domain-cards-001
sources:
  - domains/cards/capabilities/card-lifecycle-management/capability-context.md
  - traceability/traceability-matrix.md
approved_by:
  - Solution Architect
  - Product Owner
last_reviewed: 2026-06-06
expires_on: 2026-09-06
security_scan_status: passed
provenance:
  source_commit: abc1234
  source_branch: main
  generated_from: Git
token_budget: 12000
```

## Notes

- Context packages are derived assets, not source-of-truth replacements.
- Sensitive data should be excluded unless explicitly approved and classified.
