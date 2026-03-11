from pathlib import Path
import zipfile, textwrap, os, json

base = Path("/mnt/data")
out_dir = base / "agent_framework_prompt_pack"
out_dir.mkdir(exist_ok=True)

prompt3 = textwrap.dedent("""
# Prompt 3 — Implementation Architecture for a Local-First Python Agent Framework

You are acting as a **principal AI systems architect, Python framework architect, and multi-agent systems engineer**.

Your task is to transform the provided architectural analyses, handbook material, product definition, and domain decomposition into an **implementation-oriented architecture specification** for a **local-first, Python-based agent framework**.

The framework is intended for:

- multi-agent orchestration
- domain-specialized agents
- hierarchical delegation
- local execution
- protocol-based interoperability
- Python implementation
- future integration with **Higgins Interface** as the production model backend
- **OpenAI API** as the testing backend
- tool interoperability through **MCP**
- agent-to-agent collaboration through **A2A**
- optional compatibility with **LangChain-style tool abstractions**

The result must read like a **developer architecture specification** that can directly guide repository design, implementation planning, and framework prototyping.

---

## Core Objective

Produce a complete Markdown document titled:

# Local-First Multi-Agent Framework
## Implementation Architecture Specification

The document must explain how to move from:

**Product Definition**
→ **Domain Decomposition**
→ **Subdomain Slicing**
→ **Specialized Agents**
→ **Tool Routing**
→ **Execution Pipelines**
→ **Evaluation and Safety Controls**

This is not a generic essay.
It is an implementation-oriented architecture document.

---

## Required Output Structure

# Local-First Multi-Agent Framework
## Implementation Architecture Specification

---

## 1. Architectural Scope

Explain:

- target problem class
- local-first constraint
- Python as implementation language
- model backend split:
  - testing with OpenAI API
  - production with Higgins Interface
- interoperability goals
- protocol goals:
  - MCP
  - A2A

Clarify which parts belong to:

- framework core
- agent runtime
- tool layer
- protocol layer
- memory layer
- evaluation layer
- orchestration layer

---

## 2. Product Definition to Agent System Mapping

Assume the starting point is a **product definition** already split into **domains**.

Explain how to transform this into an executable agent structure.

Required flow:

Product Definition
→ Domain Map
→ Subdomain Breakdown
→ Capability Map
→ Agent Assignment
→ Tool Assignment
→ Execution Graph

Explain:

- how domains are identified
- how subdomains are sliced
- how responsibilities are assigned to specialized agents
- how domain boundaries influence orchestration

Use precise terms such as:

- bounded context
- responsibility partitioning
- capability mapping
- execution ownership
- dependency surface

---

## 3. Agent Taxonomy

Define the major agent roles in the framework.

At minimum include:

- supervisor agents
- planning agents
- tool router agents
- evaluation agents
- memory agents
- execution / worker agents
- orchestration pipeline components

For each role specify:

Purpose
Inputs
Outputs
Decision scope
State requirements
Failure modes
Observability requirements

---

## 4. Control and Planning Loops

Explain the runtime control loop.

Required sequence:

Goal Intake
→ Context Hydration
→ Planning
→ Subtask Decomposition
→ Tool / Agent Routing
→ Execution
→ Evaluation
→ Reflection / Retry / Escalation
→ Completion / Handoff

Explain:

- planner-executor loops
- supervisor-worker loops
- retry limits
- escalation rules
- termination conditions
- cost and latency controls

---

## 5. Tool-Use Architecture

Describe a Python-first tool architecture.

Include:

- tool registry
- tool metadata schema
- tool router
- structured tool invocation
- result normalization
- error handling
- approval gates
- read-only vs mutating tools

Discuss compatibility with:

- LangChain-style tool abstractions
- MCP servers / MCP clients
- local shell tools
- Python callables
- HTTP APIs
- file-system tools
- repository tools

Explain how tool selection should work:

- semantic fit
- schema fit
- domain fit
- permission fit
- execution cost fit

---

## 6. Protocol Architecture

Explain how the framework should use protocols.

### MCP
Describe:

- why MCP matters
- where MCP sits in the architecture
- how tools and context providers are exposed
- how an agent runtime consumes MCP-compatible resources

### A2A
Describe:

- how agents delegate to other agents
- task handoff envelopes
- context transfer
- result return semantics
- failure / timeout handling

Clarify the difference between:

- tool invocation
- protocol-based context access
- agent delegation

---

## 7. Memory and Context Systems

Define memory architecture for local-first execution.

Include:

- working memory
- session memory
- long-term memory
- retrieval memory
- artifact memory
- decision logs

Explain:

- state persistence
- context hydration
- summarization
- retrieval boundaries
- local storage choices
- memory invalidation
- provenance tracking

---

## 8. Orchestration Pipelines

Describe orchestration as executable pipelines / task graphs.

Include:

- task graph creation
- dependency management
- sequential vs parallel execution
- retries
- rollback / compensation strategy
- checkpointing
- resumability

Explain how orchestration differs from single-agent prompting.

---

## 9. Evaluation Architecture

Define how the system is evaluated across layers.

Layers:

- model layer
- agent layer
- pipeline layer
- application layer

Metrics should include:

- task success
- plan quality
- tool accuracy
- retrieval relevance
- latency
- token cost
- failure rate
- recovery effectiveness
- safety conformance

Explain evaluation methods:

- code-based checks
- LLM-as-judge
- human review
- trace review
- regression suites

---

## 10. Safety and Governance Controls

Explain operational safeguards.

Include:

- approval gates
- restricted tools
- timeout controls
- concurrency controls
- cost budgets
- retry caps
- loop detection
- audit logs
- read-only defaults
- policy enforcement

---

## 11. Suggested Python Framework Structure

Propose a modular Python package structure.

At minimum cover:

- agents/
- orchestration/
- tools/
- memory/
- protocols/
- evaluation/
- models/
- runtime/
- schemas/
- config/
- tests/

Explain responsibilities of each package.

---

## 12. Implementation Roadmap

Provide a staged implementation plan.

Suggested phases:

1. Local runtime skeleton
2. Tool abstraction layer
3. Planner + supervisor loop
4. Memory subsystem
5. MCP integration
6. A2A delegation layer
7. Evaluation harness
8. Production model backend abstraction
9. Hardening and test suites

Each phase must include:

- goal
- key modules
- test focus
- exit criteria

---

## Writing Requirements

Write in the style of:

- a Python framework architecture specification
- a multi-agent systems design reference
- a serious developer handbook

Avoid:

- motivational filler
- generic AI commentary
- product marketing language
- unsupported claims

Prefer:

- implementation-aware terminology
- layered architecture language
- protocol language
- orchestration language
- testability language

---

## Precision Rules

- Do not hallucinate concrete Higgins Interface APIs if not provided.
- Treat Higgins Interface as a production backend abstraction point unless specific APIs are available in the supplied material.
- Do not assume cloud-first infrastructure.
- Optimize for local-first execution.
- Prefer Python-native implementation patterns.
- Keep the design compatible with future extension.
- Make all sections reusable for framework implementation.

Do not show chain-of-thought.
Only provide the final structured architecture document.
""").strip() + "\n"

