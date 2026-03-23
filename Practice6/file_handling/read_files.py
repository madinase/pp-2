try:
    with open("sample.txt", "r") as f:
        content = f.read()
        print("--- Full File Content ---")
        print(content)

    with open("sample.txt", "r") as f:
        print("\n--- Line by Line ---")
        for i, line in enumerate(f, 1):
            print(f"Line {i}: {line.strip()}")
            
except FileNotFoundError:
    print("Error: 'sample.txt' not found. Please run write_files.py first.")