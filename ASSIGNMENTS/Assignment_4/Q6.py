# Create an abstract class employee with an abstract method calculate_salary().
# Create subclasses, Intern, FullTimeEmployee, and ContractEmployee that implement the method differently. 

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass


class Intern(Employee):
       def calculate_salary(self):
            self.stipend = 10000
            print("salary = ", self.stipend)

class FullTimeEmployee(Employee):
         def calculate_salary(self):
            self.monthly_salary = 50000
            print("salary = ", self.monthly_salary)

class ContractEmployee(Employee):
         def calculate_salary(self):
            self.hours_worked = 8
            self.rate_per_hour = 5000
            print("salary = ", self.hours_worked * self.rate_per_hour)

intern = Intern()
intern.calculate_salary()

FullTimeEmployee = FullTimeEmployee()
FullTimeEmployee.calculate_salary()

ContractEmployee = ContractEmployee()
ContractEmployee.calculate_salary()