blueprint = textwrap.dedent("""
# Agent Framework Blueprint Prompt — Local-First Python Multi-Agent System

You are acting as a **principal AI systems architect, Python framework architect, and agent-platform designer**.

Your task is to design a **local-first, Python-based, multi-agent framework blueprint** that starts from a **product definition**, decomposes it into **domains**, slices each domain into **subdomains and work packages**, and assigns these to **specialized agents** operating under a **supervisor-driven orchestration model**.

The framework must be designed for:

- local-first execution
- Python implementation
- specialized domain agents
- supervisor-driven delegation
- task planning and task slicing
- tool routing
- memory management
- evaluation pipelines
- protocol interoperability
- future production integration with **Higgins Interface**
- testing integration with **OpenAI API**
- compatibility with **MCP**
- compatibility with **A2A**
- optional compatibility with **LangChain-style tool interfaces**

The output must be a **technical blueprint**, not a summary.

---

## Core Objective

Generate a complete design blueprint for a framework that supports this flow:

Product Definition
→ Domain Decomposition
→ Domain Slicing
→ Agent Specialization
→ Tool Selection
→ Local Execution
→ Evaluation
→ Memory Update
→ Supervisor Review
→ Final Artifact / Handoff

The design must prioritize:

- precision
- modularity
- observability
- controllability
- local execution
- testability
- future extensibility

---

## Required Output Structure

# Agent Framework Blueprint
## Local-First Python Architecture

---

## 1. Framework Mission and Scope

Define:

- framework purpose
- user problem solved
- local-first operating model
- model backend strategy
- protocol strategy
- expected artifact outputs
- target implementation style in Python

---

## 2. Input Model: Product Definition and Domain Model

Explain how the framework should ingest and structure:

- product definition
- domain map
- constraints
- quality goals
- acceptance criteria
- artifact expectations

Then describe how to derive:

- domains
- subdomains
- responsibilities
- dependencies
- priority order

---

## 3. Agent Role Model

Define the complete set of agents.

At minimum include:

- supervisor agents
- planning agents
- tool router agents
- evaluation agents
- memory agents
- worker / execution agents
- artifact / documentation agents
- orchestration pipeline components

For each agent define:

- mission
- authority
- input contract
- output contract
- state needs
- escalation path
- metrics

---

## 4. Orchestration Model

Explain the orchestration topology.

Cover:

- centralized supervision
- delegated execution
- nested planning
- task graph coordination
- retries
- checkpoints
- completion criteria

Explain how the framework prevents:

- tool misuse
- loop runaway
- context loss
- duplicate work
- hidden failures

---

## 5. Tooling Model

Design a tool model for local Python agents.

Include:

- tool registry
- tool descriptors
- invocation schema
- structured outputs
- permission policies
- error normalization
- fallback logic

Propose practical local-first tool categories.

Suggested categories:
- filesystem tools
- git / repository tools
- Python execution tools
- shell tools
- test runners
- linters / formatters
- search / retrieval tools
- documentation tools
- local database tools
- HTTP client tools
- MCP-based tools

For each category, explain:
- why it matters
- risk profile
- typical agent consumers

---

## 6. Protocol Integration Model

Describe how to integrate:

### MCP
- resource access
- tool exposure
- context providers
- local interoperability

### A2A
- delegation contracts
- task envelopes
- result return
- timeout and failure semantics

Explain where these protocols sit in the architecture and how they support local agents.

---

## 7. Memory Model

Design a memory system.

Include:
- working memory
- session memory
- long-term memory
- retrieval memory
- artifact memory
- trace / decision memory

Explain:
- storage choices
- summarization strategy
- provenance handling
- invalidation rules
- privacy / local-control assumptions

---

## 8. Evaluation and Quality Model

Explain how the framework measures quality.

Include:
- planning quality
- execution success
- tool accuracy
- artifact quality
- retrieval quality
- latency
- cost
- policy adherence

Explain:
- automated evaluation
- LLM-as-judge
- human review
- regression testing
- trace inspection

---

## 9. Python Reference Architecture

Propose a Python package layout and module responsibilities.

Include concrete package suggestions.

---

## 10. Implementation Strategy

Provide a phased implementation roadmap.

Each phase should contain:
- objective
- key modules
- integration points
- validation criteria

---

## Technical Requirements

Optimize for:
- local execution
- Python 3.12+
- modular architecture
- strong typing
- schema-driven contracts
- testability
- reproducibility

Do not assume unsupported external APIs.
Treat Higgins Interface as a backend abstraction boundary unless concrete APIs are supplied.

Do not show chain-of-thought.
Only produce the final technical blueprint.
""").strip() + "\n"

