# Create a class Shape with a method area().
# create subclass circle, rectangle, and triangle that override the area() method

# main class
class Student:
    def area(self):
        print("area")

# subclass circle
class Circle(Student):
    # method override
    def area(self):
     radius = 5
     print("area of circle is = ", 3.14 * radius * radius)

class Rectangle(Student):
    def area(self):
       length = 2
       breath = 4
       print("area of the rectangle is = ", length * breath)   

class Triangle(Student):
   def area(self):
      base = 2
      height = 5
      print("area of triangle = ", 0.5 * height * base )

# object create kiya
c = Circle()
r = Rectangle()
t = Triangle()

# method call kiya
c.area()
r.area()
t.area()


