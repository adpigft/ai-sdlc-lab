# Model Risk Management

## Purpose

This document defines future model risk categories and the controls that would govern them.

It is optional and future-state.

## Risk Categories

### Hallucination

- Likelihood: medium
- Impact: medium to high
- Controls: grounded context, review gates, deterministic validation, human approval for governed output
- Owner: AI governance owner
- Monitoring: review findings, validation failures, user feedback

### Specification Drift

- Likelihood: medium
- Impact: high
- Controls: traceability, spec-aware review, context versioning, impact analysis
- Owner: product / BA owner
- Monitoring: spec review comments, traceability gaps, change impact checks

### Context Drift

- Likelihood: medium
- Impact: high
- Controls: context manifests, package versioning, drift detection, review freshness
- Owner: context owner
- Monitoring: stale package flags, context drift indicators, rework patterns

### Security Leakage

- Likelihood: low to medium
- Impact: high
- Controls: sensitivity classification, restricted context handling, token hygiene, secure MCP policy
- Owner: security owner
- Monitoring: security scans, audit logs, policy violations

### Prompt Injection

- Likelihood: medium
- Impact: high
- Controls: prompt isolation, untrusted text handling, input sanitization, review of retrieval paths
- Owner: platform security owner
- Monitoring: suspicious input patterns, review findings, security alerts

### Compliance Breach

- Likelihood: low to medium
- Impact: high
- Controls: approval gates, audit trail, retention rules, evidence capture
- Owner: compliance owner
- Monitoring: audit checks, evidence gaps, control exceptions

### Model Outage

- Likelihood: medium
- Impact: medium to high
- Controls: model fallback strategy, routing policy, outage runbook, manual override
- Owner: platform owner
- Monitoring: service availability, routing failures, error rates

## Notes

- Risk should be assessed by task, data class, and delivery criticality.
- The model risk model is a governance aid, not an implementation service.
