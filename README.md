# AI-Native SDLC Framework

## What Is This?

This repository provides a **spec-driven AI-native delivery framework** for building banking and digital platform capabilities.

The framework helps teams move from:

```text
Idea
→ Intent
→ Specification
→ Architecture
→ API Contract
→ Test Design
→ Implementation
→ Validation
→ Release
→ Feedback
```

The framework supports:

- Product Owners (PO)
- Business Analysts (BA)
- Solution Architects (SA)
- Developers
- QA Engineers
- DevSecOps Engineers

### Source of Truth

| Purpose | Tool |
|----------|----------|
| Delivery Artifacts | Git |
| Workflow & Approvals | Jira |
| Stakeholder Summaries | Confluence |
| Validation & Automation | GitHub Actions |

Git remains the single source of truth for all delivery artifacts.

---

# Repository Structure

```text
domains/
├── <domain>/
│   ├── domain-context.md
│   └── capabilities/
│       └── <capability>/
│           ├── intent/
│           ├── specs/
│           ├── context/
│           ├── contracts/
│           ├── tests/
│           ├── design/
│           ├── validation/
│           ├── release/
│           └── workflow-state.yaml

apps/
├── mobile-banking-app/

services/
├── payments/
├── cards/
├── deposits/
├── lending/
├── operations/

libraries/

platform/

framework/

traceability/

feedback/

scripts/

src/
```

---

# First Time Setup

## Prerequisites

Install:

- Git
- Java 21
- Python 3
- Codex CLI
- GitHub Account

Optional:

- Jira Access
- Confluence Access

## Validate Repository

Run:

```bash
bash scripts/validate-workflow-state.sh
bash scripts/validate-artifacts.sh
bash scripts/validate-traceability.sh
bash scripts/validate-openapi.sh
bash scripts/validate-java.sh
```

Expected result:

```text
All validations passed.
```

---

# Learn The Framework

Start with the sample capability:

```text
domains/payments/capabilities/khqr-payment-reversal/
```

Review:

```text
intent/
specs/
context/
contracts/
tests/
design/
validation/
workflow-state.yaml
```

Check current workflow state:

```text
Status.
```

---

# Creating A New Capability

Example:

```text
Existing Domain:
payments

New Capability:
KHQR Payment Reversal
```

Workflow:

```text
$new KHQR Payment Reversal

Review.
Approved.

$specification

Review.
Approved.

$architecture

Review.
Approved.

$test-design

Review.
Approved.

$implementation

Review.
Approved.

$validation

Review.
Approved.

$release
```

---

# Creating A New Domain

Example:

```text
cards
```

Create:

```text
domains/cards/domain-context.md
```

Define:

- Domain glossary
- Business boundaries
- Shared APIs
- Shared Events
- Integrations
- Security requirements
- Ownership

Then create the first capability:

```text
$new Card Replacement
```

---

# Change Request Workflow

Example:

```text
$change-request Support Partial Refund
```

Workflow:

```text
Impact Analysis
→ Review
→ Approval
→ Update Impacted Artifacts
→ Validation
→ Release
```

Only update impacted artifacts.

Do not regenerate the entire solution.

---

# Defect Workflow

Example:

```text
$defect-fix Duplicate Reversal
```

Workflow:

```text
Defect
→ Root Cause Analysis
→ Review
→ Approval
→ Fix
→ Validation
→ Release
```

Only update impacted artifacts.

---

# Frontend Model

Shared Flutter application:

```text
apps/mobile-banking-app/
```

Feature modules:

```text
apps/mobile-banking-app/features/onboarding/
apps/mobile-banking-app/features/payments/
apps/mobile-banking-app/features/cards/
apps/mobile-banking-app/features/deposits/
apps/mobile-banking-app/features/lending/
```

### Ownership

| Asset | Owner |
|---------|---------|
| App Shell | Channel Squad |
| Payments Features | Payments Squad |
| Cards Features | Cards Squad |
| Deposits Features | Deposits Squad |
| Lending Features | Lending Squad |

---

# Backend Model

Services are organized by domain:

```text
services/payments/local-payment-service/
services/payments/international-payment-service/
services/payments/remittance-service/

services/cards/card-management-service/

services/deposits/account-service/

services/lending/loan-service/

services/operations/case-management-service/
```

