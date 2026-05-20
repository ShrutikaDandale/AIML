# list students enrolled in English

info = [
("Alice", "Math"),
("Bob", "Science"),
("Alice", "Science"),
("Charlie", "Math"),
("Bob", "Math"),
("Alice", "English"),
("Charlie", "English"),
]

for name,course in info:
    if(course == "English"):
     print(name)