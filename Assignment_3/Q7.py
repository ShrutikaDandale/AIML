# Write a program that takes a string from the user and prints the number of spaces in the string
string = str(input("enter the string: "))

count = 0

for ch in string: #ch is the individual word in string
    if ch == " ":
      count += 1


print("total space:", count)
