#The map() function applies a function to every item in an iterable:

#Double all numbers in a list:
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled) 


# my examples
prices = [10, 25, 50, 100]
dollar_prices = list(map(lambda x: "$" + str(x), prices))
print(dollar_prices)


celsius = [0, 20, 30, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)


words = ["apple", "banana", "kiwi", "cherry"]
word_lengths = list(map(lambda word: len(word), words))
print(word_lengths)


scores = [60, 75, 82, 90]
updated_scores = list(map(lambda score: score + 5, scores))
print(updated_scores)


























