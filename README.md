# prompt-store

This is not a serious project repository; it is mainly a collection of unsorted prompt snippets and working notes.

## techPicturesToStory

Below is a ready-to-use master prompt for a new chat. It is designed to reproduce the same style, structure, ordering discipline, level of detail, and output formatting you requested, while being stronger and more precise for multi-agent, multi-model, agentic AI architecture and developer-handbook work.

### developer handbook

You can paste the promts in the directory directly into a new chat and then attach the image set. Find here the guidiance how to use them

- Master Prompt Template for Slide-Series Analysis and Handbook-Grade Output
  Prompt: Master Prompt Template for Slide-Series Analysis.md

- Recommended Use Pattern
  For your test runs with two picture sets, I recommend this operating pattern:

  - Variant A — Analysis-only run
    Use the prompt exactly as above and attach the pictures.

  - Variant B — Analysis + artifact generation
    Add this suffix after the master prompt if you want direct file output
    - Stronger Competition Version
      If you want the prompt to push even harder toward architecture-handbook quality, use this version header before the master prompt

    - Optional Extension for Multi-Agent / Multi-Model Architecture Work

      Prompt: Optional Extension for Multi-Agent-Multi-Model Architecture Work.md

      If you want the next chat to generalize the slide content toward multi-agent, multi-model system design, append this block

      Why this prompt is better than a simple "analyze the slides" prompt

      - This version is stronger because it explicitly controls:
      - Ordering logic
      - Evidence discipline
      - Chapter schema
      - Engineering vocabulary
      - Non-hallucination behavior
      - Appendix discipline
      - Handbook-grade style
      - Developer relevance
      - Multi-agent architectural reuse

    That is the correct level of rigor for your contest use case.

    - Practical Short Version
      If you need a shorter reusable template, use this compressed form

### prompt template specialized for architecture diagrams, protocol slides, and agent evaluation slides

 Below is a second specialized prompt template designed specifically for architecture diagrams, protocol slides, evaluation frameworks, and systems engineering content. All prompts are located in the Architecture directory

 Prompt: Prompt Template--Architecture-Protocol-Evaluation Slide Analysis.md

This template is stricter and more technical than the previous one and is optimized for:

- AI system architecture documentation
- Multi-agent system design
- Protocol and interface diagrams
- Evaluation frameworks
- Agent orchestration patterns
- Developer handbooks

It forces the LLM to interpret diagrams like a systems architect, not a summarizer.

- Prompt Template — Architecture / Protocol / evaluation Slide Analysis
    a second specialized prompt template designed specifically for architecture diagrams, protocol slides, evaluation frameworks, and systems engineering content.

    This template is stricter and more technical than the previous one and is optimized for:

  - AI system architecture documentation
  - Multi-agent system design
  - Protocol and interface diagrams
  - Evaluation frameworks
  - Agent orchestration patterns
  - Developer handbooks

    It forces the LLM to interpret diagrams like a systems architect, not a summarizer.
  - When to Use This Template
      Use this second prompt when the slides contain:

      | Slide Type                | Template Strength |
      | ----------------------- | ----------------- |
      | Architecture diagrams     | ⭐⭐⭐⭐⭐             |
      | Agent orchestration       | ⭐⭐⭐⭐⭐             |
      | Protocol diagrams         | ⭐⭐⭐⭐⭐             |
      | Evaluation frameworks     | ⭐⭐⭐⭐              |
      | Agent safety / governance | ⭐⭐⭐⭐              |
      | Concept slides            | ⭐⭐⭐               |

    Your first template is better for mixed educational slides.

    This second template is stronger for system design diagrams.

### Recommended Contest Strategy

For your agentic AI architecture handbook contest, the best workflow is:

| Step | Action | Output |
|------|--------|--------|
| **1** | Run slides through Template 1 → extract structured knowledge | Structured knowledge extraction |
| **2** | Run architecture slides through Template 2 → produce deeper system architecture interpretation | Deeper system architecture interpretation |
| **3** | Merge both outputs into unified handbook | • Agentic AI System Architecture<br/>• Developer Handbook<br/>• Part I: Foundations<br/>• Part II: Architecture Patterns<br/>• Part III: Protocols<br/>• Part IV: Evaluation <br/>• Part V   Safety & Operations|

 Execution of the steps:

- **Step 1:**

    Prompt: prompt1-step3-orig-Merge Analysis into an Agentic AI System Architecture Developer Handbook.md

- **Step 2:**
    Prompt: "prompt2-step3-orig-Merge into an Architecture-Protocol-Evaluation Handbook.md"
    Don't use prompt: promp2-step3.md

  - Why these two prompts work well?

      They produce three layers of documentation:

      | Step | Output |
      | --- | --- |
      | Step 1 | Slide knowledge extraction |
      | Step 2 | Architecture interpretation |
      | Step 3 | Developer handbook synthesis |

Then Prompt 3 generates implementation architecture.

