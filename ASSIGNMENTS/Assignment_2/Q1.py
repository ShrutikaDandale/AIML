# Write a program that takes salary as input. Using conditional statements, calculate the final tax rate based on these rules:
# •Ifsalary<30,000→5%
# •Ifsalaryis30,000–70,000→15%
# •Ifsalary>70,000→25%

salary = float(input("enter salary: "))

if (salary < 30000):
    tax = salary * 0.5 

elif (salary <= 70000):
    tax = salary * 0.15 

else:
    tax = salary * 0.25  

print("tax: ", tax)
