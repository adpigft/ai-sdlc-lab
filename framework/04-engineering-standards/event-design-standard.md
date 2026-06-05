# Event Design Standard

## Purpose

Define Kafka and event-driven architecture standards for digital banking capabilities.

## Event Ownership

- Events are owned by the producing bounded context.
- Consumers must not infer private producer state from event timing or undocumented fields.
- Event contracts require producer, consumer, architecture, QA, and operations review before implementation.
- Git-owned schemas and design artifacts remain the source of truth.

## Topic Naming

Use this topic pattern:

```text
bank.<domain>-domain.<event-name>.v1
```

Example:

```text
bank.cards-domain.card-replaced.v1
```

Dead-letter topics use:

```text
bank.<domain>-domain.<event-name>.dlq.v1
```

## Schema Governance

- Use Apache Avro or another approved schema-governed format.
- Register schemas in the approved schema registry.
- Use BACKWARD or FULL compatibility unless an exception is approved.
- Do not remove or repurpose fields in compatible versions.
- Add optional fields with safe defaults.
- Mask or tokenize sensitive identifiers.
- Do not publish full PAN, CVV, tokens, secrets, raw credentials, or sensitive customer profile details.

## Message Keys And Ordering

- Every event must have a non-null partition key.
- Choose keys that preserve ordering for the business entity that requires ordered processing.
- Common keys include customer ID, account ID, card ID, payment ID, or replacement request ID.
- Do not use random keys when ordering is required.
- Document ordering assumptions in the feature design and event contract.

## Transactional Outbox

Use transactional outbox when publishing events caused by database state changes:

1. Write business state and outbox record in the same database transaction.
2. Relay outbox records asynchronously to Kafka.
3. Use a distributed lock or partition-safe relay model to avoid duplicate concurrent publishing.
4. Mark or remove published records only after broker acknowledgement.
5. Preserve correlation ID, trace context, event ID, schema version, entity key, and creation timestamp.

## Consumer Resilience

- Consumers must be idempotent.
- Transient failures should use retry with exponential backoff.
- Permanent validation or poison-message failures must route to DLQ and alert where severity requires.
- Consumers must not halt the entire stream for one invalid message.
- Monitor lag, error rate, retry count, DLQ rate, and processing latency.

## Event Review Checklist

- Producer and owner are clear.
- Event name represents a business fact, not an implementation command.
- Topic name and version are defined.
- Schema compatibility mode is defined.
- Partition key and ordering assumptions are documented.
- Sensitive fields are masked or excluded.
- Consumer impact and retry/DLQ behavior are documented.
- Traceability links event publication to requirements and design decisions.

