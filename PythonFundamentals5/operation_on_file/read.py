# sample file ko access kiya
f = open("PythonFundamentals5/operation_on_file/sample.txt", "r")

# to read the file
data = f.read()
print(data)

# hum jab bhi apani file ko open karate hai usko close karana necessary hai

# to close the file
f.close()
