from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from config import GROQ_API_KEY, MODEL_NAME, TEMPERATURE, MAX_TOKENS


# 1. Initialize LLM
llm = ChatOpenAI(
    model=MODEL_NAME,
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
    temperature=TEMPERATURE,
    max_tokens=MAX_TOKENS
)


# 2. Planner Prompt
planner_prompt = ChatPromptTemplate.from_messages([

    ("system", """
    You are an expert Software Project Planner.

    Your job is to convert user requirements
    into clear and ordered development tasks.

    Follow these rules:
    1. Understand project requirements.
    2. Divide project into smaller tasks.
    3. Arrange tasks in correct order.
    4. Mention required technologies.
    5. Include testing and documentation.

    Return numbered tasks only.
    """),

    ("human", """
    Project Requirements:

    {requirements}

    Create a complete development plan.
    """)
])


# 3. Planner Chain
planner_chain = planner_prompt | llm | StrOutputParser()


# 4. Planner Function
def create_plan(requirements):

    plan = planner_chain.invoke({
        "requirements": requirements
    })

    return plan