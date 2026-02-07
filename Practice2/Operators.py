print(10 + 5)

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)


#Python Arithmetic Operators

x = 15
y = 4

print(x + y) #Addition
print(x - y) #Substraction
print(x * y) #Multiplication
print(x / y) #Division
print(x % y) #Modulus
print(x ** y) #Exponentiation
print(x // y) #Floor division

x = 5
y = 3
print(x + y)

x = 5
y = 3
print(x - y)

x = 5
y = 3
print(x * y)

x = 12
y = 3
print(x / y)

x = 5
y = 2
print(x % y)

x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2

x = 15
y = 2

print(x // y)

#the floor division // rounds the result down to the nearest whole number


#Division in Python:

x = 12
y = 5

print(x / y) #return a float

x = 12
y = 5

print(x // y) #return an integer


#PYTHON ASSIGNMENT OPERATORS

#Assignment operators are used to assign values to variables:

x = 5
print(x)

x = 5
x += 3
print(x)

x = 5
x -= 3
print(x)

x = 5
x *= 3
print(x)

x = 5
x /= 3
print(x)

x = 5
x%=3
print(x)

x = 5
x//=3
print(x)

x = 5
x **= 3
print(x)

x = 5
x &= 3 #and
print(x)

x = 5
x |= 3 #or
print(x)

x = 5
x ^= 3 #xor
print(x)

x = 5
x >>= 3 #сдвиг вправо
print(x)

x = 5
x <<= 3 #сдвиг влево
print(x)

print(x := 3) #same as x = 3  print(x)

#The Walrus Operator

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")


#COMPARISON OPERATORS(returs true or false)

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#Chaining Comparison Operators

x = 5

print(1 < x < 10)

print(1 < x and x < 10)


#LOGICAL OPERATORS

x = 5
print(x > 3 and x < 10)

x = 5
print(x > 3 or x < 4)

x = 5
print(not(x > 3 and x < 10))

x = 5
print(x > 0 and x < 10)

x = 5
print(x < 5 or x > 10)

x = 5
print(not(x > 3 and x < 10))


#PYTHON IDENTITY OPERATORS

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have the same content

print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)
# returns False because z is the same object as x

print(x is not y)
# returns True because x is not the same object as y, even if they have the same content

print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y) #true
print(x is y) #false


#PYTHON MEMBERSHIP OPERATORS

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)


fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)


text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)


#PYTHON BITWISE OPERATORS

print(6 & 3)

"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
"""

print(6 | 3)

"""
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111"""

# The ^ operator compares each bit and set it to 1 if only one is 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 5 = 0101

print(6 ^ 3)


print(~3)
"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100"""


print(3 << 2)
"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100"""


print(8 >> 2)
"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010"""


#PYTHON OPERATOR PRECEDENCE

print((6 + 3) - (6 + 3)) #parentheses highest

print(100 - 3 ** 3) #	Exponentiation

print(100 + ~3) # Unary plus, unary minus, and bitwise NOT

print(100 + 5 * 3)  #Multiplication, division, floor division, and modulus

print(100 - 5 * 3) #	Addition and subtraction

print(8 >> 4 - 2) #	Bitwise left and right shifts

print(6 & 2 + 1) #Bitwise AND

print(6 ^ 2 + 1) #	Bitwise XOR

print(6 | 2 + 1) #	Bitwise OR

print(5 == 4 + 1) #Comparisons, identity, and membership operators

print(not 5 == 5) # 	Logical NOT

print(1 or 2 and 3) #	AND

print(4 or 5 + 10 or 8) #	OR


#Left-to-Right Evaluation
print(5 + 4 - 7 + 3)

# my examples 

a = 10
b = 3

print(a + b)
print(a * b)
print(a // b)

x = 5
x += 2
x *= 3

print(x)

age = 20

if age >= 18 and age < 65:
    print("Working age")
else:
    print("Not working age")


list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)  
print(list1 is list2)  


fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("Banana is in the list")
else:
    print("Banana is not in the list")
