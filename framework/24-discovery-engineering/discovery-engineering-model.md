# Discovery Engineering Model

## Purpose

Discovery engineering is the read-only analysis of an existing application to establish a reliable current-state baseline for brownfield modernization.

It is the first step in the brownfield flow and feeds recovered intent, current-state specification, legacy context, and gap analysis.

## Principles

- Read-only analysis only.
- Evidence first, inference second.
- Current state is documented before target state is proposed.
- Source code, configuration, APIs, and documentation are inspected but not modified.
- Facts and assumptions are kept separate.

## Primary Outputs

- Current-state discovery
- Architecture overview
- Application inventory
- API inventory
- Data model summary
- Business rules summary
- Integration map
- Technology stack summary

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

## Exclusions

Discovery engineering does not:

- create target-state design
- create implementation plans
- modify source code
- create new business requirements
- invent future-state architecture

