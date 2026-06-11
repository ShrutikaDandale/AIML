# Create a program that:
# 1. Opens a file "log.txt" in append mode 
# 2. Adds a new log entry (like "Program run successfully") 
# 3. Opens the file in read mode and prints all logs

f = open("ASSIGNMENTS/Assignment_5/log.txt", "a")

f.write("Program run successfully" + "\n")

f.close()


f = open("ASSIGNMENTS/Assignment_5/log.txt", "r")
data = f.read()
print(data)

f.close()


# as we run our program the no. of logs will increase  because "a" (append mode) keeps adding new entries to the end of the file instead of deleting the old ones.

# PROGRAM LOGIC
# Open file in append mode
# Write the new log entry
# Close the file

# Open the same file in read mode
# Read all contents
# Print them
# Close the file