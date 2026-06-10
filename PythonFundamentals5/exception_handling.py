# try, except, else, finally

try:
    x = int(input("enter x: "))
    ans = 10/x

except ZeroDivisionError: 
    print("division buy 0 is now allowed")

else:
    print(f"ans = {ans}")       