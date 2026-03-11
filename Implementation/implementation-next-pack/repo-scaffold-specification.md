# Repository Scaffold Specification — Local-First Python Agent Framework

## Purpose

This document defines a practical repository scaffold for implementing the agentic AI system architecture as a local-first Python framework.

Target characteristics:

- Python 3.12+
- local-first execution
- multi-agent orchestration
- supervisor-based control
- MCP integration
- A2A integration
- OpenAI API for testing
- Higgins Interface as production backend abstraction
- schema-driven contracts
- strong testing and observability

---

## Repository Layout

```text
agentic-ai-system/
├─ pyproject.toml
├─ README.md
├─ .env.example
├─ .gitignore
├─ Makefile
├─ docs/
│  ├─ architecture/
│  ├─ adr/
│  ├─ diagrams/
│  └─ operator/
├─ configs/
│  ├─ runtime/
│  ├─ policies/
│  ├─ models/
│  └─ tools/
├─ schemas/
│  ├─ task.py
│  ├─ plan.py
│  ├─ tool.py
│  ├─ memory.py
│  ├─ evaluation.py
│  ├─ protocol_a2a.py
│  ├─ protocol_mcp.py
│  └─ artifact.py
├─ src/
│  └─ agentic_ai_system/
│     ├─ __init__.py
│     ├─ runtime/
│     ├─ agents/
│     ├─ planning/
│     ├─ routing/
│     ├─ protocols/
│     ├─ memory/
│     ├─ evaluation/
│     ├─ orchestration/
│     ├─ artifacts/
│     ├─ observability/
│     ├─ policies/
│     ├─ models/
│     ├─ tools/
│     └─ cli/
├─ tests/
│  ├─ unit/
│  ├─ integration/
│  ├─ subsystem/
│  ├─ e2e/
│  └─ fixtures/
├─ examples/
│  ├─ single_agent/
│  └─ full_system/
├─ scripts/
│  ├─ bootstrap/
│  ├─ eval/
│  ├─ dev/
│  └─ packaging/
└─ artifacts/
   ├─ runs/
   ├─ traces/
   ├─ reports/
   └─ packages/
```

---

## Package Responsibilities

### `src/agentic_ai_system/runtime/`
Core runtime primitives.

Modules:
- `kernel.py`
- `context.py`
- `lifecycle.py`
- `execution_state.py`

Responsibilities:
- runtime bootstrapping
- context assembly
- lifecycle state transitions
- cancellation and termination control

### `src/agentic_ai_system/agents/`
Agent implementations and base contracts.

Suggested modules:
- `base.py`
- `supervisor.py`
- `planner.py`
- `worker.py`
- `tool_router.py`
- `memory_agent.py`
- `evaluation_agent.py`

Responsibilities:
- agent role implementations
- agent capability metadata
- execution interfaces
- decision boundaries

### `src/agentic_ai_system/planning/`
Planning and decomposition subsystem.

Suggested modules:
- `decomposer.py`
- `task_graph_builder.py`
- `acceptance_criteria.py`
- `replanner.py`

Responsibilities:
- domain slicing
- task graph generation
- work package creation
- plan revision

### `src/agentic_ai_system/routing/`
Tool and agent routing.

Suggested modules:
- `tool_registry.py`
- `tool_router.py`
- `capability_matcher.py`
- `normalizer.py`
- `permission_engine.py`

Responsibilities:
- tool selection
- capability matching
- permission enforcement
- result normalization

### `src/agentic_ai_system/protocols/`
MCP and A2A protocol integration.

Suggested modules:
- `mcp_client.py`
- `mcp_adapter.py`
- `a2a_envelope.py`
- `a2a_dispatcher.py`
- `protocol_errors.py`

Responsibilities:
- protocol envelopes
- message validation
- context transfer
- timeout / retry handling

### `src/agentic_ai_system/memory/`
Memory and retrieval subsystem.

Suggested modules:
- `stores.py`
- `retrieval.py`
- `summarizer.py`
- `provenance.py`
- `invalidation.py`

Responsibilities:
- storage adapters
- retrieval and hydration
- summarization
- provenance tracking
- invalidation logic

### `src/agentic_ai_system/evaluation/`
Evaluation subsystem.

Suggested modules:
- `engine.py`
- `rubrics.py`
- `verdicts.py`
- `quality_gates.py`
- `regression.py`

Responsibilities:
- rule-based evaluation
- scoring
- verdict generation
- quality gates
- regression comparison

### `src/agentic_ai_system/orchestration/`
Pipeline and graph execution.

Suggested modules:
- `graph.py`
- `scheduler.py`
- `checkpointing.py`
- `retry.py`
- `resume.py`

Responsibilities:
- task graph execution
- dependency handling
- checkpointing
- retries
- recovery

### `src/agentic_ai_system/artifacts/`
Artifact generation and packaging.

Suggested modules:
- `markdown.py`
- `reports.py`
- `packages.py`
- `metadata.py`

Responsibilities:
- artifact generation
- packaging
- metadata stamping
- archive production

### `src/agentic_ai_system/observability/`
Tracing, logging, replay.

Suggested modules:
- `trace.py`
- `ledger.py`
- `events.py`
- `replay.py`

Responsibilities:
- event capture
- trace assembly
- run ledger
- replay utilities

### `src/agentic_ai_system/policies/`
Runtime and safety policies.

Suggested modules:
- `approval.py`
- `budgets.py`
- `tool_policies.py`
- `safety.py`

Responsibilities:
- approval gates
- budget limits
- tool restrictions
- operator safeguards

### `src/agentic_ai_system/models/`
LLM backend abstraction.

Suggested modules:
- `base.py`
- `openai_backend.py`
- `higgins_backend.py`
- `selection.py`

Responsibilities:
- model abstraction
- backend switching
- request normalization
- testing vs production separation

### `src/agentic_ai_system/tools/`
Concrete tool adapters.

Suggested categories:
- filesystem
- shell
- python execution
- git
- HTTP
- document generation
- local DB
- MCP-exposed tools

### `src/agentic_ai_system/cli/`
Operator and developer commands.

Suggested commands:
- run pipeline
- inspect trace
- replay run
- execute tests
- package artifacts

---

## Test Structure

### `tests/unit/`
Fast unit tests for schemas, pure logic, validators, selectors.

### `tests/subsystem/`
Supervisor, planner, router, memory, evaluation, orchestration each tested as subsystems.

### `tests/integration/`
Cross-domain interactions:
- planner → router
- router → tools
- execution → memory
- execution → evaluation
- supervisor → orchestration

### `tests/e2e/`
Full project scenarios.

### `tests/fixtures/`
Static fixtures:
- product definitions
- plan samples
- tool outputs
- memory records
- verdict examples

---

## Starter Implementation Order

1. schemas/
2. runtime/
3. agents/base.py
4. planning/
5. routing/
6. memory/
7. evaluation/
8. orchestration/
9. models/
10. tools/
11. cli/
12. artifacts/
13. observability/
14. policies/

---

## Initial Build Targets

### Milestone 1
- schemas compile
- runtime boots
- supervisor and planner skeletons exist

### Milestone 2
- task graph generation works
- tool registry and router functional
- local tools callable

### Milestone 3
- memory writes and retrieval work
- evaluation verdict path works
- orchestration graph can execute

### Milestone 4
- OpenAI backend integrated for testing
- Higgins backend abstraction stub integrated
- subsystem tests pass

### Milestone 5
- full-system example scenarios run end-to-end
- artifacts are packaged
- traces are replayable