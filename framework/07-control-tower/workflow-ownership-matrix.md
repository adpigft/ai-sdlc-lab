# Workflow Ownership Matrix

## Purpose

Define the canonical ownership, approval, timing, and intervention rules for the AI-SDLC Control Tower dashboard.

This matrix is the source of truth for:

- workflow state thresholds
- owner role selection
- approver role selection
- PM intervention triggers
- dashboard governance summaries

## States

| State | Owner Role | Approver Role | Expected Max Days | Jira Action | Confluence Action | GitHub Actions Trigger / Read Behavior | PM Intervention Trigger |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Candidate Imported | Delivery Lead | Product Owner | 2 | Create or preview a Jira Epic shell and attach candidate metadata. | Publish intake summary only after review. | Read candidate import evidence; do not trigger writes. | Trigger if candidate remains unreviewed beyond expected max days or lacks source metadata. |
| Intent Draft | Business Analyst | Product Owner | 3 | Create or update a Jira Story draft from approved intent inputs. | Publish intent summary preview only. | Read draft state and linked evidence; no write action. | Trigger if intent draft is stale, missing owner, or missing source traceability. |
| Intent Approved | Business Analyst | Product Owner | 1 | Sync approved intent status and maintain Jira linkage. | Publish approved intent summary. | Read approved intent evidence and branch validation results. | Trigger if approval exists but downstream spec is not started within threshold. |
| Requirements Draft | Business Analyst | Product Owner | 4 | Update or preview Jira Story details for requirements refinement. | Publish requirements summary preview only. | Read requirements draft status and required downstream gates. | Trigger if requirements draft is stale, missing approval path, or blocked. |
| Requirements Approved | Business Analyst | Product Owner | 2 | Keep Jira Story aligned with approved requirements and traceability. | Publish approved requirements summary. | Read approved requirements evidence and downstream readiness. | Trigger if design does not begin within threshold or traceability is incomplete. |
| Design Approved | Solution Architect | Solution Architect | 2 | Update Jira readiness for build and capture implementation boundary. | Publish design summary and architecture context. | Read design approval evidence and prepare build gate status. | Trigger if Ready for Build is not reached within threshold or implementation inputs are missing. |
| Ready for Build | Developer Lead | Solution Architect | 2 | Move or preview Jira work into build-ready state. | Publish readiness summary only. | Read validation baseline, traceability, and implementation readiness. | Trigger if build does not start or approvals regress. |
| In Development | Developer Lead | Developer Lead | 5 | Track implementation progress and keep Jira status current. | Publish development progress summary only if approved. | Read PR and branch evidence; surface build or PR validation signals. | Trigger if implementation is stale, blocked, or missing evidence. |
| Validation Passed | QA Lead | QA Lead | 3 | Sync validation status and keep release metadata aligned. | Publish validation summary and evidence snapshot. | Read test and validation results; do not write. | Trigger if release readiness is not started within threshold or evidence changes. |
| Release Ready | DevSecOps / Platform | DevSecOps / Platform | 2 | Prepare Jira release or change tracking for deployment approval. | Publish release-readiness summary. | Read release evidence and deployment readiness. | Trigger if release approval is not completed within threshold or release evidence is missing. |
| Released | Delivery Lead | Delivery Lead | 0 | Close or archive Jira tracking and preserve release linkage. | Publish released state summary only. | Read post-release evidence and final validation links. | Trigger if release evidence is incomplete or post-release sync is missing. |

## Interpretation Rules

- `owner_role` identifies the role that should drive the work in the current state.
- `approver_role` identifies the role that should approve the next governing gate.
- `expected_max_days` is the soft threshold used by the dashboard to surface stale work.
- `Jira Action` describes the expected workflow-tracking behavior, not a direct write requirement.
- `Confluence Action` describes the publishing expectation for synchronized views.
- `GitHub Actions Trigger / Read Behavior` defines whether the dashboard should read evidence only or expect generated validation artifacts.
- `PM Intervention Trigger` is the condition used to raise the dashboard intervention signal.

## Notes

- The dashboard may use this matrix to resolve `workflow.owner_role`, `workflow.approver_role`, `workflow.next_gate`, and `workflow.last_updated` display logic.
- The matrix does not replace `workflow-state.yaml`; it provides the governance defaults and thresholds that the dashboard can apply when workflow state is incomplete.
- A missing approver role should remain `null` in generated dashboard data unless the source artifact explicitly provides it.
- Thresholds should be treated as governance defaults and may be overridden by explicit workflow-state evidence when present.
