a = input("enter a:")
b = input("enter b:")
operation = input("Enter operation : ")

def calculator(a, b, operation):

    if operation == '+' :
        return a+b

    elif operation == '-':
        return a - b

    elif operation == '*':
        return a * b

    elif operation == '/':
        return a / b

    else:
        return "invalid"   

print(calculator(a, b, operation))    