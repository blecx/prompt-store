# Repository Structure Guide

## Design principle

This repository separates **book content**, **prompt logic**, **review**, and **evidence control** so that the manuscript can evolve without collapsing into one large unmanaged file.

## Main layers

### 1. Manuscript layer
The actual book text lives in `manuscript/`.
This includes:
- front matter
- parts and chapters
- glossary
- references
- appendices
- index seed

### 2. Prompt layer
The prompt system lives in `prompts/`.
It is split into:
- `core/` for persistent control prompts
- `quick-use/` for fast transformations
- `specialized/` for targeted book tasks

### 3. Review layer
The review assets live in `review/` and `prompts/specialized/review/`.
This enables structured critique rather than vague “improve this” requests.

### 4. Evidence layer
The evidence system lives in `refs/`.
It tracks source gathering and citation expectations.

### 5. Operating documentation
The procedural documentation lives in `docs/`.
This is especially important for novice users.

### 6. Utility layer
The build and validation utilities live in `scripts/`.
