def my_function():
  print("Hello from a function")

my_function()  
my_function()
my_function()

#Valid function names:
#calculate_sum()
#_private_function()
#myFunction2()


#repetitive code without function:
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

#With functions, you write the code once and reuse it:
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

#return value:
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

def get_greeting():
  return "Hello from a function"

print(get_greeting())

#The PASS statement:
def my_function():
  pass

#my examples
def greet_user(name):
    print("Hello,", name)

greet_user("Alex")
greet_user("Maria")
greet_user("John")

def square(number):
    return number * number

print(square(4))
print(square(7))
print(square(10))


def is_even(number):
    if number % 2 == 0:
        return True
    return False

print(is_even(4))
print(is_even(7))
print(is_even(12))


def calculate_average(grade1, grade2, grade3):
    return (grade1 + grade2 + grade3) / 3

print(calculate_average(80, 90, 85))
print(calculate_average(70, 75, 72))