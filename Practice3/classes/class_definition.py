class MyClass:  #create a class
  x = 5

p1 = MyClass() #create object 
print(p1.x) 

del p1 #delete objects

#multiple objects
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)


#The pass Statement
class Person:
  pass


#The challenge
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("John", 36)
p1.greet()

# my examples
class Car:
    wheels = 4

car1 = Car()
car2 = Car()
print(car1.wheels)
print(car2.wheels)


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Buddy", "Beagle")
dog2 = Dog("Max", "Labrador")

print(dog1.name, dog1.breed)
print(dog2.name, dog2.breed)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f"{self.title} by {self.author}")

book1 = Book("1984", "George Orwell")
book1.info()


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle1 = Circle(5)
print("Area:", circle1.area())