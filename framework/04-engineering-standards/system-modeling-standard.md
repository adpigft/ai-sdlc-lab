# System Modeling Standard

## Purpose

Define reusable system modeling standards for C4 diagrams, sequence diagrams, and data flow diagrams. These models support architecture review, security review, implementation planning, operational readiness, and stakeholder communication.

## Modeling Principles

- Model the decision or risk being reviewed.
- Use the smallest diagram that makes the system understandable.
- Keep diagrams logical unless deployment topology is the subject.
- Name actors, systems, services, datastores, queues, and external providers consistently with domain and capability language.
- Do not put full JSON payloads, raw SQL, implementation loops, or framework internals in architecture diagrams.
- Link diagrams to approved intent, requirements, design, API contracts, event contracts, or decisions where applicable.

## C4 Model Standards

| Level | Primary Audience | Required Content |
| --- | --- | --- |
| Level 1: System Context | Product, business stakeholders, architects, new team members | User roles, external systems, major platform systems, trust boundaries, and high-level data or value exchange. |
| Level 2: Container | Engineers, architects, SRE, security | Deployable units, channel apps, backend services, datastores, queues, identity providers, external providers, protocols, and ownership. |
| Level 3: Component | Engineers and reviewers | Controllers, application services, domain policies, repositories, adapters, event publishers, consumers, outbox relays, and security components inside one container. |
| Level 4: Code | Lead engineers | Optional for complex patterns only; code should usually be the source of detail. |

## Sequence Diagram Standards

A sequence diagram answers what calls what, in what order, and with what outcome.

Required:

- named participants for actors, systems, services, external dependencies, and datastores
- explicit transport or mechanism, such as HTTP, Kafka, JDBC, or asynchronous event
- operation name or endpoint name where applicable
- key identifiers that drive behavior, such as correlation ID, request ID, account ID, card ID, payment ID, or idempotency key
- response status and payload name, not full payload bodies
- material conditional branches with `alt`
- optional behavior with `opt`
- repeated behavior with `loop`
- security validation boundaries
- business rule references when they determine branch behavior
- step status labels when the diagram supports a change design, using Existing, New, or Target State

Do not include:

- full request or response bodies
- raw SQL
- self-evident framework routing steps
- low-level mapping logic
- rendered UI states
- standard OAuth token fields unless token handling is the subject

## Data Flow Diagram Standards

Use DFDs when data movement, privacy, PCI scope, regulatory scope, or threat modeling matters.

Required elements:

- external entities as data sources or destinations
- processes that transform, validate, mask, enrich, or route data
- data stores where data is persisted
- data flows showing movement between entities, processes, and stores
- trust boundaries, network boundaries, and PCI or sensitive-data boundaries
- encryption, tokenization, masking, and retention annotations where relevant

Rules:

- Data must not flow directly between two external entities without a process.
- Data must not flow directly between two stores without a process.
- Every process must have at least one input and one output.
- Sensitive data flows must identify protection controls.
- Diagrams must distinguish source-of-truth stores from projections and caches.

## Review Checklist

- Diagram scope and audience are clear.
- Ownership boundaries are visible.
- Trust boundaries and sensitive data flows are marked.
- External providers and integration protocols are identified.
- Business rule branches are traceable to approved requirements or design.
- The diagram omits payload and implementation detail that belongs in contracts or code.

