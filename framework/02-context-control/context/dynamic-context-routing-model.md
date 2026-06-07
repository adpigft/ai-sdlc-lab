# Dynamic Context Routing Model

## Purpose

Dynamic context routing decides which context packages to load for a task, feature, or review.

It improves token efficiency without losing the context needed for safe delivery.

## Routing Modes

- role-based context loading
- task-based context loading
- risk-based context loading
- change-based context loading

## Priority Order

1. enterprise context
2. domain context
3. capability context
4. feature context
5. project context
6. squad context
7. change-specific or incident-specific context

## Inclusion Rules

- include enterprise context when governance, policy, or common standards matter
- include domain context when the change touches domain rules or boundaries
- include capability context when the change touches the shared business function
- include feature context when the task is feature-specific
- include project context when delivery is managed by project-wide constraints
- include squad context when ownership, routing, or workload matters

## Exclusion Rules

- exclude unrelated domain or feature context
- exclude stale duplicate context packages
- exclude low-value examples when a more specific approved package exists
- exclude context that does not help the current decision or implementation task

## Token Budget Rules

- set a context budget before loading large context sets
- prefer the smallest set of packages that covers the task
- stop loading when the budget is exceeded and fall back to higher-priority packages only

## Fallback Behavior

If budget is exceeded:

1. keep enterprise and domain context
2. keep the active capability or feature context
3. drop unrelated project, squad, or example context
4. mark the context set as trimmed for review

## Notes

- The routing model should be deterministic enough for repeatable work but flexible enough for different squad and project structures.
- The goal is not maximum context. The goal is the minimum correct context.
