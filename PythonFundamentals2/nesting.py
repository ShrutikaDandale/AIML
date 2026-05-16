username = input("enter username: ")
password = input("enter password: ")

if (username == "admin" and password == "password"):
    print("success")
else:
    if (username != "admin"):
     print("invalid username")
    else:
       print("invalid password")    
  