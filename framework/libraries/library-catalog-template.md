# Library Catalog Template

## Purpose

Register every shared library with its owner, versioning rules, consumer squads, and compatibility requirements.

## Template

| Field | Value |
| --- | --- |
| Library Name |  |
| Library Path |  |
| Owning Squad |  |
| Technical Owner |  |
| Business Owner |  |
| Public API Surface |  |
| Internal API Surface |  |
| Known Consumers |  |
| CODEOWNERS Path |  |
| Required Reviewers |  |
| Compatibility Policy |  |
| Contract Tests |  |
| Regression Tests |  |
| Release Notes Requirement |  |

## Example

| Field | Value |
| --- | --- |
| Library Name | payment-common |
| Library Path | `libraries/payment-common/` |
| Owning Squad | Payments Platform squad |
| Technical Owner | Payments platform engineering lead |
| Business Owner | Payments platform product owner |
| Public API Surface | money types, idempotency helpers, event envelopes, shared validation |
| Internal API Surface | parsing helpers, internal mappers |
| Known Consumers | local payments, remittance, cards |
| CODEOWNERS Path | `/libraries/payment-common/` |
| Required Reviewers | Payments Platform squad, local payments, remittance, cards |
| Compatibility Policy | additive first, deprecate before removal |
| Contract Tests | consumer compatibility tests |
| Regression Tests | consumer regression suites |
| Release Notes Requirement | required for every public API change |

## Do / Don't Rules

Do:

- treat shared libraries as products
- version public API changes
- list all known consumers

Do not:

- release a breaking change without consumer review
- hide behavioral changes behind a refactor label
- let one squad own the library privately if others consume it

