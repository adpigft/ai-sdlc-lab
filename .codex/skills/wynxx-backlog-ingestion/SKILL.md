---
name: wynxx-backlog-ingestion
description: Ingest and analyze Wynxx Story Creator backlogs via MCP and map Epics, Features, User Stories, Tasks, and Test Cases into AI SDLC candidate inputs without making Wynxx the source of truth.
---

# Wynxx Backlog Ingestion Skill

## Purpose

Ingest and analyze Wynxx Story Creator backlog content through available MCP tools and map it into AI SDLC framework concepts for human review.

Wynxx is an input source, not the source of truth. Framework artifacts become source of truth only after reviewed and approved content is committed to Git through the normal AI SDLC lifecycle.

## When To Use

Use `$wynxx-backlog-ingestion` when a user wants to:

- list Wynxx projects
- list Wynxx backlogs
- inspect a backlog hierarchy
- retrieve work item details
- summarize Epics, Features, User Stories, Tasks, and Test Cases
- extract acceptance criteria
- identify candidate AI SDLC intent or specification inputs
- compare Wynxx backlog structure with existing framework hierarchy
- recommend the next framework skill after backlog review

## Inputs Needed

- Wynxx MCP connection or available MCP tool names
- Project identifier or project search criteria
- Backlog identifier or backlog search criteria
- Target domain or capability, when known
- Existing framework context to compare against, when available
- Ingestion goal, such as discovery, duplicate check, intent preparation, or specification preparation

## MCP Tool Discovery

Use available MCP tools when the environment exposes Wynxx Story Creator operations.

Expected tool capabilities may include:

- list projects
- list backlogs
- get backlog hierarchy
- get work item details
- search work items
- retrieve acceptance criteria
- retrieve linked tasks or test cases

If the exact MCP tool names are unknown, discover available tools first. If no Wynxx MCP tools are available, stop and report the missing integration instead of fabricating backlog content.

## Framework Adapter

When this skill is used inside this repository, context loading, artifact placement, lifecycle routing, approval gates, and source-of-truth rules are defined by:

- `framework/02-context-control/context/skill-context-adapter.md`
- `framework/01-lifecycle/skill-orchestration-adapter.md`
- `framework/03-delivery-governance/artifact-placement-model.md`
- `framework/06-tool-integrations/ai-sdlc-portal-mvp.md`

## Wynxx To Framework Mapping

| Wynxx Item | Framework Mapping |
| --- | --- |
| Epic | Candidate Capability or Jira Epic |
| Feature | Candidate Feature or feature group |
| User Story | Requirement candidate |
| Task | Implementation slice candidate |
| Test Case | Test design candidate |

Mapping is advisory until reviewed. Do not create framework artifacts automatically from this mapping.

## Procedure

1. Confirm the ingestion goal and the target project or backlog scope.
2. Use Wynxx MCP tools to list available projects when the project is not provided.
3. Use Wynxx MCP tools to list backlogs for the selected project.
4. Retrieve the backlog hierarchy for the selected backlog.
5. Retrieve details for relevant Epics, Features, User Stories, Tasks, and Test Cases.
6. Extract names, descriptions, acceptance criteria, business rules, dependencies, assumptions, links, statuses, owners, and priorities where available.
7. Map Wynxx hierarchy to candidate framework hierarchy.
8. Compare with existing Git-owned domain, capability, and feature context when provided or discoverable.
9. Identify duplicate, overlapping, conflicting, or ambiguous backlog items.
10. Produce reviewable candidate inputs for `$intent`, `$specification`, `$test-design`, or `$implementation` as appropriate.
11. Recommend the next framework skill, but do not execute it unless the user explicitly approves.

## Outputs Produced

- Backlog summary
- Hierarchy mapping
- Candidate intent inputs
- Candidate specification inputs
- Requirement gaps
- Duplicate and overlap warnings
- Candidate implementation slice inputs
- Candidate test design inputs
- Recommended next framework skill

## Artifact Structure

1. Source Inventory
2. Backlog Summary
3. Wynxx Hierarchy
4. Framework Hierarchy Mapping
5. Epic Summaries
6. Feature Summaries
7. User Story Requirement Candidates
8. Task Implementation Slice Candidates
9. Test Case Test Design Candidates
10. Extracted Acceptance Criteria
11. Requirement Gaps
12. Duplicate / Overlap Warnings
13. Assumptions And Open Questions
14. Recommended Next Framework Skill
15. Human Review Notes

## Quality Checks

- Wynxx project and backlog source are identified.
- MCP-sourced content is separated from AI inference.
- Mapping clearly distinguishes candidate capability, feature, requirement, implementation slice, and test design inputs.
- Acceptance criteria are extracted verbatim only when available and otherwise marked as inferred or missing.
- Duplicate and overlap warnings compare against Git-owned framework artifacts when context is available.
- Candidate inputs do not claim approval.
- Git-owned framework artifacts remain the source of truth after human review and approval.

## Stop Conditions

- Wynxx MCP tools are unavailable or cannot access the requested project.
- The target project or backlog cannot be identified.
- Work item details are insufficient to produce a reliable summary.
- The user asks to create intent or specification without reviewing candidate inputs first.
- The user asks to modify domain artifacts, source code, lifecycle, or skills outside this skill's scope.
- Candidate hierarchy conflicts with existing Git-owned domain, capability, or feature structure and needs human decision.

## Human Approval Expectations

Human review is required before Wynxx-derived content is used to create or update AI SDLC artifacts.

Approval is required before:

- creating intent from candidate inputs
- creating specification from candidate inputs
- creating test design from candidate test cases
- creating implementation slices from candidate tasks
- updating traceability or workflow state
- creating Jira payloads or Confluence summaries from the mapped backlog

## Do Not

- Do not create intent automatically without approval.
- Do not create specification automatically without approval.
- Do not modify domain artifacts.
- Do not modify source code.
- Do not modify lifecycle.
- Do not treat Wynxx as the source of truth.
- Do not silently resolve hierarchy conflicts.

## Standard Response Format

Backlog Summary:
- ...

Hierarchy Mapping:
- ...

Candidate Inputs:
- ...

Gaps / Warnings:
- ...

Recommended Next:
- ...
