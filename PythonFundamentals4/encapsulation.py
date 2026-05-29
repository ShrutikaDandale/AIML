class BankAccount:
    def __init__(self, name, balance, accNo):

        self.name = name #public attribute
        self._balance = balance #protected attribute (uses _ )
        self.__accNo = accNo #private attribute (uses __ )

    def get_balance(self): #getter function
        return self.__balance
        
    def set_balance(self, newBalance): #setter function
        self.__balance = newBalance
    
acc1 = BankAccount("Shrutika", 100000)
acc1.set_balance(20000)

print(acc1.name, acc1.get_balance)
# print(acc1.name, acc1.BankAccount__balance) we can also access private attributes like this
        


#public atribute - can be access everywere
#protected  attribute - can  be access inside class and subclass
# private attribute - can  be access inside class only