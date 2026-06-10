# List comprehension is a short and easy way to create a new list using a single line of code.
# [output for item in iterable if condition]

# hume suppose 1 to 5 numbers ka square chahiye to hum loop lagake bhi kar sakate hai
square = []

for i in range(6): #1 to 5 numbers
  square.append(i * i)

print(square)

# but instead of writting this much code we can simply use list comprehension
sq = [i*i for i in range(6)]
print(sq)

# we will get the same o/p

