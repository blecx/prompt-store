# Chapter 6 — Planning, Control, and Orchestration

## Chapter Goal
Explain how systems decide what to do next and how that decision is controlled.

## Why This Matters
Planning without execution control is fragile. Orchestration without explicit termination logic can be unsafe or inefficient.

## Core Concepts
### Planner
{{DEFINE_PLANNER}}

### Router
{{DEFINE_ROUTER}}

### Supervisor
{{DEFINE_SUPERVISOR}}

### Termination condition
{{DEFINE_TERMINATION}}

## System View
Cover:
- task decomposition
- action selection
- routing
- retry logic
- escalation
- human handoff
- loop termination

## Risks and Failure Modes
- infinite loops
- self-reinforcing bad plans
- cascading retries
- uncontrolled tool invocation
