# AI-SDLC Skill Quality Review

## 1. Executive Summary

The skill portfolio was re-evaluated after the guardrail remediation pass. Every `SKILL.md` now has an explicit `## Do Not` section, and the high-risk skills now have targeted safety boundaries. The result is a cleaner, more governable skill set with no skill below Pilot Ready.

The portfolio moved from **pilot ready overall** to **enterprise ready overall** on the updated scoring pass.

## 2. Overall Skill Quality Score

- Previous overall score: **89 / 100**
- Updated overall score: **91 / 100**
- Delta: **+2**
- Classification: **Enterprise Ready**

## 3. Skill Inventory

### Lifecycle skills
- `intent`
- `specification`
- `design`
- `test-design`
- `implementation`
- `pr-review`
- `validation`
- `release`

### Support skills
- `capability-onboarding`
- `domain-onboarding`
- `source-ingestion`
- `repo-discovery`
- `artifact-review`
- `change-request`
- `decision`
- `defect-fix`
- `feedback-capture`
- `traceability-review`
- `wynxx-backlog-ingestion`

### Brownfield modernization skills
- `discovery-engineering`
- `intent-extraction`
- `specification-extraction`
- `context-extraction`
- `gap-analysis`
- `impact-analysis`

## 4. Scorecard Table

| Skill | Previous | Updated | Delta | Classification | Remaining issues | Recommended next fixes |
| --- | ---: | ---: | ---: | --- | --- | --- |
| `artifact-review` | 86 | 90 | +4 | Enterprise Ready | Could use one more concrete artifact-path example | Keep the review checklist concise and example-driven |
| `capability-onboarding` | 91 | 92 | +1 | Enterprise Ready | Slightly example-light | Add a compact output example if needed |
| `change-request` | 87 | 90 | +3 | Enterprise Ready | Targeted-path example could be clearer | Add one sample impacted-artifact block |
| `context-extraction` | 91 | 92 | +1 | Enterprise Ready | Still depends on careful current-state vs target-state separation | Preserve the current-state / target-state split |
| `decision` | 88 | 90 | +2 | Enterprise Ready | Broad by nature; can drift if not tied to ADR discipline | Keep decisions tied to explicit records |
| `defect-fix` | 87 | 89 | +2 | Pilot Ready | Still execution-sensitive and approval-bound | Keep scope tight and avoid broad refactors |
| `design` | 92 | 93 | +1 | Enterprise Ready | Minimal remaining issues | Keep design outputs crisp and bounded |
| `discovery-engineering` | 92 | 93 | +1 | Enterprise Ready | Could use one more evidence example in practice | Continue emphasizing evidence over inference |
| `domain-onboarding` | 91 | 92 | +1 | Enterprise Ready | Slightly example-light | Keep boundary and ownership capture explicit |
| `feedback-capture` | 85 | 88 | +3 | Pilot Ready | Still broad enough to become a catch-all | Keep follow-up tied to a clear owner and artifact |
| `gap-analysis` | 90 | 91 | +1 | Enterprise Ready | Depends on target-state quality | Keep severity and owner classification explicit |
| `impact-analysis` | 91 | 92 | +1 | Enterprise Ready | Low residual risk | Continue requiring traceability inputs where available |
| `implementation` | 89 | 90 | +1 | Enterprise Ready | Scope discipline still depends on upstream approvals | Keep implementation slices narrow |
| `intent` | 92 | 93 | +1 | Enterprise Ready | Minimal remaining issues | Keep business outcome and exclusions explicit |
| `intent-extraction` | 91 | 92 | +1 | Enterprise Ready | Confidence discipline still matters | Continue labeling recovered content clearly |
| `pr-review` | 92 | 93 | +1 | Enterprise Ready | Minimal remaining issues | Keep review scope and approval gates explicit |
| `release` | 89 | 90 | +1 | Enterprise Ready | Still evidence-dependent by design | Keep release claims tied to traceability and validation |
| `repo-discovery` | 84 | 87 | +3 | Pilot Ready | Open-ended repository analysis can vary in depth | Add small output examples and evidence anchors |
| `source-ingestion` | 85 | 88 | +3 | Pilot Ready | Summary quality still depends on evidence discipline | Keep extraction notes and confidence visible |
| `specification` | 92 | 93 | +1 | Enterprise Ready | Minimal remaining issues | Keep requirements explicit and testable |
| `specification-extraction` | 91 | 92 | +1 | Enterprise Ready | Inferred items still need careful labeling | Preserve the evidence/inference split |
| `test-design` | 91 | 92 | +1 | Enterprise Ready | Minimal remaining issues | Keep negative and NFR coverage explicit |
| `traceability-review` | 91 | 92 | +1 | Enterprise Ready | Minor judgment calls may remain on mapping completeness | Keep source-reference mapping explicit |
| `validation` | 91 | 92 | +1 | Enterprise Ready | Minimal remaining issues | Keep validation evidence strong and reviewable |
| `wynxx-backlog-ingestion` | 84 | 88 | +4 | Pilot Ready | Still integration-specific and MCP-dependent | Preserve Story Creator references and keep Tasks/Test Cases reference-only |

