#The sorted() function can use a lambda as a key for custom sorting:

#Sort a list of tuples by the second element:
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)


#Sort strings by length:
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)


# my examples
products = [("Laptop", 1200), ("Phone", 800), ("Tablet", 600)]
sorted_products = sorted(products, key=lambda x: x[1])
print(sorted_products)


numbers = [-10, 5, -3, 8, -2]
sorted_numbers = sorted(numbers, key=lambda x: abs(x))
print(sorted_numbers)


students = [("John", 20), ("Anna", 22), ("Mike", 19)]
sorted_by_name = sorted(students, key=lambda x: x[0])
print(sorted_by_name)



words = ["apple", "banana", "kiwi", "cherry"]
sorted_by_last_letter = sorted(words, key=lambda word: word[-1])
print(sorted_by_last_letter)





