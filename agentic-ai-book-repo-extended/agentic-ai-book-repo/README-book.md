# Agentic AI Book Repository — Extended Authoring Kit

This repository is a **novice-friendly but production-oriented manuscript system** for writing a serious technical book on **Agentic AI**.

It is designed for four use cases:

1. **You want to write a full book** in Markdown with a disciplined structure.
2. **You want to use prompts as an authoring system**, not as random one-off requests.
3. **You want to turn research or analysis into book-ready prose** quickly.
4. **You want a GitHub-ready repo** that can evolve into a long-term writing project.

---

## Start Here

If you are new, use these files in this order:

1. `docs/01-quickstart.md`
2. `docs/02-novice-usage-guide.md`
3. `docs/03-detailed-usage-guide.md`
4. `prompts/core/book-skill-extended.md`
5. `prompts/quick-use/research-to-book-skill.md`

---

## What This Repo Contains

### Manuscript layer
- `manuscript/` — front matter, parts, chapters, glossary, references, appendices, index
- `templates/` — templates for the book, chapters, sections, appendices, glossary entries
- `dist/` — generated combined manuscript output

### Prompt layer
- `prompts/core/` — master prompts that define the authoring discipline
- `prompts/quick-use/` — fast prompts for turning research into book-ready output
- `prompts/specialized/` — prompts for TOC design, chapter architecture, section deepening, evaluation, governance, protocols, glossary work, references, review, and restructuring

### Review and quality layer
- `review/` — lector prompt, review checklist, review log
- `refs/` — bibliography, source log, citation policy
- `docs/` — operating instructions, usage paths, quality gates, workflow playbooks

### Automation layer
- `scripts/` — build and validation helpers
- `.github/` — workflow and collaboration scaffolding

---

## Fastest Path for a Beginner

### Path A — You want a full book
Read `docs/01-quickstart.md` and then use:
- `prompts/core/book-skill-extended.md`
- `prompts/specialized/toc/toc-from-book-brief.md`
- `prompts/specialized/chapters/full-chapter-draft.md`
- `prompts/specialized/review/technical-lector-review.md`

### Path B — You already have research and want book-ready text
Use:
- `docs/04-quick-usage-as-formatting-skill.md`
- `prompts/quick-use/research-to-book-skill.md`

### Path C — You already have a draft and want to improve it
Use:
- `prompts/specialized/restructuring/manuscript-gap-analysis.md`
- `prompts/specialized/sections/deepen-technical-section.md`
- `prompts/specialized/review/technical-lector-review.md`

---

## Build Commands

Build one combined manuscript file:

```bash
python scripts/build_book.py
```

Check unresolved placeholders:

```bash
python scripts/check_placeholders.py
```

Create a new chapter file:

```bash
python scripts/create_chapter.py "16-runtime-guardrails" "04-part-iv-governance-safety-and-operations"
```

The combined manuscript is written to:

```text
dist/book-manuscript.md
```

---

## Recommended Working Method

Use the repo like this:

1. Define the book scope in `book.yaml`
2. Build or revise the TOC with a prompt from `prompts/specialized/toc/`
3. Draft chapters into `manuscript/`
4. Log sources in `refs/source-log.md`
5. Maintain glossary and references continuously
6. Run a review pass using `review/` prompts and checklists
7. Build the combined manuscript in `dist/`
8. Repeat until the manuscript becomes structurally stable

---

## Important Practical Advice

- Do not attempt to perfect the entire book in one pass.
- Treat prompts as **operating instructions**, not magic.
- Separate **drafting**, **technical correction**, **reference collection**, and **review**.
- Keep your glossary alive from day one.
- Track unresolved claims, missing evidence, and weak sections explicitly.
- Do not publish until legal, citation, trademark, and rights details are validated.

---

## Main Documents to Read

- `docs/01-quickstart.md`
- `docs/02-novice-usage-guide.md`
- `docs/03-detailed-usage-guide.md`
- `docs/05-authoring-lifecycle.md`
- `docs/06-prompt-selection-guide.md`
- `docs/07-quality-gates.md`
- `docs/08-research-to-book-workflow.md`
