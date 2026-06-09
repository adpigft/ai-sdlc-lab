# Agent Run Log Schema

## Purpose

Define a lightweight JSON schema for agent run telemetry and review feedback.

## Example Shape

```json
{
  "agent_run_id": "run-20260607-001",
  "feature_id": "FEAT-CARDREP-001",
  "workflow_state": "Requirements Approved",
  "skill_id": "implementation",
  "context_manifest_id": "ctx-manifest-card-replacement",
  "model": "GPT-4o",
  "tools": [
    "read_file",
    "validate_artifacts"
  ],
  "inputs": {
    "artifacts": [
      "intent",
      "requirements",
      "design"
    ]
  },
  "outputs": {
    "status": "passed"
  },
  "validation_results": [
    {
      "name": "traceability",
      "status": "passed"
    }
  ],
  "human_feedback": {
    "status": "approved",
    "comment": ""
  },
  "metrics": {
    "prompt_tokens": 0,
    "completion_tokens": 0,
    "total_tokens": 0,
    "cost": 0
  },
  "retry_count": 0,
  "rework_count": 0,
  "timestamps": {
    "started_at": "2026-06-07T00:00:00Z",
    "finished_at": "2026-06-07T00:05:00Z"
  }
}
```

## Notes

- The schema is intentionally lightweight so it can be written, inspected, and aggregated later.
- Additional fields may be added later if they remain additive and do not break existing consumers.
