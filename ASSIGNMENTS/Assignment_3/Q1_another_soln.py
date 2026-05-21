# A palindrome string is equal to the reversed version of the string. We can use a loop to reverse the string manually 

word = input("Enter the string: ")
reverse = "" #empty word

for char in word:
    reverse = char + reverse
    #means char="" + reverse alphabet empty value plus reverse alphabet
    #char in word means a single alphabet in a word 
    
    
    if word == reverse:
     print("Palindrome")
    else:
     print("Not Palindrome")


# logic explanation
# let word = cat
# reverse = "" (empty)
# char = "c"
# reverse = char + reverse
# reverse = "c" + ""
# reverse = "c"

# second iteration
# char = "a"
# reverse = "a" + "c"
# reverse = "ac"

# same aise hi pura word reverse hoga and then reverse word ko and original word ko hum compare karenge