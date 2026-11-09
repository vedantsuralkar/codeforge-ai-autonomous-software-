from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from config import API_KEY, MODEL_NAME


llm = ChatOpenAI(
    model=MODEL_NAME,
    api_key=API_KEY,
    temperature=0
)

tester_prompt = ChatPromptTemplate.from_messages([
    ("system", """
    You are an Expert Python Software Tester.

    Your responsibilities:
    1. Analyze the given Python code.
    2. Identify possible test scenarios.
    3. Generate pytest test cases.
    4. Include positive and negative test cases.
    5. Check edge cases.
    """),
    ("human", """
    Python Code:
    {code}

    Generate complete pytest test cases for this code.
    """)
])

tester_chain = tester_prompt | llm | StrOutputParser()


def generate_test_cases(code):
    return tester_chain.invoke({
        "code": code
    })