# ADR-0001: AI SDLC Source Of Truth

## Status

Accepted

## Date

2026-06-01

## Context

AI-assisted delivery creates more artifacts, drafts, prompts, summaries, and recommendations than a traditional SDLC. Without clear ownership, teams may treat generated text as approved evidence or lose the link between business intent, Jira work, code, tests, release decisions, and feedback.

The repository is being established before application code exists, so the first decision must define where authoritative SDLC information lives.

## Decision

This repository is the versioned source of truth for AI SDLC operating content, including workflows, skills, standards, templates, traceability, feedback, and ADRs.

Jira remains the system of record for work items, status, assignment, delivery approvals, defects, risks, and release scope.

GitHub remains the system of record for pull requests, commits, code review, and CI evidence.

SonarCloud remains the system of record for static analysis and quality gate results.

Confluence is a publication surface for approved operating-model content, not the canonical editing location.

AI-generated artifacts are drafts until a human approval gate records the decision in Jira, GitHub, or an ADR.

## Consequences

- SDLC templates and standards are reviewed through repository changes.
- Jira links must appear in intent, specs, validation, release notes, and traceability.
- Confluence pages should be generated or updated from approved repository content where practical.
- Pull requests and CI evidence must link back to Jira and requirement IDs once application code exists.
- AI recommendations cannot satisfy human approval gates.

## Payment Example

For KHQR payment initiation, a requirement such as duplicate payment prevention must be traceable from business intent to Jira, spec, API contract, test evidence, validation report, release approval, and post-release feedback.
