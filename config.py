import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

load_dotenv(os.path.join(BASE_DIR, ".env"))

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = "openai/gpt-oss-120b"

TEMPERATURE = 0.2
MAX_TOKENS = 2000

PROJECT_NAME = "CodeForge AI"

MAX_RETRIES = 3

GENERATED_PROJECTS_DIR = "generated_projects"
SANDBOX_DIR = "sandbox"

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Check your .env file!")