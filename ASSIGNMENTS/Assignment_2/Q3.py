# Write a function that prints the digits of a number,.Q3digitsnForeg:,thereare3digitsinit3,1and2&weneedtoprintthem.n = 312[-TherightmostdigitofanumberNisN%10.HintAndtoremovetherightmostdigitfromanumber,wecandoN=N/10.]
def print_digits(n):

    while n > 0:
        digit = n % 10
        print(digit)

        n = n // 10


print_digits(312)