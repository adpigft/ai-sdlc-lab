# Frontend Catalog Template

## Purpose

Define shared Flutter app ownership, app shell ownership, shared component ownership, domain feature module ownership, allowed paths, restricted paths, and approval rules.

The frontend catalog removes guesswork before implementation starts.

## Shared Flutter App Ownership Model

A single shared Flutter app can host multiple banking domains:

```text
apps/mobile-banking-app/
  shell/
  shared/
  features/
    onboarding/
    deposits/
    payments/
    cards/
    lending/
    operations/
```

The folders above are placement examples only. This template does not create the app folders.

## Ownership Rules

| Area | Owner | Responsibility |
| --- | --- | --- |
| App Shell | Channel Platform Squad | app bootstrap, routing shell, auth bootstrap, navigation shell, telemetry bootstrap |
| Shared Components | Channel Platform Squad | design-system integration, shared components, shared state utilities, shared validation components |
| Domain Feature Modules | Domain squads | domain screens, forms, feature state, domain API client usage, feature-specific validation |

Feature modules are owned by domain squads:

- `features/onboarding/` owned by Onboarding Squad
- `features/deposits/` owned by Deposits Squad
- `features/payments/` owned by Payments Squad
- `features/cards/` owned by Cards Squad
- `features/lending/` owned by Lending Squad
- `features/operations/` owned by Operations Squad

## Catalog Entry Format

| Field | Description |
| --- | --- |
| `app_name` | Frontend application name. |
| `app_path` | Planned or existing app path. |
| `shell_owner` | Owner of app shell and global runtime behavior. |
| `shared_component_owner` | Owner of shared UI components and shared frontend utilities. |
| `feature_module_path` | Domain feature path. |
| `feature_owner_squad` | Squad that owns the feature module. |
| `allowed_paths` | Paths the owning squad may modify for an approved slice. |
| `restricted_paths` | Paths that require other owner approval or must not be touched. |
| `approval_rules` | Required approvals for module, shell, shared, or cross-feature changes. |

## Mobile Banking App Example

| app_name | app_path | area | owner | allowed_paths | restricted_paths | approval_rules |
| --- | --- | --- | --- | --- | --- | --- |
| mobile-banking-app | `apps/mobile-banking-app/` | shell | Channel Platform Squad | `apps/mobile-banking-app/shell/**` | `apps/mobile-banking-app/features/**` unless impacted squad approves | Channel Platform approval; impacted domain review for route/nav/auth impact |
| mobile-banking-app | `apps/mobile-banking-app/` | shared | Channel Platform Squad | `apps/mobile-banking-app/shared/**` | feature modules unless impacted squad approves | Channel Platform approval; impacted feature regression required |
| mobile-banking-app | `apps/mobile-banking-app/` | onboarding feature | Onboarding Squad | `apps/mobile-banking-app/features/onboarding/**` | shell, shared, other features | Onboarding approval; Channel Platform approval for shell/shared impact |
| mobile-banking-app | `apps/mobile-banking-app/` | deposits feature | Deposits Squad | `apps/mobile-banking-app/features/deposits/**` | shell, shared, other features | Deposits approval; Channel Platform approval for shell/shared impact |
| mobile-banking-app | `apps/mobile-banking-app/` | payments feature | Payments Squad | `apps/mobile-banking-app/features/payments/**` | shell, shared, other features | Payments approval; Channel Platform approval for shell/shared impact |
| mobile-banking-app | `apps/mobile-banking-app/` | cards feature | Cards Squad | `apps/mobile-banking-app/features/cards/**` | shell, shared, other features | Cards approval; Channel Platform approval for shell/shared impact |
| mobile-banking-app | `apps/mobile-banking-app/` | lending feature | Lending Squad | `apps/mobile-banking-app/features/lending/**` | shell, shared, other features | Lending approval; Channel Platform approval for shell/shared impact |
| mobile-banking-app | `apps/mobile-banking-app/` | operations feature | Operations Squad | `apps/mobile-banking-app/features/operations/**` | shell, shared, other features | Operations approval; Channel Platform approval for shell/shared impact |

## Cross-Feature And Shared Change Rules

- Shared frontend changes require platform/channel approval.
- Cross-feature changes require impacted squad review.
- Shell routing, auth, navigation, telemetry, and design-system integration are not module-local.
- Feature squads must not modify another feature module without explicit owner approval.
- Implementation plans must define `target_app`, `target_frontend_module`, `allowed_paths`, `restricted_paths`, and required approvals before coding.
