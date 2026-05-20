# Ask the user for a string and chec kwhether it is a palindrome or not. 
# A palindrome is a string which is same when we read it forward & backward. Eg- “madam”, “racecar” etc.

word = input("Enter the string: ")

i = 0
j = len(word) - 1

while i < j:
    if word[i] != word[j]:
        print("Not Palindrome")
        break

    i += 1
    j -= 1

else:
    print("Palindrome")