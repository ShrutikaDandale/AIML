# Take a decimal number as input (like 47.78) and output its:
# •integer part-45
# •fractional part-.78

a = float(input("enter no. "))
integer_part = int(a)
fraction_part = (a - integer_part )
print(integer_part)
print(fraction_part)
