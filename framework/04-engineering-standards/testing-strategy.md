# Testing Strategy

## Purpose

This strategy defines reusable testing guidance for AI SDLC delivery across projects. It complements `framework/04-engineering-standards/standards/testing-standards.md` and does not change the lifecycle, add skills, or replace feature-level test artifacts.

Use this document to decide what testing is needed, who owns it, which tests should be automated, and how AI-generated tests are governed before feature delivery moves through existing approval gates.

## 1. Testing Taxonomy

| Test Type | Purpose | Typical Evidence | Primary Stage |
| --- | --- | --- | --- |
| Acceptance tests | Validate approved business behavior, scenarios, and edge cases from the specification. | `tests/acceptance.feature`, validation report, traceability rows | `$test-design`, `$validation` |
| Unit tests | Validate isolated domain rules, calculations, state transitions, and error handling. | Source test files, coverage output, PR evidence | `$implementation`, `$pr-review` |
| Integration tests | Validate service, database, queue, external processor, ledger, notification, or fraud-service boundaries. | Integration test output, mocked or sandbox dependency evidence | `$implementation`, `$validation` |
| Contract tests | Validate API, event, and schema compatibility between producers and consumers. | OpenAPI validation, schema checks, consumer/provider evidence | `$design`, `$test-design`, `$pr-review` |
| Security tests | Validate authorization, authentication, input handling, replay resistance, data masking, and sensitive-data controls. | Security test output, review findings, static analysis, approved exceptions | `$test-design`, `$pr-review`, `$validation` |
| Performance tests | Validate latency, throughput, capacity, timeout, retry, and degradation behavior for agreed NFRs. | Load test output, NFR evidence, monitoring evidence | `$test-design`, `$validation` |
| Resilience tests | Validate retries, idempotency, duplicate handling, failover, rollback, recovery, and reconciliation. | Scenario evidence, operational test output, incident simulation notes | `$test-design`, `$validation` |
| Operational tests | Validate logging, metrics, traces, alerting, dashboards, runbooks, and release observability. | Observability checks, release evidence, validation report | `$validation`, `$release` |
| Regression tests | Protect previously approved behavior from unintended change. | Automated suite output, impacted capability evidence | `$implementation`, `$pr-review`, `$validation` |
| Exploratory tests | Investigate usability, edge cases, integration ambiguity, and risk areas not fully covered by scripted tests. | Session notes, defects, feedback entries | `$validation`, `$feedback-capture` |

## 2. Testing Ownership Model

| Role | Accountability |
| --- | --- |
| PO / BA | Own business acceptance intent, scenario meaning, requirement priority, and approval that tests represent expected behavior. |
| QA Lead / QA | Own test strategy application, acceptance scenarios, negative scenarios, validation evidence, defect verification, and release recommendation. |
| Developer / Developer Lead | Own unit, integration, regression, and implementation-level automation. Provide runnable evidence in PRs. |
| Solution Architect | Own test impact for architecture, APIs, events, integrations, resilience, NFRs, and cross-domain compatibility. |
| Security / DevSecOps | Own security testing expectations, CI security gates, secret handling, platform controls, and risk acceptance evidence. |
| Platform / SRE | Own environment readiness, observability validation, deployment verification, rollback checks, and operational evidence. |
| AI Assistant | May draft tests, identify gaps, propose automation candidates, and summarize evidence, but does not approve tests or replace human accountability. |

Testing ownership follows existing artifact and approval ownership. This model does not create new lifecycle states or approval gates.

## 3. Testing Automation Maturity Model

| Level | Description | Expected Behavior |
| --- | --- | --- |
| Level 0: Manual evidence | Tests are executed manually or reviewed as checklists. | Acceptable for early discovery and one-off evidence only when risk is low and approval records the limitation. |
| Level 1: Scripted checks | Repeatable local scripts validate formatting, contracts, workflow state, traceability, or build health. | Required for framework validation and PR readiness where scripts exist. |
| Level 2: CI-executed tests | Automated tests run in CI for pull requests and protected branches. | Required for stable feature implementation once executable code exists. |
| Level 3: Risk-based quality gates | CI blocks merge on required suites, coverage thresholds, static analysis, contract checks, and security findings. | Recommended for regulated or multi-squad delivery. |
| Level 4: Continuous validation | Tests, monitoring, synthetic checks, and production telemetry validate behavior before and after release. | Target state for high-risk banking flows, critical APIs, and operationally sensitive capabilities. |

Maturity level is chosen per capability or feature based on risk, not as a mandatory lifecycle change.

## 4. Phase 1 Pilot Scope

Phase 1 keeps testing practical and framework-level. It proves the control model before expanding automation.

In scope:

- Maintain acceptance scenarios in feature-level `tests/acceptance.feature` artifacts.
- Require traceability from mandatory requirements to planned tests or explicit review controls.
- Run existing framework validation scripts locally and in GitHub Actions.
- Use OpenAPI validation where contracts exist.
- Use Java validation where executable Java code exists.
- Record test and validation evidence in `validation/validation-report.md`.
- Identify automation candidates during `$test-design`, `$implementation`, and `$pr-review`.
- Treat AI-generated tests as drafts requiring human review.

Out of scope for Phase 1:

- New lifecycle states.
- New skills.
- Mandatory enterprise coverage thresholds.
- Mandatory end-to-end test environments for every feature.
- Tool-specific test management system integration.
- Changes to domain artifacts or application source code as part of this strategy.

## 5. Future Phases

Future phases may add project-specific automation depth without changing the framework lifecycle.

