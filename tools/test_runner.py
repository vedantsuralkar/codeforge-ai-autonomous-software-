
import subprocess
import sys
from pathlib import Path

from langchain_core.tools import tool


BASE_DIR = Path("sandbox").resolve()


@tool
def run_pytest(test_path: str = ".") -> str:
    """Run pytest on a file or directory inside sandbox."""

    try:
        full_path = (BASE_DIR / test_path).resolve()

        if not full_path.is_relative_to(BASE_DIR):
            return "Error: Invalid test path!"

        if not full_path.exists():
            return "Error: Test path not found!"

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "pytest",
                str(full_path),
                "-v"
            ],
            cwd=str(BASE_DIR),
            capture_output=True,
            text=True,
            timeout=30,
            shell=False
        )

        return (
            f"TEST OUTPUT:\n{result.stdout}\n"
            f"TEST ERRORS:\n{result.stderr}\n"
            f"RETURN CODE: {result.returncode}"
        )

    except subprocess.TimeoutExpired:
        return "Testing stopped: Time limit exceeded!"

    except Exception as e:
        return f"Testing error: {str(e)}"


test_runner_tools = [
    run_pytest
]
