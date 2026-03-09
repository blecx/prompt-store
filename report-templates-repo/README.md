# Report Templates Repository

A publication-grade, practitioner-oriented repository for producing **high-value technical and strategic reports** from scratch or from **deep research output**.

This repository is designed for two modes of work:

1. **Full report production**: from brief, scope, evidence, analysis, and recommendations to a complete report.
2. **Post-formatting mode**: take an existing research or analysis result and transform it into a disciplined, executive-usable report.

The package is intentionally opinionated. It assumes that good reports must be:

- decision-oriented
- structurally explicit
- evidence-aware
- limitation-aware
- gap-aware
- actionable
- reviewable by another expert

## Who this is for

- novice users who need a safe, guided workflow
- analysts writing technical, architecture, market, risk, or vendor reports
- consultants transforming research into executive deliverables
- engineers producing decision documents with evidence and trade-offs

## What is inside

- `docs/` — onboarding, novice guide, detailed operating instructions, quick-use mode, quality gates
- `templates/` — report templates, section templates, deep-research brief templates, evidence templates
- `prompts/` — reusable prompt library for world-class report generation and review
- `report/` — split report skeleton with front matter, core sections, and back matter
- `refs/` — bibliography stub, source log, citation policy
- `review/` — lector/reviewer assets and checklists
- `scripts/` — utility scripts to assemble and validate the report
- `.github/` — workflow stubs, issue templates, and pull request template
- `dist/` — assembled report output

## Fastest path

Read in this order:

1. `docs/01-quickstart.md`
2. `docs/02-novice-usage-guide.md`
3. `docs/04-quick-usage-as-formatting-skill.md`
4. `prompts/core/report-skill-extended.md`
5. `prompts/quick-use/deep-research-to-report-skill.md`

## Core principle

A strong report does not merely restate source material. It does five things:

1. defines the decision context,
2. makes the scope explicit,
3. distinguishes findings from interpretation,
4. states recommendations with rationale and implications,
5. declares limitations, unresolved gaps, and next steps.

## Suggested workflow

1. Create the **report brief** from `templates/deep-research-request-template.md` or your own brief.
2. Use `prompts/core/report-skill-extended.md` as the control prompt.
3. Draft an outline with `prompts/specialized/outlines/report-outline-from-brief.md`.
4. Draft or transform the report.
5. Run the review prompts in `prompts/specialized/quality/`.
6. Consolidate the report with `scripts/build_report.py`.

## Output quality target

This repository targets **real-world best practice**, not generic essay output. The prompts are written to minimize:

- vague claims
- weak structure
- missing assumptions
- unsupported recommendations
- absent risk analysis
- missing evidence trails
- superficial executive summaries

## Minimal command line usage

```bash
python scripts/check_placeholders.py
python scripts/export_manifest.py
python scripts/build_report.py
```
