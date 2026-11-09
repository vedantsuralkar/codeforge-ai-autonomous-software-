
import subprocess
from pathlib import Path

from langchain_core.tools import tool


BASE_DIR = Path("sandbox").resolve()


# Only approved commands
ALLOWED_COMMANDS = {
    ("python", "--version"),
    ("pip", "--version"),
    ("git", "status"),
    ("git", "diff"),
    ("git", "log", "-5", "--oneline"),
    ("pytest", "--version")
}


@tool
def run_terminal_command(command: str) -> str:
    """Execute an approved terminal command inside sandbox."""

    try:
        parts = command.split()

        if tuple(parts) not in ALLOWED_COMMANDS:
            return "Error: Command is not allowed!"

        result = subprocess.run(
            parts,
            cwd=str(BASE_DIR),
            capture_output=True,
            text=True,
            timeout=10,
            shell=False
        )

        return (
            f"OUTPUT:\n{result.stdout}\n"
            f"ERROR:\n{result.stderr}\n"
            f"RETURN CODE: {result.returncode}"
        )

    except subprocess.TimeoutExpired:
        return "Terminal command timed out!"

    except Exception as e:
        return f"Terminal error: {str(e)}"


terminal_tools = [
    run_terminal_command
]
