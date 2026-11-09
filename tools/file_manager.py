
from tools.file_manager import *

# Create file
create_file("demo.py", "print('Hello AI')")

# Read file
print(read_file("demo.py"))

# Edit file
edit_file(
    "demo.py",
    "Hello AI",
    "Hello Developer"
)

# List files
list_files()
