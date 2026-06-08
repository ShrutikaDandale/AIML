# duck typing
class Teacher():
    def get_designation(self):
        print("designation = Teacher")

class Accountant():
    def get_designation(self):
        print("designation = Teacher")

t1 = Teacher()
t1.get_designation()

acc1 = Accountant() 
acc1.get_designation() 

# Python ko farak nahi padta object kis class ka hai. Usse sirf ye dekhna hai ki object ke paas required method hai ya nahi.
# dono class alag alag hai ek teacher hai and ek accountant hai Dono classes mein get_designation() method hai. to classes bhale alag alg ho par method same hi hai 
# jab code chala to python ne ye nahi dekha ki t1 teacher class ka hai ya acc1 accountant class ka hain usne bas ye dekha ki dono ke oas get_designation method hai and run kiya