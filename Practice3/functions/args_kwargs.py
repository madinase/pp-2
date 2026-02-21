#*args and **kwargs allow functions to accept a unknown number of arguments.

#Arbitrary Arguments - *args | tuple
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")


def my_function(greeting, *names): #regular arguments with *args
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")


def my_function(*numbers): #calculates the sum of any number of values
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))


def my_function(*numbers): #finding maximum value
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1))


#Arbitrary Keyword Arguments - **kwargs | dictionary
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")


def my_function(username, **details): #**kwargs with Regular Arguments
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")


#1.regular parameters 2.*args 3.**kwargs
def my_function(title, *args, **kwargs): #Combining *args and **kwargs
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")


#Unpacking Arguments
def my_function(a, b, c):  #Unpacking Lists with *
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)


def my_function(fname, lname):  #Unpacking Dictionaries with **
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")


#my examples
def calculate_total(*prices):
    total = 0
    for price in prices:
        total += price
    return total

print("Total:", calculate_total(5.99, 12.50, 3.45))
print("Total:", calculate_total(100, 250))


def favorite_movies(*movies):
    print("My favorite movies are:")
    for movie in movies:
        print("-", movie)

favorite_movies("Titanic", "Avatar", "Inception")


def create_profile(**info):
    print("User Profile:")
    for key, value in info.items():
        print(key + ":", value)

create_profile(name="Alex", age=20, city="London", hobby="Gaming")




def food_order(customer_name, *items, **details):
    print("Customer:", customer_name)
    
    print("Ordered items:")
    for item in items:
        print("-", item)
    
    print("Order details:")
    for key, value in details.items():
        print(key + ":", value)

food_order(
    "John",
    "Pizza",
    "Burger",
    address="Main Street 10",
    payment="Card"
)