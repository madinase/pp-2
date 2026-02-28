#Generator that generates squares up to N
def square_generator(n):
    for i in range(n + 1):
        yield i * i

n = 5
for value in square_generator(n):
    print(value)


#Print even numbers between 0 and n (comma-separated)
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
print(",".join(str(num) for num in even_numbers(n)))


#a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = 50
for num in divisible_by_3_and_4(n):
    print(num)

# to yield the square of all numbers from (a) to (b)
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

for value in squares(3, 7):
    print(value)


#a generator that returns all numbers from (n) down to 0.
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

for number in countdown(5):
    print(number)