print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Strings are Arrays
a = "Hello, World!"
print(a[1])

#Looping Through a String
for x in "banana":
  print(x)

#String Length
a = "Hello, World!"
print(len(a))

#Check String
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#SLICING STRINGS
b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])  #Negative Indexing 

#MODIFY STRINGS

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#CONCATENATE STRINGS

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#STRING FORMAT

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)


#ESCAPE CHARACTERS

txt = "We are the so-called \"Vikings\" from the north."

txt = 'It\'s alright.' #single quote
print(txt) 

txt = "This will insert one \\ (backslash)." #backslash
print(txt) 

txt = "Hello\nWorld!" #new line
print(txt) 

txt = "Hello\rWorld!" #carriage return
print(txt) 

txt = "Hello\tWorld!" #Tab
print(txt) 

txt = "Hello \bWorld!" #backspace
print(txt) 

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 


#STRING METHODS

txt = "python is FUN!"
x = txt.capitalize()
print (x)

txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

txt = "banana"
x = txt.center(20)
print(x)

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

txt = "My name is Ståle"
x = txt.encode()
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

txt = "Company12"
x = txt.isalnum()
print(x)

txt = "CompanyX"
x = txt.isalpha()
print(x)

txt = "Company123"
x = txt.isascii()
print(x)

txt = "1234"
x = txt.isdecimal()
print(x)

txt = "50800"
x = txt.isdigit()
print(x)

txt = "Demo"
x = txt.isidentifier()
print(x)

txt = "hello world!"
x = txt.islower()
print(x)

txt = "565543"
x = txt.isnumeric()
print(x)

txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)

txt = "   "
x = txt.isspace()
print(x)

txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

txt = "welcome to the jungle"
x = txt.split()
print(x)

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

txt = "Welcome to my world"
x = txt.title()
print(x)

mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

txt = "Hello my friends"
x = txt.upper()
print(x)

txt = "50"
x = txt.zfill(10)
print(x)


# my examples 

x = "What is your name?"
print(x)

x = "Python"
print(x[0])  

for letter in "cat":
    print(letter)

x = "apple"
print(len(x))

txt = "I have a dog"
print("cat" in txt)

x = "School"
print(x[1:5])
