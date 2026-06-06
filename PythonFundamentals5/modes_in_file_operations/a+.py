# a+ - appen and read, write

f = open("PythonFundamentals5/operation_on_file/sample.txt", "a+")

f.write("123") 
print(f.read())

f.close()

# append me text pehele last me write hoga and then uske bad read hoga but append me pointer end se shuru hota hai isiliye kuch bhi read nahi hoga 