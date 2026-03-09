# Novice Usage Guide

## What this package does

This package helps you create reports that look and behave like professional deliverables instead of unstructured AI output.

It gives you:

- structure
- prompts
- templates
- review tools
- quality checks

## What a good report is

A good report answers five questions clearly:

1. **What problem or decision is this about?**
2. **What was examined and how?**
3. **What was found?**
4. **What does it mean?**
5. **What should happen next?**

If your draft does not answer these questions, it is not yet a strong report.

## The easiest safe workflow

### 1. Start from the deep-research template

Open `templates/deep-research-request-template.md`.

Fill in:

- objective
- audience
- key questions
- scope boundaries
- exclusions
- expected output

### 2. Use the extended report skill

Open `prompts/core/report-skill-extended.md` and paste it before your actual request.

This acts like a control layer. It tells the model to behave like a disciplined report generator.

### 3. Generate the outline first

Do not start with a full report unless the subject is very small.

Instead ask:

```text
Using the report skill, create a detailed report outline for this brief.
```

### 4. Generate sections one by one

Start with:

- executive summary
- scope and methodology
- findings
- analysis
- recommendations

### 5. Review before trusting the result

AI-generated reports often look polished while still containing hidden problems. Common failures are:

- claims without support
- recommendations that do not follow from findings
- repeated content across sections
- generic conclusions
- missing limitations

Run the review prompts in `prompts/specialized/quality/`.

## When to use the quick-use skill

Use `prompts/quick-use/research-to-report-skill.md` or `prompts/quick-use/deep-research-to-report-skill.md` when:

- you already have raw material
- you need a strong format quickly
- you want the model to reorganize content into a real report

## What to edit manually

You should always review and possibly revise:

- executive summary wording
- recommendations and decision implications
- sensitive claims
- risk ratings
- any business-critical numbers
- the references section

## Minimum viable report

If you are in a hurry, produce these sections at minimum:

1. title and objective
2. executive summary
3. scope and method
4. key findings
5. recommendations
6. risks and limitations
7. references
