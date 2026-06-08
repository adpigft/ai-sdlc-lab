# Brownfield Modernization Flow

## Flow

Existing Application
→ Discovery Engineering
→ Intent Extraction
→ Specification Extraction
→ Context Extraction
→ Gap Analysis
→ Target-State Specification
→ Design
→ Implementation
→ Validation
→ Traceability
→ Release

## Flow Intent

The flow preserves the existing application as the starting point and progressively converts observed behavior into governed modernization artifacts.

## Stage Responsibilities

- Discovery Engineering: establish current-state facts.
- Intent Extraction: recover business intent from behavior and documentation.
- Specification Extraction: recover the current-state requirements surface.
- Context Extraction: capture architecture, integration, operational, and deployment context.
- Gap Analysis: compare current state with target-state goals and identify the modernization delta.
- Target-State Specification: define the desired behavior after modernization.
- Design: translate the target-state specification into architecture and solution design.
- Implementation: deliver approved slices.
- Validation: prove the delivered behavior.
- Traceability: maintain end-to-end evidence.
- Release: assess readiness and publish the release record.

## Rules

- Each stage must preserve evidence from the previous stage.
- Current-state facts are not overwritten by target-state assumptions.
- Major changes require impact analysis before proceeding.
- No source application files are modified during discovery and extraction stages.

