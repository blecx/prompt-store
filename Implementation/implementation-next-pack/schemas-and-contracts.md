# Schemas and Contracts Specification

## Purpose

This document defines the primary schema layer for the local-first Python multi-agent framework.

Recommended implementation style:
- Pydantic v2 models
- explicit enums
- strict typing
- immutable IDs
- schema version fields where needed

---

## Core Design Rules

- every transportable object must have an ID
- every persisted object must include provenance metadata
- every protocol envelope must include status and error fields
- tool results must distinguish raw payload, normalized payload, and execution metadata
- plan nodes must be independently addressable
- evaluation verdicts must carry evidence references

---

## Task Envelope

```python
class TaskEnvelope(BaseModel):
    task_id: str
    parent_task_id: str | None = None
    domain: str
    subdomain: str | None = None
    title: str
    objective: str
    acceptance_criteria: list[str]
    constraints: list[str] = []
    priority: Literal["low", "medium", "high", "critical"]
    status: Literal["new", "assigned", "running", "blocked", "done", "failed"]
    assigned_agent_role: str | None = None
    tool_hints: list[str] = []
    context_refs: list[str] = []
```

Purpose:
- canonical work package
- routing target
- orchestration node input

---

## Plan Graph

```python
class PlanNode(BaseModel):
    node_id: str
    task_id: str
    title: str
    depends_on: list[str] = []
    execution_mode: Literal["sequential", "parallel"]
    expected_artifacts: list[str] = []
    risk_flags: list[str] = []
    owner_role: str

class PlanGraph(BaseModel):
    plan_id: str
    root_objective: str
    nodes: list[PlanNode]
    assumptions: list[str] = []
    stop_conditions: list[str] = []
```

Purpose:
- explicit execution graph
- orchestration input
- dependency validation

---

## Tool Descriptor

```python
class ToolDescriptor(BaseModel):
    tool_name: str
    category: str
    description: str
    input_schema_ref: str
    output_schema_ref: str
    is_mutating: bool
    permission_level: Literal["safe", "guarded", "restricted"]
    supported_domains: list[str]
    timeout_seconds: int
    local_only: bool = True
```

Purpose:
- registry entry
- router matching input
- permission matrix source

---

## Tool Invocation and Result

```python
class ToolInvocation(BaseModel):
    invocation_id: str
    tool_name: str
    task_id: str
    arguments: dict
    caller_role: str
    requested_at: datetime

class ToolExecutionMetadata(BaseModel):
    duration_ms: int
    exit_status: str
    stderr_excerpt: str | None = None
    warnings: list[str] = []

class ToolResult(BaseModel):
    invocation_id: str
    tool_name: str
    raw_payload: dict | str | list | None = None
    normalized_payload: dict
    metadata: ToolExecutionMetadata
    provenance_ref: str | None = None
```

Purpose:
- traceable tool execution
- normalized routing output
- debugging evidence

---

## Memory Record

```python
class MemoryRecord(BaseModel):
    record_id: str
    memory_class: Literal["working", "session", "long_term", "retrieval", "artifact", "decision"]
    title: str
    content: str
    tags: list[str] = []
    source_refs: list[str] = []
    supersedes: list[str] = []
    created_at: datetime
```

Purpose:
- portable storage record
- provenance-aware retrieval unit

---

## Retrieval Query and Result

```python
class RetrievalQuery(BaseModel):
    query_id: str
    requester_role: str
    question: str
    scope: list[str] = []
    top_k: int = 5

class RetrievalHit(BaseModel):
    record_id: str
    relevance_score: float
    snippet: str
    provenance_ref: str | None = None

class RetrievalResult(BaseModel):
    query_id: str
    hits: list[RetrievalHit]
```

Purpose:
- deterministic retrieval interface
- context hydration input

---

## Evaluation Verdict

```python
class EvaluationScore(BaseModel):
    metric_name: str
    value: float
    rationale: str | None = None

class EvaluationVerdict(BaseModel):
    verdict_id: str
    subject_ref: str
    layer: Literal["model", "plan", "tool_execution", "artifact", "pipeline", "application"]
    decision: Literal["accept", "accept_with_warnings", "revise", "replan", "escalate", "reject"]
    scores: list[EvaluationScore]
    warnings: list[str] = []
    evidence_refs: list[str] = []
```

Purpose:
- quality gate output
- regression evidence
- escalation trigger

---

## A2A Task Handoff

```python
class A2ATaskEnvelope(BaseModel):
    message_id: str
    sender_role: str
    receiver_role: str
    task: TaskEnvelope
    attached_context_refs: list[str] = []
    deadline_hint: str | None = None
    retry_count: int = 0
```

Purpose:
- cross-agent delegation
- reproducible inter-agent handoff

---

## A2A Response

```python
class A2AResponseEnvelope(BaseModel):
    message_id: str
    task_id: str
    responder_role: str
    status: Literal["accepted", "rejected", "running", "completed", "failed", "blocked"]
    artifact_refs: list[str] = []
    error_message: str | None = None
    evaluation_ref: str | None = None
```

Purpose:
- stateful delegation response
- orchestration status feedback

---

## MCP Resource Descriptor

```python
class MCPResourceDescriptor(BaseModel):
    resource_name: str
    resource_type: str
    description: str
    operations: list[str]
    auth_mode: str | None = None
    local_endpoint_hint: str | None = None
```

Purpose:
- MCP capability registry entry
- discovery metadata

---

## Artifact Descriptor

```python
class ArtifactDescriptor(BaseModel):
    artifact_id: str
    artifact_type: str
    title: str
    path: str
    generator_role: str
    related_task_ids: list[str]
    created_at: datetime
```

Purpose:
- packaging metadata
- output inventory
- evaluation subject reference