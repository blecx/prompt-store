# Implementation Workboard — Domain and Phase Backlog

## Purpose

This document converts the architecture into an implementation workboard that can be turned into issues, milestones, or sprint packages.

---

## Phase 1 — Foundations

### Runtime Core
- define execution context schema
- implement runtime kernel
- implement lifecycle states
- add unit tests

### Schemas
- define task envelope
- define plan graph
- define tool descriptor
- define tool result
- define evaluation verdict
- define memory record
- define A2A envelopes
- define artifact descriptor

### Configuration
- define config schema
- define runtime profile loader
- define policy loader

Exit criteria:
- schema package stable
- runtime bootable
- config validation passes

---

## Phase 2 — Core Agents

### Supervisor
- create supervisor skeleton
- add delegation interface
- add escalation hooks
- add approval gate stubs

### Planner
- create decomposition engine
- build plan graph creator
- add acceptance criteria propagation

### Tool Router
- create tool registry
- add capability matcher
- add permission engine
- add normalizer

Exit criteria:
- supervisor can assign
- planner can produce plan graph
- router can choose tool deterministically

---

## Phase 3 — Execution Subsystems

### Protocol Layer
- implement MCP client abstraction
- implement A2A envelopes
- implement dispatch flow
- implement timeout / retry handling

### Memory
- implement local storage adapters
- implement retrieval API
- implement provenance capture
- implement summarization pipeline

### Evaluation
- implement verdict engine
- implement rule checks
- implement quality gates

Exit criteria:
- protocol messages validated
- retrieval works
- verdict generation works

---

## Phase 4 — Orchestration

### Graph Engine
- implement graph model
- implement scheduler
- implement checkpoint manager
- implement retry controller
- implement resume flow

### Observability
- implement trace collector
- implement run ledger
- implement replay hooks

Exit criteria:
- graph can execute
- failures are visible
- checkpoints recover

---

## Phase 5 — Tools and Models

### Tools
- filesystem adapter
- shell adapter
- python executor
- git adapter
- HTTP adapter
- document generator
- MCP tool integration

### Models
- OpenAI backend for testing
- Higgins backend abstraction stub
- model selection layer

Exit criteria:
- tools callable through router
- testing backend operational
- production abstraction boundary present

---

## Phase 6 — Artifacts and Packaging

### Artifact generation
- markdown artifact builder
- report formatter
- package builder
- metadata stamping

### Packaging
- output inventory
- ZIP package builder
- artifact validation

Exit criteria:
- end-to-end artifacts generated
- package inventory valid

---

## Phase 7 — Validation and Regression

### Test harness
- unit test suites
- subsystem suites
- end-to-end scenarios
- regression baselines

### Example projects
- 5 single-agent scenarios
- 5 full-system scenarios

Exit criteria:
- deterministic runs
- baseline regression available
- scenario set documented

---

## Review lanes per phase

For each implementation item, maintain:
- build owner
- review owner
- test owner
- debug owner

This prevents incomplete “code only” delivery.