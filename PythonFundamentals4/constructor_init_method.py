# create a class
class Student:
    
#constructor created  
    def __init__(self, name, cgpa): #self is compulsory it will always come
       self.name = name
       self.cgpa = cgpa

# method created to return the cgpa
# agar method ko yaha create nahi kiya hota to bhi hume return me cgpa milta hi but humne professinal way me object se cgpa manga naki directly access kiya
    def get_cgpa(self):
     return self.cgpa

# object created to assign some values to constructor
stu1 = Student("shanku", 9.77)
stu2 = Student("pitu", 9.65)
stu3 = Student("kiki", 9.97)

# ab values assign ho gayi to unhe print karana hoga

# print the values using print
print(stu1.cgpa)
print(stu2.name, stu2.cgpa)
print(stu3.name)

print(stu1.get_cgpa())
