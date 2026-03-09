# Quickstart

## Best path for a first-time user

Follow these steps exactly.

### Step 1 — Choose your mode

Choose one:

- **Mode A: Full report generation** — you want to create a report from a brief or research process
- **Mode B: Format an existing research result** — you already have deep research, notes, or analysis and want a professional report

### Step 2 — Open the right control prompt

Use one of these:

- `prompts/core/report-skill-extended.md` for full, high-rigor work
- `prompts/quick-use/deep-research-to-report-skill.md` for turning deep-research output into a report

### Step 3 — Provide the source material

Possible inputs:

- your report brief
- notes
- research findings
- deep-research output
- interview summaries
- architecture analysis
- vendor comparison

### Step 4 — Ask for one concrete output

Examples:

- create a report outline
- draft the executive summary
- transform this research into a board-ready report
- rewrite this analysis into findings, implications, and recommendations

### Step 5 — Review the result

Run at least these review prompts afterward:

- `prompts/specialized/quality/evidence-gap-review.md`
- `prompts/specialized/quality/consistency-and-contradiction-review.md`
- `prompts/specialized/quality/technical-lector-review.md`

### Step 6 — Move the result into the report skeleton

Use the section files under `report/` and then run:

```bash
python scripts/check_placeholders.py
python scripts/build_report.py
```

## Fastest possible use

Paste this sequence into ChatGPT:

1. contents of `prompts/quick-use/deep-research-to-report-skill.md`
2. your research or deep-research result
3. this instruction:

```text
Transform the material into a professional report with:
- executive summary
- scope and methodology
- key findings
- analysis and implications
- options and trade-offs
- recommendations
- roadmap
- risks and limitations
- references and appendices placeholders
```
