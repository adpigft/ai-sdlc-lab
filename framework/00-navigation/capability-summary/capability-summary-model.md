# Capability Summary Model

## Purpose

A capability summary is a lightweight single-page navigation aid for one capability. It improves context loading, token efficiency, and user navigation by pointing to the current state, active artifacts, ownership, placement, integrations, validation, release status, and next command.

The summary is not a source of truth.

## Authority Rules

- Source artifacts remain authoritative.
- `workflow-state.yaml` remains authoritative for lifecycle state, current skill, active artifact, pending gate, blockers, approvals, and next command.
- Intent, requirements, architecture, API contract, tests, implementation plan, validation report, release notes, traceability, and feedback artifacts remain authoritative for their own content.
- If a summary disagrees with a source artifact, treat the summary as stale and report the inconsistency.

## When A Capability Summary Is Useful

Use a capability summary when:

- users need a fast orientation point
- a capability has many artifacts
- multiple squads need to understand ownership and placement quickly
- context loading needs to stay small
- `Status.` should be easier to explain to non-technical users
- release, validation, traceability, or implementation placement is being reviewed

For a small lab capability, the summary is optional. For 3+ squads, it is recommended. For 10+ squads, it should be generated and validated.

## When It Should Be Generated

Generate a capability summary after the capability has enough source artifacts to summarize meaningfully, usually after one of these points:

- intent and workflow state are created
- requirements is approved
- architecture and placement metadata are available
- implementation plan is approved
- validation evidence exists
- release readiness is being prepared

Do not generate a summary before the source artifacts exist.

## When It Should Be Refreshed

Refresh the summary when any of these change:

- `workflow-state.yaml`
- approved artifact status
- pending gate or blockers
- implementation placement metadata
- APIs, events, or integrations
- NFR highlights
- validation status
- release status
- traceability status
- next command

## Generation And Validation

Capability summaries should be generated or validated where possible. Manual summaries are acceptable during early pilots, but the preferred future model is:

- generate from source artifacts
- validate referenced paths
- validate lifecycle state against `workflow-state.yaml`
- validate traceability and release status against source evidence
- fail or warn when the summary is stale

## What A Summary Must Not Do

A capability summary must not:

- replace intent
- replace requirements
- replace architecture or ADRs
- replace API contracts
- replace test design
- replace implementation plans
- replace validation reports
- replace release notes
- replace traceability
- override workflow state
- invent approvals or release readiness

