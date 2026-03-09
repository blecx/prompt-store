# Quick Usage as a Formatting Skill

## Purpose

This mode is for users who already have a research or analysis result and want to **format, normalize, and upgrade** it into a professional report.

## Best prompt to use

Use:

- `prompts/quick-use/research-to-report-skill.md`
- or `prompts/quick-use/deep-research-to-report-skill.md`

## What this does

It converts a source text into a structured report with:

- executive summary
- decision context
- scope and method
- findings
- analysis
- implications
- recommendations
- roadmap
- risks and limitations
- reference placeholders

## Paste pattern

```text
[PASTE THE QUICK-USE REPORT SKILL PROMPT FIRST]

Now transform the following material into a publication-grade report.
Target audience: <executives / architects / product managers / procurement / mixed>
Report type: <technical assessment / architecture review / vendor analysis / strategy / risk>
Decision to support: <decision>
Required tone: professional, explicit, gap-aware, non-generic

SOURCE MATERIAL:
<insert research, analysis, notes, or deep-research output>
```

## Best practice settings

Tell the model explicitly:

- do not merely summarize
- separate findings from interpretation
- surface assumptions and evidence gaps
- avoid unsupported certainty
- provide implementation-oriented recommendations
- identify unresolved issues

## Fast post-review prompt

After generation, run:

```text
Review the report for structural gaps, unsupported claims, contradictions, missing assumptions, missing trade-offs, and weak recommendations. Then provide a corrected version.
```
