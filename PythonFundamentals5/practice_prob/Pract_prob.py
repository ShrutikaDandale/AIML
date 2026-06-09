# WORD SEARCH - find in which line does the particular word exists

data = True
line = 1
word = "Python"

with open("PythonFundamentals5/practice_prob/practice.txt", "r") as f:
  
  while data: 
    data = f.readline()
    if("Python" in data):
     print(f"{word} found at line {line}") 
     break

    print(data) 
    line += 1
          
# humne file ko open r mode me kiya hai to har ek line read hogi and print line wise hogi bez readline use kiya hai agar line mili to word found ye statement execute hoga nahi to break loop ke bahar aake print(data) ye execute hoga

#by using the readline hum line by line apane data ko print karate hai but humare file me bohot sari lines ho sakti hai to barf bar same hi code na likhana pade isiliye humne yaha pe while loop use kiya hai 
