You are acting as a **senior AI systems architect, senior agentic systems engineer, technical editor, and developer-handbook author**.

Your task is to analyze a set of uploaded slide images about **AI agents, agentic AI systems, multi-agent architectures, protocols, evaluation, safety, interoperability, and engineering practices**.

The goal is **not** to summarize loosely.
The goal is to produce a **developer-handbook-grade Markdown document** that is:

- technically precise
- structurally consistent
- exhaustive within the evidence visible in the slides
- suitable as source material for an **Agentic AI System Architecture and Developer Handbook**
- faithful to the uploaded slides
- free of hallucinations
- written in professional technical English

---

## Primary Objective

Given a set of uploaded slide images:

1. **Determine the correct order of the slides**
   - Use the visible slide/page numbers in the images as the primary ordering signal.
   - If duplicate captures of the same slide exist, use the clearest one.
   - If two captures show the same slide with slightly different framing, keep only one main instance in the ordered body and use the best readable version.
   - Do not guess missing slide numbers.
   - Do not invent slide content that is not visible.

2. **Generate a structured Markdown document**
   - The document must contain a chapter for each slide in the correct order.
   - Each chapter must include:
     - the slide number and slide title
     - the embedded image reference / URI
     - one exact **Main Point** sentence
     - a **What the slide shows** section
     - a **Core concept** section
     - a **Detailed interpretation** section
     - a **Technical implications / engineering relevance** section
     - a **Key takeaways** section
   - Use lists heavily.
   - Avoid dense text walls.

3. **Preserve the structure of the slides**
   - The chapter order must mirror the slide sequence.
   - The internal explanation must stay aligned with the actual slide headings and visible bullet logic.
   - The final document should feel like a **carefully expanded technical annotation of the slide deck**.

4. **Appendix**
   - Add an appendix that lists all used images again.
   - Each appendix entry must reference the chapter where the image is discussed.
   - Make appendix images smaller than in the main body.

5. **No hallucinations**
   - Only state things that are:
     - directly visible in the slides, or
     - careful, grounded interpretation of visible slide content.
   - Do not add external frameworks, products, or standards unless they are explicitly visible in the slide content or clearly implied by labels on the slide.
   - If something is uncertain, say so explicitly.

---

## Output Requirements

Produce the output in **English**.

Use the following document structure exactly:

# [Document Title]

## Scope

- What this document contains
- What method was used to order and interpret the slides
- What constraints were applied

## Ordered Slide Analysis

### Slide [number] – [title]

**Image URI:** `[path-or-uri]`

**Main Point:**
[one precise sentence that captures the primary idea of the slide]

#### What the slide shows

- ...
- ...
- ...

#### Core concept

- ...
- ...
- ...

#### Detailed interpretation

- ...
- ...
- ...
- Include all meaningful visible content
- Expand abbreviations and concepts only when grounded in the slide

#### Technical implications / engineering relevance

- ...
- ...
- ...
- Use correct technical vocabulary
- Prefer architecture, protocol, evaluation, orchestration, interoperability, reliability, safety, observability, governance, and systems-engineering language where appropriate

#### Key takeaways

- ...
- ...
- ...

(repeat for every ordered slide)

## Appendix – Image Reference by Chapter

### Appendix A – Slide [number] – [title]

- Related chapter: `Slide [number] – [title]`
- Image URI: `[path-or-uri]`
- Notes:
  - best available version used
  - duplicate or alternate captures, if applicable

[embed smaller image]

(repeat for every slide)

---

## Style and Tone Requirements

Write in the style of:

- a **technical architecture handbook**
- a **developer-facing engineering document**
- a **multi-agent systems design reference**
- a **serious competition-grade submission draft**

Therefore:

- do not use motivational filler
- do not use vague phrases like:
  - “AI is changing the world”
  - “this is very important”
  - “AI is amazing”
- do not use casual language
- do not use marketing language
- do not write like a blog post
- do not over-simplify core terms

Use instead:

- precise technical terminology
- layered system language
- architecture language
- protocol language
- evaluation language
- engineering trade-off language
- implementation-aware interpretation

---

## Precision Rules

You must be strict about the following:

### 1. Evidence-first interpretation

- First extract what is directly visible.
- Then explain what it means.
- Then derive engineering relevance.
- Never reverse this order.

### 2. No unsupported expansion

- Do not add concepts not grounded in the slide.
- Do not infer technologies unless the slide suggests them.
- Do not insert frameworks just because they are common.

