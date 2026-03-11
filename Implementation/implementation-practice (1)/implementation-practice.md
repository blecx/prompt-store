# Implementation Practice Document — Domain-Based Execution Model

## Purpose
This document converts the generated architecture context into implementation domains suitable for coding jobs, reviews, testing, and debugging.

## Domain set
1. Runtime Core
2. Supervisor and Control
3. Planning
4. Tool Routing and Tool Layer
5. Protocol Layer (MCP / A2A)
6. Memory and Retrieval
7. Evaluation and Quality Gates
8. Orchestration Pipelines
9. Artifact and Document Generation
10. Observability and Debugging
11. Configuration and Policy
12. Test and Regression Harness

## Domain breakdown

### 1. Runtime Core
Coding jobs:
- runtime kernel
- agent base classes
- execution context model
- lifecycle hooks
- state carrier objects
Review jobs:
- separation of concerns
- interface stability
- dependency discipline
Testing jobs:
- context creation
- lifecycle transitions
- error propagation
Debugging jobs:
- runtime state drift
- unexpected lifecycle transitions

### 2. Supervisor and Control
Coding jobs:
- supervisor agent
- delegation controller
- approval gate handler
- run ledger integration
- escalation policies
Review jobs:
- authority boundaries
- policy correctness
- escalation safety
Testing jobs:
- correct routing
- escalation on failure
- approval checkpoints
Debugging jobs:
- duplicate delegation
- dead-end routing
- stale policy decisions

### 3. Planning
Coding jobs:
- planner interfaces
- decomposition engine
- dependency graph builder
- acceptance criteria propagation
- replanning loop
Review jobs:
- decomposition quality
- dependency correctness
Testing jobs:
- under-decomposition
- over-decomposition
- circular dependencies
Debugging jobs:
- invalid work package structure
- planner loop instability

### 4. Tool Routing and Tool Layer
Coding jobs:
- tool descriptor schema
- registry
- router policy engine
- adapters for filesystem, shell, Python, git, HTTP, MCP
- result normalizer
Review jobs:
- permission boundaries
- adapter consistency
Testing jobs:
- correct tool selection
- schema mismatch handling
- fallback routing
Debugging jobs:
- wrong tool chosen
- unsafe mutation path

### 5. Protocol Layer
Coding jobs:
- MCP client abstractions
- A2A task envelope
- response envelope
- timeout / retry semantics
Testing jobs:
- envelope validation
- timeout behavior
Debugging jobs:
- broken delegation
- context transfer loss

### 6. Memory and Retrieval
Coding jobs:
- storage adapters
- retrieval APIs
- summarization pipeline
- provenance tracking
- invalidation logic
Testing jobs:
- retrieval relevance
- stale reads
- contradictory memory
Debugging jobs:
- polluted memory
- provenance gaps

### 7. Evaluation and Quality Gates
Coding jobs:
- evaluation engine
- rubric schemas
- verdict pipeline
- quality gate engine
Testing jobs:
- artifact scoring
- rule checks
- policy compliance
Debugging jobs:
- evaluator drift
- inconsistent scoring

### 8. Orchestration Pipelines
Coding jobs:
- graph model
- node scheduler
- checkpoint manager
- retry controller
- resumability engine
Testing jobs:
- graph execution
- retry behavior
- checkpoint recovery
Debugging jobs:
- deadlocks
- lost checkpoints

### 9. Artifact and Document Generation
Coding jobs:
- markdown artifact builder
- report formatter
- packaging routines
Testing jobs:
- artifact generation
- packaging correctness
Debugging jobs:
- missing files
- invalid archive structure

### 10. Observability and Debugging
Coding jobs:
- trace collector
- run ledger
- log schema
- replay utilities
Testing jobs:
- trace completeness
- replay stability
Debugging jobs:
- missing event chains
- non-reproducible failures

### 11. Configuration and Policy
Coding jobs:
- config schemas
- policy loader
- budget rules
- approval rule engine
Testing jobs:
- config validation
- policy enforcement
Debugging jobs:
- invalid precedence
- unsafe defaults

### 12. Test and Regression Harness
Coding jobs:
- test harness
- fixtures
- sample projects
- scenario runner
Testing jobs:
- unit tests
- subsystem tests
- end-to-end tests
- drift detection
Debugging jobs:
- flaky tests
- unstable fixtures

## Five example projects to test individual agents

### 1. Supervisor Routing Drill
Goal:
- validate supervisor delegation and escalation
Input:
- small product definition with three domains and one blocked task
Success criteria:
- correct worker assignment
- escalation triggered
- run ledger updated

### 2. Planner Task-Decomposition Drill
Goal:
- validate decomposition quality
Input:
- product definition for a small CLI tool with clear acceptance criteria
Success criteria:
- domain map created
- task graph created
- dependencies valid

### 3. Tool Router Capability Drill
Goal:
- validate tool selection and normalization
Input:
- five subtasks requiring filesystem, shell, Python, git, and HTTP access
Success criteria:
- correct tool selected per task
- normalized results returned
- unsafe tool path rejected

### 4. Memory Retrieval Drill
Goal:
- validate memory write, summarize, retrieve, and provenance
Input:
- short execution trace plus two artifacts and one conflicting update
Success criteria:
- relevant retrieval
- provenance preserved
- contradiction surfaced

### 5. Evaluation Rubric Drill
Goal:
- validate artifact scoring and quality gates
Input:
- one good artifact, one weak artifact, one policy-violating artifact
Success criteria:
- correct verdicts
- warnings generated
- reject path triggered for policy violation

## Five example projects to test the full system

### 1. Small Local CLI Product
Objective:
- build a local command-line utility from product definition to packaged artifact
Success criteria:
- working implementation plan
- generated artifacts
- quality gate pass

### 2. Documentation Generator
Objective:
- convert a technical source bundle into a handbook package
Success criteria:
- handbook produced
- appendix generated
- archive valid

### 3. Local Data Processing Utility
Objective:
- design and implement a small local ETL/data-normalization tool
Success criteria:
- implementation outline complete
- test plan present
- malformed cases caught

### 4. Multi-Domain Web-App Skeleton
Objective:
- produce architecture, module layout, and task graph for a small local-first web app
Success criteria:
- domains separated cleanly
- workboard generated
- critical interfaces identified

### 5. Regression and Failure-Recovery Simulation
Objective:
- simulate a partially failing workflow and observe the recovery path
Success criteria:
- failure isolated
- recovery path documented
- no silent failure

## Recommended next documents
1. implementation domain workboard
2. repository scaffold specification
3. schemas and contracts
4. tool permission matrix
5. evaluation rubric set
6. regression harness design
7. debugging handbook
8. CI workflow design
9. ADR set
