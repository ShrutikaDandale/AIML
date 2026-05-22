class Student:
    def __init__(self, name, cgpa): #self is compulsory it will always come
       self.name = name
       self.cgpa = cgpa

    def get_cgpa(self):
     return self.cgpa

stu1 = Student("shanku", 9.77)
stu2 = Student("pitu", 9.65)
stu3 = Student("kiki", 9.97)

print(stu1.cgpa)
print(stu2.name, stu2.cgpa)
print(stu3.name)

print(stu1.get_cgpa())  

