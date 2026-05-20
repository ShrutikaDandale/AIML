s = {1, 2, 2, 3, 4}
s1 = {1, 9, 2, 7, 4}

# add(val) - adds a value
s.add(5)
print(s)

# remove(val) - remove value
s.remove(6)
print(s)

# clear() - empty the set
s.clear()
print(s)

# pop() - removes a random value
s.pop()
print(s)


# union(set2) - returns new union
print(s.union(s1))

# intersection(set2) - returns new intersection
print(s.intersection(s1))