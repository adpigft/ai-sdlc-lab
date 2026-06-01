---
name: change-impact-analysis
description: Analyze change requests without regenerating the entire solution.
---

# Change Impact Analysis Skill

## Purpose
Analyze change requests without regenerating the entire solution.

## When to use
Use when a requested change may affect requirements, design, tests, or code, and a narrow impact assessment is needed before action.

## Inputs
- change request
- intent
- spec
- context
- APIs
- tests
- code
- traceability

## Process
1. Identify impacted artifacts.
2. Identify impacted requirements.
3. Identify impacted APIs.
4. Identify impacted tests.
5. Identify impacted code.
6. Identify impacted slices.
7. Assess risks.
8. Return a recommendation.

## Output
- impacted artifacts
- impacted requirements
- impacted APIs
- impacted tests
- impacted code
- impacted slices
- risks

## Rules
- no code generation
- no artifact modification
- impact analysis only

## Classification
- low
- medium
- high

## Recommendation
- targeted change
- major redesign
- future phase

## Human gate
Use the analysis result to decide whether the change is approved and how it should proceed.
