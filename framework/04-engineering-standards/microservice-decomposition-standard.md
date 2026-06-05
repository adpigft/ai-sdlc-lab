# Microservice Decomposition Standard

## Purpose

Define bounded-context and modularity rules for deciding when a capability belongs in one service, multiple services, shared libraries, or shared platforms.

## Core Rules

- Each microservice must align to a clear bounded context.
- A service must own a cohesive business capability with explicit boundaries.
- Services must communicate through versioned APIs, schema-governed events, or approved integration protocols.
- Each service must own its datastore.
- Immediate consistency belongs inside a service boundary.
- Cross-service consistency uses events, sagas, reconciliation, or other approved eventual-consistency patterns.
- Aggregate roots coordinate changes to domain entities inside the bounded context.

## Split Drivers

Split a service when one or more factors materially justify the operational and integration cost:

| Driver | Signal |
| --- | --- |
| Scope | The service contains unrelated business responsibilities. |
| Volatility | One part changes frequently while another must remain stable. |
| Scalability | Workload shape or throughput differs significantly. |
| Fault isolation | Downstream or provider failures should not affect unrelated journeys. |
| Security | Different data classification, access model, PCI scope, or regulatory control applies. |
| Extensibility | Third-party plugins or vendor-specific behavior require isolation. |
| Ownership | Different squads need independent delivery and review boundaries. |

## Consolidation Drivers

Keep responsibilities together when:

- strong ACID transactions are required
- business invariants span the same aggregate boundary
- splitting would create distributed transactions without clear value
- shared rules change together and must remain consistent
- latency-sensitive orchestration would become fragile across services
- ownership is the same and operational complexity would increase without benefit

## Shared Code Governance

| Mechanism | Use When |
| --- | --- |
| Shared utility | Logic is stable, low-risk, and not domain-specific. |
| Shared library | Behavior is reusable, versioned, backward compatible, and owned. |
| Shared service | Behavior changes frequently or requires independent deployment. |
| Template | Teams need consistent bootstrap structure without runtime coupling. |

Shared libraries must not become a hidden domain model shared across bounded contexts.

## Decomposition Review Checklist

- Bounded context name and owner are clear.
- Service responsibilities and exclusions are documented.
- Data ownership is explicit.
- APIs and events are versioned and owned.
- Cross-service consistency model is documented.
- Security and compliance boundaries are understood.
- Scaling and failure-isolation assumptions are testable.
- Implementation placement and allowed paths can be identified before code changes.

