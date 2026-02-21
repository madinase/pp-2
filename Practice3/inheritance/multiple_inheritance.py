class Flyer:
    def fly(self):
        return "I fly"

class Swimmer:
    def swim(self):
        return "I swim!"

class Duck(Flyer, Swimmer):
    pass

donald = Duck()
print(donald.fly()) 
print(donald.swim()) 

# my examples
class Walker:
    def walk(self):
        return "I can walk"

class Swimmer:
    def swim(self):
        return "I can swim"

class Frog(Walker, Swimmer):
    pass

frog1 = Frog()
print(frog1.walk())
print(frog1.swim())



class Drivable:
    def drive(self):
        return "I can drive"

class Floatable:
    def float(self):
        return "I can float"

class AmphibiousVehicle(Drivable, Floatable):
    pass

vehicle1 = AmphibiousVehicle()
print(vehicle1.drive())
print(vehicle1.float())



class Teacher:
    def teach(self):
        return "I can teach"

class Coder:
    def code(self):
        return "I can code"

class TechTeacher(Teacher, Coder):
    pass

tt1 = TechTeacher()
print(tt1.teach())
print(tt1.code())



class MusicPlayer:
    def play_music(self):
        return "Playing music"

class Camera:
    def take_photo(self):
        return "Taking a photo"

class Smartphone(MusicPlayer, Camera):
    pass

phone1 = Smartphone()
print(phone1.play_music())
print(phone1.take_photo())