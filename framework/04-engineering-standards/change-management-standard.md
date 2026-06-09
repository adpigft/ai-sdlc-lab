# Change Management Standard

## Purpose

Define how changes are introduced safely across APIs, events, databases, services, channel apps, infrastructure, and AI SDLC artifacts.

## Source Of Truth

Git remains the source of truth for standards, requirements, designs, contracts, tests, implementation, validation, release notes, traceability, and decisions. Jira tracks workflow. Confluence publishes reviewed summaries.

## Change Classification

| Change Type | Examples | Required Control |
| --- | --- | --- |
| Documentation | Standards, templates, design text | Review for consistency, links, and scope. |
| Requirement | Intent or requirements change | PO / BA approval and traceability update. |
| Architecture | Design, API, event, integration, state model | Architect and impacted-owner approval. |
| API contract | OpenAPI operations, schemas, errors | API owner and consumer review. |
| Event contract | Topic, schema, key, compatibility | Producer, consumer, and platform review. |
| Database | Schema, migration, retention, data fix | DBA/platform review, rollback, migration evidence. |
| Implementation | Source, tests, configuration | PR review, CI gates, validation evidence. |
| Release | Deployment, rollback, monitoring | Release approval and operational readiness. |

## Backward Compatibility

- Additive changes are preferred.
- Removing fields, changing meanings, narrowing enum values, changing event keys, or changing status semantics requires explicit compatibility review.
- API and event breaking changes require versioning, migration plan, consumer communication, and rollback strategy.
- Database migrations must support rolling deployment.

## Migration Sequencing

1. Introduce compatible contract or schema changes.
2. Deploy producers or services that can handle old and new behavior.
3. Migrate data or consumers.
4. Switch reads or consumers to new behavior.
5. Remove old behavior in a later approved release.

## Release Evidence

Release readiness must include:

- approved scope
- linked requirements and design
- CI results
- test and validation evidence
- security and quality gate results
- database migration evidence where applicable
- API/event compatibility evidence where applicable
- observability and rollback plan
- known risks and accepted exceptions

## Emergency Changes

Emergency changes must still preserve:

- minimal scope
- human approval
- audit trail
- rollback plan
- post-change validation
- follow-up documentation and traceability updates

Emergency delivery is not permission to bypass permanent evidence; missing evidence must be captured after stabilization.

