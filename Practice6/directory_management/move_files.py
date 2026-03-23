import shutil
import os

source = "sample.txt"
destination_dir = "parent/child"
destination_path = os.path.join(destination_dir, "moved_sample.txt")

os.makedirs(destination_dir, exist_ok=True)


if os.path.exists(source):
    shutil.move(source, destination_path)
    print(f"File moved successfully to: {destination_path}")
else:
    print(f"Source file '{source}' not found.")

if os.path.exists(destination_path):
    print("Verification: File exists in the new location.")