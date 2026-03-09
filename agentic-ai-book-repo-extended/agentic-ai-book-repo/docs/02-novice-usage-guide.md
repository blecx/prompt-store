# Novice Usage Guide

This guide assumes you have never built a technical book workflow before.

## Core idea

This repository separates the book process into five distinct activities:

1. **Structure** — what the book contains
2. **Drafting** — writing the prose
3. **Research control** — tracking sources and open questions
4. **Review** — checking technical and editorial quality
5. **Assembly** — combining files into one manuscript

If you keep these separate, quality improves quickly.

---

## Mental model

Think of the repo as a small production system.

- `manuscript/` = the actual book
- `templates/` = reusable writing frames
- `prompts/` = instructions for generating or improving content
- `review/` = quality control
- `refs/` = evidence and citation memory
- `docs/` = operating manuals
- `scripts/` = utilities

---

## Which prompt should a beginner use first?

### For planning the book
Use:
- `prompts/core/book-skill-extended.md`
- `prompts/specialized/toc/toc-from-book-brief.md`

### For writing a chapter
Use:
- `prompts/specialized/chapters/full-chapter-draft.md`

### For improving a section
Use:
- `prompts/specialized/sections/deepen-technical-section.md`

### For turning research into chapter-ready text
Use:
- `prompts/quick-use/research-to-book-skill.md`

### For quality review
Use:
- `prompts/specialized/review/technical-lector-review.md`

---

## Minimal reliable workflow

### Option 1 — Build the book from scratch
1. Define your book brief.
2. Generate a TOC.
3. Accept that the TOC will change later.
4. Draft one foundational chapter.
5. Review it.
6. Fix terminology.
7. Continue chapter by chapter.

### Option 2 — You already have notes or research
1. Collect the material.
2. Use the quick-format skill prompt.
3. Ask for a chapterized version.
4. Ask for missing gaps and glossary entries.
5. Store the output in `manuscript/`.
6. Review and refine.

---

## How to paste prompts correctly

A prompt works better if you provide all required inputs.

Bad input:

```text
Write a chapter about agents.
```

Good input:

```text
Use the book-skill prompt.
Write Chapter 4 for a technical book on Agentic AI.
Audience: software architects and senior engineers.
Purpose: explain the boundary between model, agent, tool, and workflow.
Required topics: definitions, control flow, memory, tool invocation, failure modes, examples.
Constraints: no hype language, explicit trade-offs, publication-grade Markdown.
```

---

## What to do when a result feels weak

Usually one of these is missing:
- chapter purpose
- target audience
- book context
- required distinctions
- desired depth
- output structure
- constraints on terminology and style

Weak output is usually a weak instruction problem, not only a model problem.
