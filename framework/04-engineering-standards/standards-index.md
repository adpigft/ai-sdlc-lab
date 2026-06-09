# Engineering Standards Index

## Purpose

This index is the entry point for reusable enterprise engineering standards. The standards are framework-level guidance for delivery teams and do not change lifecycle order, skills, workflow orchestration, domain artifacts, or source code.

Backend standards are Java-first: Java 21, Spring Boot 3.x, Gradle, OpenAPI Generator, Spring Security, OpenTelemetry, Micrometer, JUnit 5, Mockito, RestAssured, Testcontainers, Flyway, JaCoCo, Sonar, Spotless, Checkstyle, PMD, SpotBugs, Jib or Docker, Helm, and GitHub Actions.

## Standards

| Standard | Purpose |
| --- | --- |
| `java-spring-boot-bootstrap.md` | Java 21 and Spring Boot 3.x service structure, clean architecture, coding, build, packaging, and repository conventions. |
| `flutter-bootstrap.md` | Flutter channel app and feature module standards, including feature-first architecture, state management, secure storage, accessibility, and test types. |
| `openapi-generation-standard.md` | Contract-first REST API design and OpenAPI Generator expectations for Java services and Flutter clients. |
| `api-security-standard.md` | REST, GraphQL, OAuth2/OIDC, JWT validation, authorization, abuse-control, and sensitive-data API security standards. |
| `database-design-standard.md` | PostgreSQL, MongoDB, schema migration, data ownership, encryption, backup, and recovery standards. |
| `event-design-standard.md` | Kafka, event naming, schema governance, partitioning, retry, DLQ, and transactional outbox standards. |
| `testing-standard.md` | Automation testing layers, tooling, data management, reporting, and CI expectations. |
| `security-quality-gates.md` | Security, static analysis, coverage, dependency, container, secret, and branch protection quality gates. |
| `ai-code-review-standard.md` | Human review expectations for AI-generated code, tests, artifacts, and design changes. |
| `microservice-decomposition-standard.md` | DDD bounded-context decomposition, modularity, service splitting, and consolidation guidance. |
| `reference-architecture-standard.md` | Clean Architecture, C4, sequence, data-flow, observability, deployment, and folder structure reference. |
| `system-modeling-standard.md` | C4, sequence, and data flow diagram standards for architecture, security, and delivery review. |
| `observability-standard.md` | OpenTelemetry, Micrometer, structured logging, tracing, metrics, alerting, and telemetry evidence standards. |
| `shared-library-gradle-standard.md` | Java shared library governance, Gradle tooling, generated code, versioning, and publication standards. |
| `change-management-standard.md` | Backward-compatible delivery, migration sequencing, API/event change control, release evidence, and rollback expectations. |
| `testing-strategy.md` | Framework-level testing taxonomy, ownership, maturity model, AI-generated testing guidance, and skill mapping. |

## Non-Goals

- These documents do not create implementation approval.
- These documents do not add lifecycle stages or skills.
- These documents do not replace feature-level intent, requirements, design, test design, implementation plan, validation, or release artifacts.
- These documents do not authorize domain artifact or source-code changes without the relevant lifecycle approval.
