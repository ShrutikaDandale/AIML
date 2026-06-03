# Create the following classes: Herbivore, Carnivor, Omnivor with some attributes & methods. Then create a class Bear that inherits from all the above classes to showcase how multiple inheritance works.

class Herbivor:
    def eat_plants(self): #method
        print("eat plants")

class Carnivore:
    def eat_meat(self):
        print("eat meat")

class Omnivore:
    def eat_both(self):
        print("eat both")


class Bear(Herbivor, Carnivore, Omnivore):
    def __init__(self, name):
        self.name = name 

# humne name attr liya isliye name assign kiya
b1 = Bear("bhaloo")

        # methods ko call kiya
b1.eat_plants()
b1.eat_meat()
b1.eat_both()



