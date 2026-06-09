# Model Routing Strategy

## Purpose

This model defines future rules for selecting models by task type and risk.

## Routing Rules

- small task -> cheap model
- requirements -> mid-tier model
- architecture -> premium model
- validation -> specialized model

## Fallback Strategy

- if the preferred model is unavailable, route to the next approved model for the task class
- if no approved fallback exists, stop and require human decision

## Outage Strategy

- use the approved fallback chain
- record the outage and the routing decision
- do not silently switch to an unapproved model

## Quality Thresholds

- the selected model must meet the minimum quality threshold for the task class
- higher-risk tasks require stronger models and stronger review

## Notes

- Routing is a governance decision, not a hidden optimization.
- Approved model choices should remain visible in the audit trail.
