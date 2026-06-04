---
name: test-design
description: Create acceptance, negative, integration, security, regression, and NFR test scenarios from approved requirements and design.
---

# Test Design Skill

## Purpose

Define QA-owned test scenarios and coverage before implementation or validation relies on them.

## When To Use

Use `$test-design` after specification approval and after enough design context exists to test the behavior, contracts, integrations, risks, and NFRs.

## Inputs Needed

- Approved intent and specification
- Design context and contracts where applicable
- Business rules, edge cases, and NFR targets
- Risk, security, performance, integration, and operational constraints
- Existing tests or regression scope when applicable

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, approval gates, and lifecycle behavior are defined by:

- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/01-lifecycle/skill-orchestration-adapter.md`

## Procedure

1. Confirm approved requirements are available.
2. Derive happy path, negative, boundary, duplicate, timeout, audit, reconciliation, and domain-relevant scenarios.
3. Include integration, security, performance, availability, and operational scenarios when risks apply.
4. Identify test data, mocks, dependencies, environments, and evidence expectations.
5. Map tests to requirements and critical NFRs.
6. Keep QA acceptance and validation scenarios separate from developer unit-test implementation detail.
7. Stop for QA review before implementation relies on the test design.

## Outputs Produced

- Acceptance scenarios
- Negative, edge-case, integration, security, regression, and NFR scenarios where applicable
- Test data, dependency, and evidence notes
- Coverage summary and gaps
- Review request for QA approval

## Artifact Structure

1. Acceptance Tests
2. Negative Tests
3. Edge Cases
4. Integration Coverage
5. Regression Coverage
6. NFR Coverage
7. Test Data Requirements

## Quality Checks

- Tests map to approved requirements and acceptance criteria.
- Key NFRs have validation scenarios or explicit gaps.
- Negative, failure, duplicate, timeout, and edge cases are covered where relevant.
- Scenarios are clear enough for implementation and validation teams.
- No source code is generated.

## Stop Conditions

- Requirements lack an acceptance basis.
- Required design or contract context is missing.
- NFR targets are missing and cannot be recorded as open questions.
- QA approval is missing for downstream use.

## Human Approval Expectations

QA approval is required before implementation or validation depends on the test design.

## Standard Response Format

Created/Updated:
- ...

Pending Review:
- ...

Blockers:
- ...

Next:
- ...
