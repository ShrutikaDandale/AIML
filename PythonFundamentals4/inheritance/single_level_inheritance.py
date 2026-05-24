# single level
# parent class
class Animal:
    def sound(self):
        print("Animals make sounds")

# child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

d1 = Dog()

d1.sound()   # inherited from Animal
d1.bark()    # from Dog