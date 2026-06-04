---
name: repo-discovery
description: Extract repo architecture, coding, testing, API, security, and delivery conventions from an existing codebase.
---

# Repo Discovery Skill

## Purpose

Analyze an existing repository to extract architecture, coding, testing, API, security, and delivery conventions.

## When To Use

Use `$repo-discovery` when a team receives an existing repository or needs to bootstrap standards from an existing implementation.

## Inputs Needed

- Repository path
- Technology stack
- Target scope
- Areas to inspect
- Known standards

## Framework Adapter

When this skill is used inside this repository, context loading and human review expectations are defined by:

- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/01-lifecycle/skill-orchestration-adapter.md`

## Procedure

1. Inspect the repository structure and relevant implementation areas.
2. Identify technology stack, architecture patterns, API style, event style, testing style, coding conventions, security patterns, and CI/build patterns.
3. Note reusable components and any gaps or risks.
4. Summarize findings so standards can be updated or documented.
5. Stop for human review before treating recommendations as policy.

## Outputs Produced

- Repo discovery summary
- Recommended standards updates
- Reusable component notes
- Gaps and risks list

## Artifact Structure

1. Repository Overview
2. Technology Stack
3. Folder Structure
4. Architecture Pattern
5. API Style
6. Event Style
7. Testing Style
8. Coding Standards
9. Security Patterns
10. Build / CI/CD Patterns
11. Reusable Components
12. Gaps / Risks

## Quality Checks

- Findings are grounded in the inspected repository.
- The summary separates observation from recommendation.
- Gaps and risks are visible.
- No source code is changed by this skill.

## Stop Conditions

- Repository path is missing.
- Target scope is unclear.
- The user asks for standards enforcement rather than discovery.

## Human Approval Expectations

Human review is required before discovery findings become repository standards.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
