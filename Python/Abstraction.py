from abc import ABC , abstractmethod

class Animal(ABC):                                          # Abstract Class
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):                                      # Child Class
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat Meows")

d = Dog()
d.sound()
c = Cat()
c.sound()

