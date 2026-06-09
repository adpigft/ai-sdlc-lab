# Discovery Engineering Model

## Purpose

Discovery is the read-only analysis of an existing application to establish a reliable current-state baseline for brownfield modernization.

It is the first step in the brownfield flow and feeds modernization readiness review, intent definition, specification definition, solution design, and gap analysis.

## Principles

- Read-only analysis only.
- Evidence first, inference second.
- Current state is documented before target state is proposed.
- Source code, configuration, APIs, and documentation are inspected but not modified.
- Evidence, inference, and target-state thinking are kept separate.
- Discovery limitations are explicitly documented.

## Required and Considered Outputs

Discovery should always produce or consider:

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
- `current-state-discovery.md`
- `discovery-evidence.md`

The following supporting artifacts may also be produced when evidence depth justifies them:

- current-state summary
- architecture overview
- application inventory
- API inventory
- data model summary
- business rules summary
- integration map
- technology stack summary
- limitations and assumptions log

## Evidence Model

Discovery evidence should cite:

- file paths
- classes
- functions
- endpoints
- configuration keys
- database tables or schemas
- build and deployment files
- runtime observations, when available

Any item that cannot be directly evidenced must be labeled as an inference.

## Current-State Scope

Discovery should capture:

- architecture style
- application boundaries
- major components
- UI entry points
- services and APIs
- data stores
- batch jobs and schedulers
- integration points
- authentication and authorization assumptions
- deployment assumptions
- external dependencies
- observed business rules
- technical debt and modernization constraints

## Exclusions

Discovery engineering does not:

- create target-state design
- create implementation plans
- modify source code
- create new business requirements
- invent future-state architecture
