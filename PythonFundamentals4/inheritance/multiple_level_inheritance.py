class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Student:
    def __init__(self, cgpa):
        self.cgpa = cgpa

class TA(Teacher, Student):
    def __init__(self, salary, cgpa, name):
        Teacher.__init__(self, salary)
        Student.__init__(self, cgpa)
        self.name = name

ta1 = TA(15_000, 9.3, "shrutika")

print(ta1.name, ta1.cgpa, ta1.salary)