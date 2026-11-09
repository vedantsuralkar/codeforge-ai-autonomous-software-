
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

    print("\n[MANAGER] Understanding user request...")

    response = ask_ai(
        "Understand this software development request "
        "and summarize the requirements:\n"
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
    Design software architecture.

    Requirements:
    {state['user_request']}

    Development Plan:
    {state['plan']}

    Provide folder structure and file responsibilities.
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
    Generate Python project code.

    Requirements:
    {state['user_request']}

    Plan:
    {state['plan']}

    Architecture:
    {state['architecture']}

    Provide complete code with filenames.
    """

    code = ask_ai(prompt)

    return {
        "code": code
    }


# ==========================================
# 5. TESTER AGENT
# ==========================================

def tester_node(state: AgentState):

    print("\n[TESTER] Checking generated code...")

    prompt = f"""
    Analyze the generated code.

    Code:
    {state['code']}

    Identify syntax errors and potential bugs.
    """

    result = ask_ai(prompt)

    return {
        "test_result": result
    }


# ==========================================
# 6. DEBUGGER AGENT
# ==========================================

def debugger_node(state: AgentState):

    print("\n[DEBUGGER] Analyzing errors...")

    prompt = f"""
    Fix the problems found by the Tester.

    Generated Code:
    {state['code']}

    Test Results:
    {state['test_result']}

    Return corrected code.
    """

    result = ask_ai(prompt)

    return {
        "debug_result": result
    }


# ==========================================
# 7. DOCUMENTATION AGENT
# ==========================================

def documentation_node(state: AgentState):

    print("\n[DOCUMENTATION] Creating documentation...")

    prompt = f"""
    Create README documentation for this project.

    Requirements:
    {state['user_request']}

    Architecture:
    {state['architecture']}

    Code:
    {state['debug_result']}
    """

    documentation = ask_ai(prompt)

    return {
        "documentation": documentation
    }


# ==========================================
# BUILD LANGGRAPH WORKFLOW
# ==========================================

workflow = StateGraph(AgentState)

workflow.add_node("manager", manager_node)
workflow.add_node("planner", planner_node)
workflow.add_node("architect", architect_node)
workflow.add_node("developer", developer_node)
workflow.add_node("tester", tester_node)
workflow.add_node("debugger", debugger_node)
workflow.add_node("documentation", documentation_node)


# ==========================================
# CONNECT AGENTS
# ==========================================

workflow.add_edge(START, "manager")

workflow.add_edge("manager", "planner")

workflow.add_edge("planner", "architect")

workflow.add_edge("architect", "developer")

workflow.add_edge("developer", "tester")

workflow.add_edge("tester", "debugger")

workflow.add_edge("debugger", "documentation")

workflow.add_edge("documentation", END)


# ==========================================
# COMPILE GRAPH
# ==========================================

app = workflow.compile()


# ==========================================
# RUN WORKFLOW
# ==========================================

def run_workflow(user_request):

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
