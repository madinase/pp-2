#Properties are variables that belong to a class. They store data for each object created from the class.

#Create a class with properties:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

#Access the properties of an object:
class Car: 
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)


#Change the age property:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print(p1.age)

p1.age = 26
print(p1.age)

#Delete properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 30)

del p1.age

print(p1.name) # This works
# print(p1.age) # This would cause an error


#Class Properties vs Object Properties
class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

#Change a class property:
class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"

print(p1.lastname)
print(p2.lastname)

#Add a new property to an object:
class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)

#challenge
class Student:
  def __init__(self, name, grade):
    self.name = name
    self.grade = grade

s1 = Student("Anna", "A")# Create an object

print(s1.grade)# Print the grade

s1.grade = "B"# Change the grade

print(s1.grade)# Print the updated grade


# my examples
class Car:
    wheels = 4  

    def __init__(self, brand, model):
        self.brand = brand  
        self.model = model

car1 = Car("Toyota", "MErcedes")
car2 = Car("Honda", "Gelengvagen")

print(car1.brand, car1.model, car1.wheels)
print(car2.brand, car2.model, car2.wheels)



class Person:
    species = "Human"

    def __init__(self, name):
        self.name = name

p1 = Person("Alex")
p2 = Person("Maria")

Person.species = "Homo Sapiens"

print(p1.name, p1.species)
print(p2.name, p2.species)



class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Joel")
s1.grade = "A"

s2 = Student("Ellie")
s2.grade = "B"

print(s1.name, s1.grade)
print(s2.name, s2.grade)



class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("1984", "George Orwell")
del book1.author

print(book1.title)
