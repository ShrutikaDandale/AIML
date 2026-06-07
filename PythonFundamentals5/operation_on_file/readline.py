# readline - (read)gives output line by line
f = open("PythonFundamentals5/operation_on_file/sample.txt", "r")

# to read the file line by line
data = f.readline()
print(data)
# ye ek line print karega

data = f.readline()
print(data)
# ye dusari line print karega

f.close()
