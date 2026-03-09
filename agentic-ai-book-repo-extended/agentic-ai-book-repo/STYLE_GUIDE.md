# Style Guide

## Tone
Write like a serious technical book, not a blog post or marketing page.

## Core discipline
- Prefer explicit structure over prose drift.
- Define terms before heavy reuse.
- Mark assumptions clearly.
- Distinguish system description from recommendation.
- Separate analysis from prescription.

## Terminology control
Use canonical wording for:
- model
- agent
- tool
- workflow
- orchestration
- runtime
- protocol
- memory
- planning
- evaluation
- observability
- governance

If a term is introduced or redefined, update `manuscript/90-back-matter/90-glossary.md`.

## Chapter discipline
Each substantial chapter should contain:
- chapter goal
- why it matters
- core concepts
- system view
- design choices and trade-offs
- risks and failure modes
- practical guidance
- summary
- key takeaways

## Tables and figures
Use tables for:
- comparisons
- decision matrices
- role boundaries
- failure modes
- evaluation criteria

Use diagrams only when they clarify:
- architecture
- control flow
- protocol interaction
- state transitions
- deployment boundaries
- evaluation flow

## Prohibited patterns
Avoid:
- hype language
- undefined abstractions
- casual anthropomorphism without qualification
- claims without source or explicit framing
- hidden assumptions about autonomy or safety
