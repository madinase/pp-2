#Inheritance allows us to define a class that inherits all the methods and properties from another class.
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()

#challenge:
class Animal:
  def __init__(self, name):
    self.name = name

  def speak(self):
    print(self.name)

class Dog(Animal):
  pass

d1 = Dog("Rex")
d1.speak()


# my examples
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)

class Car(Vehicle):
    pass

car1 = Car("Toyota")
car1.show_brand()



class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

class Manager(Employee):
    pass

manager1 = Manager("Alice", 5000)
manager1.show_info()



class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "makes a sound")

class Cat(Animal):
    pass

cat1 = Cat("Whiskers")
cat1.speak()



class Shape:
    def __init__(self, color):
        self.color = color

    def show_color(self):
        print("Color:", self.color)

class Rectangle(Shape):
    pass

rect1 = Rectangle("Blue")
rect1.show_color()