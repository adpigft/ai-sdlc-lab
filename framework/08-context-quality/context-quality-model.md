# Context Quality Model

## Purpose

Context is a governed asset in this framework.

It shapes what an agent sees, how it reasons, and which outputs it can safely produce. Context therefore needs the same discipline as other delivery assets: versioning, review, validation, provenance, and security controls.

## Context Lifecycle

Create -> Validate -> Package -> Distribute -> Observe -> Improve

## Quality Layers

| Layer | Purpose | Typical Check |
| --- | --- | --- |
| L1 Syntax | Verify the context is machine-readable and structurally valid. | YAML/JSON/Markdown parse checks, schema checks. |
| L2 Structure | Verify the expected sections and relationships are present. | Required headings, fields, references, and hierarchy checks. |
| L3 Completeness | Verify the context contains the required inputs for the task. | Missing section detection, required metadata coverage. |
| L4 Consistency | Verify the context does not contradict source facts. | Cross-check against Git artifacts, traceability, and known state. |
| L5 Usefulness / Evals | Verify the context helps an agent do useful work. | Task evals, judge rubrics, review outcomes, and human feedback. |

## Evaluation Rules

- Deterministic checks validate objective facts.
- LLM judges validate semantic quality.
- Task evals validate practical usefulness.
- Humans approve business and risk decisions.

## Governance Rules

- Context packages must have provenance.
- Context packages must be scoped to a project, domain, capability, squad, feature, or operational need.
- Context security scanning is required before distribution.
- Context drift must be observable after distribution.
- Context reuse is allowed only through versioned packages.
- Sensitive data must not be packaged by default.

## Notes

- This model defines the control layer for future context packaging and observability.
- It does not replace Git-owned framework artifacts.
