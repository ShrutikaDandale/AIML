# agar humare class ke and instance ke pas same name ka attibute hai to higher priority instance ko hogi and instance ki value print hogi

class Student:
    collage_name = "TGPCET" 
    pie = 3.24

    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa
        self.pie = 3.12

stu1 = Student("Shanku", 9.2) 

print(stu1.name)
print(Student.collage_name)
print(stu1.pie)

print(Student.pie)
# if we specifically access with class name then the class value will be print




# here, pie is in both class and instance 
# so higher priority will be given to instance