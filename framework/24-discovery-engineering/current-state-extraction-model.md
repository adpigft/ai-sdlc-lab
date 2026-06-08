# Current-State Extraction Model

## Purpose

Current-state extraction converts evidence from the source application into structured modernization inputs without changing the application.

## Extraction Layers

1. Architecture layer
2. Application layer
3. API layer
4. Data layer
5. Business-rule layer
6. Integration layer
7. Operational layer
8. Security layer

## Required Artifacts

- current-state-discovery.md
- architecture-overview.md
- application-inventory.md
- api-inventory.md
- data-model.md
- business-rules.md
- integration-map.md
- technology-stack.md

## Evidence Rules

- Ground every extracted item in the observed source.
- If evidence is partial, state the limit of confidence.
- If evidence is absent, record an unknown rather than inventing a fact.
- Distinguish current-state extraction from target-state recommendations.

## Confidence Guidance

- High: direct evidence from code, configuration, or documentation.
- Medium: evidence plus a small amount of inference.
- Low: mostly inferred from behavior or indirect signals.

