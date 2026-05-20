#Student Enrolments
# Given a list of tuples with info(name, subject):

# list all unique course
# list students enrolled in English
# create dictionary (student, set of courses)


# list all unique course solution
info = [
("Alice", "Math"),
("Bob", "Science"),
("Alice", "Science"),
("Charlie", "Math"),
("Bob", "Math"),
("Alice", "English"),
("Charlie", "English"),
]

# create a empty set
unique_courses = set() #create a empty set

for tup in info: #info ke andar ke tuple

    unique_courses.add(tup[1]) #unique_course empty set hai uske andar tup[1] ki value (means tuple ke andar 1 index pe courses hai to courses ki value) add hogi

    print(unique_courses) #courses print hoge 


                     #OR

for name,course in info:
    print(course)
    # ye easy way hai