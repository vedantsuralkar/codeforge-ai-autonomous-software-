
import subprocess
import tempfile
import os
import sys


class ExecutionEnvironment:

    def __init__(self, timeout=10):
        self.timeout = timeout

    def execute_code(self, code):

        temp_dir = None

        try:
            # Create temporary directory
            temp_dir = tempfile.mkdtemp(
                prefix="ai_sandbox_"
            )

            # Create Python file
            file_path = os.path.join(
                temp_dir,
                "main.py"
            )

            with open(file_path, "w", encoding="utf-8") as file:
                file.write(code)

            # Execute Python code
            result = subprocess.run(
                [sys.executable, file_path],
                capture_output=True,
                text=True,
                timeout=self.timeout,
                cwd=temp_dir
            )

            return {
                "success": result.returncode == 0,
                "output": result.stdout,
                "error": result.stderr,
                "return_code": result.returncode
            }

        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "output": "",
                "error": "Execution Timeout",
                "return_code": None
            }

        except Exception as e:
            return {
                "success": False,
                "output": "",
                "error": str(e),
                "return_code": None
            }

        finally:
            if temp_dir and os.path.exists(temp_dir):
                import shutil
                shutil.rmtree(temp_dir, ignore_errors=True)
