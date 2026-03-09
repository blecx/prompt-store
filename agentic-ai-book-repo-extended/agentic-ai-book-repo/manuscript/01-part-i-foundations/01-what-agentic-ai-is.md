# Chapter 1 — What Agentic AI Is

## Chapter Goal
Define the term **agentic AI** with enough precision that it can be used analytically rather than rhetorically.

## Why This Matters
The term is widely used but often stretched to cover simple assistants, scripted workflows, or generic automation. A technical book needs a narrower and operationally useful definition.

## Reader Outcomes
- Distinguish agentic AI from adjacent concepts.
- Explain why agency claims require explicit system boundaries.
- Evaluate whether a concrete system qualifies as agentic in a meaningful sense.

## Core Concepts

### Agentic AI
{{DEFINE_AGENTIC_AI}}

### Agency boundary
{{DEFINE_AGENCY_BOUNDARY}}

### Autonomy
{{DEFINE_AUTONOMY}}

## System View
A working definition should account for:
- goal handling
- action selection
- state or memory handling
- tool or environment interaction
- control boundary
- termination or escalation conditions

## Design Choices and Trade-Offs

| Choice | Benefits | Costs | Failure Modes | When Not to Use |
|---|---|---|---|---|
| Narrow definition | conceptual clarity | excludes fuzzy edge cases | over-pruning borderline systems | when surveying broad market language |
| Broad definition | inclusive coverage | conceptual dilution | every workflow becomes “agentic” | when technical precision is required |

## Risks and Failure Modes
- Treating all tool-using assistants as agentic.
- Confusing workflow branching with agentic control.
- Claiming autonomy without specifying human control limits.

## Practical Guidance
Create a classification table for example systems and evaluate them against explicit criteria rather than intuitive labeling.

## Summary
This chapter should establish the definitional baseline for the whole manuscript.

## Key Takeaways
- Agentic AI requires explicit system criteria.
- Definitions must expose control structure.
- Terminology drift weakens the whole book.

## Source Needs
- definitional sources
- system taxonomy sources
