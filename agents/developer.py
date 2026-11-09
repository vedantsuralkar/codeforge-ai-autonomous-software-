
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
# 2. DEVELOPER PROMPT
# ==========================================

developer_prompt = ChatPromptTemplate.from_messages([

    ("system", """
    You are an Expert Python Software Developer.

    Your responsibility is to generate clean,
    modular and functional software code.

    Follow these rules:

    1. Follow the given software architecture.
    2. Generate code file by file.
    3. Use proper Python naming conventions.
    4. Add error handling.
    5. Add comments where necessary.
    6. Follow PEP 8 guidelines.
    7. Include necessary imports.
    8. Avoid incomplete code.
    9. Do not use unnecessary dependencies.

    Return code with clear filename headings.
    Use Python code blocks for Python files.
    """),

    ("human", """
    Project Requirements:

    {requirements}

    Software Architecture:

    {architecture}

    Generate the project source code.
    """)
])


# ==========================================
# 3. CREATE DEVELOPER CHAIN
# ==========================================

developer_chain = (
    developer_prompt
    | llm
    | StrOutputParser()
)


# ==========================================
# 4. DEVELOPER FUNCTION
# ==========================================

def generate_code(requirements, architecture):

    code = developer_chain.invoke({

        "requirements": requirements,

        "architecture": architecture

    })

    return code
