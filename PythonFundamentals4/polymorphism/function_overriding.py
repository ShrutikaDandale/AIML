# polymorphism - multiple fuction same name
# function overriding (inheritance) - redefining parent class fxn in  child class

class Employee:
    def get_designation(self):
        print("designation =  Employee")

class Teacher(Employee):
    def get_designation(self):
        print("designation = Teacher")

t1 = Teacher()
t1.get_designation()           


# Method Overriding: When a child class(Teacher) creates a method with the same name(get_designation) as a method in the parent class(Employee), the child's method replaces (overrides) the parent's method for objects of the child class.