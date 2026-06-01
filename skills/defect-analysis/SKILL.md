---
name: defect-analysis
description: Analyze defects.
---

# Defect Analysis Skill

## Purpose
Analyze defects.

## When to use
Use when a defect has been reported and needs classification before corrective action.

## Inputs
- defect report
- source code
- tests
- traceability

## Process
1. Review the reported defect.
2. Inspect the relevant source, tests, and traceability.
3. Determine the most likely root cause category.
4. Record evidence and recommended next action.

## Output
- root cause category

## Categories
- requirement defect
- architecture defect
- design defect
- code defect
- test defect
- operational defect

## Rules
- no code changes
- diagnosis only

## Human gate
Use the diagnosis to decide the corrective workflow and approval path.
