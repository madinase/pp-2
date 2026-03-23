with open("sample.txt", "w") as f:
    f.write("Line 1: Initial data\nLine 2: Python is fun.")

with open("sample.txt", "a") as f:
    f.write("\nLine 3: This is an appended line.")

with open("sample.txt", "r") as f:
    print("--- File Content ---")
    print(f.read())