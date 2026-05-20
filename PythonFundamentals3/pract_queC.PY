# create dictionary (student, set of courses)

info = [
("Alice", "Math"),
("Bob", "Science"),
("Alice", "Science"),
("Charlie", "Math"),
("Bob", "Math"),
("Alice", "English"),
("Charlie", "English"),
]

dict = {} #create a dict abhi dict empty hai

for name,course in info: 
    if(dict.get(name) == None): #info me agar dict ke anadr name add kiya add if vo name exist kara nahi hai yaniki none to

        dict.update({name: set()}) #to dict ko update karake usme name and empty sem dalenge

        dict[name].add(course) #ssathme empty set ki jaga course bhi add karenge

    else: #agar if ki condition false ho gayi yaniki name none nahi hai and already dict me exist karata hai to else me aayenge

        dict[name].add(course) #aagr dict me name and course already exist karata hai to simply name and course print karenge aur aage badhenge

print(dict) #to print whole dictionary

