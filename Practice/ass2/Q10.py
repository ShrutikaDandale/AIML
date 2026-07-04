
secret = 25

while True:

 num = int(input("Enter num :"))

 if secret < num:
   print("Too High")

 elif secret > num:
  print("Too Low")

 else:
  print("Correct")
  break