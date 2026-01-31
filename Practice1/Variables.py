x = 5
y = "John"
print(x)
print(y)

#my examples

name = "Madina"
season = "winter"
month = "April"
food = "omelette"
color = "red"
age = 17
date = 12
year = 2026
count = 3
weight = 50

print(name)
print(season)
print(month)
print(food)
print(color)
print(age)
print(date)
print(year)
print(count)
print(weight)


x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)


#Casting

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Get the Type

x = 5
y = "John"
print(type(x))
print(type(y))


#Single or Double Quotes?

x = "John"
# is the same as
x = 'John'

#Case-Sensitive

a = 4
A = "Sally"
#A will not overwrite a

#Python - Variable Names

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#my examples

name = "Joel"
NameSurname = "Joel Miller"
name_surname = "Joel Miller"
NAME_suRn4me = "Joel Miller"
NAMESURNAME2_namesurname = "Joel"

myVariableName = "John" #Camel Case
MyVariableName = "John" #Pascal Case
my_variable_name = "John" #Snake Case


#Python Variables - Assign Multiple Values

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


#my examples

x , y , z = "Ratchet" , "Clank" , "Rivet"
print(x)
print(y)
print(z)

x = y = z = "Cinemas"
print(x)
print(y)
print(z)

characters = ["Miles Morales" , "Peter Parker" , "Ganke", "Mary Jane"]
x , y , z , w = characters
print(x)
print(y)
print(z)
print(w)

valutas = ["tenge" , "rubl" , "dollar"]
first , second , third = valutas
print(first)
print(second)
print(third)


animals = ["cat" , "dog" , "horse"]
a , b , c = animals
print(a)
print(b)
print(c)

colors = ["red" , "blue" , "black"] 
r , b , B = colors
print(r)
print(b)
print(B)

subjects = ["ADS" , "Statistics" , "Databases"]
x1 , x2 , x3 = subjects
print(x1)
print(x2)
print(x3)

#Python - Output Variables

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)


x = 5
y = "John"
print(x, y)

# my examples

a = "Learning"
b = "Python"
c = "is fun"
print(a, b, c)

a = "I "
b = "love "
c = "coding"
print(a + b + c)

x = 7
y = 3
print(x + y)

x = 7
y = "days"
print(x, y)


#Global Variables

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()




x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)



def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)




x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)



#my examples
x = "great"

def myfunc():
    print("Python is " + x)

myfunc()


x = "cool"

def myfunc2():
    x = "easy"
    print("Reading is " + x)

myfunc2()

print("Reading is " + x)


def myfunc3():
    global x
    x = "powerful"

myfunc3()

print("Python is " + x)