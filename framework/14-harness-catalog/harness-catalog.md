# Harness Catalog

## Purpose

Harnesses define the minimum guided environment for a task or change type.

They help the framework choose the right context, skill sequence, validation gates, and stop conditions.

## Harness Types

### Greenfield Feature Harness

- Purpose: start a new feature from intent
- Entry criteria: approved intent and target feature scope
- Required context packages: enterprise, domain, capability, feature
- Skills invoked: intent, requirements, design, test-design, implementation, validation
- Tools used: local repo, validations, traceability checks
- Validation gates: intent, spec, design, tests, traceability, release
- Outputs: approved feature artifacts and execution plan
- Stop conditions: missing approval or unclear scope

### Brownfield Discovery Harness

- Purpose: understand existing system before change
- Entry criteria: existing feature or service, unclear current state
- Required context packages: enterprise, domain, capability, current feature
- Skills invoked: repo-discovery, source-ingestion, change-request
- Tools used: repo inspection, docs review, traceability review
- Validation gates: current-state validation, impact analysis
- Outputs: current-state summary and impact notes
- Stop conditions: incompatible scope or missing ownership

### In-Flight Change Harness

- Purpose: handle a change on approved work in progress
- Entry criteria: change after spec approval
- Required context packages: approved feature and impacted context packages
- Skills invoked: change-request, design, test-design, validation
- Tools used: diff review, validation, traceability
- Validation gates: impact assessment, regression review, release readiness
- Outputs: controlled change plan
- Stop conditions: major impact without approval

### Major Change Harness

- Purpose: handle large scope or breaking change
- Entry criteria: design-approved item with major delta
- Required context packages: enterprise, domain, capability, feature, impacted dependencies
- Skills invoked: change-request, decision, design, test-design, release
- Tools used: impact analysis, review checks, validation suite
- Validation gates: architecture review, API review, security review, release risk review
- Outputs: change decision and revision plan
- Stop conditions: unresolved compatibility or governance gap

### Bug Fix Harness

- Purpose: fix a defect with minimal scope
- Entry criteria: validated defect or incident
- Required context packages: feature, defect context, impacted dependencies
- Skills invoked: defect-fix, validation, traceability-review
- Tools used: reproduction, targeted tests, diff review
- Validation gates: reproduce, fix, regression, traceability
- Outputs: defect fix and evidence
- Stop conditions: ambiguous root cause or wider change detected

### PR Review Harness

- Purpose: review a pull request against approved artifacts
- Entry criteria: PR ready for review
- Required context packages: feature and any impacted context packages
- Skills invoked: pr-review, traceability-review, validation
- Tools used: diff, tests, contract checks, review checks
- Validation gates: code, spec, design, API, test, security, traceability, release readiness
- Outputs: review report and findings
- Stop conditions: missing approval artifacts or major mismatch

### Release Readiness Harness

- Purpose: confirm release readiness
- Entry criteria: validated feature or release candidate
- Required context packages: feature, release context, operational context
- Skills invoked: release, validation, traceability-review
- Tools used: validation results, release notes, risk review
- Validation gates: release checklist and approval checks
- Outputs: release readiness record
- Stop conditions: unresolved risk or missing approvals

### Context Recovery Harness

- Purpose: rebuild usable context after loss, drift, or staleness
- Entry criteria: context package stale, missing, or inconsistent
- Required context packages: enterprise plus affected domain or feature context
- Skills invoked: repo-discovery, source-ingestion, context packaging tasks
- Tools used: context review, manifest check, drift review
- Validation gates: context quality and provenance checks
- Outputs: refreshed context package set
- Stop conditions: uncertain provenance or conflicting sources

### Migration Harness

- Purpose: support platform or domain migration
- Entry criteria: migration scope and target state defined
- Required context packages: enterprise, source, target, impacted features
- Skills invoked: change-request, design, validation, release
- Tools used: dependency review, impact analysis, validation
- Validation gates: compatibility, cutover, rollback, release readiness
- Outputs: migration plan and evidence
- Stop conditions: unassessed breaking change
