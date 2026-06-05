# Testing Standard

## Purpose

Define automation testing standards for Java backend services, Flutter channel applications, APIs, events, databases, and CI quality gates.

This standard complements `testing-strategy.md`, which defines testing taxonomy, ownership, maturity, AI-generated testing strategy, automation assessment, and lifecycle skill mapping.

## Test Pyramid

| Layer | Purpose | Preferred Tools |
| --- | --- | --- |
| Unit | Isolated domain rules, application handlers, validators, mappers, state transitions. | JUnit 5, Mockito, AssertJ |
| Component | Service slice with Spring context, local configuration, mocked external ports. | JUnit 5, Spring Boot Test, Mockito |
| API | REST endpoint behavior, request validation, response mapping, error model. | RestAssured, Spring Boot Test |
| Integration | Database, Kafka, external adapter, outbox, and infrastructure boundary behavior. | Testcontainers, WireMock, embedded or containerized dependencies |
| Contract | Producer and consumer compatibility for APIs and events. | OpenAPI validation, Pact, schema registry compatibility checks |
| Security | AuthN/AuthZ, scope checks, replay resistance, data masking, dependency/security scans. | Spring Security tests, Sonar, dependency scanners |
| Performance | Latency, throughput, saturation, retry behavior, and degradation. | K6, Gatling, JMeter, approved observability tools |
| Flutter | State, widgets, golden visual regression, and app journeys. | Flutter test, golden_toolkit, Patrol, Appium |

## Java Backend Test Structure

```text
src/test/java/com/<company>/<domain>/<service>/
├── unit/
├── component/
├── integration/
├── contract/
└── performance/
```

## Java Test Tooling

- Use JUnit 5 as the default test engine.
- Use Mockito for test doubles.
- Use RestAssured for API tests.
- Use Testcontainers for PostgreSQL, Kafka, WireMock-compatible service virtualization, and other local integration dependencies.
- Use JaCoCo for coverage evidence.
- Publish test and coverage evidence to Sonar.

## Data And Environment Rules

- Use deterministic synthetic test data.
- Do not use production customer data.
- Mask or tokenize any copied data used for testing.
- Reset or recreate test containers between tests where state isolation is required.
- Avoid shared mutable integration environments for PR-blocking tests.
- Record non-deterministic test dependencies as risks.

## CI Expectations

- Run fast unit tests on every pull request.
- Run API, component, and contract checks where impacted.
- Run integration tests when persistence, messaging, or external adapter behavior changes.
- Run performance tests for approved NFRs before release.
- Quarantine flaky tests immediately and track remediation as defects.
- Do not lower coverage or disable tests without explicit approval and traceable rationale.

## Acceptance And Traceability

- Acceptance scenarios must map to approved requirements, business rules, and edge cases.
- Automated tests must map to requirement IDs, design decisions, defects, or risks where practical.
- Validation reports must cite executed test evidence, skipped tests, known gaps, and approval recommendation.

