# if our file doesent exits in the folder then 'x' creates the file and open it for writting

f = open("PythonFundamentals5/operation_on_file/sample2.txt", "x")#sample2 dosent exits

f.write("some random text")

f.close()