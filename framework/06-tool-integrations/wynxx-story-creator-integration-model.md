# Wynxx Story Creator Integration Model

## Purpose

Wynxx Story Creator generates backlog candidates from PRD, BRD, and discovery inputs.

## Role Separation

- Wynxx Story Creator = requirements and backlog generation / intake
- AI-SDLC Framework = governed delivery lifecycle
- Git = delivery source of truth
- Jira = delivery tracking synchronized view
- Confluence = published knowledge synchronized view
- GitHub / GitLab = engineering execution and validation evidence

## Mapping

| Wynxx Story Creator Item | AI-SDLC Mapping |
| --- | --- |
| Epic | AI-SDLC Capability Candidate |
| Feature | AI-SDLC Feature Candidate |
| User Story | AI-SDLC Intent Candidate |
| Task | Reference only / optional implementation hint |
| Test Case | Reference only / optional validation hint |

## Rule

Do not import Wynxx Story Creator Tasks and Test Cases as first-class AI-SDLC delivery artifacts.

AI-SDLC generates implementation slices and validation artifacts after Intent, Specification, and Design are approved.

## Resilience Rule

AI-SDLC must store source metadata from Wynxx Story Creator because backlog items may be deleted, renamed, regenerated, or moved.

## Source Metadata Example

```yaml
source:
  system: wynxx-story-creator
  project_id: 14
  project_name: MSB POC - Project 02
  backlog_id: 44
  backlog_name: Wynxx POC - BRD v3 - NBO PROJECT - Document 1
  work_item_id: 770
  work_item_type: EPIC
  work_item_title: Credential Lifecycle Management
  imported_at: 2026-06-07
```

## Future Positioning

AI-SDLC can later become a delivery lifecycle module within the broader Wynxx platform.