roles = {
"supervisor_agents_prompt.md": textwrap.dedent("""
# Specialized Prompt — Supervisor Agents

You are acting as a **principal architect for supervisor-driven multi-agent systems**.

Your task is to design a **highly sophisticated supervisor-agent architecture** for a **local-first Python agent framework**.

Context:
- Input starts from a product definition already split into domains.
- Each domain is further sliced into subdomains and work packages.
- Specialized agents execute domain-specific work.
- Supervisor agents coordinate, govern, and validate the overall process.
- Production model backend will later use **Higgins Interface**.
- Testing backend uses **OpenAI API**.
- Protocols to consider:
  - **MCP**
  - **A2A**
- Tool abstractions should remain compatible with Python-native patterns and optionally LangChain-style tool interfaces.

---

## Objective

Produce a complete architecture specification for supervisor agents.

Focus on:
- authority model
- delegation model
- domain routing
- escalation logic
- checkpoint design
- policy enforcement
- completion validation
- observability
- local execution constraints

---

## Required Output Structure

# Supervisor Agent Architecture
## Local-First Python Design Specification

### 1. Mission of the Supervisor Agent
Explain:
- why the supervisor exists
- what decisions it owns
- what it must never do directly
- how it differs from a planner
- how it differs from a worker agent

### 2. Inputs and Outputs
Define:
- input envelope
- domain map input
- task graph input
- policy input
- output contracts
- escalation outputs
- completion outputs

### 3. Responsibility Boundaries
Specify:
- orchestration ownership
- delegation ownership
- approval ownership
- policy and safety ownership
- evaluation trigger ownership

### 4. Delegation Model
Explain:
- when to delegate
- how to choose specialized agents
- how to handle nested delegation
- how to avoid duplicate work
- how to handle unavailable agents
- how A2A task handoff should work

### 5. Checkpoint and Approval Design
Cover:
- approval gates
- confidence thresholds
- retry caps
- budget gates
- mutating vs read-only operations
- artifact review checkpoints

### 6. Observability and Control
Define:
- required logs
- execution traces
- delegation traces
- policy decisions
- anomaly detection
- loop detection

### 7. Failure Modes
Cover:
- invalid routing
- delegation dead ends
- worker disagreement
- partial completion
- timeout conditions
- stale context
- policy conflicts

### 8. Suggested Local Tooling
Propose tools a supervisor may use indirectly or directly with strict limits:
- task graph inspector
- artifact state tracker
- policy engine
- run ledger
- audit logger
- A2A dispatcher
- MCP capability registry
- budget tracker
- execution status monitor

For each tool:
- purpose
- read/write risk
- invocation frequency
- why local-first matters

### 9. Python Implementation Model
Propose:
- classes
- interfaces
- schemas
- config structures
- test strategy

### 10. Evaluation Criteria
Define how supervisor-agent quality is measured.

Use precise engineering language.
Do not show chain-of-thought.
Only provide the final design specification.
""").strip() + "\n"),

