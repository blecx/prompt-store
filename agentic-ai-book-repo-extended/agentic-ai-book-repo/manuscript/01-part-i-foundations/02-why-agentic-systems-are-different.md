# Chapter 2 — Why Agentic Systems Are Different

## Chapter Goal
Explain what changes once software systems can plan, select actions, invoke tools, and adapt behavior across steps.

## Why This Matters
Engineering, evaluation, and governance requirements change when system behavior is not reducible to a single prompt-response interaction.

## Reader Outcomes
- Explain the operational difference between single-turn AI and agentic systems.
- Identify where complexity enters the lifecycle.
- Recognize why evaluation and oversight become harder.

## Core Concepts
### Multi-step execution
{{DEFINE_MULTI_STEP_EXECUTION}}

### Tool mediation
{{DEFINE_TOOL_MEDIATION}}

### Control loop
{{DEFINE_CONTROL_LOOP}}

## System View
Contrast:
- static prompt-response systems
- scripted workflows
- dynamic tool-using systems
- agentic control loops

## Design Choices and Trade-Offs

| Choice | Benefits | Costs | Failure Modes | When Not to Use |
|---|---|---|---|---|
| Keep workflow deterministic | predictability | reduced flexibility | brittle edge-case handling | when adaptation is core |
| Allow adaptive action selection | flexible behavior | harder evaluation and observability | drift, looping, unsafe actions | when governance is weak |

## Risks and Failure Modes
- Hidden state causing non-obvious behavior changes.
- Tool chains amplifying errors.
- Evaluation methods lagging behind system complexity.

## Practical Guidance
Describe the system as a control loop, not as a model call.

## Summary
Agentic systems differ because the unit of analysis is the **behavioral loop**, not the isolated model response.
