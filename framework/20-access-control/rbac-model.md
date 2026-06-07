# RBAC Model

## Purpose

This model defines future role-based access controls for AI-SDLC governance assets.

## Roles

- Viewer
- Contributor
- Reviewer
- Approver
- Administrator

## Permission Areas

### Context

- Viewer: read only
- Contributor: propose or edit in draft contexts
- Reviewer: review and comment
- Approver: approve selected context packages
- Administrator: manage policies and ownership

### Skills

- Viewer: inspect skill documentation
- Contributor: use approved skills
- Reviewer: review skill output
- Approver: approve skill changes
- Administrator: manage skill governance

### Harnesses

- Viewer: inspect harness definitions
- Contributor: use approved harnesses
- Reviewer: review harness selection
- Approver: approve harness changes
- Administrator: manage harness catalog

### Workflow States

- Viewer: read state
- Contributor: propose changes through approved workflow
- Reviewer: comment on state transitions
- Approver: approve state transitions
- Administrator: manage state policy

### Jira Publishing

- Viewer: no publish
- Contributor: no publish
- Reviewer: review only
- Approver: approve publish
- Administrator: manage integration controls

### Confluence Publishing

- Viewer: no publish
- Contributor: no publish
- Reviewer: review only
- Approver: approve publish
- Administrator: manage integration controls

### Release Readiness

- Viewer: read readiness
- Contributor: provide evidence
- Reviewer: assess evidence
- Approver: approve release
- Administrator: manage release policy

## Notes

- This RBAC model is a future governance foundation.
- It should align with platform policy and audit requirements when implemented.
