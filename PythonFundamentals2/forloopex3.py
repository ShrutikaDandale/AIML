# count the no. of vowels in the given string
word = "artificial"
count = 0

for ch in word:
    if(ch == 'a'or ch == 'e'or ch == 'i'or ch == 'o'  or ch == 'u'  ):
        count +=1
print("cont of vowels: ", count)