## 5. Top Strengths

- Every skill now has an explicit `Do Not` section.
- The core lifecycle skills remain deterministic and approval-driven.
- Brownfield skills clearly separate evidence, inference, and confidence.
- External tool handling is more explicit and safer.
- The portfolio is reusable across greenfield, brownfield, and support workflows.

## 6. Common Weaknesses

- Some support skills are still intentionally broader than the core lifecycle skills.
- `repo-discovery`, `source-ingestion`, `feedback-capture`, and `wynxx-backlog-ingestion` still depend heavily on operator judgment.
- A few skills would benefit from one more concrete output sample or artifact skeleton.
- The most execution-adjacent skills still require disciplined upstream approvals to stay safe.

## 7. High-Risk Skills

- `wynxx-backlog-ingestion`
- `repo-discovery`
- `source-ingestion`
- `feedback-capture`

These are not below Pilot Ready, but they still need careful scope control because they are broader, more external-input driven, or more integration-specific than the core lifecycle skills.

## 8. Skills Ready for Demo

All skills are acceptable for demo usage within their intended scope. The most polished enterprise-ready set is:

- `artifact-review`
- `capability-onboarding`
- `change-request`
- `context-extraction`
- `decision`
- `design`
- `discovery-engineering`
- `domain-onboarding`
- `gap-analysis`
- `impact-analysis`
- `implementation`
- `intent`
- `intent-extraction`
- `pr-review`
- `release`
- `specification`
- `specification-extraction`
- `test-design`
- `traceability-review`
- `validation`

## 9. Skills Requiring Improvement Before Pilot

The following skills remain Pilot Ready but are still the most likely to benefit from follow-up tuning before a wider pilot:

- `repo-discovery`
- `source-ingestion`
- `feedback-capture`
- `wynxx-backlog-ingestion`

## 10. Recommended Fixes

1. Add one more compact example output block to the broad support skills if they are used frequently.
2. Keep evidence-versus-inference language tight in `repo-discovery`, `source-ingestion`, and `feedback-capture`.
3. Continue preserving Story Creator source references in `wynxx-backlog-ingestion`.
4. Keep execution-adjacent skills tightly bounded to approved scope.

## 11. Recommended Skill Quality Gates

- Every skill must keep an explicit `Do Not` block.
- Skills that touch source code, external systems, or workflow state must clearly state approval gates.
- Extraction skills must separate evidence from inference and use confidence labels where appropriate.
- External-integration skills must preserve source references and forbid accidental writes.
- Review skills must remain review-only unless explicitly asked to patch.

## 12. Final Verdict

The AI-SDLC skill portfolio is now **enterprise ready overall** for controlled use. The remediation pass fixed the primary guardrail defect, improved the higher-risk skills, and kept the portfolio consistent with Git as source of truth and approval-gated delivery behavior.
