# Create a class with attributes _name, _roll_no, and _marks. Provide getter and setter methods with validation (e.g., marks cannot be negative, roll number has to be between 1 & 100 & name cannot be empty)
class Student:
   pass

   def __init__(self, name, roll_no, marks):
       self.__name = name  
       self.__roll_no = roll_no
       self.__marks = marks

def get_name(self): #getter function
        return self.__name
        
def set_name(self, name): #setter function
        if name == "":
              print(f"invalid") 
        else:
              print(name)
        self.__name = name

        if (1 <= roll_no <= 100):
              print(roll_no)

            else:
              print("invalid")