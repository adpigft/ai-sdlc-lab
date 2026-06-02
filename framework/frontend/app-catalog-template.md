# Frontend App Catalog Template

## Purpose

Register each frontend application, shared shell, and feature module with its owning squad and cross-squad review requirements.

## Template

| Field | Value |
| --- | --- |
| App Name |  |
| App Path |  |
| Owning Squad |  |
| Platform Owner |  |
| Feature Modules |  |
| Shared Shell Ownership |  |
| Shared Design System |  |
| Public Entry Points |  |
| Backend Dependencies |  |
| CODEOWNERS Path |  |
| Required Reviewers |  |
| UI Regression Tests |  |
| API Contract Tests |  |
| Rollback Notes |  |

## Example

| Field | Value |
| --- | --- |
| App Name | mobile-banking-app |
| App Path | `apps/mobile-banking-app/` |
| Owning Squad | Mobile Banking squad |
| Platform Owner | Platform Frontend squad |
| Feature Modules | local payments, remittance, cards |
| Shared Shell Ownership | Mobile Banking squad + Platform Frontend for shell/core routing |
| Shared Design System | Platform Frontend squad |
| Public Entry Points | login, dashboard, payments, remittance, cards |
| Backend Dependencies | local-payment-service, remittance-service, card-management-service |
| CODEOWNERS Path | `/apps/mobile-banking-app/` |
| Required Reviewers | Mobile Banking squad, Platform Frontend for shell changes, impacted feature squad for module changes |
| UI Regression Tests | shell smoke tests, module regression tests |
| API Contract Tests | service contract tests for each backend dependency |
| Rollback Notes | feature flag or shell rollback depending on change type |

## Do / Don't Rules

Do:

- split shell ownership from feature-module ownership
- name the owning squad for each module boundary
- require platform review for shell or shared runtime changes

Do not:

- let every feature squad own the full app shell
- ship a shared shell change without regression coverage
- treat UI changes as isolated when they alter shared routes, auth, or telemetry

