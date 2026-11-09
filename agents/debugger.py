from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from config import API_KEY, MODEL_NAME


llm = ChatOpenAI(
    model=MODEL_NAME,
    api_key=API_KEY,
    temperature=0
)

debugger_prompt = ChatPromptTemplate.from_messages([
    ("system", """
    You are an Expert Python Debugger.

    Your responsibilities:
    1. Analyze Python code.
    2. Identify syntax and logical errors.
    3. Explain the root cause.
    4. Provide corrected code.
    5. Suggest improvements.
    """),
    ("human", """
    Python Code:
    {code}

    Error Message:
    {error}

    Debug this code and provide the corrected version.
    """)
])

debugger_chain = debugger_prompt | llm | StrOutputParser()


def debug_code(code, error):
    return debugger_chain.invoke({
        "code": code,
        "error": error
    })