"planning_agents_prompt.md": textwrap.dedent("""
# Specialized Prompt — Planning Agents

You are acting as a **principal architect for planning-centric agent systems**.

Your task is to design a **planning-agent architecture** for a **local-first Python multi-agent framework**.

Context:
- The system starts from a product definition divided into domains.
- Each domain is recursively sliced into subdomains, tasks, and work packages.
- Planning agents convert goals into executable plans for specialized agents.
- Production model backend later: **Higgins Interface**
- Testing backend: **OpenAI API**
- Protocols:
  - **MCP**
  - **A2A**
- Python is the implementation language.

---

## Objective

Produce a complete design specification for planning agents.

Focus on:
- decomposition strategy
- plan granularity
- dependency modeling
- bounded-context planning
- plan revision
- failure recovery
- handoff readiness

---

## Required Output Structure

# Planning Agent Architecture
## Local-First Python Design Specification

### 1. Planning Mission
Explain:
- what planning agents are responsible for
- how they transform goals into plans
- why planning must be separated from execution in complex systems

### 2. Inputs and Outputs
Define:
- product definition input
- domain context input
- constraints input
- available agent/tool map
- output plan schema
- execution graph output
- escalation output

### 3. Decomposition Strategy
Explain:
- domain slicing
- subdomain slicing
- work package creation
- acceptance criteria propagation
- risk-aware planning
- dependency mapping

### 4. Plan Structures
Describe:
- linear plans
- DAG/task graphs
- hierarchical plans
- iterative refinement plans

### 5. Planning Loops
Explain:
- initial planning
- reflection / revision
- replanning triggers
- uncertainty handling
- stop conditions

### 6. Coordination with Supervisor and Workers
Clarify:
- what the supervisor decides
- what the planner decides
- when to return for escalation
- how to package subtasks for workers

### 7. Suggested Local Tooling
Propose local tools:
- task graph builder
- requirements parser
- dependency analyzer
- acceptance-criteria checker
- spec linter
- artifact diff tool
- schema validator
- local retrieval/search tool
- MCP context provider client

For each tool:
- purpose
- why a planner needs it
- risk profile
- preferred output format

### 8. Python Implementation Model
Propose:
- planner interfaces
- plan schemas
- graph structures
- validation hooks
- test strategy

### 9. Failure Modes
Cover:
- under-decomposition
- over-decomposition
- circular dependencies
- invalid work packages
- ambiguity leakage
- missing acceptance criteria

### 10. Evaluation Criteria
Define how planning quality is measured:
- plan completeness
- dependency correctness
- execution readiness
- replan frequency
- task ambiguity rate

Use precise engineering language.
Do not show chain-of-thought.
Only provide the final design specification.
""").strip() + "\n"),

