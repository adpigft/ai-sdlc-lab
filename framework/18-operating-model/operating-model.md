# Operating Model

## Purpose

This document defines future ownership and governance structure for enterprise-scale AI-SDLC adoption.

## Ownership Model

- Context Owner: owns context quality, versioning, provenance, and drift response
- Skill Owner: owns skill behavior, prompts, and review guidance
- Harness Owner: owns harness definition, entry criteria, and stop conditions
- Domain Owner: owns domain boundaries and business context
- Capability Owner: owns capability-level business function and shared context
- Feature Owner: owns feature delivery scope and approval flow
- Control Tower Owner: owns visibility model and governance reporting
- AgentOps Owner: owns run telemetry, feedback loops, and operational metrics

## RACI

| Activity | Context Owner | Skill Owner | Harness Owner | Domain Owner | Capability Owner | Feature Owner | Control Tower Owner | AgentOps Owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| context package approval | A | C | C | C | C | C | I | I |
| skill update | C | A | C | I | I | I | I | C |
| harness definition | C | C | A | I | I | I | I | C |
| domain boundary change | C | I | I | A | C | I | I | I |
| capability change | C | I | I | C | A | I | I | I |
| feature delivery approval | I | I | I | C | C | A | I | I |
| control tower model change | C | C | C | I | I | I | A | C |
| agent telemetry policy | C | C | I | I | I | I | I | A |

## Escalation Paths

- feature risk -> feature owner -> capability owner -> domain owner
- context issue -> context owner -> capability owner -> control tower owner
- skill issue -> skill owner -> harness owner -> control tower owner
- observability issue -> AgentOps owner -> control tower owner -> platform owner

## Governance Forums

- delivery governance review
- context governance review
- architecture review
- release readiness review
- observability and AgentOps review

## Notes

- This operating model is a future-state structure.
- The current delivery workflow remains unchanged unless separately approved.
