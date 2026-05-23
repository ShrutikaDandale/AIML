# PRODUCT STORE
# Design and create an online store for products (name, price)
# track total products being created
# create a static method to calculate discount on each product based on a % parameter

class Product:
    count = 0

    def __init__(self, name, price): #intance
        self.name = name
        self.price = price
        Product.count += 1 #class attribute

    def get_info(self): #instance method   
        print(f"product has {self.name} name and {self.price}")

    @classmethod
    def get_count(cls): #class method
       print(f"total products in store = {cls.count}")

    @staticmethod
    def calc_discount(price, discount):
      print(f"discounted price ={price - (discount * price / 100)}")


p1 = Product("laptop", 70000)
p2 = Product("phone", 40000)
p3 = Product("pen", 10)

Product.get_count()

p1.calc_discount(p1.price, 12) #static