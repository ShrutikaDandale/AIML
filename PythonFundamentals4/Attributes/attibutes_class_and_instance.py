class Student:
    collage_name = "TGPCET" #class attribute

    def __init__(self, name, cgpa):
        self.name = name #instance attributes
        self.cgpa = cgpa

stu1 = Student("Shanku", 9.2) #this is object

print(stu1.name) # we can only acces the instance attributes using object

print(Student.collage_name) #we can access the class attributs using both object and class
#print(stu1.collage_name)

