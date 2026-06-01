---
name: api-review
description: Review API contracts for REST standards, security, idempotency, correlation ID, error model, versioning, and backward compatibility. Use when OpenAPI or API contracts need approval.
---

# API Review Skill

## Purpose
Review API contracts for REST standards, security, idempotency, correlation ID, error model, versioning, and backward compatibility.

## When to use
Use when an API contract is ready for review before QA or implementation.

## Inputs
- OpenAPI or API contract
- spec
- context
- traceability

## Process
1. Review resource and method design.
2. Review security, idempotency, and correlation controls.
3. Review errors, versioning, and compatibility.
4. Return API review findings only.

## Outputs
- API review findings

## Quality checks
- REST standards
- security
- idempotency
- correlation ID
- error model
- versioning
- backward compatibility

## Human gate
Human approval is required before test design or implementation.

## Next skill
integration-test-design

