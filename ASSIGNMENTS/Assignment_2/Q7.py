while True:
    n = (input("enter num: "))

    if n == "Quit":
        break

    n = int(n)

    if n >= 0:
        print("Positive")

    else:
        print("Negative")