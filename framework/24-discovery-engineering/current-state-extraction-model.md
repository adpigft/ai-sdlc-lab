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

- `current-state-discovery.md`
- `quick-scan.md`
- `business-rules-catalog.md`
- `application-inventory.md`
- `architecture-overview.md`
- `api-inventory.md`
- `data-model.md`
- `state-machine.md`
- `integration-inventory.md`
- `domain-decomposition.md`
- `technical-debt.md`
- `discovery-evidence.md`

## Evidence Rules

- Ground every extracted item in the observed source.
- If evidence is partial, state the limit of confidence.
- If evidence is absent, record an unknown rather than inventing a fact.
- Distinguish current-state extraction from target-state recommendations.
- Separate evidence from inference and current-state from target-state thinking.

## Confidence Guidance

- High: direct evidence from code, configuration, or documentation.
- Medium: evidence plus a small amount of inference.
- Low: mostly inferred from behavior or indirect signals.
