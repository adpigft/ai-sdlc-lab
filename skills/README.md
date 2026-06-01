# Codex Skills

This folder is the canonical project-local Codex skill location for the AI SDLC.

Each skill follows the Codex folder-based structure:

```text
skill-name/
├── SKILL.md
├── references/
├── assets/
└── scripts/
```

## Available Skills

Use these skills in the AI SDLC order defined by `AGENTS.md`:

| Skill | Purpose |
| --- | --- |
| `ba-intent` | Capture discovery questions, business intent, scope, outcomes, assumptions, and approval gates. |
| `ba-specification` | Convert approved intent into functional requirements, NFRs, business rules, acceptance criteria, and open questions. |
| `architect-context` | Create architecture context, system boundaries, integration view, risks, and design assumptions. |
| `architect-api` | Create OpenAPI contracts from approved requirements and architecture context. |
| `qa-test-design` | Create acceptance tests and coverage scenarios from approved requirements and API contracts. |
| `traceability` | Maintain end-to-end traceability across intent, requirements, API, tests, validation, release, Jira, and Confluence. |
| `developer-implementation` | Generate implementation only after approved intent, specification, architecture, API, tests, and traceability. |
| `qa-validation` | Validate implementation against approved requirements, API contract, acceptance tests, and traceability. |
| `devsecops-release` | Prepare release notes, deployment readiness, rollback plan, monitoring checks, and release approval evidence. |
| `feedback` | Capture review findings, defects, change requests, stakeholder feedback, and controlled corrections. |

## Legacy Skill Notes

`.ai/skills-legacy/` contains legacy/reference role instructions only. New Codex work should use the folder-based skills in `skills/`.
