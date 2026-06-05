# Shared Library And Gradle Tooling Standard

## Purpose

Define standards for Java shared libraries, Gradle build conventions, generated code, plugins, and reusable platform tooling.

## Shared Library Rules

Shared libraries are allowed when behavior is stable, reusable, versioned, and owned. They must not become a hidden shared domain model across bounded contexts.

Use a shared library for:

- stable cross-cutting infrastructure helpers
- API or event generated models where ownership and compatibility are clear
- logging, tracing, masking, and error handling utilities
- test support utilities
- client wrappers with clear versioning and compatibility rules

Do not use a shared library for:

- volatile business rules
- aggregate behavior owned by one bounded context
- orchestration logic that changes with one capability
- provider-specific behavior that should be isolated behind a service adapter
- shared mutable state

## Library Ownership

Each shared library must define:

- owner
- purpose
- public API surface
- compatibility promise
- supported Java and Spring Boot versions where applicable
- release and deprecation policy
- known consumers
- security and license scan expectations

## Java Gradle Tooling

Java services and libraries should standardize on Gradle Groovy or Gradle Kotlin DSL.

Required build capabilities:

- Java 21 toolchain configuration
- dependency locking or approved dependency governance
- OpenAPI Generator integration where REST contracts exist
- Avro or schema generation where event contracts exist
- Spotless formatting
- Checkstyle rules
- PMD rules
- SpotBugs analysis
- JUnit 5 test execution
- JaCoCo coverage reporting
- Sonar report publication
- Jib or Docker image build for services
- Helm package or chart validation for deployable services

## Generated Code Governance

- Generated code must be reproducible from versioned contracts or schemas.
- Generated code must not be manually edited.
- Generated outputs must be isolated from handwritten domain and application logic.
- Build pipelines must fail when generated code is stale where that check is supported.
- PRs must identify generated-code changes and the source contract or schema that caused them.

## Versioning

- Use semantic versioning for libraries and Gradle plugins.
- Breaking changes require major version updates, migration notes, and consumer impact review.
- Backward-compatible additions require minor versions.
- Bug fixes require patch versions.
- Deprecated APIs must include removal timeline and replacement guidance.

## Publication

- Publish libraries and plugins to approved artifact repositories.
- Sign or verify artifacts where policy requires.
- Publish source and documentation artifacts where useful for consumers.
- Do not publish artifacts containing secrets, environment-specific values, or generated credentials.

## Review Checklist

- The shared library is justified instead of copying, service extraction, or local implementation.
- Ownership and compatibility rules are clear.
- Public APIs are small and stable.
- Build tooling uses the approved Java quality stack.
- Generated code is reproducible and isolated.
- Consumers and migration risks are identified.

