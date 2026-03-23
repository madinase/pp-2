names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

val = "100"
if isinstance(val, str):
    num = int(val)
    print(f"Converted {type(val)} to {type(num)}")