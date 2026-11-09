
import streamlit as st
import os
import sys

# ==========================================
# PROJECT PATH
# ==========================================

ROOT_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.insert(0, ROOT_DIR)


# ==========================================
# IMPORT WORKFLOW
# ==========================================

from workflow.graph import run_workflow


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="CodeForge AI",
    page_icon="🤖",
    layout="wide"
)


# ==========================================
# SESSION STATE
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ==========================================
# APPLICATION HEADER
# ==========================================

st.title("🤖 CodeForge AI")

st.caption(
    "Autonomous AI Software Development Platform "
    "| Powered by Groq + LangGraph"
)

st.divider()


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("⚙️ Settings")

    st.selectbox(
        "AI Model",
        ["openai/gpt-oss-120b"],
        disabled=True
    )

    st.info("Powered by Groq API")

    st.markdown("### AI Agents")

    agents = [
        "Manager Agent",
        "Planner Agent",
        "Architect Agent",
        "Developer Agent",
        "Tester Agent",
        "Debugger Agent",
        "Documentation Agent"
    ]

    for agent in agents:
        st.write("✓", agent)

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ==========================================
# USER REQUIREMENTS
# ==========================================

st.subheader("💻 Describe Your Software Requirement")

user_prompt = st.text_area(
    "Enter your project requirements:",
    placeholder=(
        "Example: Create a Student Management "
        "System using Python, Flask and MySQL..."
    ),
    height=160
)


# ==========================================
# GENERATE PROJECT
# ==========================================

if st.button(
    "🚀 Generate Project",
    type="primary",
    use_container_width=True
):

    if not user_prompt.strip():

        st.warning("Please enter your software requirement.")

    else:

        st.session_state.messages.append({
            "role": "user",
            "content": user_prompt
        })

        try:

            with st.spinner(
                "🤖 CodeForge AI agents are working..."
            ):

                # Execute complete LangGraph workflow
                result = run_workflow(user_prompt)

            st.success("Project generation completed!")

            st.divider()

            st.header("📁 Generated Project")

            # Display workflow outputs
            sections = {
                "plan": "📋 Development Plan",
                "architecture": "🏗️ Software Architecture",
                "code": "💻 Generated Code",
                "test_result": "🧪 Testing Report",
                "debug_result": "🐛 Debugged Code",
                "documentation": "📚 Documentation"
            }

            for key, title in sections.items():

                value = result.get(key, "")

                with st.expander(title, expanded=(key == "plan")):

                    if value:
                        st.markdown(value)
                    else:
                        st.info("No output generated.")

            st.session_state.messages.append({
                "role": "assistant",
                "content": "Project generation completed successfully."
            })

        except Exception as e:

            st.error(f"Project generation failed: {str(e)}")


# ==========================================
# CONVERSATION HISTORY
# ==========================================

st.divider()

st.subheader("💬 Conversation History")

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "CodeForge AI | Autonomous Software Engineering"
)
