# instance method use self parameter which can access both the class method and instance(self) method
class Laptop:
    storage_type = "ssd" #class

def __init__(self, RAM, storage): #intance
        self.Ram = RAM
        self.storage = storage

def get_info(self): #function      
      print(f"laptop has{self.Ram} RAM and {self.storage} {self.storage_type}") #instance method calls both self and class

l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb", "256gb")

l1.get_info() #call function