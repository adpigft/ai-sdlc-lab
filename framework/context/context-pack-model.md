# Context Pack Model

## Purpose

Define lightweight context routing and token discipline for AI SDLC work without adding heavy indexing, vector databases, or search tooling.

The goal is simple: `current_skill` plus `workflow-state.yaml` determines what Codex should read, what it may read if needed, what it must avoid, and when it must stop.

## Core Rule

Read the smallest set of authoritative artifacts required for the current lifecycle stage.

Do not read the whole repository unless the user explicitly asks for a framework or repository-wide assessment.

## Source Artifacts Remain Authoritative

Context packs and indexes are navigation aids only.

Authoritative sources remain:

- `workflow-state.yaml` for current state, current skill, pending gate, blockers, and artifact paths
- domain context under `domains/<domain>/domain-context.md`
- capability artifacts under `domains/<domain>/capabilities/<capability>/`
- framework standards, templates, and workflow docs
- traceability and feedback artifacts
- approved source code inside allowed implementation paths

Indexes must not replace or override source artifacts.

## Required Reads

Required reads are the files that must be loaded before work starts for a stage.

Examples:

- active skill `SKILL.md`
- active capability `workflow-state.yaml`
- active domain `domain-context.md`
- the artifact owned by the current stage
- required framework guidance for the current stage

If a required read is missing, stop and report the blocker.

## Optional Reads

Optional reads are only loaded when the current task needs them.

Examples:

- standards for API, security, testing, or coding
- Jira or Confluence generator notes
- service, frontend, or shared asset ownership guidance
- related domain context when cross-domain impact is identified
- traceability when coverage, validation, release, change, or defect impact is being reviewed

Optional reads should be purposeful and explained briefly.

## Forbidden Reads

Forbidden reads are files or directories that should not be loaded for a stage because they waste tokens or create risk.

Examples:

- source code before implementation approval
- unrelated domains
- unrelated capabilities
- unrelated services or frontend modules
- generated payload directories
- archives unless the user explicitly asks

Forbidden reads may become escalation reads only when a real dependency, defect, or approval requires them.

## Escalation Reads

Escalation reads are additional files loaded after the minimum context proves insufficient.

Use escalation reads when:

- a required artifact references another artifact
- cross-domain impact is discovered
- a test, validation, defect, or release issue needs evidence
- placement metadata points to existing code in approved paths
- an approval, blocker, or open question cannot be understood from required reads

Before using an escalation read, prefer the narrowest specific file or path.

## Token Discipline

Use these rules:

- Read stage-specific context first.
- Prefer `workflow-state.yaml` artifact paths over repository-wide search.
- Prefer domain context over unrelated capability examples.
- Prefer exact files over folders.
- Use `rg` for targeted lookup.
- Summarize long artifacts instead of repeatedly re-reading them.
- Do not load all framework docs for ordinary lifecycle work.
- Do not load source code until implementation or validation requires it.
- Stop when a missing approval or blocker makes further reading unnecessary.

## Context Pack Shape

Each stage context pack defines:

- purpose
- required reads
- optional reads
- forbidden reads
- expected outputs
- stop conditions

The stage context pack is a routing guide. It does not replace the active skill.

## Practical Flow

1. Read the active skill.
2. Read `workflow-state.yaml` when a capability exists.
3. Read the domain context for the active domain.
4. Read only the current stage artifact and required upstream artifacts.
5. Read placement metadata before code-impacting work.
6. Escalate only when evidence requires it.
7. Stop on missing approval, missing artifact, missing placement, or restricted path impact.
