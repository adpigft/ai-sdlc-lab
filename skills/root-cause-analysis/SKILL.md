---
name: root-cause-analysis
description: Perform structured RCA.
---

# Root Cause Analysis Skill

## Purpose
Perform structured RCA.

## When to use
Use after a defect or failure has been confirmed and the team needs the underlying cause.

## Inputs
- failure symptoms
- defect evidence
- logs, traces, or test results
- relevant artifacts

## Method
- 5 Whys
- Fishbone
- Contributing Factors

## Process
1. Reconstruct the failure timeline.
2. Apply 5 Whys.
3. Map contributing factors with Fishbone.
4. Separate root cause from symptoms.
5. Identify corrective and preventive actions.

## Output
- root cause
- corrective action
- preventive action

## Rules
- do not implement fixes
- analysis only

## Human gate
Use the RCA result to approve the corrective workflow and prioritize remediation.
