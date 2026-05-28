class Laptop:
    storage_type = "ssd" #class

def __init__(self, RAM, storage): #intance
        self.Ram = RAM
        self.storage = storage

@classmethod #class method - agar humne kisi function ki method classmethod define kardi to vo function ka behaviour change hoke vo as a class act karega
def get_storage_type(cls):
      print(f"storage type = {cls.storage_type}")


def get_info(self): #function      
      print(f"laptop has{self.Ram} RAM and {self.storage} {self.storage_type}") #instance method calls both self and class

l1 = Laptop("16gb", "512gb")


l1.get_storage_type() #method class called
# Laptop.get_storage_type() we can also write in this way using the object