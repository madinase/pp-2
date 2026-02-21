#The self parameter is a reference to the current instance of the class.
#Use self to access class properties:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()

#The self parameter links the method to the specific object:
class Person:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()
p2.printname()

#self Does Not Have to Be Named "self"
class Person:
  def __init__(myobject, name, age): #it has to be the first parameter 
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()


#Access multiple properties using self:
class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

#Calling Methods with self
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()

#challenge:
class Car:
  def __init__(self, brand):
    self.brand = brand

  def show(self):
    print(self.brand)

c1 = Car("Ford")

c1.show()

# my examples
class IceCream:
    def __init__(self, flavor, scoops):
        self.flavor = flavor
        self.scoops = scoops

    def serve(self):
        print(f"Serving {self.scoops} scoop(s) of {self.flavor} ice cream!")

ice1 = IceCream("Chocolate", 2)
ice1.serve()


class FruitBasket:
    def __init__(self, owner):
        self.owner = owner
        self.fruits = []

    def add_fruit(self, fruit):
        self.fruits.append(fruit)
        print(f"Added {fruit} to {self.owner}'s basket")

basket = FruitBasket("Emma")
basket.add_fruit("Apple")
basket.add_fruit("Banana")
print("Fruits in basket:", basket.fruits)



class GamePlayer:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I'm {self.name}"

    def welcome(self):
        message = self.greet()
        print(message + "! Ready to play?")

player1 = GamePlayer("вфтш")
player1.welcome()


class Candy:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"This candy is called {self.name} ")

c1 = Candy("Lollipop")
c1.show()