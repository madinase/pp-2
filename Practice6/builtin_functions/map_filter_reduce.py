from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
total_sum = reduce(lambda x, y: x + y, numbers)

print(f"Squared: {squared}\nEvens: {evens}\nTotal Sum: {total_sum}")