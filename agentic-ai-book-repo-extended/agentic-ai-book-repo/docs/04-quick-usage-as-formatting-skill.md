# Quick Usage as a Formatting Skill

This path is for users who do **not** want to run a full book workflow yet.

## Goal

Take an existing research result, analysis, workshop note, whitepaper summary, or technical outline and convert it into **book-ready Markdown** with better structure, terminology discipline, and publication quality.

---

## Use this file

`prompts/quick-use/research-to-book-skill.md`

---

## What it does

It acts like a reusable formatting and quality-control layer.

It tells the model to:
- convert loose analysis into chapter-grade prose
- remove hype and vague phrasing
- define terms
- expose structure and trade-offs
- add missing subsections
- identify evidence gaps
- recommend glossary entries, tables, and diagrams

---

## Minimal invocation

```text
[Paste prompts/quick-use/research-to-book-skill.md]

Now transform the following research into book-ready material.
Book context: technical book on Agentic AI for software architects.
Target chapter: Planning, Control, and Orchestration.
Audience: advanced practitioners.
Desired output length: 2,000–3,000 words.

Source material:
[PASTE RESEARCH OR ANALYSIS]
```

---

## Good use cases

- turning research notes into a real chapter draft
- converting a slide analysis into manuscript prose
- converting architecture analysis into a chapter section
- cleaning up a rough LLM answer into technical-book style
- generating glossary candidates and evidence gaps from raw notes

---

## Output you should request

Request these sections explicitly when useful:
- revised chapter text
- missing concepts
- unsupported claims
- glossary entries to add
- references to gather
- suggested figures and tables
- unresolved questions

---

## Best practice

Do not ask it to invent evidence.
Ask it to mark missing evidence and references explicitly.