"tool_router_agents_prompt.md": textwrap.dedent("""
# Specialized Prompt — Tool Router Agents

You are acting as a **principal architect for tool-routing and tool-selection systems** in multi-agent AI frameworks.

Your task is to design a **tool router architecture** for a **local-first Python agent framework**.

Context:
- The system uses specialized agents.
- Work originates from a product definition split into domains and subdomains.
- Tool routers select the right local tools, MCP resources, or execution pathways for each subtask.
- Production backend later: **Higgins Interface**
- Testing backend: **OpenAI API**
- Protocols:
  - **MCP**
  - **A2A**
- Optional compatibility with LangChain-style tool abstractions.
- Local execution is mandatory by default.

---

## Objective

Produce a complete design specification for tool router agents.

Focus on:
- capability matching
- permission-aware selection
- schema matching
- local-first routing
- fallback routing
- tool failure handling
- structured result normalization

---

## Required Output Structure

# Tool Router Agent Architecture
## Local-First Python Design Specification

### 1. Routing Mission
Explain:
- what a tool router is
- why routing should be isolated as a first-class concern
- how routing differs from planning and execution

### 2. Inputs and Outputs
Define:
- task input
- tool registry input
- policy input
- execution constraints
- selected tool output
- fallback plan output
- normalization output

### 3. Tool Selection Logic
Explain selection dimensions:
- domain fit
- task fit
- schema fit
- safety fit
- permission fit
- latency/cost fit
- local availability

### 4. Tool Categories
Design a local-first tool catalog including:
- filesystem
- shell
- Python execution
- git/repository
- testing
- linting/formatting
- retrieval/search
- local database
- HTTP client
- document generation
- MCP tools

For each category define:
- use cases
- risks
- expected input/output shape
- ideal consumers

### 5. Result Normalization
Explain:
- structured outputs
- schema enforcement
- error normalization
- provenance tagging
- trace attachment

### 6. Fallback and Recovery
Cover:
- tool unavailable
- schema mismatch
- permission denied
- execution timeout
- invalid result
- degraded mode routing

### 7. Suggested Local Tooling
Propose framework components:
- tool registry
- capability index
- policy checker
- MCP adapter
- result normalizer
- sandbox executor
- timeout controller
- provenance recorder

### 8. Python Implementation Model
Propose:
- tool descriptor schema
- router interfaces
- selection policies
- adapters
- tests

### 9. Failure Modes
Cover:
- wrong tool selection
- unsafe routing
- local/remote mismatch
- mutating tool misuse
- ambiguous capabilities

### 10. Evaluation Criteria
Define metrics such as:
- routing precision
- fallback success rate
- unsafe selection rate
- normalization success
- latency overhead

Use precise engineering language.
Do not show chain-of-thought.
Only provide the final design specification.
""").strip() + "\n"),

