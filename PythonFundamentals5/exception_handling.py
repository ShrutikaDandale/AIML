# try, except, else, finally
# suppose program me error aaya hai to program stop hota hai use handle karane ke liye hum exception handling use karake hai taki program ka flow bana rahe

try:
    x = int(input("enter x: "))
    ans = 10/x

except ZeroDivisionError: 
    print("division buy 0 is now allowed")

except ValueError:
    print("invalid input")

else:
    print(f"ans = {ans}")       