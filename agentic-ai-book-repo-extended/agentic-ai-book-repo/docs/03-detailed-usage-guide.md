# Detailed Usage Guide

This guide explains how to use the repository as a real technical-book workflow.

## 1. Workflow modes

### Mode A — Full-book authoring
Use this when you are writing the manuscript chapter by chapter.

Primary files:
- `book.yaml`
- `prompts/core/book-skill-extended.md`
- `prompts/specialized/toc/`
- `prompts/specialized/chapters/`
- `review/`
- `refs/`

### Mode B — Research-to-book transformation
Use this when you already have source notes, research results, or analytical summaries.

Primary files:
- `prompts/quick-use/research-to-book-skill.md`
- `prompts/specialized/research/research-to-structured-chapter.md`
- `prompts/specialized/review/evidence-gap-review.md`

### Mode C — Draft rescue / structural repair
Use this when a draft exists but is inconsistent or too shallow.

Primary files:
- `prompts/specialized/restructuring/manuscript-gap-analysis.md`
- `prompts/specialized/sections/deepen-technical-section.md`
- `prompts/specialized/review/technical-lector-review.md`

---

## 2. Recommended sequence

### Phase 1 — Scope the book
Complete `book.yaml`.
Decide:
- reader profile
- scope and exclusions
- practical vs theoretical balance
- publishing intent
- chapter depth

### Phase 2 — Create the structure
Use the TOC prompts to create:
- parts
- chapters
- chapter purposes
- chapter outcomes
- glossary pressure points
- appendix candidates

### Phase 3 — Draft foundational chapters first
For this subject, draft early chapters on:
- what agentic AI is
- what it is not
- components and system boundaries
- models, tools, memory, orchestration

These early chapters stabilize terminology.

### Phase 4 — Build the evidence system
Whenever you write, update:
- `refs/source-log.md`
- `manuscript/90-back-matter/90-glossary.md`
- `manuscript/90-back-matter/91-references.md`

### Phase 5 — Review aggressively
Use the lector prompt after every major chapter.
Treat criticism as part of the writing system.

### Phase 6 — Assemble and inspect
Build the manuscript and read the combined output for:
- repetition
- contradictory terminology
- weak transitions
- missing references
- appendix inflation

---

## 3. Prompt operating patterns

### Pattern 1 — Control prompt + task prompt
This is the preferred method.

1. Paste `prompts/core/book-skill-extended.md`
2. Then paste a task prompt from `prompts/specialized/`
3. Then paste your specific content inputs

### Pattern 2 — One-shot quick formatting
Use `prompts/quick-use/research-to-book-skill.md`
This is best for transforming already-existing research.

### Pattern 3 — Review-only pass
Paste a draft section and use a review prompt.
Do not ask for new drafting until the issues are identified.

---

## 4. How to manage chapter quality

Every chapter should answer these questions:
- Why is this chapter in the book?
- What must the reader understand afterward?
- Which adjacent concepts must be separated clearly?
- Which failure modes must be discussed?
- Which design trade-offs matter here?
- Which terms belong in the glossary?
- Which tables or diagrams would reduce ambiguity?

---

## 5. How to keep output publication-oriented

Require these elements consistently:
- clear heading hierarchy
- defined scope
- explicit distinctions
- examples or scenarios where useful
- operational implications
- limitations
- summary and takeaways
- editorial notes for later evidence gathering

---

## 6. When to use specialized prompts

Use specialized prompts when you need precision, for example:
- protocol chapters
- evaluation chapters
- safety and governance chapters
- case-study chapters
- glossary extraction
- source-to-reference conversion

General prompts are usually not enough for strong technical-book quality.