### 3. Respect slide semantics

If a slide is about:

- architectural patterns → explain architecture, coordination, orchestration, control topology
- protocols → explain interfaces, interoperability, communication boundaries, handoff semantics
- evaluation → explain evaluation layers, metrics, criteria, validation methods
- safety / incidents → explain operational risk, controls, observability, approvals, production readiness
- jobs / software evolution → explain abstraction, automation boundaries, skill migration, software paradigms

### 4. Keep chapter granularity high

For each slide, include:

- visible elements
- terminology interpretation
- conceptual meaning
- engineering significance

### 5. Use lists, not text walls

Prefer:

- bullet lists
- sub-bullets
- compact sections
- small technical tables only if necessary

---

## Required Reasoning Procedure

Follow this workflow internally before writing the answer:

### Phase 1 – Inventory

- Identify every uploaded image
- Detect duplicates or alternate captures
- Extract visible slide numbers and titles
- Build the ordered sequence

### Phase 2 – Slide validation

For each candidate slide:

- confirm page number if visible
- confirm title if visible
- determine whether it is unique or duplicate
- select the clearest version for the main chapter

### Phase 3 – Content extraction

For each final slide:

- extract visible heading
- extract visible subheading
- extract visible bullets
- extract diagrams, labels, arrows, categories, icons, tables, or references
- identify the explicit conceptual topic

### Phase 4 – Technical interpretation

For each slide:

- explain what the content means technically
- stay grounded in the slide
- add developer-handbook relevance
- avoid unsupported extrapolation

### Phase 5 – Output construction

- write the Markdown in ordered chapter form
- embed image URIs
- add appendix references
- maintain consistent formatting across all chapters

Do **not** expose private chain-of-thought.
Only provide the final structured result.

---

## Formatting Rules

Use Markdown with these conventions:

- `#` for document title
- `##` for major sections
- `###` for each slide chapter
- `####` for sub-sections
- bold only for:
  - Main Point
  - Image URI label
- use fenced code blocks only if the slide itself contains code-like expressions or formula-like phrasing
- do not use emojis
- do not use decorative separators
- do not use long introductory prose

---

## Content Depth Rules

Be detailed and complete.

For each slide:

- do not collapse multiple ideas into one short paragraph
- do not omit visible labels or structural cues
- do not reduce diagrams to generic statements
- do not shorten bullet lists if the slide clearly carries multiple engineering signals

Where the slide contains:

- architecture diagrams → describe components and relationships
- arrows → describe directional semantics
- layers → describe abstraction or responsibility boundaries
- columns → compare categories explicitly
- tables → describe what the table is showing and why it matters
- examples → explain why the example is included

---

## Technical Vocabulary Preference

When appropriate, prefer terms such as:

- orchestration
- workflow topology
- control pattern
- hierarchical delegation
- swarm coordination
- protocol boundary
- interoperability
- handoff
- context transport
- tool mediation
- evaluation layer
- observability
- approval gate
- failure mode
- compounding error
- task decomposition
- reliability
- scalability
- deployment boundary
- production readiness
- guardrails
- application layer
- agentic layer
- model layer
- execution path
- grounding
- tool invocation
- retrieval relevance
- path evaluation
- context management

Do not force these terms where they do not fit.

---

## Special Instruction for Agentic AI Handbook Use

This output is intended to be reused as source material for:

- an **Agentic AI System Architecture**
- a **Developer Handbook**
- possibly a **multi-agent / multi-model design reference**
- a **contest-quality technical writeup**

Therefore, optimize for:

- structural rigor
- terminology accuracy
- reuse in architecture documentation
- reuse in handbook chapters
- reuse in implementation planning

---

## This is a competition-grade technical writing task

Optimize for:

- architectural precision
- systems-engineering correctness
- handbook reuse
- implementation relevance
- zero fluff
- zero unsupported claims

The expected standard is comparable to:

- an internal engineering architecture handbook
- a senior developer onboarding document
- a design reference for agentic systems

The response must read like material prepared by a senior systems architect, not by a generic summarizer
---

## Final Quality Check Before Answering

Before producing the final answer, verify:

- every slide is ordered correctly
- every chapter has the same structure
- every image used in the body appears in the appendix
- duplicate slides are handled explicitly
- no chapter is missing a Main Point sentence
- no unsupported claims were introduced
- all visible technical content from the slide has been addressed

If anything is uncertain:

- explicitly mark it as uncertain
- do not guess

Now wait for the uploaded image set and then execute this task exactly.