"evaluation_agents_prompt.md": textwrap.dedent("""
# Specialized Prompt — Evaluation Agents

You are acting as a **principal architect for evaluation-driven agent systems**.

Your task is to design a **dedicated evaluation-agent architecture** for a **local-first Python multi-agent framework**.

Context:
- Work begins with product definition, domain decomposition, and specialized agent execution.
- Evaluation agents assess outputs, plans, traces, tool use, and policy compliance.
- Production backend later: **Higgins Interface**
- Testing backend: **OpenAI API**
- Protocols:
  - **MCP**
  - **A2A**
- Python is the implementation language.

---

## Objective

Produce a complete design specification for evaluation agents.

Focus on:
- multi-layer evaluation
- artifact quality
- plan quality
- execution-trace quality
- policy compliance
- regression testing
- handoff readiness
- local-first evidence capture

---

## Required Output Structure

# Evaluation Agent Architecture
## Local-First Python Design Specification

### 1. Evaluation Mission
Explain:
- why evaluation must be a dedicated subsystem
- what is evaluated
- when evaluation happens
- how evaluation differs from supervision

### 2. Evaluation Layers
Cover:
- model layer
- plan layer
- tool-execution layer
- artifact layer
- pipeline layer
- application layer

### 3. Inputs and Outputs
Define:
- candidate artifact input
- plan input
- trace input
- policy input
- rubric input
- score output
- verdict output
- escalation output

### 4. Evaluation Methods
Explain:
- rule-based checks
- schema checks
- test-based checks
- LLM-as-judge
- human review
- differential / regression comparison
- trace review

### 5. Suggested Local Tooling
Propose:
- rubric engine
- test harness
- schema validator
- trace analyzer
- regression runner
- artifact comparator
- policy checker
- result ledger

For each:
- purpose
- why local-first matters
- evidence captured
- risks

### 6. Quality Gates
Define:
- accept
- accept with warnings
- revise
- replan
- escalate
- reject

### 7. Python Implementation Model
Propose:
- evaluator interfaces
- rubric schemas
- verdict schemas
- scoring pipeline
- regression suite design

### 8. Failure Modes
Cover:
- false accept
- false reject
- low-signal rubrics
- incomplete evidence
- evaluator drift
- inconsistent verdicts

### 9. Metrics
Define:
- pass rate
- rework rate
- regression failure rate
- false-accept rate
- trace coverage
- rubric coverage

### 10. Operational Use
Explain how evaluation agents interact with:
- supervisors
- planners
- tool routers
- memory agents
- orchestration pipelines

Use precise engineering language.
Do not show chain-of-thought.
Only provide the final design specification.
""").strip() + "\n"),

"memory_agents_prompt.md": textwrap.dedent("""
# Specialized Prompt — Memory Agents

You are acting as a **principal architect for memory-centric agent systems**.

Your task is to design a **memory-agent architecture** for a **local-first Python multi-agent framework**.

Context:
- The framework starts from product definition and domain decomposition.
- Specialized agents create plans, execute work, evaluate results, and produce artifacts.
- Memory agents manage state, retrieval, artifact history, and decision provenance.
- Production backend later: **Higgins Interface**
- Testing backend: **OpenAI API**
- Protocols:
  - **MCP**
  - **A2A**
- Python is the implementation language.
- Local control of memory is mandatory by default.

---

## Objective

Produce a complete design specification for memory agents.

Focus on:
- working memory
- session memory
- long-term memory
- retrieval memory
- artifact memory
- trace / decision memory
- summarization and compaction
- provenance and invalidation

---

## Required Output Structure

# Memory Agent Architecture
## Local-First Python Design Specification

### 1. Memory Mission
Explain:
- why memory must be explicit
- what state must be stored
- how memory supports planning, execution, and evaluation

### 2. Memory Classes
Define:
- working memory
- session memory
- long-term memory
- retrieval memory
- artifact memory
- decision memory

### 3. Inputs and Outputs
Define:
- observation input
- artifact input
- trace input
- retrieval query input
- memory update output
- retrieval result output
- summary output

### 4. Storage Model
Explain local-first storage options such as:
- files
- SQLite / local database
- vector store
- structured JSON/YAML/Markdown artifacts
- append-only logs

Clarify what belongs in which store.

### 5. Retrieval and Context Hydration
Explain:
- retrieval triggers
- ranking
- chunking
- relevance
- context assembly
- provenance tagging

### 6. Summarization and Compaction
Cover:
- when to summarize
- how to avoid losing critical context
- compression strategies
- change tracking

### 7. Suggested Local Tooling
Propose:
- local vector index
- artifact catalog
- trace ledger
- summary generator
- provenance recorder
- invalidation engine
- context packager
- MCP resource adapter

### 8. Python Implementation Model
Propose:
- memory interfaces
- storage adapters
- schemas
- retrieval APIs
- tests

### 9. Failure Modes
Cover:
- stale memory
- polluted memory
- wrong retrieval
- provenance loss
- over-compression
- contradictory summaries

### 10. Evaluation Criteria
Define:
- retrieval relevance
- hydration quality
- provenance completeness
- stale-read rate
- memory consistency

Use precise engineering language.
Do not show chain-of-thought.
Only provide the final design specification.
""").strip() + "\n"),

