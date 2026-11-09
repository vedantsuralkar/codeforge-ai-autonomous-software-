from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from config import API_KEY, MODEL_NAME


llm = ChatOpenAI(
    model=MODEL_NAME,
    api_key=API_KEY,
    temperature=0
)

documentation_prompt = ChatPromptTemplate.from_messages([
    ("system", """
    You are an Expert Technical Documentation Writer.

    Your responsibilities:
    1. Generate README.md.
    2. Explain project features.
    3. Provide installation instructions.
    4. Explain project folder structure.
    5. Provide execution instructions.
    6. Document API endpoints if available.
    """),
    ("human", """
    Project Requirements:
    {requirements}

    Project Architecture:
    {architecture}

    Generate complete project documentation in Markdown.
    """)
])

documentation_chain = (
    documentation_prompt | llm | StrOutputParser()
)


def generate_documentation(requirements, architecture):
    return documentation_chain.invoke({
        "requirements": requirements,
        "architecture": architecture
    })