# Flutter Bootstrap Standard

## Purpose

Define Flutter channel app and feature module standards for digital banking delivery. Flutter standards remain channel-focused and compatible with feature-first Clean Architecture.

## Technology Baseline

| Area | Standard |
| --- | --- |
| Architecture | Feature-first Clean Architecture |
| State management | BLoC or Riverpod |
| Dependency injection | GetIt and Injectable |
| Networking | Dio and Retrofit-generated clients |
| Routing | GoRouter or AutoRoute |
| Secure storage | flutter_secure_storage |
| Local storage | Hive or sqflite with encryption where sensitive |
| Visual regression | golden_toolkit or equivalent golden testing |
| Integration testing | Patrol, Appium, or approved mobile integration framework |
| CI/CD | GitHub Actions and approved mobile release orchestration |

## Feature-First Structure

```text
flutter-feature-name/
├── pubspec.yaml
├── analysis_options.yaml
├── android/
├── ios/
├── assets/
│   ├── icons/
│   └── themes/
├── lib/
│   ├── main.dart
│   ├── app/
│   │   ├── config/
│   │   └── observers/
│   ├── core/
│   │   ├── error/
│   │   ├── network/
│   │   ├── theme/
│   │   └── utils/
│   └── features/
│       └── <feature>/
│           ├── data/
│           │   ├── datasources/
│           │   ├── models/
│           │   └── repositories/
│           ├── domain/
│           │   ├── entities/
│           │   ├── usecases/
│           │   └── repositories/
│           └── presentation/
│               ├── bloc/
│               ├── pages/
│               └── widgets/
└── test/
    ├── unit/
    ├── widget/
    ├── golden/
    └── integration/
```

## Architecture Rules

- UI widgets must render state and emit user intents; they must not contain business calculations or network orchestration.
- Domain use cases must be independent from UI and transport details.
- Data repositories must isolate remote APIs, cache, and model parsing.
- Generated Retrofit clients must be kept in the network/data boundary.
- Feature modules must own their journeys and avoid accidental shared component changes.
- Shared channel components require Channel Platform review.

## Security Requirements

- Use Authorization Code Flow with PKCE for mobile authentication.
- Store tokens and sensitive local values in secure storage.
- Disable mobile backup for sensitive local files and secure preferences.
- Use certificate pinning where approved by the channel security model.
- Sanitize deep-link route parameters before navigation.
- Use privacy shielding for sensitive pages when the app is backgrounded.
- Disable screenshots on approved sensitive journeys.
- Use feature flags for high-risk flows and rollback control.

## UI Foundation

- Use design tokens for colors, typography, spacing, elevations, and interactive states.
- Map tokens to Material 3 variables where possible.
- Support light and dark modes where channel policy requires.
- Provide loading, success, empty, error, and retry states for asynchronous journeys.
- Preserve accessibility labels, focus order, and target sizing.
- Meet WCAG 2.1 AA contrast expectations and support system text scaling up to 2.0 without broken layouts.
- Support localization, right-to-left layouts where required, local date formats, and localized currency strings.

## Testing Expectations

| Test Type | Purpose |
| --- | --- |
| Unit | Validate BLoC/Riverpod state transitions, use cases, model parsers, and validation logic. |
| Widget | Validate component rendering, interaction behavior, and UI states. |
| Golden | Detect visual regressions across approved screen sizes and themes. |
| Integration | Validate app-level customer journeys with mocked or approved sandbox backends. |

## CI/CD Expectations

- Define build flavors for dev, staging, and production.
- Run formatting, linting, unit tests, widget tests, and golden tests in CI where practical.
- Run dependency vulnerability and license scanning.
- Build Android and iOS release artifacts through approved CI/CD orchestration.
- Retrieve signing credentials from approved secret managers only.
- Publish beta builds through approved TestFlight and Google Play testing channels after required approvals.

