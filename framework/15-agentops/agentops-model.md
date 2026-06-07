# AgentOps Model

## Purpose

AgentOps defines the operational metadata needed to observe, measure, and improve agent-assisted work.

It covers execution, quality, cost, rework, and human feedback.

## Capture Fields

- agent run id
- skill version
- context package versions
- model used
- tool calls
- token usage
- output status
- validation status
- human feedback
- retry or rework count
- improvement recommendation

## Operational Questions

- What ran?
- What context was used?
- What tools were called?
- What did it cost?
- Did it pass validation?
- Did a human need to correct it?
- What should improve next time?

## Notes

- AgentOps is a framework foundation, not a runtime dependency.
- The same run metadata can later feed dashboard visibility, quality metrics, and improvement loops.
