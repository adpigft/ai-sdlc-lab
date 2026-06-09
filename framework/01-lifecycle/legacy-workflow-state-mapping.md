# Legacy Workflow State Mapping

## Purpose

Map older workflow labels to the canonical workflow model.

Use this mapping when reading existing artifacts, older dashboards, or legacy workflow state files.

## Mappings

| Legacy Label | Canonical Label |
| --- | --- |
| `idea` | Candidate Imported |
| `intent_review` | Intent Draft |
| `requirements_review` | Requirements Draft |
| `design_review` | Design Approved |
| `test_review` | Validation Passed |
| `implementation_ready` | Ready for Build |
| `implementation_in_progress` | In Development |
| `pr_review_ready` | In Development |
| `validation_ready` | Validation Passed |
| `release_ready` | Release Ready |
| `released` | Released |
| `blocked` | Any canonical state with a blocking condition |

## Additional Legacy Phrase Mapping

| Legacy Phrase | Canonical Label |
| --- | --- |
| Draft for Architect Review | Design Approved |
| Ready for QA | Validation Passed |
| Ready for Build | Ready for Build |
| In Progress | In Development |
| Done | Released |

## Notes

- If a legacy label maps to multiple canonical states, prefer the state that matches the surrounding artifact evidence.
- Legacy labels are compatibility aliases only.
- New workflow-state content should use the canonical labels.
