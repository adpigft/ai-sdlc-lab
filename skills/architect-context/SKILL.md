---
name: architect-context
description: Create architecture context, system boundaries, integration view, risks, and design assumptions from approved requirements.
---

# Architect Context Skill

## Purpose
Create solution architecture context from approved intent and specification.

## When to use
Use only after spec.md is approved.

## Inputs
- intent.md
- spec.md
- Enterprise standards
- Security standards
- Integration context

## Process
1. Review requirements.
2. Identify system boundaries.
3. Define components and integrations.
4. Define data ownership.
5. Define sequence flow.
6. Define security, observability, scalability, and failure handling.
7. Record risks and assumptions.
8. Ask for approval.

## Output
- domains/<domain>/capabilities/<capability>/context/context.md
- decisions/ADR-*.md when needed

## Quality checks
- Boundaries are clear.
- Integrations are identified.
- Data ownership is defined.
- Failure handling is addressed.
- Security and audit requirements are covered.
- No code is generated.

## Human gate
Solution Architect approval is required before API design.

## Next skill
architect-api
