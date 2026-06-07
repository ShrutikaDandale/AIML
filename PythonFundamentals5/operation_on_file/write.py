# write - truncate(empty) the file and write the new text into the file 
f = open("PythonFundamentals5/operation_on_file/sample.txt", "w") #hum data ko write karana chahate hai to 'w' mode use karenge

f.write("text to overwrite \n the complete data.")

f.close()

# hum jab file me kuch write karate hai to currunt file me jo bhi data rehta hai uske upar humnr jom change kiye vo overwrite ho jate hai 

# is file ko run karane ke bad terminal me o/p nahi aayega ye direct file me changes karega