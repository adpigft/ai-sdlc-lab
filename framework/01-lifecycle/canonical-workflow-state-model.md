# Canonical Workflow State Model

## Purpose

Define the canonical workflow states used across the AI-SDLC framework.

This model is the stable reference for governance, the Control Tower, and workflow-state interpretation.

Brownfield modernization may introduce additional supporting review and planning artifacts, but the canonical workflow here remains the source of truth for lifecycle state interpretation.

## Canonical Workflow

Candidate Imported -> Intent Draft -> Intent Approved -> Requirements Draft -> Requirements Approved -> Design Approved -> Ready for Build -> In Development -> Validation Passed -> Release Ready -> Released

## State Definitions

### Candidate Imported

- Owner role: Delivery Lead
- Approver role: Product Owner
- Entry criteria: a backlog candidate or imported idea exists
- Exit criteria: candidate is reviewed and accepted for intent drafting

### Intent Draft

- Owner role: Business Analyst
- Approver role: Product Owner
- Entry criteria: candidate is accepted for intent discovery and drafting
- Exit criteria: intent is reviewed and approved

### Intent Approved

- Owner role: Business Analyst
- Approver role: Product Owner
- Entry criteria: intent is complete enough for approval
- Exit criteria: requirements drafting may begin

### Requirements Draft

- Owner role: Business Analyst
- Approver role: Product Owner
- Entry criteria: approved intent exists
- Exit criteria: requirements are reviewed and approved

### Requirements Approved

- Owner role: Business Analyst
- Approver role: Product Owner
- Entry criteria: requirements are complete and reviewable
- Exit criteria: design work may begin

### Design Approved

- Owner role: Solution Architect
- Approver role: Solution Architect
- Entry criteria: design, API, or architecture content has been reviewed and approved
- Exit criteria: build readiness can be assessed

### Ready for Build

- Owner role: Developer Lead
- Approver role: Solution Architect
- Entry criteria: design approval and implementation readiness are complete
- Exit criteria: implementation may begin

### In Development

- Owner role: Developer Lead
- Approver role: Developer Lead
- Entry criteria: implementation is actively in progress
- Exit criteria: development is ready for validation

### Validation Passed

- Owner role: QA Lead
- Approver role: QA Lead
- Entry criteria: implementation has passed validation evidence checks
- Exit criteria: release readiness may be prepared

### Release Ready

- Owner role: DevSecOps / Platform
- Approver role: DevSecOps / Platform
- Entry criteria: validation is complete and release evidence is ready
- Exit criteria: release may proceed

### Released

- Owner role: Delivery Lead
- Approver role: Delivery Lead
- Entry criteria: release has been approved and completed
- Exit criteria: release closure and post-release tracking are complete

## Notes

- This is the canonical workflow for future state interpretation.
- `workflow.state` values in generated data should align to this model.
- Legacy labels should be mapped to these states through the legacy mapping document.
