# Write a program to check whether two lists share no common elements. 
# share no common elements list1 =[1,2,3,4] list2 =[5,6,7,8]
# share common elements list1 =[1,2,3] list2 =[3,4]

s1 = set(map(int, input("Enter elements: ").split()))
s2 = set(map(int, input("Enter elements: ").split()))


if(s1.intersection(s2) == 0):
     print("share no common elements")

else:
       print("share common elements")
       
