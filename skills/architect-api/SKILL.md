---
name: architect-api
description: Create OpenAPI contracts from approved requirements and architecture context.
---

# Architect API Skill

## Purpose
Create or update API contracts based on approved specification and architecture context.

## When to use
Use after architecture context is approved.

## Inputs
- spec.md
- context.md
- .ai/standards/api-standards.md
- .ai/standards/security-standards.md

## Process
1. Identify API operations.
2. Define request and response schemas.
3. Define errors.
4. Add security scheme.
5. Add correlation ID.
6. Add idempotency key for payment commands.
7. Validate API coverage against requirements.
8. Ask for approval.

## Output
- domains/<domain>/capabilities/<capability>/contracts/openapi.yaml

## Quality checks
- APIs map to requirements.
- Error responses are complete.
- Security is defined.
- Idempotency is included where required.
- Correlation ID is included.
- No implementation code is generated.

## Human gate
Architect approval is required before QA test design.

## Next skill
qa-test-design
