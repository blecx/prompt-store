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

- Recommended Contest Strategy

For your agentic AI architecture handbook contest, the best workflow is:

- **Step 1:** Run slides through Template 1
    → extract structured knowledge.

    Prompt: prompt1-step3-orig-Merge Analysis into an Agentic AI System Architecture Developer Handbook.md

- **Step 2:** Run architecture slides through Template 2
    → produce deeper system architecture interpretation.
    Merge into an Architecture / Protocol / Evaluation Handbook. Paste this into a new chat after you provide the outputs from:

  - the ordered slide analysis
  - the architecture-focused slide analysis
    Prompt: prompt2-step3-orig-Merge into an Architecture-Protocol-Evaluation Handbook.md

    Multi-Agent Orchestration / Tool-Use Architecture. This template is designed for real agent framework design.

    Prompt: prompt2-step3-orig-Merge into an Architecture-Protocol-Evaluation Handbook.md
    Don't use prompt: promp2-step3.md

- **Step 3:** Merge both outputs into a unified handbook-grade document.
    Merge into a Multi-Agent Orchestration and Tool-Use Design Reference. Paste this into a new chat after you  provide the outputs from:

  - the prior slide analysis
  - the architecture-focused interpretation
  - the orchestration / planning / tool-use analysis

    Prompt: prompt3-step3-orig-Developer Handbook Synthesis for Agentic AI Systems.md

    Don't use Prompt: prompt2-step3.md

Merge both outputs into:

- Agentic AI System Architecture
- Developer Handbook
Prompt: prompt3-step3-orig-Developer Handbook Synthesis for Agentic AI Systems.md

Structure:

- Part I   Foundations
- Part II  Architecture Patterns
- Part III Protocols
- Part IV  Evaluation
- Part V   Safety & Operations

- Merge Analysis into an Agentic AI System Architecture Developer Handbook
  Use the prompt of the same name.

- Multi-Agent Orchestration / Tool-Use Architecture
   This template is designed for real agent framework design.This template is designed for real agent framework design.
  **Paste into a new chat**

Step 4 Implementation Blueprint Prompt.
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

## Step 5 — Repository Scaffold Generation

This step converts the Step-4 Implementation Blueprint into an actual project repository structure with starter Python code, schemas, and configuration.

The goal is that an engineer (or AI coding agent) can immediately start implementing the framework.

### Step 5 — Repository Scaffold Generation

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

If you want, I can also generate a third prompt template specialized for multi-agent orchestration, planning loops, and tool-use architectures (AutoGPT-style systems, supervisor agents, task planners, tool routers, etc.).
That one is extremely useful for designing real agent frameworks.

If you want, I can also generate a third prompt template specialized for multi-agent orchestration, planning loops, and tool-use architectures (AutoGPT-style systems, supervisor agents, task planners, tool routers, etc.).
That one is extremely useful for designing real agent frameworks.

- Step 5 — Comprehensive Prompt Agent Framework Repository Scaffold Generator
