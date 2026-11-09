
from tools.file_manager import file_manager_tools

from tools.code_executor import code_executor_tools

from tools.terminal import terminal_tools

from tools.git_tools import git_tools

from tools.test_runner import test_runner_tools


ALL_TOOLS = (
    file_manager_tools
    + code_executor_tools
    + terminal_tools
    + git_tools
    + test_runner_tools
)
