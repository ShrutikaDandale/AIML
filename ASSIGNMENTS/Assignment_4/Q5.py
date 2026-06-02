# Create a base class vehical with attributes like brand and model. 
# Create two subclasses car and bike that add extra attributes - seats (inCar) & engine_cc (in Bike).

# parent class
class Vehical:

    def __init__(self, brand , model):
        self.brand = brand
        self.model = model

# child class
class Car(Vehical):
    
      def __init__(self, brand, model, seats):
        super().__init__(brand, model)#super() ko hum pareeent class ke constructor ko inherit karaneke liye use karate hai
        self.seats = seats

      def display(self):
        print("Brand =", self.brand)
        print("Model =", self.model)
        print("Seats =", self.seats)

# child class
class Bike(Vehical):

     def __init__(self, brand, model, engine_cc):
         super().__init__(brand, model)
         self.engine_cc = engine_cc 

    # Display method
     def display(self):
        print("Brand =", self.brand)
        print("Model =", self.model)
        print("Engine =", self.engine_cc, "cc")

# Objects create kiye
c1 = Car("BMW", "M5", 4)
b1 = Bike("ninja", "n-900", 360)

   # Methods call kiye
c1.display()
b1.display()
