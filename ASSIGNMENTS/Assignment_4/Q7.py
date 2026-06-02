# Create a class Person that allows the constructor to work with: 
# •name only 
# •name + age
# •name + age + address 
# As direct constructor overloading (multiple constructors) are not allowed but we have to use default parameters to simulate constructor overloading.

class Person:
    def __init__(self, name, age = 18, address = "nagpur"):
        self.name = name
        self.age = age
        self.address = address


# matlab hume bas 3 bar 3 alag alag ways me constructor ko call karasna hai isisliye humne 3 alag alag ways se objects create kiye haina
p1 = Person("kookie")
p2 = Person("kookie", 20)
p3 = Person("kookie", 20, "S.korea")
# Question ka main point ye nahi hai ki 3 alag logon ke objects banao. Main point ye hai ki ek hi constructor ko 3 different ways se call karke dikhana hai isiliye humne tino bhi bar ek hi name liya hai

# yahape costructor ko overlodding dikhane ke liye humne p1 me bhi name age and add print kiya and same for p2 and p3
# balki hume to bas p1 me namde p2 me name age and p3 me name age add print karawana tha 
print(p1.name, p1.age, p1.address)
print(p2.name, p2.age, p2.address)
print(p3.name, p3.age, p3.address)













    # hume yahape first line me sirf name hi print print karana hai isiliye name ko kuch assign nahimkiya but second line me hume name ke sath sath age bhi print karrawani hai isiliye humne 2nd line me age ko value assign ki and sath sathme 3rd line ko bhi assign kiya 
