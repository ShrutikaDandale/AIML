# Create a program that: 
# 1. Opens a file "names.txt" in write mode
# 2. Writes 5 names (one per line) entered by the user
# 3. Then opens the same file in read mode and prints all names

f = open("ASSIGNMENTS/Assignment_5/names.txt", "w") 
for i in range(5):
    name = (input("enter user name:" ))
    f.write(name + "\n")
f.close()