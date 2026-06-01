---
name: developer-implementation
description: Generate implementation and tests only after approved intent, specification, architecture, API, tests, and traceability.
---

# Developer Implementation Skill

## Purpose
Generate implementation from approved artifacts.

## When to use
Use only after intent, specification, architecture, API, tests, and traceability are approved.

## Inputs
- spec.md
- context.md
- openapi.yaml
- acceptance.feature
- .ai/standards/coding-standards.md
- .ai/standards/security-standards.md
- .ai/standards/testing-standards.md

## Process
1. Read approved artifacts.
2. Explain proposed package/module structure.
3. Explain domain model and service flow.
4. List impacted files.
5. Ask for approval before coding.
6. Generate implementation and tests.
7. If a spec gap is found, stop and report it instead of coding around it.

## Outputs
- Application code under src/
- Unit tests
- Integration tests

## Quality checks
- Follows clean/hexagonal architecture.
- Tests are included.
- No secrets are committed.
- Sensitive data is not logged.
- Error handling is explicit.
- Code maps to approved requirements.

## Human gate
Developer and Architect code review required before validation.

## Next skill
qa-validation
