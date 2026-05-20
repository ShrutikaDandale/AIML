# Create a dictionary where:
# •Keys = student names 
# •Values = marks(integer) 
# Write a menu-based program where user presses a key (ʼAʼ,‘Bʼ,‘Cʼ,‘Dʼ) depending on the operation they want to perform on the dictionary 

# A - Add a student
# B - Update marks 
# C - Search for a student
# D - Display all students and marks

info = {
    "shanku": 9.67,
    "pitu": 9.87,
    "kiki": 8.32
}

key = input("enter the key: ")

# A
if(key == "A"):
         name = input("enter new student name")
         marks = float(input("Enter new marks: "))
         info.update({
                name:marks
    })
         print(info)


# B
elif(key == "B"):
    name = input("Enter new student name: ")
    marks = float(input("Enter new marks: "))

    info[name] = marks 
    print(info)

# C
elif(key == "C"):

    name = input("Enter student name to search: ")

    if name in info:
        print(name, "marks are:", info[name])
    else:
        print("Student not found")


# D
elif(key == "D"):

   print(info)


else:
    print("Invalid key")     
