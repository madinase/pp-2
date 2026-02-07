fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
  print(x)


for x in range(2, 6):
  print(x)


for x in range(2, 30, 3):
  print(x)


for x in range(6):
  print(x)
else:
  print("Finally finished!")



for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")



adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


for x in [0, 1, 2]:
  pass


#my examples

numbers = [1, 2, 3, 4, 5]

for n in numbers:
    print(n)

colors = ["red", "green", "blue"]

for color in colors:
    if color == "green":
        break
    print(color)

animals = ["cat", "dog", "bird"]

for animal in animals:
    if animal == "dog":
        continue
    print(animal)


for i in range(1, 6):
    print(i)


sizes = ["small", "medium"]
items = ["shirt", "jacket"]

for size in sizes:
    for item in items:
        print(size, item)