### Ownership

Each squad owns its services and APIs.

---

# APIs, Events, and Integrations

## APIs

API contracts are stored in:

```text
contracts/openapi.yaml
```

## Events

Event definitions are stored under:

```text
events/
```

Examples:

```text
PaymentCreated
PaymentReversed
CardIssued
AccountOpened
LoanApproved
```

## Integrations

Examples:

```text
Core Banking
Cards Processor
AML
Fraud
Notifications
Payment Rails
```

Integration details belong in:

```text
context/
```

---

# Bootstrap Templates

Platform teams provide reusable templates:

```text
platform/templates/flutter-app-template/

platform/templates/spring-boot-service-template/

platform/templates/shared-library-template/

platform/templates/kafka-service-template/
```

Use templates for consistency across squads.

---

# Standards

The framework follows shared standards for:

- Architecture
- API Design
- Security
- Coding
- Testing
- Observability
- Release Management

Standards are maintained under:

```text
framework/
```

---

# Multi-Squad Governance

## Ownership Rules

| Asset | Owner |
|----------|----------|
| Domain Context | Domain Owner |
| Capability | Product Squad |
| Service | Service Owner |
| API Contract | Service Owner |
| Event Schema | Producing Squad |
| Shared Library | Platform Squad |
| Flutter Shell | Channel Squad |

### Rules

- Squads own their domains.
- Shared assets require owner approval.
- APIs and events must be reviewed before breaking changes.
- All changes must be traceable.

---

# When Can Code Be Created?

Application code must not be created until:

- Intent Approved
- Specification Approved
- Architecture Approved
- API Contract Approved
- Test Design Approved
- Traceability Reviewed
- Implementation Slice Approved

Only then may teams modify:

```text
src/
services/
apps/
libraries/
```

---

# What Is Stored In src?

The framework separates delivery artifacts from implementation code.

## Delivery Artifacts

```text
domains/
```

Contains:

- Intent
- Specifications
- Architecture
- Contracts
- Tests
- Validation
- Release Evidence

## Source Code

```text
src/main/
src/test/
```

Contains:

- Application Code
- Unit Tests
- Integration Tests

Example:

```text
domains/payments/capabilities/khqr-payment-reversal/

src/main/java/payments/khqrreversal/
src/test/java/payments/khqrreversal/
```

---

# Automation

## GitHub Actions

Validates:

- Workflow State
- Artifacts
- Traceability
- OpenAPI Contracts
- Java Compilation
- Tests

## Jira

Current:

```text
Offline Payload Generation
```

Future:

```text
Epic Creation
Story Creation
Status Synchronisation
Approval Synchronisation
```

## Confluence

Current:

```text
Offline Summary Generation
```

Future:

```text
Automatic Publishing
```

---

# Commands

## User Commands

```text
$new

$change-request

$defect-fix

Status.

Review.

Approved.

Proceed.
```

## Lifecycle Commands

```text
$specification

$architecture

$test-design

$implementation

$validation

$release

$traceability-review

$feedback-capture
```

---

# Definition Of Ready (DoR)

Before implementation:

- Intent Approved
- Specification Approved
- Architecture Approved
- API Contract Approved
- Test Design Approved
- Traceability Reviewed
- Implementation Slice Approved

---

# Definition Of Done (DoD)

For an implementation slice:

- Code Complete
- Tests Passing
- Traceability Updated
- Validation Evidence Captured
- Review Complete

Release approval is separate from DoD.

---

# Golden Rules

1. Git is the source of truth.
2. Jira manages workflow and approvals.
3. Confluence publishes stakeholder summaries.
4. Do not generate code before approvals.
5. Do not regenerate entire solutions for changes.
6. Do not modify another squad's service without approval.
7. Keep changes small and traceable.
8. Human approvals are mandatory.
9. AI assists delivery but does not replace governance.
10. Every requirement must trace to implementation, validation, and release evidence.

---

# First Exercise

Try the framework with a simple capability:

```text
$new Test Capability

Review.
Approved.

$specification

Review.
Approved.

Status.
```

Do not implement code in the first exercise.

Focus on understanding the workflow before moving to implementation.