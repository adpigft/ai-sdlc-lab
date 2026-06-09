# AI Code Review Standard

## Purpose

Define how AI-generated or AI-assisted engineering work must be reviewed before it is accepted into enterprise delivery.

## Review Principle

AI output is untrusted until reviewed, tested, and approved by accountable humans. AI may draft code, tests, design text, migration plans, and review notes only within the approved lifecycle stage and scope.

## Required Review Focus

| Area | Review Questions |
| --- | --- |
| Scope | Does the change stay inside approved intent, requirements, design, and implementation plan? |
| Traceability | Does the change link to requirements, design decisions, tests, validation evidence, and Jira where applicable? |
| Architecture | Does it preserve clean architecture, ownership boundaries, and allowed paths? |
| Security | Does it avoid sensitive-data leakage, weak auth, unsafe defaults, and secret exposure? |
| API/Event compatibility | Does it preserve contract compatibility or document approved breaking changes? |
| Data safety | Does it preserve migration safety, auditability, retention, and rollback options? |
| Tests | Are tests meaningful, deterministic, and mapped to approved behavior? |
| Operational readiness | Are logs, metrics, traces, alerts, and runbook impacts considered? |
| Maintainability | Is the implementation simple, readable, and aligned to project conventions? |

## AI-Generated Code Rules

- Do not accept generated code that bypasses approved artifacts.
- Do not accept generated code that modifies unrelated paths.
- Do not accept generated code that hardcodes credentials, endpoints, tokens, or customer data.
- Do not accept generated tests that assert invented behavior.
- Do not accept generated migrations without rollback and compatibility review.
- Do not accept generated API or event contracts without owner and consumer review.

## Review Evidence

PR review must record:

- AI-assisted areas
- prompt assumptions that materially shaped the output
- files changed
- tests and validation evidence
- known limitations or unresolved questions
- human approval outcome

## Human Accountability

AI does not approve intent, requirements, design, tests, implementation, validation, release, security risk, architecture decisions, or production changes. Accountable owners remain responsible for final approval.

