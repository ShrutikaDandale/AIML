# suppose we have a list and we want to convert all the -ve no.s to 0 by using the list comprehension

nums = [-2, 3, -3, 4, -1, 7]

nums = [0 if val<0 else val for val in nums]
print(nums)
