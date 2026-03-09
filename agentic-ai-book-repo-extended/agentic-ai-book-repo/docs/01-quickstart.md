# Quickstart

This file is for the fastest possible safe start.

## Goal

Get from zero to a usable book workflow in one sitting.

## What you need

- a title or working title
- a rough audience idea
- a rough scope idea
- this repository
- a chat model that can follow structured prompts

## 10-minute startup path

### Step 1 — Fill the minimum metadata
Open `book.yaml` and set at least:
- working title
- subtitle or temporary subtitle
- target audience
- purpose
- tone
- current status

### Step 2 — Read the master operating prompt
Open:

`prompts/core/book-skill-extended.md`

This is the master prompt. It defines the standards for how content should be generated.

### Step 3 — Generate or improve the table of contents
Use:

`prompts/specialized/toc/toc-from-book-brief.md`

Paste the prompt into a chat, then provide:
- book title
- audience
- purpose
- constraints
- desired depth

### Step 4 — Draft one chapter only
Do not draft the whole book at once.
Start with one chapter using:

`prompts/specialized/chapters/full-chapter-draft.md`

### Step 5 — Put the result into `manuscript/`
Store the resulting chapter in the relevant manuscript folder.

### Step 6 — Capture terminology and sources immediately
Update:
- `manuscript/90-back-matter/90-glossary.md`
- `refs/source-log.md`
- `manuscript/90-back-matter/91-references.md`

### Step 7 — Review the chapter
Use:

`prompts/specialized/review/technical-lector-review.md`

### Step 8 — Build the combined manuscript
Run:

```bash
python scripts/build_book.py
```

---

## Fastest path for formatting research into book style
If you already have research, notes, or analysis and want them rewritten into book-ready material, use:

- `docs/04-quick-usage-as-formatting-skill.md`
- `prompts/quick-use/research-to-book-skill.md`

---

## Avoid these beginner mistakes

- drafting multiple chapters before the terminology stabilizes
- skipping the glossary until the end
- mixing speculation and explanation without labels
- writing like a blog instead of a technical book
- using prompts without giving context, audience, and chapter purpose
- failing to record sources while the material is fresh
