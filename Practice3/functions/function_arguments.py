#with one argument:
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

#with 2 arguments:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#Default Parameter Values
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")


def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Keyword Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog") #here we can see that the order does not matter

#The phrase Keyword Arguments is often shortened to kwargs in Python documentation.


#Positional Arguments:

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog") #the order matter in Positional arguments

#Mixing Positional and Keyword Arguments

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5) #positional arguments must come before kwargs


#Passing Different Data Types

#1.List
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

#2.Dict
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)


#return values:
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

#return List
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#return tuple
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

#Positional-Only Arguments
def my_function(name, /): #we add , /  |AFTER|
  print("Hello", name)

my_function("Emil")


#Keyword-Only Arguments
def my_function(*, name): #we add * ,  |BEFORE|
  print("Hello", name)

my_function(name = "Emil")


#Combining Positional-Only and Keyword-Only:

def my_function(a, b, /, *, c, d): #Arguments before / are positional-only, and arguments after * are keyword-only
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)

#my examples

def student_info(name, age, country="USA"):
    print("Name:", name)
    print("Age:", age)
    print("Country:", country)

student_info("Alex", 20)
student_info("Maria", 22, "Canada")


def order_product(product, quantity, price):
    total = quantity * price
    print("Product:", product)
    print("Quantity:", quantity)
    print("Total price:", total)

order_product(product="Laptop", quantity=2, price=900)
order_product(quantity=5, price=3, product="Notebook")

def print_scores(scores):
    for score in scores:
        print("Score:", score)

student_scores = [85, 90, 78, 92]
print_scores(student_scores)


def calculate_total(price, tax, /, *, discount):
    return price + tax - discount

total = calculate_total(100, 10, discount=5)
print("Final total:", total)
