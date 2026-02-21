class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
x.welcome()

# my examples
class Animal:
    def __init__(self, species):
        self.species = species

    def show_species(self):
        print("Species:", self.species)

class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self.breed = breed

    def show_info(self):
        print("Species:", self.species, "| Breed:", self.breed)

dog1 = Dog("Canine", "Beagle")
dog1.show_info()



class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")

manager1 = Manager("Alice", 5000, "HR")
manager1.show_info()



class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

class Car(Vehicle):
    def __init__(self, brand, wheels, color):
        super().__init__(brand, wheels)
        self.color = color

    def show_info(self):
        print(f"Brand: {self.brand}, Wheels: {self.wheels}, Color: {self.color}")

car1 = Car("Toyota", 4, "Red")
car1.show_info()


class Shape:
    def __init__(self, color):
        self.color = color

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect1 = Rectangle("Blue", 5, 10)
print("Color:", rect1.color)
print("Area:", rect1.area())