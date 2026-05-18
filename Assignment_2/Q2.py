# Write a function that takes two integers and a and b prints all even numbers between them (inclusive).
a = int(input("enter a "))
b = int(input("enter b "))
def even_no(a, b):
     for i in range(a, b + 1):
        if i % 2 == 0:
            print(i)
even_no(a, b)