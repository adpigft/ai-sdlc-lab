# AI SDLC Lab - Codex Project Instructions

## Repository purpose
This repository demonstrates an AI-native SDLC for banking delivery using Codex, skills, Jira, Confluence, GitHub, GitHub Actions, SonarCloud, traceability, feedback, and human approval gates.

## Important directories
- `skills/`: Codex-native project skills. Each skill is a folder with `SKILL.md`.
- `.ai/workflows/`: lifecycle workflows and orchestration notes.
- `.ai/standards/`: engineering, API, security, and testing standards.
- `.ai/templates/`: reusable artifact templates.
- `domains/`: business domains, capabilities, specs, contracts, tests, validation, and release artifacts.
- `traceability/`: end-to-end traceability matrix.
- `feedback/`: review findings, corrections, defects, and change requests.
- `.github/workflows/`: GitHub Actions validation and CI placeholders.
- `src/`: application code. Do not generate code until approved.

## Default AI SDLC flow
Do not jump directly to code.

For any new feature, follow this order:
1. `skills/ba-intent/SKILL.md`
2. `skills/ba-specification/SKILL.md`
3. `skills/architect-context/SKILL.md`
4. `skills/architect-api/SKILL.md`
5. `skills/qa-test-design/SKILL.md`
6. `skills/traceability/SKILL.md`
7. `skills/developer-implementation/SKILL.md`
8. `skills/qa-validation/SKILL.md`
9. `skills/devsecops-release/SKILL.md`
10. `skills/feedback/SKILL.md`

## Interaction rule
When the user says `Start new feature: <feature name>`:
1. Use `ba-intent` first.
2. Ask discovery questions.
3. Do not create artifacts until sufficient intent is captured.
4. Summarize understanding.
5. Ask for approval.
6. Create or update only the artifact owned by the active skill.
7. Move to the next skill only after human approval.

## Human approval gates
- Intent requires PO / BA approval.
- Specification requires BA / PO approval.
- Architecture context requires Architect approval.
- API contract requires Architect approval.
- Tests require QA approval.
- Traceability requires BA, Architect, and QA review.
- Implementation requires Developer and Architect review.
- Validation requires QA approval.
- Release requires PO, QA, Architect, and DevSecOps approval.

## File ownership
- Intent: `domains/**/intent/intent.md`
- Specification: `domains/**/specs/spec.md`
- Context/design: `domains/**/context/context.md`
- API contract: `domains/**/contracts/openapi.yaml`
- Acceptance tests: `domains/**/tests/acceptance.feature`
- Validation: `domains/**/validation/validation-report.md`
- Release: `domains/**/release/release-notes.md`
- Traceability: `traceability/traceability-matrix.md`
- Feedback: `feedback/feedback-log.md`

## Safety rules
- Never modify unrelated files.
- Never generate code before approved intent, specification, architecture, API, tests, and traceability.
- If an approved artifact has a gap, stop and report it instead of coding around it.
- Keep changes small and reviewable.
- Always summarize impacted files.
