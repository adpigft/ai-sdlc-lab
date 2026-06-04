# Lightweight Indexing Model

## Purpose

Lightweight indexes improve navigation, context routing, and token discipline across the AI-SDLC framework. They help users and AI agents find the right framework guidance, domain context, capability context, feature artifacts, owners, and lifecycle state without reading the whole repository.

Indexes are navigation aids only. They are not source-of-truth artifacts.

## Authority Rules

- `workflow-state.yaml` remains authoritative for lifecycle state, current artifact, pending gate, approvals, blockers, and next skill.
- Source artifacts always win over index content.
- Git remains the source of truth for domain context, capability context, feature artifacts, traceability, feedback, standards, release evidence, and code.
- Indexes must not override capability context, feature artifacts, workflow state, validation evidence, traceability, or approval gates.
- If an index disagrees with a source artifact, treat the index as stale and report it.

## Index Types

### Framework Index

The framework index helps users find canonical framework documents by topic.

Recommended path:

```text
framework/index.md
```

It should reference framework guidance such as lifecycle, context packs, prompt patterns, placement, ownership, standards, Jira, Confluence, validation, and automation.

### Domain Index

The domain index helps users find domain context, owners, capabilities, integrations, APIs, events, and placement assumptions for one domain.

Recommended path:

```text
domains/<domain>/domain-index.md
```

It should point to `domains/<domain>/domain-context.md`, capability folders, and feature folders. It must not duplicate the domain context in full.

### Capability Artifact Index

The capability artifact index helps users find all artifacts for one capability and understand their current lifecycle role.

Recommended path:

```text
domains/<domain>/capabilities/<capability>/features/<feature>/artifact-index.md
```

It should point to intent, specification, architecture, contracts, tests, implementation plan, validation, release, workflow state, traceability references, and feedback references.

## Recommended Usage

| Scale | Recommendation |
| --- | --- |
| Lab or single capability | Optional |
| 3+ squads | Recommended |
| 10+ squads | Required |

For lab use, `rg`, `find`, `README.md`, `framework/00-navigation/document-map.md`, and `workflow-state.yaml` are usually enough. As more squads and domains are added, indexes reduce context loading and help avoid accidental cross-domain reads.

## Future Automation Approach

Indexes should eventually be:

- generated from source artifacts
- validated by scripts
- refreshed as part of pull requests
- checked for stale paths and stale status
- treated as invalid when they disagree with source artifacts

Indexes should not be manually maintained as primary content. Manual edits may be acceptable during early pilots, but the long-term model is generated and validated indexes.

## Validation Expectations

Future validation should check:

- referenced files exist
- referenced workflow-state files exist
- index state does not contradict `workflow-state.yaml`
- source artifact paths are non-empty where required
- domain and capability IDs match folder paths
- stale links are reported
