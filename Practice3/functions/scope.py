#A variable is only available from inside the region it is created. This is called scope.

def myfunc():
  x = 300 #local scope
  print(x)

myfunc()


def myfunc():
  x = 300
  def myinnerfunc(): #function inside function
    print(x)
  myinnerfunc()

myfunc()


x = 300 #global scope

def myfunc():
  print(x)

myfunc()

print(x)


#Naming Variables
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)


def myfunc():
  global x #global keyword
  x = 300

myfunc()

print(x)


x = 300

def myfunc():
  global x #to change global variable
  x = 200

myfunc()

print(x)


#Nonlocal Keyword
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x #the variable will belong to the outer function
    x = "hello"
  myfunc2()
  return x

print(myfunc1())


#The LEGB Rule (LOCAL ENCLOSING GLOBAL BUILT-IN)
x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)


# my examples

x = "global value"

def show_value():
    x = "local value"
    print("Inside function:", x)

show_value()
print("Outside function:", x)


counter = 0

def increase_counter():
    global counter
    counter += 1

increase_counter()
increase_counter()
print("Counter:", counter)


def outer_function():
    message = "Start"

    def inner_function():
        nonlocal message
        message = "Changed"

    inner_function()
    return message

print("Result:", outer_function())


name = "Global"

def outer():
    name = "Enclosing"

    def inner():
        name = "Local"
        print("Inner:", name)

    inner()
    print("Outer:", name)

outer()
print("Global:", name)