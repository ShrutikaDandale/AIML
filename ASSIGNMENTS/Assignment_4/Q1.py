class BankAccount:
    bank_name = "BOI"

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(" deposit Balance =", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("withdraw Balance =", self.balance)
        else:
            print("No balance")

    def check_balance(self):
        print("check Balance =", self.balance)


# object
acc1 = BankAccount(101, "Aman", 5000)

acc1.deposit(1000)
acc1.withdraw(2000)
acc1.check_balance()

print("Bank:", BankAccount.bank_name)