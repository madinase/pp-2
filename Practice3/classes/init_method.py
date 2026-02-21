class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

#Without the __init__() method, you would need to set properties manually for each object:
class Person:
  pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)


class Person: #using __init__()
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 28)

print(p1.name)
print(p1.age)

#Set a default value for the age parameter
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)

#Multiple Parameters:
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)


#Code Challenge __init__ method
class Dog:
  def __init__(self, name, age):
       self.name = name
       self.age = age
        
  def bark(self):
        print(f"{self.name} says Woof!")

d1 = Dog("Buddy", 3)
d1.bark()

# my examples
class Student:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

s1 = Student("Dias")
s2 = Student("Omirserik", 22)

print(s1.name, s1.age)
print(s2.name, s2.age)


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car("Toyota", "Corolla", 2020)
print(car1.brand, car1.model, car1.year)


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Rex", 4)
dog1.bark()


class Book:
    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author

b1 = Book("Martin Iden", "London")
b2 = Book("Python")

print(b1.title, "-", b1.author)
print(b2.title, "-", b2.author)