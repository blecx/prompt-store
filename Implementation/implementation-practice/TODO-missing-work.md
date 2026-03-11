# ToDo List — Remaining Work

## Already covered
- slide evidence extraction
- architecture interpretation
- handbook synthesis
- orchestration architecture
- Python implementation blueprint
- framework blueprint
- supervisor / planning / tool-router / memory / evaluation / orchestration subsystem design
- baseline diagrams
- operator manual

## Still missing with prompt suggestions

### 1. Repository / package scaffold
Prompt:
Generate a complete local-first Python repository scaffold for the framework blueprint. Include package structure, starter modules, schemas, interfaces, configs, tests, and runtime entry points. Optimize for Python 3.12+, MCP, A2A, and local execution.

### 2. Coding domain breakdown
Prompt:
Split the implementation architecture into coding domains. For each domain define modules, interfaces, coding tasks, review tasks, testing tasks, and debugging tasks. Produce a developer work package matrix.

### 3. Schemas and contracts
Prompt:
Design the schema layer for the agent framework. Produce Pydantic-style data contracts for tasks, tools, plans, memory, evaluation, and A2A delegation.

### 4. Tool catalog and permission matrix
Prompt:
Create a tool catalog and permission matrix for the local-first multi-agent system. Include categories, risk levels, allowed consumers, approval requirements, and fallback strategy.

### 5. Protocol layer design
Prompt:
Design the protocol layer for MCP and A2A in a local-first Python agent framework. Specify message envelopes, routing rules, timeout handling, retries, and error semantics.

### 6. Evaluation rubrics and quality gates
Prompt:
Generate evaluation rubrics and quality gates for planning, routing, memory retrieval, artifact quality, policy compliance, and orchestration success. Include quantitative and qualitative criteria.

### 7. Regression harness
Prompt:
Design a regression harness for the local-first agent framework. Cover single-agent tests, subsystem tests, cross-agent tests, and end-to-end workflow tests.

### 8. Observability and debugging guide
Prompt:
Create a debugging and observability handbook for the multi-agent system. Include traces, run ledgers, event correlation, replay, timeout diagnosis, tool failure diagnosis, and policy-failure diagnosis.

### 9. Local development workflow
Prompt:
Define the local development workflow for the Python agent framework. Include environment setup, test execution, sample runs, debug modes, artifact inspection, and package validation.

### 10. CI / automation workflow
Prompt:
Generate a CI design for the Python agent framework including linting, typing, unit tests, schema validation, regression tests, artifact checks, and packaging.

### 11. Security and governance design
Prompt:
Produce a security and governance design for a local-first agent system. Cover secrets, approvals, tool restrictions, budgets, audit trails, and operator intervention.

### 12. ADR set
Prompt:
Generate an ADR set for the agent framework covering local-first execution, Python choice, supervisor orchestration, MCP and A2A integration, memory strategy, evaluation strategy, and testing strategy.

### 13. Extended diagram pack
Prompt:
Use diagram-pack/prompt-generate-diagrams.md.

### 14. Example project pack
Prompt:
Generate a practice project pack for the multi-agent framework. Include five single-agent test projects and five full-system test projects. Define goals, inputs, expected outputs, evaluation criteria, and failure signals.

### 15. Implementation workboard
Prompt:
Convert the implementation architecture into a domain-based implementation workboard with backlog, milestones, dependencies, reviews, tests, and debugging tasks.

## Recommended next execution order
1. Implementation domain breakdown
2. Repository/package scaffold
3. Schemas and contracts
4. Tool catalog / permission matrix
5. Protocol layer design
6. Evaluation rubrics
7. Regression harness
8. Observability and debugging guide
9. Local development workflow
10. CI workflow
11. Security and governance
12. ADR set
13. Example project pack
14. Extended diagrams
15. Implementation workboard
