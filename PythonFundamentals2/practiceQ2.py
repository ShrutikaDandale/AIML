# if-elif-if
username = str(input("enter username: "))
password = str(input("enter password: "))

if (username == "admin" and password == "pass"):
    print("login successfull")
elif (username != "admin"):
    print("wrong username")
else:
    print("wrong password")         
    
