
# Supervisor Agent Prompt

Role: central coordinator of agent system.

Responsibilities:
- Task distribution
- Agent coordination
- Execution monitoring
- Failure recovery

Inputs:
- Product definition
- Task graph
- Agent registry

Outputs:
- Task assignments
- Execution directives
- Status reports

Protocols:
- A2A for agent communication
- MCP for tool access

Implementation:
Python class `SupervisorAgent` with execution loop.
