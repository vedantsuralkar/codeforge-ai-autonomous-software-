
from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from agents.manager import ask_ai
from agents.planner import create_plan


# ==========================================
# WORKFLOW STATE
# ==========================================

class AgentState(TypedDict):

    user_request: str
    plan: str
    architecture: str
    code: str
    test_result: str
    debug_result: str
    documentation: str


# ==========================================
# 1. MANAGER AGENT
# ==========================================

def manager_node(state: AgentState):

    print("\n[MANAGER] Understanding requirements...")

    response = ask_ai(
        "Understand the following software requirements "
        "and summarize them clearly:\n"
        + state["user_request"]
    )

    return {
        "user_request": response
    }


# ==========================================
# 2. PLANNER AGENT
# ==========================================

def planner_node(state: AgentState):

    print("\n[PLANNER] Creating development plan...")

    plan = create_plan(state["user_request"])

    return {
        "plan": plan
    }


# ==========================================
# 3. ARCHITECT AGENT
# ==========================================

def architect_node(state: AgentState):

    print("\n[ARCHITECT] Designing architecture...")

    prompt = f"""
You are an expert software architect.

Requirements:
{state['user_request']}

Development Plan:
{state['plan']}

Create:
1. Project architecture
2. Folder structure
3. File responsibilities
4. Required technologies
5. Database design if required.
"""

    architecture = ask_ai(prompt)

    return {
        "architecture": architecture
    }


# ==========================================
# 4. DEVELOPER AGENT
# ==========================================

def developer_node(state: AgentState):

    print("\n[DEVELOPER] Generating code...")

    prompt = f"""
You are an expert Python developer.

Generate complete project code.

Requirements:
{state['user_request']}

Plan:
{state['plan']}

Architecture:
{state['architecture']}

Rules:
1. Generate working code.
2. Mention filename before every code file.
3. Include imports.
4. Follow proper coding standards.
5. Include requirements.txt.
6. Do not skip important files.
"""

    code = ask_ai(prompt)

    return {
        "code": code
    }


# ==========================================
# 5. TESTER AGENT
# ==========================================

def tester_node(state: AgentState):

    print("\n[TESTER] Testing generated code...")

    prompt = f"""
You are a software testing engineer.

Analyze this generated project:

{state['code']}

Check:
1. Syntax errors
2. Logical errors
3. Missing imports
4. Missing dependencies
5. Potential runtime errors

Provide a detailed testing report.
"""

    result = ask_ai(prompt)

    return {
        "test_result": result
    }


# ==========================================
# 6. DEBUGGER AGENT
# ==========================================

def debugger_node(state: AgentState):

    print("\n[DEBUGGER] Fixing detected issues...")

    prompt = f"""
You are an expert Python debugging engineer.

Generated Code:
{state['code']}

Testing Report:
{state['test_result']}

Analyze the errors and provide corrected code.

If no errors are found, preserve the original code.

Return complete corrected code with filenames.
"""

    result = ask_ai(prompt)

    return {
        "debug_result": result
    }


# ==========================================
# 7. DOCUMENTATION AGENT
# ==========================================

def documentation_node(state: AgentState):

    print("\n[DOCUMENTATION] Creating README...")

    prompt = f"""
You are a technical documentation engineer.

Create a professional README.md.

Project Requirements:
{state['user_request']}

Architecture:
{state['architecture']}

Final Code:
{state['debug_result']}

Include:
1. Project overview
2. Features
3. Technologies
4. Installation
5. Configuration
6. Execution instructions
7. Project structure
"""

    documentation = ask_ai(prompt)

    return {
        "documentation": documentation
    }


# ==========================================
# BUILD LANGGRAPH WORKFLOW
# ==========================================

def create_workflow():

    workflow = StateGraph(AgentState)

    # Register agents
    workflow.add_node("manager", manager_node)
    workflow.add_node("planner", planner_node)
    workflow.add_node("architect", architect_node)
    workflow.add_node("developer", developer_node)
    workflow.add_node("tester", tester_node)
    workflow.add_node("debugger", debugger_node)
    workflow.add_node("documentation", documentation_node)

    # Connect agents
    workflow.add_edge(START, "manager")
    workflow.add_edge("manager", "planner")
    workflow.add_edge("planner", "architect")
    workflow.add_edge("architect", "developer")
    workflow.add_edge("developer", "tester")
    workflow.add_edge("tester", "debugger")
    workflow.add_edge("debugger", "documentation")
    workflow.add_edge("documentation", END)

    # Compile graph
    return workflow.compile()


# ==========================================
# RUN WORKFLOW
# ==========================================

def run_workflow(user_request):

    app = create_workflow()

    initial_state = {
        "user_request": user_request,
        "plan": "",
        "architecture": "",
        "code": "",
        "test_result": "",
        "debug_result": "",
        "documentation": ""
    }

    result = app.invoke(initial_state)

    return result
