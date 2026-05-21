# Write a program that takes salary as input. Using conditional statements, calculate the final tax rate based on these rules:
# •Ifsalary<30,000→5%
# •Ifsalaryis30,000–70,000→15%
# •Ifsalary>70,000→25%

salary =  float(input("enter your salary: "))
if (salary < 30000):
      print("5%")
elif(salary == 30000 and salary == 70000):
      print("15%")
elif(salary > 70000):
       print("25%")
else:
    print("invalid")
