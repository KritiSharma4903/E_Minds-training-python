# class MyClass:              # create class
#     x = 5
#     y = 10
# p1 = MyClass()              # create object (we can create multiple objects)
# p2 = MyClass()
# p3 = MyClass()
# print(p1.x)
# print(p1.x)
# print(p1.y)


#---------------------- __init__()---------------------------

# class Person:
#     def __init__(self, name, age, city, country):
#         self.name = name
#         self.age = age
#         self.city = city
#         self.country = country

# p1 = Person("Linus", 30, "Oslo", "Norway")

# print(p1.name)
# print(p1.age)
# print(p1.city)
# print(p1.country)


# class Person:
#     def __init__(self, name):
#         self.name = name
#     def greet(self):
#         return "Hello, " + self.name
#     def welcome(self):
#         message = self.greet()
#         print(message+ "! Welcome to our website.")
# p1 = Person("Tobias")
# p1.welcome()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def celebrate_birthday(self):
#         self.age += 1
#         print(f"Happy birthday! You are now {self.age}")

# p1 = Person("Linus", 25)
# p1.celebrate_birthday()
# p1.celebrate_birthday()



#-----------with or without __str__()---------------------

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p1 = Person("Emil", 36)
# print(p1)


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} ({self.age})"
# p1 = Person("Tobias", 36)
# print(p1)


# class Playlist:
#   def __init__(self, name):
#     self.name = name
#     self.songs = []

#   def add_song(self, song):
#     self.songs.append(song)
#     print(f"Added: {song}")

#   def remove_song(self, song):
#     if song in self.songs:
#       self.songs.remove(song)
#       print(f"Removed: {song}")

#   def show_songs(self):
#     print(f"Playlist '{self.name}':")
#     for song in self.songs:
#       print(f"- {song}")

# my_playlist = Playlist("Favorites")
# my_playlist.add_song("Bohemian Rhapsody")
# my_playlist.add_song("Stairway to Heaven")
# my_playlist.show_songs()


# class Person:
#     def __init__(self,name):
#         self.name = name
#     def greet(self):
#         print("Hello!")
# p1 = Person("Emil")
# del Person.greet
# p1.greet


#------------------------------Inheritance---------------------
class Person:
    def __init__(self,fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()


#-------------------------Polymorphism--------------------------

class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("Cat meows")
d = Dog()       # Object of Dog class
c = Cat()       # Object of Cat class
d.sound()    # function call
c.sound()


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")


car1 = Car("Ford", "Mustang")       
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747")     

for x in (car1, boat1, plane1):
  x.move()

#--------------------- Encapsulation -----------------------

class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = 0

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Grade must be between 0 and 100")

    def get_grade(self):
        return self.__grade
    
    def get_status(self):
        return self.__grade
    
    def get_status(self):
        if self.__grade >= 60:
            return "Passed"
        else:
            return "Failed"
        
student = Student("Emil")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())


#---------------------Inner Class ---------------------------
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()

    class Engine:
        def __init__(self):
            self.status = "Off"

        def start(self):
            self.status = "Running"
            print("Engine started")

        def stop(self):
            self.status = "Off"
            print("Engine stopped")

    def drive(self):
        if self.engine.status == "Running":
            print(f"Driving the {self.brand} {self.model}")
        else:
            print("Start the engine first!")

car = Car("Toyota", "Corolla")
car.drive()
car.engine.start()
car.drive()