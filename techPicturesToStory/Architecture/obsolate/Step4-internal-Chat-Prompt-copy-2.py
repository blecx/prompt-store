from pathlib import Path
import zipfile, textwrap

base = Path("/mnt/data")
out_dir = base / "agent_framework_prompt_pack"
out_dir.mkdir(exist_ok=True)

files = {}

files["prompt_3_implementation_architecture.md"] = textwrap.dedent("""
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

files["agent_framework_blueprint_prompt.md"] = textwrap.dedent("""
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

files["supervisor_agents_prompt.md"] = textwrap.dedent("""
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

## Required Output Structure

# Supervisor Agent Architecture
## Local-First Python Design Specification

### 1. Mission of the Supervisor Agent
### 2. Inputs and Outputs
### 3. Responsibility Boundaries
### 4. Delegation Model
### 5. Checkpoint and Approval Design
### 6. Observability and Control
### 7. Failure Modes
### 8. Suggested Local Tooling
### 9. Python Implementation Model
### 10. Evaluation Criteria

For tooling, propose concrete local-first components such as:
- task graph inspector
- artifact state tracker
- policy engine
- run ledger
- audit logger
- A2A dispatcher
- MCP capability registry
- budget tracker
- execution status monitor

For each proposed tool explain:
- purpose
- read/write risk
- invocation frequency
- local-first relevance

Use precise engineering language.
Do not show chain-of-thought.
Only provide the final design specification.
""").strip() + "\n"

files["planning_agents_prompt.md"] = textwrap.dedent("""
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

## Required Output Structure

# Planning Agent Architecture
## Local-First Python Design Specification

### 1. Planning Mission
### 2. Inputs and Outputs
### 3. Decomposition Strategy
### 4. Plan Structures
### 5. Planning Loops
### 6. Coordination with Supervisor and Workers
### 7. Suggested Local Tooling
### 8. Python Implementation Model
### 9. Failure Modes
### 10. Evaluation Criteria

For tooling, propose concrete local components such as:
- task graph builder
- requirements parser
- dependency analyzer
- acceptance-criteria checker
- spec linter
- artifact diff tool
- schema validator
- local retrieval/search tool
- MCP context provider client

Use precise engineering language.
Do not show chain-of-thought.
Only provide the final design specification.
""").strip() + "\n"

files["tool_router_agents_prompt.md"] = textwrap.dedent("""
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

## Required Output Structure

# Tool Router Agent Architecture
## Local-First Python Design Specification

### 1. Routing Mission
### 2. Inputs and Outputs
### 3. Tool Selection Logic
### 4. Tool Categories
### 5. Result Normalization
### 6. Fallback and Recovery
### 7. Suggested Local Tooling
### 8. Python Implementation Model
### 9. Failure Modes
### 10. Evaluation Criteria

Tool categories to consider:
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

Use precise engineering language.
Do not show chain-of-thought.
Only provide the final design specification.
""").strip() + "\n"

files["evaluation_agents_prompt.md"] = textwrap.dedent("""
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

## Required Output Structure

# Evaluation Agent Architecture
## Local-First Python Design Specification

### 1. Evaluation Mission
### 2. Evaluation Layers
### 3. Inputs and Outputs
### 4. Evaluation Methods
### 5. Suggested Local Tooling
### 6. Quality Gates
### 7. Python Implementation Model
### 8. Failure Modes
### 9. Metrics
### 10. Operational Use

Suggested local tooling:
- rubric engine
- test harness
- schema validator
- trace analyzer
- regression runner
- artifact comparator
- policy checker
- result ledger

Use precise engineering language.
Do not show chain-of-thought.
Only provide the final design specification.
""").strip() + "\n"

files["memory_agents_prompt.md"] = textwrap.dedent("""
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

## Required Output Structure

# Memory Agent Architecture
## Local-First Python Design Specification

### 1. Memory Mission
### 2. Memory Classes
### 3. Inputs and Outputs
### 4. Storage Model
### 5. Retrieval and Context Hydration
### 6. Summarization and Compaction
### 7. Suggested Local Tooling
### 8. Python Implementation Model
### 9. Failure Modes
### 10. Evaluation Criteria

Suggested local tooling:
- local vector index
- artifact catalog
- trace ledger
- summary generator
- provenance recorder
- invalidation engine
- context packager
- MCP resource adapter

Use precise engineering language.
Do not show chain-of-thought.
Only provide the final design specification.
""").strip() + "\n"

files["orchestration_pipelines_prompt.md"] = textwrap.dedent("""
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

## Required Output Structure

# Orchestration Pipeline Architecture
## Local-First Python Design Specification

### 1. Pipeline Mission
### 2. Pipeline Inputs and Outputs
### 3. Execution Model
### 4. Retry and Recovery
### 5. Coordination with Other Agents
### 6. Suggested Local Tooling
### 7. Python Implementation Model
### 8. Failure Modes
### 9. Evaluation Criteria
### 10. Hardening Strategy

Suggested local tooling:
- task graph engine
- state store
- checkpoint manager
- queue / scheduler
- trace collector
- retry controller
- timeout controller
- artifact sink
- MCP/A2A adapters

Use precise engineering language.
Do not show chain-of-thought.
Only provide the final design specification.
""").strip() + "\n"

files["README_prompt_usage_guide.md"] = textwrap.dedent("""
# Prompt Pack Usage Guide

This archive contains a staged prompt set for building a **local-first, Python-based, multi-agent framework architecture**.

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

Expected output:
- structured slide analysis
- architecture-focused interpretation
- ordered chapter set

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

### Stage 4 — Specialized Role Prompts
Recommended order:
1. `supervisor_agents_prompt.md`
2. `planning_agents_prompt.md`
3. `tool_router_agents_prompt.md`
4. `memory_agents_prompt.md`
5. `evaluation_agents_prompt.md`
6. `orchestration_pipelines_prompt.md`

Reason:
- supervision defines governance and routing ownership
- planning defines decomposition logic
- tool routing defines execution pathways
- memory defines state continuity
- evaluation defines quality gates
- orchestration binds everything into runtime execution

Required context for each specialized prompt:
- framework blueprint from Stage 3
- relevant domain model
- tool constraints
- local-first rule
- Python implementation requirement
- production/testing backend split

## Minimum Context Package to Carry Forward

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
- agreed package/module layout

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

## Suggested Deliverables

After the full prompt chain, target:
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
""").strip() + "\n"

for name, content in files.items():
    (out_dir / name).write_text(content, encoding="utf-8")

zip_path = base / "agent_framework_prompt_pack.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for path in sorted(out_dir.iterdir()):
        z.write(path, arcname=f"agent_framework_prompt_pack/{path.name}")

print(zip_path)
print(len(files))
