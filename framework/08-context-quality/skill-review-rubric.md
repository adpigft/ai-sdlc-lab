# Skill Review Rubric

## Purpose

Use this rubric to review Codex skills before they are relied on for delivery work.

## Checks

| Check | What To Verify |
| --- | --- |
| Purpose | The skill states what problem it solves and what it does not solve. |
| Trigger condition | The skill clearly defines when it should be used. |
| Required inputs | The skill names the inputs it needs to proceed. |
| Output contract | The skill describes the expected output shape or response format. |
| Constraints | The skill lists hard limits, safety rules, and scope boundaries. |
| Stop-for-review rule | The skill clearly says when it must stop and wait for human review. |
| Validation steps | The skill defines how outputs are checked. |
| Allowed tools | The skill names the tools or capabilities it may use. |
| Forbidden actions | The skill states what it must not do. |
| Examples | The skill includes at least one realistic usage example or standard response shape. |
| Failure handling | The skill says how to behave when data is missing, ambiguous, or blocked. |

## Review Outcome

- Pass: the skill is clear, bounded, and safe to use.
- Needs revision: the skill has scope gaps, missing stop conditions, or unclear outputs.
- Blocked: the skill would create unsafe or unverifiable actions.

## Notes

- Review should prefer explicit safety over cleverness.
- A skill that cannot explain its stop condition is not ready for delivery use.
