# Skill Context Adapter

## Purpose

Define how generic skills load context inside this AI-SDLC framework.

Skills describe reusable procedures. This adapter decides what the skill should read, may read, must avoid, and when it must escalate or stop.

## Always-On Reads

For normal feature delivery, read only:

- the active skill document
- the active `workflow-state.yaml`, when a feature exists
- the active domain context
- the active capability context, when available
- the active feature artifacts required by the current stage
- the relevant stage context pack in `framework/02-context-control/context/stage-context-packs.md`

Do not load the full `framework/` folder during normal feature delivery.

## Stage-Specific Reads

Stage-specific reads are defined in:

```text
framework/02-context-control/context/stage-context-packs.md
```

Use the stage pack to choose required, optional, forbidden, and escalation reads.

## Optional Reads

Optional reads are allowed only when needed for the active task:

- same-domain examples for style
- standards relevant to the active stage
- Jira or Confluence guidance when generating offline payloads or summaries
- indexes or capability summaries as navigation aids
- related domain context when impact analysis identifies cross-domain impact

Indexes and summaries do not replace source artifacts.

Support skills such as `capability-onboarding`, `source-ingestion`, `repo-discovery`, and `artifact-review` may use the same context-loading principles, but they are not lifecycle stages and should still read only the smallest relevant source set.

## Forbidden Reads

Unless explicitly required by the active stage or approved impact analysis, do not read:

- unrelated domains
- unrelated feature artifacts
- source code before implementation
- source outside approved paths during implementation or PR review
- restricted paths without owner approval
- release artifacts during early-stage delivery
- full framework folders during normal feature work

## Escalation Rules

Escalate before reading broader context when:

- another domain is impacted
- a shared asset is impacted
- source code outside approved scope is needed
- restricted paths are needed
- API or event producer-consumer compatibility needs review
- validation, traceability, release notes, or workflow state disagree

Escalation should identify the owner, reason, and smallest additional context needed.

## Token Discipline

- Start from current skill and workflow state.
- Prefer explicit artifact paths over repository-wide search.
- Read source artifacts before summaries.
- Read only directly relevant standards.
- Use indexes only for routing.
- Summarize long artifacts instead of loading unrelated content.
- Full framework reads are reserved for framework assessment or framework changes.

## Source Of Truth

Source artifacts remain authoritative:

- `workflow-state.yaml` is authoritative for lifecycle state.
- Domain context is authoritative for domain boundary.
- Capability context is authoritative for capability boundary.
- Feature artifacts are authoritative for delivery scope.
- Traceability is authoritative for requirement-to-evidence links.
- Validation and release artifacts are authoritative for validation and release evidence.
