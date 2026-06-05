# Database Design Standard

## Purpose

Define reusable database standards for transactional and document storage in digital banking systems.

## Storage Selection

| Store | Use When |
| --- | --- |
| PostgreSQL | Transactional records, ACID consistency, relational constraints, money movement, lifecycle state, audit references, operational reporting. |
| MongoDB or document store | Audit documents, unstructured payloads, session telemetry, device configuration, or hierarchical documents without relational integrity requirements. |

PostgreSQL is the default for business transaction state. NoSQL requires explicit design justification.

## PostgreSQL Standards

- Each microservice owns its database schema.
- Services must not share writable database tables across bounded contexts.
- Use explicit primary keys, foreign keys within the service boundary, constraints, indexes, and optimistic locking where needed.
- Use database transactions for immediate consistency within the service boundary.
- Use eventual consistency and events for cross-service propagation.
- Configure connection pools according to pod limits to prevent database exhaustion.
- Prefer read replicas only for queries that tolerate replica lag.

Recommended HikariCP baseline:

```properties
spring.datasource.hikari.maximum-pool-size=10
spring.datasource.hikari.idle-timeout=600000
spring.datasource.hikari.max-lifetime=1800000
```

## Schema Migration

- Use Flyway for all schema changes unless another approved migration tool is explicitly selected.
- Do not run raw production DDL outside approved migration pipelines.
- Migrations must be versioned, reviewed, repeatable in lower environments, and linked to release evidence.
- Destructive migrations require explicit rollback and data recovery planning.

Backward-compatible migration sequence:

1. Add new nullable columns or new tables.
2. Deploy application version that supports old and new shapes.
3. Backfill or migrate records.
4. Deploy application version that reads the new shape.
5. Remove deprecated columns or tables in a later release.

## MongoDB Standards

- Use explicit indexes for all query filters.
- Keep documents below platform document-size limits.
- Avoid unbounded embedded arrays.
- Use bulk writes for high-volume append workloads where safe.
- Use sharding only after access pattern and volume justification.
- Do not store card PAN, CVV, tokens, secrets, or sensitive profile data unless an approved encryption and retention model exists.

## Data Ownership

- Each service owns its transactional data and published event facts.
- Consumer read models must be treated as projections, not source-of-truth records.
- Master customer profile data remains owned by the customer profile capability.
- Processor references may be stored for traceability, but external processors remain the system of record for their own execution state.
- Audit records must preserve evidence without leaking sensitive data.

## Security And Recovery

- Encrypt databases at rest with approved customer-managed keys where available.
- Use TLS for database connections.
- Use short-lived credentials or managed identity where supported.
- Keep databases in private network segments.
- Enable point-in-time recovery for critical stores with a minimum 30-day retention target unless a stricter policy applies.
- Test restore procedures before production release for critical services.

