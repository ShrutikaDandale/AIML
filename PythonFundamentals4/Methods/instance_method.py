# instance method use self parameter which can access both the class method and instance(self) method (ex- self.storage_type ye ek class method hai bu still ise self ne acess kiya)

# CLASS CREATED common for all laptops
class Laptop:
    storage_type = "ssd" #class

# INSTANCE CREATED - unique for all laptops
def __init__(self, RAM, storage): 
        self.RAM = RAM
        self.storage = storage

# METHOD CREATED - to get the values as output or to print the info of laptops we created a method 
def get_info(self):       
      print(f"laptop has{self.RAM} RAM and {self.storage} {self.storage_type}") 

# object created - to assign values
l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb", "256gb")

#to print the info of laptop we write above function
l1.get_info() #call function