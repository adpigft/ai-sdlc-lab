# Framework Index Template

## Purpose

Navigation aid for framework-level guidance. This index must point to canonical documents and must not duplicate them.

## Authority

- Canonical guidance lives in the linked framework documents.
- `framework/document-map.md` remains the canonical document map.
- If this index disagrees with a canonical document, the canonical document wins.

## Topics

| Topic | Canonical Document | Notes |
| --- | --- | --- |
| User onboarding | `README.md` | Start here for framework usage. |
| Codex operating rules | `AGENTS.md` | Repository-level AI behavior. |
| Workflow state | `framework/workflow/workflow-state-guide.md` | Lifecycle state and gates. |
| Review / Approved / Status | `framework/workflows/review-approval-flow.md` | User navigation commands. |
| Context routing | `framework/context/context-pack-model.md` | Stage-specific reads. |
| Stage context packs | `framework/context/stage-context-packs.md` | Required, optional, and forbidden reads by stage. |
| Prompt patterns | `framework/prompt-patterns/prompt-pattern-model.md` | Lightweight execution patterns. |
| Implementation placement | `framework/service-architecture/implementation-placement-model.md` | Target placement and allowed paths. |
| Service ownership | `framework/service-architecture/service-catalog-template.md` | Service catalog format. |
| Frontend ownership | `framework/frontend/frontend-catalog-template.md` | Frontend app/module ownership. |
| Shared assets | `framework/multi-squad/shared-asset-ownership-model.md` | Libraries, events, APIs, templates. |
| Path governance | `framework/multi-squad/path-governance-model.md` | Allowed/restricted paths and review. |
| Standards | `framework/standards/` | Engineering, API, security, testing, release. |
| Automation | `scripts/` | Local validation scripts. |
| GitHub Actions | `.github/workflows/` | CI validation guardrails. |
| Jira foundation | `scripts/jira/README.md` | Offline payload generation. |
| Confluence foundation | `scripts/confluence/README.md` | Offline summary generation. |

## Maintenance

This file should be generated or validated in the future. Do not use it as a replacement for canonical framework documents.

