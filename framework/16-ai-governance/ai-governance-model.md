# AI Governance Model

## Purpose

This model defines future enterprise AI governance above the delivery framework.

It is optional and future-state. It does not change the current delivery workflow.

## Scope

- AI usage policies
- prompt governance
- context governance
- approved model registry
- human approval requirements
- model risk classification
- data sensitivity classification
- AI audit requirements
- prompt injection controls
- secure MCP usage

## Data Sensitivity Classes

- L1 Public: safe for broad sharing and low-risk examples
- L2 Internal: internal business material with limited distribution
- L3 Confidential: sensitive business, delivery, or operational material
- L4 Restricted: highly sensitive material, regulated content, or material requiring explicit control

## Allowed AI Activities

- drafting controlled delivery artifacts for human review
- summarizing approved context and approved source material
- generating candidate analysis and options
- helping with validation, review, and traceability support
- assisting with approved operational analysis that excludes secrets and restricted data

## Restricted AI Activities

- using unapproved context as source of truth
- exposing secrets, tokens, credentials, or restricted production data
- bypassing human approval requirements
- creating or publishing governed artifacts without approval
- sending restricted data to unapproved models or connectors
- executing privileged actions through MCP or similar connectors without explicit control

## Human Oversight Requirements

- human approval is required for business, compliance, and risk decisions
- human review is required before publishing governed output
- restricted data requires explicit handling controls and review
- model selection for higher-risk data classes must be governed

## Prompt Governance

- prompts must be reviewable and attributable
- prompts should carry the minimum context needed for the task
- prompt injection risks must be treated as an input trust issue
- system, task, and data context should remain separated where possible

## Context Governance

- context packages must be versioned and reviewable
- only approved context should be used for governed delivery work
- stale or conflicting context should be flagged before use
- context provenance should remain visible for audits

## Approved Model Registry

- approved models are defined centrally
- models should be selected by task risk, data sensitivity, and governance need
- deprecated models should not be used for governed work
- model routing should be controlled rather than ad hoc

## AI Audit Requirements

- record what model was used
- record what context was used
- record what tool actions were taken
- record what approvals were obtained
- record what validation occurred
- record what human feedback was provided

## Prompt Injection Controls

- isolate untrusted text from trusted instructions
- do not allow retrieved content to override system governance
- treat external content as data, not instructions
- review any prompt path that may accept adversarial input

## Secure MCP Usage

- use only approved MCP servers
- keep credentials and tokens out of prompts and artifacts
- prefer read-only operations for discovery and review
- separate read-only and mutation capabilities by governance
- require explicit approval before invoking sensitive tools

## Notes

- This model is a future governance layer above delivery, not a replacement for delivery controls.
- It should remain additive and optional until formally adopted.
