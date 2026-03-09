# Research-to-Book Workflow

This workflow converts research or analysis into book-grade text.

## Step 1 — Start with source material
Possible inputs:
- web research summary
- literature notes
- architecture analysis
- slide analysis
- workshop notes
- LLM-generated analytical draft

## Step 2 — Normalize the material
Remove obvious duplication and group related points.

## Step 3 — Use the quick-format skill
Use:
- `prompts/quick-use/research-to-book-skill.md`

## Step 4 — Ask for missing gaps
Then run:
- `prompts/specialized/review/evidence-gap-review.md`

## Step 5 — Push the result into the manuscript
Store the improved section or chapter in the correct manuscript file.

## Step 6 — Capture glossary and references
Update the glossary and source log immediately.

## Step 7 — Run a lector review
Use:
- `prompts/specialized/review/technical-lector-review.md`
