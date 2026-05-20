# Input two lists of integers from the user. Merge them into one list and sort the result.

list1 = list(map(int, input("Enter list1: ").split()))
list2 = list(map(int, input("Enter list2: ").split()))

result = list1 + list2

result.sort()

print(result)