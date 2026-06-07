# Tool Change Resilience

## Purpose

This model explains how the framework can survive tool swaps without losing delivery continuity or traceability.

## Replace Jira with Azure DevOps

- keep feature and workflow truth in Git
- map Jira issue references to Azure DevOps work item references through the external reference model
- keep traceability rows stable by preserving the Git-owned feature identifier
- update only the synchronized view layer, not the source of truth

## Replace Confluence with SharePoint

- keep approved documentation in Git
- publish the reviewed view to SharePoint through an adapter
- preserve document identifiers and source artifact references in Git
- treat SharePoint as a mirrored published view

## Replace GitHub Actions with GitLab CI

- keep validation intent and expected evidence in Git
- map pipeline runs and evidence references through the external reference model
- keep validation status tied to Git-owned artifacts and run outputs
- change only the CI adapter, not the delivery truth

## Keep Traceability Stable

- use stable Git-owned IDs for domain, capability, feature, and artifact references
- store external references as links, not as the primary identity
- preserve history when the external tool changes
- avoid re-keying traceability just because the external platform changed

## Notes

- Tool resilience is a future-state capability.
- The framework should not become dependent on any single external platform identity model.
