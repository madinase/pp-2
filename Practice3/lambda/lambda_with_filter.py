#The filter() function creates a list of items for which a function returns True

#Filter out even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8] 
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers)) 
print(odd_numbers)



# my examples
scores = [45, 78, 88, 52, 90, 33]
passed_students = list(filter(lambda x: x >= 60, scores))
print(passed_students)


words = ["apple", "banana", "kiwi", "strawberry", "pear"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(long_words)


numbers = [-10, 5, -3, 8, 0, 12]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print(positive_numbers)


ages = [12, 17, 18, 21, 15, 30]
adults = list(filter(lambda age: age >= 18, ages))
print(adults)





