# Ask the user for a temperature in Celsius (string input). Convert it to float, then calculate and print temperature in Fahrenheit. 
# Conversion formula: FahrenheitTemp = (CelsiusTemp∗(9/5))+32

a = input("enter temp: ")
a = float(a)
a = (a * (9/5) + 32)
print(a)