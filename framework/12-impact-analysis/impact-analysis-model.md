# Impact Analysis Model

## Purpose

Impact analysis assesses the effect of mid-project changes and major changes before they move forward.

It answers a simple question: what breaks, what needs review, what sequencing changes are required, and who must approve the next step.

## Inputs

- changed intent
- changed requirements
- changed design
- changed API contract
- changed code
- changed test
- changed context package or context manifest
- traceability matrix
- workflow state
- Jira links
- Confluence links

## Impact Categories

- requirement impact
- component impact
- API impact
- integration impact
- data impact
- code impact
- test impact
- operational impact
- security impact
- release impact
- implementation sequencing impact

## Output Model

An impact assessment should identify:

- impacted features
- impacted artifacts
- impacted tests
- impacted owners
- implementation sequencing
- risks
- recommended next action

## Gate Rule

No major change moves forward without an impact assessment.

If the assessment is incomplete, the change remains in review and must not be treated as approved.

## Recommended Assessment Steps

1. Identify the change and its scope.
2. Compare the change to approved artifacts and workflow state.
3. Identify downstream artifacts and owners.
4. Classify the impact category or categories.
5. Separate confirmed, assumption-based, and deferred impacts when needed.
6. Decide whether the change is minor, in-flight, major, or post-release.
7. Record the recommended next action, sequencing, and required approvals.

## Notes

- Git remains the source of truth for the assessment record.
- Jira and Confluence are synchronized views only when approved workflow integration exists.
- Control Tower can consume the output later as a visibility layer, but it does not replace the assessment itself.
