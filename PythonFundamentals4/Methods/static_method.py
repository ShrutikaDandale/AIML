# suppose for a laptop class we wanted a function that can calculate a price of a laptop based on the discount
class Laptop:
    storage_type = "ssd" #class

def __init__(self, RAM, storage): #intance
        self.Ram = RAM
        self.storage = storage

@classmethod #class method
def get_storage_type(cls):
      print(f"storage type = {cls.storage_type}")


def get_info(self): #function      
      print(f"laptop has{self.Ram} RAM and {self.storage} {self.storage_type}") #instance method calls both self and class


@staticmethod
def calc_discount(price, discount):
      final_price = price - (discount * price / 100)
      print(f"discounted price ={final_price}")


l1 = Laptop("16gb", "512gb")

l1.calc_discount(40000, 10)