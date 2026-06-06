# r+ - read and write the file

f = open("PythonFundamentals5/operation_on_file/sample.txt", "r+")

f.write("123") #123 already existing text ko overwrite karega
print(f.read())

f.close()

# at first file me text write hoga fir read hoga