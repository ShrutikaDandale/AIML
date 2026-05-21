# Ask the user for a string and print:
# •All unique characters
# •The count of unique characters

string = str(input("enter the string: "))
unique_char = set(string) # set remove duplicate from a string and seperate each character from string

print("All unique characters:", unique_char)
print("count of unique characters:", len(unique_char))

# unique character means unique alphabet with no repetation