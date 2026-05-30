# abstraction - hiding internal details and showing ony essential features
# we make the bluprint of the class which in parent class and the actual work performs in the child class

from abc import ABC, abstractmethod #ABC - abstraction based classes

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Lion():
        def make_sound(self):
            print("Roar")

    
class Cow():
        def make_sound(self):
            print("Moo")

lion = Lion()
lion.make_sound() 

cow = Cow()
cow.make_sound()              


# here parent class is animal andchild class is lion where in parent class we created a maje sound fuction which is bluepribt and dos nothing while the actual work is done of making sound is performed in the child class lion make soud roar