- **Step 3:** Merge both outputs into a unified handbook-grade document.
    Merge into a Multi-Agent Orchestration and Tool-Use Design Reference. Paste this into a new chat after you  provide the outputs from:

      - the prior slide analysis
      - the architecture-focused interpretation
      - the orchestration / planning / tool-use analysis

    Below are two prompts you can paste directly into a new chat.

    1️⃣ Step-3 Prompt (Merge + Handbook Generation)
    2️⃣ Third Prompt Template (Multi-Agent Orchestration & Tool-Use Architectures)

    *They are designed for serious architecture documentation, not casual summaries.*

  - **Prompt 1** Merge Analysis into an Agentic AI System Architecture Developer Handbook

    **Paste this into a new chat.** Prompt: step3-prompt1-Merge into a Multi-Agent Orchestration and Tool-Use Design Reference.md

  - **Prompt 2** Multi-Agent Orchestration / Tool-Use Architecture
       This template is designed for **real agent framework design**.T

      **Paste into a new chat**  Prompt: step3-prompt2-Multi-Agent Orchestration-Tool-Use Architecture.md

  - **Prompt 3** generates **implementation architecture**.
    (still searching prompt)

  - **Prompt 4** Agent Framework Blueprint Prompt
    It produces things like:

    - Supervisor agents
    - Planning agents
    - Tool routers
    - Evaluation agents
    - Memory agents
    - Orchestration pipelines

    Essentially a complete AI-agent framework design.

    That one is extremely powerful for your Agentic AI System Architecture contest.

    Archive That includes all. The content is:
The archive has been recreated successfully.

You can download it here:

**[Download the ZIP archive](techPicturesToStory/ArchiveStep4/agent_framework_prompt_pack_v2.zip)**

In the project you find it in directory "agent_framework_prompt_pack"

#### Contents of the archive

```code
agent_framework_prompt_pack/
│
├─ prompt_3_implementation_architecture.md
├─ agent_framework_blueprint_prompt.md
├─ supervisor_agents_prompt.md
├─ planning_agents_prompt.md
├─ tool_router_agents_prompt.md
├─ evaluation_agents_prompt.md
├─ memory_agents_prompt.md
├─ orchestration_pipelines_prompt.md
└─ README_prompt_usage_guide.md
```

#### What the package includes

1. **Prompt 3 – Implementation Architecture**
  Prompt: prompt_3_implementation_architecture.md
   - Generates the full **Python multi-agent framework architecture specification**

2. **Agent Framework Blueprint Prompt**
   Prompt: agent_framework_blueprint_prompt.md
   - Produces the **complete framework design**

3. **Specialized Agent Prompts**
   Prompt: follow the prompts in the archive containing the string in the name
   - Supervisor agents
   - Planning agents
   - Tool router agents
   - Memory agents
   - Evaluation agents
   - Orchestration pipelines

4. **Usage Guide**

   - Explains how to run prompts **step-by-step**
   - Lists the **required context for each stage**
   - Shows the **recommended order of prompts**

#### Workflow this package supports

```code
Slide / Source Analysis
        ↓
Implementation Architecture
        ↓
Framework Blueprint
        ↓
Supervisor Agents
        ↓
Planning Agents
        ↓
Tool Router Agents
        ↓
Memory Agents
        ↓
Evaluation Agents
        ↓
Orchestration Pipelines
```

##### Result

Running this chain produces a full **Agentic AI System Architecture and Developer Handbook**, including:

- local-first Python agent framework
- domain-driven agent decomposition
- MCP and A2A protocol integration
- supervisor orchestration
- tool routing layer
- evaluation system
- memory subsystem
- orchestration runtime

---

If you want, I can also generate a **visual architecture diagram of this framework (agent layers + pipelines + protocols)** that fits directly into your **AI-Agent Framework repository documentation**.

======

- **Step 4** Python Implementation Blueprint for an Agent Framework.
You can paste it directly into a new chat after you have the Step 3 Developer Handbook Synthesis output.

This prompt is designed to turn the handbook into a real implementation-oriented Python architecture specification for a local-first, multi-agent, multi-model agent framework.

Prompt: prompt1-step4.md

After running Step 4, the next useful derivations are usually:

    - Python package skeleton
    - dataclass / Pydantic schemas
    - base agent classes
    - orchestration runtime
    - MCP tool adapter layer
    - A2A message contracts
    - evaluation pipeline
    - local test harness

### restoring the state of step 4

Primary restore entry inside the archive:

- `step4-stage-archive/00_START_HERE.md`
- `step4-stage-archive/context/RESTORE_CONTEXT_PROMPT.md`
- `step4-stage-archive/artifacts/Python_Agent_Framework_Implementation_Blueprint.md`

Archive is found in state-step4 directory. So you can take a fresh chat and load that state of step4. And then continue with step 5. This avoids to run every time through the whole process when dsigining a new agentic system!

- **Step 5** — Repository Scaffold Generation

This step converts the Step-4 Implementation Blueprint into an actual project repository structure with starter Python code, schemas, and configuration.

The goal is that an engineer (or AI coding agent) can immediately start implementing the framework.

- Step 5 — Repository Scaffold Generation

     This step converts the Step-4 Implementation Blueprint into an actual project repository structure with starter Python code, schemas, and configuration.
     The goal is that an engineer (or AI coding agent) can immediately start implementing the framework.

     This step produces:
      - Repository structure
      - Python module skeletons
      - Base agent classes
      - Protocol interfaces
      - Orchestration runtime
      - Tool registry
      - Memory system
      - Evaluation framework
      - Configuration system
      - Testing scaffolding

  - Step 5 — Comprehensive Prompt Agent Framework Repository Scaffold Generator
