# it help to skip few numbers in the loop 
# suppose we took numbers and we have to skip the multiple of 3

i = 1
while (i <= 10):
    i += 1
    if (i % 3 == 0):   
        continue
    print(i)
  
print("loop end,nwe are outside loop")    



# same logic for odd even 
# i = 1
# while (i < 10): agar idhar <= use kiya to value 11 tak print hoke aayegi bez loop increment hoga so we only use <
    # i += 1
    # if (i % 2 == 0):   
        # continue
    # print(i)