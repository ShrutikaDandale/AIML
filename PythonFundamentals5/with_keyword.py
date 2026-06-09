# hum file ko open karate hai to hume close bi karna padata hai to hume bar bar file ko close na karana pade isiliye hum with keyword ko use karate hai

with open("PythonFundamentals5/sample3.txt", "r") as f:
    data = f.read() 
    print(data)