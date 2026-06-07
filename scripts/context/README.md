# Context Scripts

This folder is reserved for future context governance scripts.

## Planned Scripts

- `validate-context.py`
- `validate-skills.py`
- `package-context.py`
- `scan-context-security.py`
- `check-context-drift.py`
- `generate-context-health.py`

## Intended Roles

- `validate-context.py` should verify syntax, structure, completeness, and references.
- `validate-skills.py` should check skills against the review rubric and stop rules.
- `package-context.py` should build versioned context packages from approved Git sources.
- `scan-context-security.py` should flag sensitive or unsafe content before packaging.
- `check-context-drift.py` should compare packages against current artifacts and signals.
- `generate-context-health.py` should summarize package freshness, drift, and quality signals.

## Rules

- Do not call external systems by default.
- Do not package sensitive data without approval.
- Keep Git as the source of truth.
- Keep this folder lightweight until a script is approved for implementation.
