# Given a tuple of integers, create:
# •A tuple of all even numbers
# •A tuple of all odd numbers

tup = (1, 2, 4, 3, 5, 6)

even = () # create a empty tuple for even no.s
odd = () #create a empty tuple for odd no.s

for num in tup:
  if num % 2 == 0:
      even = even + (num,) # even = even + (num,) means even = () + (single tuple value,)
    #num, - single value tuple 
  else:
        odd = odd + (num,) #same logic as even

print("odd tuple", even) 
print("even tuple", odd)  