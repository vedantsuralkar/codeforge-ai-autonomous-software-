
import subprocess
from pathlib import Path

from langchain_core.tools import tool


BASE_DIR = Path("sandbox").resolve()


def run_git(args):

    result = subprocess.run(
        ["git"] + args,
        cwd=str(BASE_DIR),
        capture_output=True,
        text=True,
        timeout=15,
        shell=False
    )

    if result.returncode != 0:
        return f"Git Error:\n{result.stderr}"

    return result.stdout or "Git operation successful!"


@tool
def git_init() -> str:
    """Initialize a Git repository inside sandbox."""

    return run_git(["init"])


@tool
def git_status() -> str:
    """Check Git repository status."""

    return run_git(["status"])


@tool
def git_add_all() -> str:
    """Stage all changes in the sandbox Git repository."""

    return run_git(["add", "--all"])


@tool
def git_commit(message: str) -> str:
    """Commit staged changes with the provided message."""

    if not message.strip():
        return "Error: Commit message cannot be empty!"

    return run_git(["commit", "-m", message])


@tool
def git_log() -> str:
    """Display the last five Git commits."""

    return run_git(["log", "-5", "--oneline"])


git_tools = [
    git_init,
    git_status,
    git_add_all,
    git_commit,
    git_log
]