"orchestration_pipelines_prompt.md": textwrap.dedent("""
# Specialized Prompt — Orchestration Pipelines

You are acting as a **principal architect for orchestration runtimes and pipeline execution systems**.

Your task is to design an **orchestration-pipeline architecture** for a **local-first Python multi-agent framework**.

Context:
- The system starts from a product definition split into domains and subdomains.
- Specialized agents perform planning, routing, memory, execution, and evaluation.
- Orchestration pipelines coordinate these roles into executable workflows and task graphs.
- Production backend later: **Higgins Interface**
- Testing backend: **OpenAI API**
- Protocols:
  - **MCP**
  - **A2A**
- Python is the implementation language.

---

## Objective

Produce a complete design specification for orchestration pipelines.

Focus on:
- task-graph execution
- sequential and parallel steps
- checkpointing
- retries
- resumability
- failure handling
- dependency tracking
- local execution control

---

## Required Output Structure

# Orchestration Pipeline Architecture
## Local-First Python Design Specification

### 1. Pipeline Mission
Explain:
- why orchestration must be explicit
- how orchestration differs from planning
- how orchestration differs from supervision

### 2. Pipeline Inputs and Outputs
Define:
- plan input
- task graph input
- state input
- policy input
- artifact output
- trace output
- status output

### 3. Execution Model
Explain:
- step execution
- node lifecycle
- dependency resolution
- sequential vs parallel execution
- backpressure
- queueing
- checkpointing

### 4. Retry and Recovery
Cover:
- retry policies
- node-level retry
- stage-level retry
- compensation / rollback
- resume from checkpoint
- degraded mode execution

### 5. Coordination with Other Agents
Explain how pipelines interact with:
- supervisors
- planners
- tool routers
- memory agents
- evaluation agents
- workers

### 6. Suggested Local Tooling
Propose:
- task graph engine
- state store
- checkpoint manager
- queue / scheduler
- trace collector
- retry controller
- timeout controller
- artifact sink
- MCP/A2A adapters

### 7. Python Implementation Model
Propose:
- runtime classes
- node abstractions
- graph schemas
- execution context
- event hooks
- tests

### 8. Failure Modes
Cover:
- deadlocks
- starvation
- lost checkpoints
- duplicate execution
- hidden partial failure
- state drift

### 9. Evaluation Criteria
Define:
- pipeline success rate
- checkpoint recovery rate
- duplicate execution rate
- dependency correctness
- mean recovery time

### 10. Hardening Strategy
Explain:
- logging
- audit trails
- replay
- deterministic tests
- chaos / fault injection
- regression suites

Use precise engineering language.
Do not show chain-of-thought.
Only provide the final design specification.
""").strip() + "\n"),
}

