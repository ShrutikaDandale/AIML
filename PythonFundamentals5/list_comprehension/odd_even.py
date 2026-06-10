# if we want the squares of odd no.s only then by using loop we have to write a lengthy cod and hav to use the if statment but we can do similar thing using list co mprehension
sqr = [i * i for i in range(6) if (i % 2) != 0]
print(sqr)

# if we want the squares of even no.s only then by using loop we have to write a lengthy cod and hav to use the if statment but we can do similar thing using list co mprehension
square = [i * i for i in range(6) if (i % 2) == 0]
print(square)