# Detailed Usage Guide

## 1. Operating model

This repository supports two dominant workflows.

### Workflow A — Full report production

Use this when you are starting from a brief, research question, or assignment.

Sequence:

1. define assignment
2. create research/deep-research brief
3. generate report outline
4. generate sections
5. run quality reviews
6. assemble final report

### Workflow B — Research-to-report transformation

Use this when you already have:

- deep-research output
- notes from another model
- interview transcripts
- architecture analysis
- internal documentation
- draft findings

Sequence:

1. standardize source input
2. instruct model with quick-use report skill
3. generate structured report
4. review and strengthen weak sections
5. merge into report skeleton

## 2. Recommended section order

For most technical and strategic reports, draft in this order:

1. report objective
2. outline
3. scope and methodology
4. findings
5. analysis and implications
6. options and trade-offs
7. recommendations
8. roadmap
9. risks and limitations
10. executive summary last

This order works because the executive summary should reflect the completed logic of the report.

## 3. Required quality controls

Every serious report should state:

- what was examined
- what was not examined
- how evidence was obtained
- where confidence is high or low
- what assumptions were required
- what recommendations follow and why
- what could invalidate the conclusions

## 4. Converting deep research into a report

When converting deep research, do not allow the output to remain a research memo.

A report must additionally provide:

- decision framing
- synthesis across findings
- implications
- action path
- explicit limitations

## 5. Report types supported well by this package

- technical assessment reports
- architecture review reports
- vendor comparison reports
- risk and control reports
- strategy reports
- maturity assessment reports
- decision-support briefings

## 6. Failure modes to watch for

### Structural failure

The output is long but lacks clear section function.

### Evidence failure

Claims are stated confidently without visible support or evidence status.

### Recommendation failure

Recommendations are generic, disconnected, or impossible to execute.

### Scope failure

The report silently expands beyond the assignment.

### Audience failure

The report is written either too technically or too vaguely for the intended reader.

## 7. Recovery strategy when a draft is weak

Use these in sequence:

1. `prompts/specialized/restructuring/report-gap-analysis.md`
2. `prompts/specialized/quality/evidence-gap-review.md`
3. `prompts/specialized/quality/consistency-and-contradiction-review.md`
4. section-specific builder prompts
5. `prompts/specialized/quality/technical-lector-review.md`
