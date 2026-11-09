
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from config import GROQ_API_KEY, MODEL_NAME, TEMPERATURE, MAX_TOKENS


# 1. Initialize LLM
llm = ChatGroq(
    model=MODEL_NAME,
    api_key=GROQ_API_KEY,
    temperature=TEMPERATURE,
    max_tokens=MAX_TOKENS
)


# 2. Create system prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", """
    You are an Autonomous AI Software Engineer.

    Your responsibilities:
    1. Understand user requirements.
    2. Suggest software solutions.
    3. Break projects into smaller tasks.
    4. Generate clean Python code.
    5. Explain your decisions.

    Be accurate and professional.
    """),

    ("human", "{user_input}")
])


# 3. Create AI chain
chain = prompt | llm | StrOutputParser()


# 4. Manager function
def ask_ai(user_input):

    response = chain.invoke({
        "user_input": user_input
    })

    return response
