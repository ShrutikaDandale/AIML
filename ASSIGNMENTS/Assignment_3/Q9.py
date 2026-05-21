# Given a list, print all elements that appear more than once in the list.

lst = list(map(int, input("Enter numbers: ").split()))

seen = set() # no repeated element
repeated = set()

for num in lst: #stores valus to num from list
     if num in seen:
        repeated.add(num) #store the value in repeated  
     else:
        seen.add(num) #Store the value in seen 

print("Repeated elements:", repeated)        