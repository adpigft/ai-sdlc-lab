# Observability Standard

## Purpose

Define observability and telemetry standards for Java Spring Boot services, Flutter channel apps, event consumers, integrations, and deployment platforms.

## Baseline

| Area | Standard |
| --- | --- |
| Tracing | OpenTelemetry with W3C trace context propagation. |
| Metrics | Micrometer for Java services and approved telemetry SDKs for channels. |
| Logging | Structured JSON logs in production. |
| Correlation | `X-Correlation-ID` propagated across inbound requests, outbound calls, events, logs, traces, and audit evidence. |
| Health | Spring Boot Actuator liveness and readiness probes for Java services. |
| Dashboards | Service, API, event, database, dependency, and business-flow dashboards for operationally critical capabilities. |

## Golden Signals

Every service must expose telemetry for:

- latency: average, p95, p99, timeout rate
- traffic: request rate, event rate, job rate, command rate
- errors: 4xx, 5xx, business rejection, dependency failure, DLQ rate
- saturation: CPU, memory, thread pools, database pool usage, queue lag, disk or connection pressure

## Metric Naming

Use namespaced metric names:

```text
bank.<domain>.<service>.<metric_name>.<unit>
```

Examples:

```text
bank.cards.card_lifecycle.replacement_submission.seconds
bank.payments.payment_reversal.processor_error.count
```

## Structured Logging

Production logs must include:

| Field | Requirement |
| --- | --- |
| `timestamp` | UTC ISO 8601 timestamp. |
| `level` | INFO, WARN, ERROR, DEBUG. |
| `service` | Service identifier. |
| `trace_id` | OpenTelemetry trace identifier where available. |
| `span_id` | OpenTelemetry span identifier where available. |
| `correlation_id` | Request or workflow correlation ID. |
| `message` | Safe, masked log message. |

Do not log raw passwords, tokens, PAN, CVV, full addresses, national identifiers, authentication payloads, or unmasked customer profile data.

## Trace Propagation

- Propagate W3C `traceparent` and `tracestate` headers across HTTP and GraphQL calls.
- Propagate trace context in Kafka headers.
- Preserve correlation ID through synchronous calls, asynchronous events, outbox relay, retry, and DLQ handling.
- Ensure external integration adapters start spans for provider calls.
- Ensure database, cache, and queue spans are captured where supported.

## Sampling

- Capture 100% of error and exception traces for critical banking journeys where storage and policy allow.
- Use approved adaptive sampling for successful high-volume traffic.
- Never sample away audit evidence.
- Ensure sampled traces are sufficient for release validation and incident diagnosis.

## Alerting

Alerts must be actionable and tied to service ownership.

Recommended alert categories:

- elevated API or event processing failure rate
- dependency timeout or circuit breaker open state
- database connection saturation
- queue consumer lag
- DLQ growth
- audit persistence failure
- high unauthorized-attempt rate
- failed health or readiness probes
- breached business-flow SLO

## Review Checklist

- Logs are structured and masked.
- Metrics cover golden signals and material business events.
- Traces propagate through HTTP, GraphQL, Kafka, database, and external provider boundaries where applicable.
- Dashboards and alerts identify owner, severity, and response expectation.
- Validation and release evidence link to observability checks for implemented code.

