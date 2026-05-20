num =  [1, 2, 3, 5, 10, 7]
x = 10
idx = 0
for val in num:
    if(val == x):
     print("index of x is: ", idx)
    #  OR print(f"x found at idx=(idx)")
     break
    idx += 1