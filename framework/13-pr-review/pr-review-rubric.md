# PR Review Rubric

## Dimensions

- requirement alignment
- design alignment
- API compatibility
- test adequacy
- security awareness
- observability readiness
- backward compatibility
- traceability completeness
- release risk

## Scoring

Each dimension is scored from 1 to 5.

- 5 = strong
- 4 = acceptable
- 3 = needs attention
- 2 = weak
- 1 = unacceptable

## Approval Rule

- No dimension may be below 4 for approval.
- If a reviewer approves with a lower score, the reviewer must record an explicit human override reason.

## Scoring Guidance

- Requirement alignment: PR matches the approved intent and specification.
- Design alignment: implementation follows the approved design and placement.
- API compatibility: public contract remains compatible or is changed through approved process.
- Test adequacy: tests cover happy path, negative path, and important regressions.
- Security awareness: secure defaults, input handling, and sensitive-data handling are preserved.
- Observability readiness: logs, metrics, and validation evidence are adequate for support.
- Backward compatibility: existing consumers are not broken without controlled change.
- Traceability completeness: links from intent through release are intact.
- Release risk: operational and delivery risk are understood and acceptable.

## Notes

- The rubric is a review aid, not a replacement for judgment.
- Human reviewers remain accountable for the final decision.
