# Chapter 5 — Models, Tools, Memory, and State

## Chapter Goal
Separate the major building blocks that are often conflated.

## Why This Matters
A model is not a tool, a tool is not memory, and memory is not the same as state. Mixing these concepts causes architecture defects.

## Core Concepts
### Model
{{DEFINE_MODEL}}

### Tool
{{DEFINE_TOOL}}

### Memory
{{DEFINE_MEMORY}}

### State
{{DEFINE_STATE}}

## Design Questions
- Which data must persist across steps?
- Which memory is retrieved versus written?
- What remains external to the model?
- Which tools are synchronous, asynchronous, or side-effecting?
