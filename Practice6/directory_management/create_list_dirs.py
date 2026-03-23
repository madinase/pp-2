import os

os.makedirs("parent/child/grandchild", exist_ok=True)

print("Items in directory:", os.listdir("."))

py_files = [f for f in os.listdir(".") if f.endswith(".py")]
print("Python files found:", py_files)