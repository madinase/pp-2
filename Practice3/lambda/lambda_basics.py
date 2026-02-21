#lambda arguments : expression

x = lambda a : a + 10
print(x(5)) #Add 10 to argument a, and return the result:


x = lambda a, b : a * b
print(x(5, 6))


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#Why Use Lambda Functions?
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2) #always doubles the number you send in

print(mydoubler(11))


def myfunc(n): #always triples the number you send in
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


# my examples

square = lambda x: x ** 2

print(square(4))
print(square(9))



is_even = lambda x: x % 2 == 0

print(is_even(10))
print(is_even(7))



final_price = lambda price, tax: price + (price * tax / 100)

print(final_price(100, 20))
print(final_price(250, 10))



create_greeting = lambda name: "Hello, " + name + "!"

print(create_greeting("Alex"))
print(create_greeting("Maria"))












