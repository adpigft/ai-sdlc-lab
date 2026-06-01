# Security Standards

## Scope

These standards apply to all AI-assisted SDLC artifacts and future banking payment implementation.

## Baseline Controls

- Classify data before designing or implementing a feature.
- Protect customer identity, account, card, QR, token, device, authentication, and transaction data.
- Enforce least privilege for users, services, CI jobs, and deployment roles.
- Use secrets management; never store secrets in repository files.
- Require human review for security-sensitive changes.

## Payment Threat Areas

- Duplicate payment execution.
- QR payload tampering.
- Session theft or replay.
- Unauthorized beneficiary substitution.
- Limit bypass.
- Fraud-screening bypass.
- Sensitive data leakage in logs, traces, analytics, or support tooling.
- Inconsistent status between channels, ledger, and payment processor.

## AI Usage Controls

- Do not paste secrets, production customer data, private keys, credentials, or full payment payloads into AI prompts.
- Use synthetic or masked examples in specs, tests, and prompts.
- Treat AI output as untrusted until reviewed.
- Record material AI-assisted decisions in traceability or ADRs when they affect architecture, security, or release posture.

## Required Evidence

- Threat model or security review for payment initiation and status flows.
- Dependency and secret scanning in GitHub Actions.
- SonarCloud security analysis before release.
- Jira-linked risk acceptance for unresolved high or critical findings.
