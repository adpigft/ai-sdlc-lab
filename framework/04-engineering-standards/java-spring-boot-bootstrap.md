# Java Spring Boot Bootstrap Standard

## Purpose

Define the Java-first backend service baseline for enterprise digital banking services. This standard converts backend guidance to Java 21 and Spring Boot 3.x while preserving clean architecture, API-first delivery, security, observability, and CI/CD expectations.

## Technology Baseline

| Area | Standard |
| --- | --- |
| Language | Java 21 |
| Framework | Spring Boot 3.x |
| Build | Gradle Groovy or Gradle Kotlin DSL |
| API generation | OpenAPI Generator |
| Security | Spring Security, OAuth2, OIDC, JWT validation |
| Persistence | PostgreSQL by default, MongoDB by approved exception |
| Migration | Flyway |
| Testing | JUnit 5, Mockito, RestAssured, Testcontainers |
| Quality | Spotless, Checkstyle, PMD, SpotBugs, JaCoCo, Sonar |
| Telemetry | OpenTelemetry and Micrometer |
| Packaging | Jib or Docker, Helm |
| CI | GitHub Actions |

## Clean Architecture Layers

Every service must isolate business logic from transport, persistence, messaging, and third-party details.

| Layer | Responsibilities | Restrictions |
| --- | --- | --- |
| Domain | Aggregates, entities, value objects, domain policies, domain events, invariants. | No Spring annotations, JPA annotations, HTTP DTOs, JSON serialization annotations, or infrastructure imports. |
| Application | Command handlers, query handlers, workflow coordinators, ports, transaction boundaries, orchestration. | Depends on domain and narrow ports, not concrete adapters. |
| Transport | REST controllers, GraphQL resolvers where approved, request validation, auth boundary, response mapping. | Must not contain business rules beyond request validation and actor/context extraction. |
| Persistence | JPA entities, repositories, migration scripts, database mappers. | Must not leak persistence models into domain logic. |
| Integration | External clients, anti-corruption adapters, provider request/response mapping. | Must hide provider-specific details behind application ports. |
| Messaging | Kafka producers, consumers, outbox relay, schema mapping. | Must preserve idempotency, ordering, correlation, and schema compatibility. |

## Java Coding Rules

- Prefer immutable domain objects and explicit constructors or factories that validate invariants.
- Use records for simple immutable DTOs where framework compatibility allows.
- Use sealed interfaces or enums for closed domain state sets when they improve clarity.
- Avoid static global state for business behavior.
- Keep checked and unchecked exception usage consistent through a service-level exception policy.
- Use narrow interfaces for outbound ports and repositories.
- Keep transactions in application services, not controllers.
- Keep mapping explicit at service boundaries.
- Do not log raw passwords, tokens, PAN, CVV, national identifiers, full addresses, or sensitive profile data.

Example domain value:

```java
public record ReplacementReason(String value) {
    public ReplacementReason {
        if (value == null || value.isBlank()) {
            throw new IllegalArgumentException("replacement reason is required");
        }
    }
}
```

## Repository Structure

Backend services must use this structure:

```text
service-name/
├── build.gradle or build.gradle.kts
├── settings.gradle or settings.gradle.kts
├── openapi/
├── asyncapi/
├── helm/
├── src/main/java/com/<company>/<domain>/<service>/
│   ├── Application.java
│   ├── transport/
│   ├── application/
│   ├── domain/
│   ├── persistence/
│   ├── integration/
│   ├── messaging/
│   ├── security/
│   ├── observability/
│   └── config/
└── src/test/java/com/<company>/<domain>/<service>/
    ├── unit/
    ├── component/
    ├── integration/
    ├── contract/
    └── performance/
```

## Build And Quality Plugins

Each service must configure:

- OpenAPI generation for inbound REST contracts and generated DTO/interfaces.
- Spotless for formatting.
- Checkstyle for structural code rules.
- PMD for maintainability and defect-prone patterns.
- SpotBugs for bytecode-level defect detection.
- JaCoCo for coverage reporting.
- Sonar reporting for quality and security evidence.
- Jib or Docker image build.
- Helm packaging or release chart validation.

## Packaging And Runtime

- Build immutable artifacts once and promote the same artifact across environments.
- Use Jib or multi-stage Docker builds to produce minimal runtime images.
- Publish container image, Helm chart, and build metadata through approved artifact repositories.
- Configure Spring Boot Actuator liveness and readiness endpoints.
- Run containers as non-root with read-only filesystem where possible.
- Use environment variables and secret managers for runtime configuration.

## Pull Request Evidence

Backend PRs must include:

- linked requirement IDs and Jira references where available
- test evidence from unit, component, integration, contract, and security checks as applicable
- generated-code summary where OpenAPI or schema generation is involved
- JaCoCo and Sonar evidence
- migration and rollback notes when persistence changes exist
- observability and operational impact notes

