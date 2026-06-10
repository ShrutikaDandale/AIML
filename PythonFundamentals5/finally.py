# finally- it is like some block of code jo run hona hi chahiye irrespective of apne program me exception aaye ya na aaye

try:
    x = int(input("enter x: "))
    ans = 10/x

except ZeroDivisionError: 
    print("division buy 0 is now allowed")

except ValueError:
    print("invalid input")

else:
    print(f"ans = {ans}")  

finally:
    print("end of program")

 #agar humare progra me exception aaye ya na aaye fir bhi finally run hoga hi 
