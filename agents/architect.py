
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from config import API_KEY, MODEL_NAME


# ==========================================
# 1. INITIALIZE LLM
# ==========================================

llm = ChatOpenAI(
    model=MODEL_NAME,
    api_key=API_KEY,
    temperature=0
)


# ==========================================
# 2. ARCHITECT PROMPT
# ==========================================

architect_prompt = ChatPromptTemplate.from_messages([

    ("system", """
    You are an Expert Software Architect.

    Your responsibility is to design complete
    software project architecture.

    Analyze the given project requirements
    and create the following:

    1. Technology Stack
    2. Project Folder Structure
    3. File Responsibilities
    4. Database Design
    5. API Endpoints
    6. Application Workflow
    7. Security Considerations

    Follow clean architecture principles.

    Provide a professional and detailed design.
    """),

    ("human", """
    Project Requirements:

    {requirements}

    Development Plan:

    {plan}

    Design the complete software architecture.
    """)
])


# ==========================================
# 3. CREATE ARCHITECT CHAIN
# ==========================================

architect_chain = (
    architect_prompt
    | llm
    | StrOutputParser()
)


# ==========================================
# 4. ARCHITECT FUNCTION
# ==========================================

def design_architecture(requirements, plan):

    architecture = architect_chain.invoke({

        "requirements": requirements,

        "plan": plan

    })

    return architecture
