x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

#int
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# my examples (int)

a = 5
b = 100
c = -20
d = 0
e = 999999

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


#float
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# my examples (float)

a = 3.5
b = 0.0
c = -7.25
d = 10.99
e = 1.2e3

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


#complex
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# my examples (complex)

a = 2 + 3j
b = 5j
c = -4j
d = 1 + 0j
e = -6 + 2j

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


#convert from one type to another

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# my examples

a = 10      
b = 4.5      
c = 2j        

print(type(a))
print(type(b))
print(type(c))

a = float(a)
b = int(b)
c = complex(b)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


#random number
import random

print(random.randrange(1, 10))

# my example

import random

a = random.randrange(2, 11)
b = random.randrange(10, 50)
c = random.randrange(100, 200)
d = random.randrange(0, 5)
e = random.randrange(1, 100)

print(a)
print(b)
print(c)
print(d)
print(e)
 