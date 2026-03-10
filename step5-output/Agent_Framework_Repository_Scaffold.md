# Agent Framework Repository Scaffold
## Python Multi-Agent System

This repository scaffold is the concrete Step 5 starter project derived from the implementation blueprint.

## 1 Repository Structure

```text
agent-framework/
├── pyproject.toml
├── README.md
├── requirements.txt
├── config/
├── examples/
├── scripts/
├── src/agent_framework/
│   ├── agents/
│   ├── config/
│   ├── evaluation/
│   ├── memory/
│   ├── orchestration/
│   ├── protocols/
│   ├── runtime/
│   ├── schemas/
│   └── tools/
└── tests/
```

### Directory purpose
- `agents/`: agent roles and execution contracts
- `orchestration/`: task graph scheduling and lifecycle management
- `tools/`: tool interface and registry
- `memory/`: local-first persistence and context assembly
- `evaluation/`: deterministic and extensible evaluation strategies
- `protocols/`: MCP, A2A, and model backend abstraction boundaries
- `runtime/`: logging and event tracing
- `schemas/`: dataclass artifacts for all core objects
- `config/`: YAML configuration loading
- `tests/`: unit and orchestration tests
- `examples/`: starter runnable workflow

## 2 Core Schemas

Implemented in `src/agent_framework/schemas/models.py`.

Included artifacts:
- `ProductDefinition`
- `Domain`
- `Subdomain`
- `WorkItem`
- `TaskNode`
- `ExecutionPlan`
- `AcceptanceCriteria`
- `EvaluationPlan`
- `EvaluationResult`
- `QualityScore`

## 3 Agent Base Classes

Implemented in `src/agent_framework/agents/`.

Included agents:
- `BaseAgent`
- `SupervisorAgent`
- `PlanningAgent`
- `ToolRouterAgent`
- `EvaluationAgent`
- `MemoryAgent`
- `PipelineAgent`

## 4 Task Graph Engine

Implemented in `src/agent_framework/orchestration/task_graph.py`.

Responsibilities:
- node registration
- dependency tracking
- ready-task selection
- completion detection
- failure detection

## 5 Orchestration Runtime

Implemented in `src/agent_framework/orchestration/orchestrator.py`.

Lifecycle:
1. receive `ProductDefinition`
2. invoke `PlanningAgent`
3. build `TaskGraph`
4. assign task via `SupervisorAgent`
5. execute worker agent
6. evaluate outputs
7. retry or complete

## 6 Tool System

Implemented in `src/agent_framework/tools/`.

Included:
- `BaseTool`
- `ToolResult`
- `ToolRegistry`
- `EchoTool`

## 7 Memory System

Implemented in `src/agent_framework/memory/`.

Included:
- `MemoryStore`
- `TaskStateStore`
- `ArtifactStore`
- `RetrievalIndex`
- `ContextAssembler`

## 8 Protocol Interfaces

Implemented in `src/agent_framework/protocols/`.

Included:
- `MCPClient`
- `AgentMessage`
- `A2AMessageBus`
- `BaseModelBackend`
- `DummyModelBackend`
- `OpenAIModelBackend`
- `HigginsModelBackend`

## 9 Evaluation Subsystem

Implemented in `src/agent_framework/evaluation/`.

Included evaluators:
- `DeterministicEvaluator`
- `LLMJudgeEvaluator`
- `ManualReviewEvaluator`

## 10 Logging and Observability

Implemented in `src/agent_framework/runtime/`.

Included:
- `get_logger`
- `Event`
- `EventBus`

## 11 Configuration System

Implemented in:
- `config/defaults.yaml`
- `src/agent_framework/config/loader.py`

## 12 Testing Structure

Included:
- `tests/test_agents.py`
- `tests/test_orchestrator.py`
- `tests/test_tools.py`
- `tests/test_memory.py`
- `tests/test_protocols.py`

## 13 Example Execution Script

Included:
- `examples/run_example.py`

## 14 Development Roadmap

- Phase 1: core runtime and schemas
- Phase 2: richer agent roles and orchestration policies
- Phase 3: stronger tool system and memory backends
- Phase 4: protocol integration hardening
- Phase 5: evaluation depth and observability hardening

## Full Pipeline Summary

| Step | Result |
|---|---|
| Step 1 | Slide knowledge extraction |
| Step 2 | Architecture interpretation |
| Step 3 | Developer handbook synthesis |
| Step 4 | Python implementation blueprint |
| **Step 5** | **Repository scaffold + starter framework** |

## What Step 5 Enables

This scaffold now supports:
- local repository initialization
- AI-assisted coding continuation
- incremental implementation of agent roles
- orchestration experiments
- future CI/CD, issues, and plugin development