| Phase | Focus | Possible Additions |
| --- | --- | --- |
| Phase 2 | Broader CI automation | Unit and integration test execution, coverage reporting, linting, static analysis, contract compatibility checks. |
| Phase 3 | Quality gates | Branch protection, required CI checks, coverage thresholds, security scan blocking rules, dependency policy gates. |
| Phase 4 | Environment and release validation | Ephemeral environments, smoke tests, synthetic monitoring, deployment verification, rollback rehearsal evidence. |
| Phase 5 | Continuous assurance | Production telemetry checks, automated control evidence, model-assisted regression analysis, release risk dashboards. |

Each future phase should be introduced through approved framework changes and project governance, not by bypassing the current lifecycle.

## 6. CI/CD Integration Points

| Integration Point | Purpose | Current / Target Use |
| --- | --- | --- |
| Pull request validation | Detect broken artifacts, contracts, traceability, or build behavior before merge. | Current GitHub Actions runs framework validation scripts. |
| Protected branch validation | Prevent unvalidated changes from entering authoritative branches. | Target branch protection should require relevant CI checks. |
| Contract validation | Check OpenAPI and schema compatibility where contracts exist. | Current OpenAPI script validates available contracts. |
| Build and unit test execution | Check executable code health and fast regression behavior. | Current Java validation is available where Java code exists. |
| Security and static analysis | Identify vulnerable dependencies, insecure code, and policy violations. | Target integration with approved project tools such as SonarCloud or equivalent scanners. |
| Release validation | Confirm validation evidence, release readiness, rollback, and known risks before release. | Current release-readiness script checks Git evidence consistency. |
| Post-release monitoring | Confirm deployed behavior and operational health after release. | Future target using project observability tooling. |

CI/CD validates evidence. It does not replace required human approvals.

## 7. AI-Generated Testing Strategy

AI may assist testing by:

- Drafting acceptance scenarios from approved intent and specification.
- Suggesting negative, boundary, security, integration, resilience, and NFR scenarios.
- Proposing unit and integration test cases from approved design and implementation plans.
- Reviewing traceability gaps between requirements, tests, implementation, and validation evidence.
- Summarizing validation output and identifying missing evidence.
- Generating candidate test code after implementation is approved.

AI-generated tests must:

- Be reviewed by the accountable human owner before approval.
- Trace to approved requirements, design decisions, risks, or defects.
- Avoid inventing unapproved behavior or hidden requirements.
- Avoid hardcoded secrets, customer data, production credentials, or sensitive identifiers.
- Be treated as untrusted until executed or reviewed with evidence.
- Be updated when approved requirements, contracts, design, or defects change.

AI must stop and report a gap when approved upstream artifacts are missing, stale, or inconsistent. It must not code around missing test design, approval evidence, or traceability.

## 8. Automation Candidate Assessment

Use this assessment during `$test-design`, `$implementation`, `$pr-review`, and `$validation` to decide which checks should be automated.

| Assessment Factor | Automate When | Prefer Manual / Review Control When |
| --- | --- | --- |
| Business criticality | Failure would affect money movement, customer access, regulatory reporting, fraud controls, or auditability. | Scenario is informational or low-risk. |
| Repeatability | The same check will be run across PRs, releases, or regression cycles. | The check is exploratory or one-time. |
| Determinism | Inputs, environment, and expected outputs are stable enough for reliable execution. | Results require subjective judgment or unstable external systems. |
| Execution cost | Automation is cheaper than repeated manual execution after initial setup. | Setup cost is high and expected reuse is low. |
| Failure signal | Failure points clearly to a defect, contract break, configuration issue, or missing evidence. | Failure would produce ambiguous or noisy results. |
| Data safety | Synthetic or masked data can validate behavior without sensitive exposure. | Test data cannot be safely automated yet. |
| Environment availability | Required dependencies can be mocked, simulated, containerized, or made available in CI. | Dependencies are unavailable and cannot be safely simulated. |
| Compliance value | Automated evidence helps prove control operation, traceability, or release readiness. | Human attestation is the required control. |

Automation candidates should be recorded in feature test design, implementation plans, PR review notes, or validation reports according to the active skill.

## 9. Mapping to Framework Skills

| Skill | Testing Strategy Use |
| --- | --- |
| `$intent` | Capture business outcomes, risk areas, exclusions, and validation expectations at a high level. Do not design tests prematurely. |
| `$specification` | Define testable functional requirements, NFRs, business rules, edge cases, and acceptance criteria. |
| `$design` | Identify test-impacting APIs, events, integrations, data, state transitions, security controls, resilience behavior, and observability needs. |
| `$test-design` | Create acceptance, negative, integration, contract, security, regression, and NFR scenarios from approved requirements and design. Assess automation candidates. |
| `$implementation` | Add or update approved automated tests for the active implementation slice and collect local evidence. |
| `$pr-review` | Review test coverage, automation evidence, CI output, standards alignment, traceability, and unresolved risks before validation. |
| `$validation` | Execute or review approved validation evidence, record results, identify defects or gaps, and make release-readiness recommendations. |
| `$release` | Confirm validation evidence, unresolved defects, accepted risks, rollback checks, and operational readiness are reflected in release notes. |
| `$traceability-review` | Check that requirements, tests, implementation evidence, validation evidence, and release references are connected. |
| `$feedback-capture` | Record defects, stakeholder findings, missed scenarios, automation gaps, and lessons learned for follow-up. |
| `$defect-fix` | Use RCA to identify missing or weak tests and add targeted regression coverage after approval. |
| `$change-request` | Reassess impacted requirements, tests, automation candidates, validation evidence, and release risk. |
| `$decision` | Capture architecture or testing decisions when automation scope, environment strategy, tool choice, or quality gates require approval. |

This mapping describes how testing strategy supports existing skills. It does not add new skills or alter lifecycle order.
