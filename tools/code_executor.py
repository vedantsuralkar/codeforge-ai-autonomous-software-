
import os
import sys
import subprocess
from pathlib import Path

from langchain_core.tools import tool


BASE_DIR = Path("sandbox").resolve()


def get_safe_path(file_path):
    """Validate file path inside sandbox."""

    full_path = (BASE_DIR / file_path).resolve()

    if not full_path.is_relative_to(BASE_DIR):
        raise ValueError("Access outside sandbox is not allowed!")

    return full_path


@tool
def execute_python_code(file_path: str) -> str:
    """Execute a Python file inside the sandbox and return output."""

    try:
        full_path = get_safe_path(file_path)

        if not full_path.is_file():
            return "Error: Python file not found!"

        if full_path.suffix != ".py":
            return "Error: Only Python files are allowed!"

        result = subprocess.run(
            [sys.executable, str(full_path)],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=str(BASE_DIR)
        )

        return (
            f"OUTPUT:\n{result.stdout}\n"
            f"ERROR:\n{result.stderr}\n"
            f"RETURN CODE: {result.returncode}"
        )

    except subprocess.TimeoutExpired:
        return "Execution stopped: Time limit exceeded!"

    except Exception as e:
        return f"Execution error: {str(e)}"


@tool
def check_python_version() -> str:
    """Check installed Python version."""

    result = subprocess.run(
        [sys.executable, "--version"],
        capture_output=True,
        text=True,
        timeout=5
    )

    return result.stdout.strip() or result.stderr.strip()


code_executor_tools = [
    execute_python_code,
    check_python_version
]
