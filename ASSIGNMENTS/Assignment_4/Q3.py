# Create a class with attributes _name, _roll_no, and _marks. Provide getter and setter methods with validation (e.g., marks cannot be negative, roll number has to be between 1 & 100 & name cannot be empty)

class Student:

    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    # Getter methods
    def get_name(self):
        return self.__name

    def get_roll_no(self):
        return self.__roll_no

    def get_marks(self):
        return self.__marks

    # Setter methods
    def set_name(self, name):
        if name != "":
            self.__name = name
        else:
            print("Invalid name")

    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self.__roll_no = roll_no
        else:
            print("Invalid roll number")

    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Invalid marks")


s1 = Student("Rahul", 10, 85)

# shows the orirginal value
print(s1.get_name())
print(s1.get_roll_no())
print(s1.get_marks())

# update the values
s1.set_name("Aman")
s1.set_roll_no(50)
s1.set_marks(90)

# shows the value after update
print(s1.get_name())
print(s1.get_roll_no())
print(s1.get_marks())