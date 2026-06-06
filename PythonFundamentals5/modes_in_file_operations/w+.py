# w+ - write and readf = open("PythonFundamentals5/operation_on_file/sample.txt", "r+")

f = open("PythonFundamentals5/operation_on_file/sample.txt", "w+")

f.write("123") 
print(f.read())

f.close()

# w+ se sari chize overwrite ho jayegi aur puri file khali ho jayegi sirf abhi jo text likha hai 123 voprint hoga 
# bez w me puri file truncate ho jati hai