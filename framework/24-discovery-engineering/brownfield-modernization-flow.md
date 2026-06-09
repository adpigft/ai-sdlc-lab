# Brownfield Modernization Flow

## Flow

```text
Existing Application
→ Discovery
→ Discovery Review
→ Modernization Readiness Review
→ Intent
→ Intent Review
→ Requirements Definition
→ Requirements Review
→ Design Input Review
→ Design
→ Design Review
→ Gap Analysis
→ Impact Analysis
→ Implementation Readiness
→ Implementation Planning
→ Vertical Slice Planning
→ Implementation Architecture
→ Implementation
→ Validation
→ PR Review
→ Release
```

## Flow Intent

The flow preserves the existing application as the starting point and progressively converts observed behavior into governed modernization artifacts. Brownfield phases are additive and optional where the project already has approved upstream context.

## Stage Responsibilities

- Discovery: establish current-state facts, evidence, limitations, and confidence.
- Discovery Review: challenge evidence quality, completeness, and inference boundaries.
- Modernization Readiness Review: decide whether discovery is sufficient to begin modernization intent work.
- Intent: define the target business state, operating model, and first-release scope.
- Intent Review: validate that the target-state intent is coherent, bounded, and approval-ready.
- Requirements Definition: convert approved intent into implementable requirements.
- Requirements Review: validate completeness, traceability, policy handling, and testability.
- Design Input Review: identify missing architecture decisions before final solution design.
- Design: define target architecture, implementation placement, and dynamically selected design artifacts.
- Design Review: validate the design, decisions, and placement direction.
- Gap Analysis: compare current-state discovery to target specification and solution design.
- Impact Analysis: assess implementation impact without creating the implementation plan itself.
- Implementation Readiness: determine what must close before implementation can start.
- Implementation Planning: define slices, dependencies, risks, and the build-ready plan.
- Vertical Slice Planning: ensure business slices are vertically deliverable where possible and include frontend, backend, data, API, domain, observability, tests, acceptance criteria, and traceability.
- Implementation Architecture: define module structure, package structure, migration strategy, implementation standards, and testing strategy.
- Implementation: deliver approved slices.
- Validation: prove the delivered behavior.
- PR Review: check the implemented slice against approved scope and placement.
- Release: assess readiness and publish the release record.

## Rules

- Each stage must preserve evidence from the previous stage.
- Current-state facts are not overwritten by target-state assumptions.
- Evidence must be separated from inference and target-state thinking.
- Discovery limitations must be explicitly documented.
- Major changes require impact analysis before proceeding.
- No source application files are modified during discovery and extraction stages.
- Greenfield delivery can still use the canonical lifecycle without the brownfield-only stages.