guide = textwrap.dedent("""
# Prompt Pack Usage Guide

This archive contains a staged prompt set for building a **local-first, Python-based, multi-agent framework architecture**.

The prompts are designed to be used **in sequence**.
They progressively convert raw source material into:

1. architecture interpretation
2. implementation architecture
3. framework blueprint
4. specialized role specifications

---

## Recommended Prompt Order

### Stage 1 — Source Analysis
Use your earlier slide-analysis and architecture-analysis prompts first.

Purpose:
- extract grounded concepts from source material
- preserve slide structure
- identify architecture patterns, protocols, evaluation models, and operational constraints

Required context:
- uploaded slide images or source documents
- clear ordering requirements
- non-hallucination constraint

Output needed before Stage 2:
- structured analysis in Markdown
- architecture-focused interpretation
- ordered chapter set

---

### Stage 2 — Implementation Architecture
Use:

- `prompt_3_implementation_architecture.md`

Purpose:
- convert conceptual architecture material into an implementation-oriented system architecture
- define runtime layers, protocols, memory, evaluation, and orchestration concerns
- map product definition → domain model → specialized agent runtime

Required context:
- output of Stage 1
- product definition, if available
- domain decomposition, if available
- local-first Python requirement
- model-backend strategy:
  - OpenAI API for testing
  - Higgins Interface for production later

Expected output:
- implementation architecture specification
- package/module recommendations
- runtime and protocol design
- roadmap

---

### Stage 3 — Agent Framework Blueprint
Use:

- `agent_framework_blueprint_prompt.md`

Purpose:
- produce the framework-level blueprint
- formalize agent roles, orchestration model, tool model, protocol integration model, memory model, evaluation model, and implementation strategy

Required context:
- output of Stage 2
- product definition
- domain map / domain decomposition
- target artifacts and quality goals
- protocol requirements (MCP, A2A)
- Python-first implementation constraint

Expected output:
- complete framework blueprint
- reusable architecture baseline
- reference for repo structure and implementation planning

---

### Stage 4 — Specialized Role Prompts
Use the specialized prompts one after another.
Each prompt refines a specific subsystem.

Recommended order:

1. `supervisor_agents_prompt.md`
2. `planning_agents_prompt.md`
3. `tool_router_agents_prompt.md`
4. `memory_agents_prompt.md`
5. `evaluation_agents_prompt.md`
6. `orchestration_pipelines_prompt.md`

Reason for this order:
- supervision defines governance and routing ownership
- planning defines decomposition logic
- tool routing defines execution pathways
- memory defines state continuity
- evaluation defines quality gates
- orchestration pipelines bind everything into runtime execution

Required context for each specialized prompt:
- the framework blueprint from Stage 3
- relevant domain model
- any tool constraints
- local-first rule
- Python implementation requirement
- production/testing backend split

---

## Minimum Context Package to Carry Between Chats

When starting a new chat for any later-stage prompt, bring this context:

### 1. Product Definition
Include:
- problem statement
- goals
- constraints
- quality requirements
- expected outputs / artifacts

### 2. Domain Model
Include:
- domains
- subdomains
- dependencies
- ownership boundaries

### 3. Architecture Baseline
Include:
- implementation architecture output
- framework blueprint output
- any agreed package/module layout

### 4. Runtime Constraints
Include:
- local-first requirement
- Python 3.12+ target
- testing backend = OpenAI API
- production backend = Higgins Interface abstraction
- protocols = MCP and A2A
- optional LangChain-style tool compatibility

### 5. Governance Constraints
Include:
- approval gates
- read-only default tools
- logging requirements
- evaluation requirements
- safety controls

---

## Practical Advice for Running the Prompt Chain

### Keep prompts in separate chats when:
- the context window becomes crowded
- the output becomes too broad
- you want independent subsystem specifications

### Keep prompts in the same chat when:
- the system still needs strong shared context
- you want the model to directly build on prior responses

### Best practice
At the end of each stage, create a compact handoff summary containing:
- architecture decisions
- terminology conventions
- package layout decisions
- role boundaries
- open questions

Use that handoff summary as the seed for the next stage.

---

## Suggested Deliverable Sequence

After running the prompt chain, you should aim to have:

1. source analysis
2. architecture interpretation
3. implementation architecture specification
4. framework blueprint
5. supervisor-agent design
6. planning-agent design
7. tool-router design
8. memory-agent design
9. evaluation-agent design
10. orchestration-pipeline design

These outputs together can be merged into:

- an Agentic AI System Architecture
- a Developer Handbook
- a Python framework specification
- a multi-repository implementation plan

---

## Notes on Tools and Local-First Focus

The prompts intentionally bias toward local-first agents and Python.

Typical tool proposals across the prompts include:
- filesystem tools
- shell tools
- Python execution
- git/repository tools
- test runners
- linters/formatters
- local retrieval/index tools
- SQLite or local structured stores
- MCP adapters
- A2A dispatch envelopes

This aligns with:
- iterative framework prototyping
- secure local development
- controllable evaluation
- later integration into a larger production system

---

## File List

- `prompt_3_implementation_architecture.md`
- `agent_framework_blueprint_prompt.md`
- `supervisor_agents_prompt.md`
- `planning_agents_prompt.md`
- `tool_router_agents_prompt.md`
- `evaluation_agents_prompt.md`
- `memory_agents_prompt.md`
- `orchestration_pipelines_prompt.md`
- `README_prompt_usage_guide.md`

""").strip() + "\n"

# write files
(out_dir / "prompt_3_implementation_architecture.md").write_text(prompt3, encoding="utf-8")
(out_dir / "agent_framework_blueprint_prompt.md").write_text(blueprint, encoding="utf-8")
(out_dir / "README_prompt_usage_guide.md").write_text(guide, encoding="utf-8")
for name, content in roles.items():
    (out_dir / name).write_text(content, encoding="utf-8")

zip_path = base / "agent_framework_prompt_pack.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for p in sorted(out_dir.iterdir()):
        z.write(p, arcname=f"agent_framework_prompt_pack/{p.name}")

print("Created:", zip_path)
print("Files:")
for p in sorted(out_dir.iterdir()):
    print("-", p.name)
