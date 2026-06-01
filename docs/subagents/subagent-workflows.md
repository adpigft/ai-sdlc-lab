# Subagent Workflows

## Purpose

Subagents may be used for parallel review in this repository. They are not the normal sequential SDLC workflow and must not bypass the active skill order defined in `AGENTS.md`.

## Default Rule

The normal delivery workflow remains sequential:

1. Intent.
2. Specification.
3. Architecture context.
4. API contract.
5. QA test design.
6. Traceability.
7. Implementation.
8. Validation.
9. Release.
10. Feedback.

Subagents are allowed only as review helpers after an artifact exists or when a human asks for parallel critique.

## Appropriate Subagent Uses

- Independent security review of a completed specification.
- Independent QA coverage review of acceptance scenarios.
- Architecture consistency review across context, API, and traceability.
- Release readiness review comparing validation evidence, risks, and release notes.
- Documentation consistency review across README, AGENTS, Confluence docs, and ADRs.

## Not Allowed

- Running subagents to skip discovery questions.
- Creating implementation before approved intent, specs, tests, and traceability.
- Treating subagent output as human approval.
- Letting subagents modify unrelated files.
- Using subagents to override GitHub Actions, SonarCloud, Jira approval, or signed artifact gates.

## Review Pattern

When subagents are used:

1. Define the exact artifact and review question.
2. Keep each subagent scoped to one review angle.
3. Compare findings against Git source files.
4. Record accepted findings in feedback or traceability where relevant.
5. Ask for human approval before applying corrections.

## Human Gate

Subagent findings are advisory. For lab work, explicit user chat confirmation is acceptable approval evidence. For real delivery, approval must be backed by Jira status, pull request approval, or signed artifact approval.
