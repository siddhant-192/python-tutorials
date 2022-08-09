#Implement linear search using list

l=[10,3,21,45,3,22,33,65,9]
num=int(input("Enter number to search : "))

flag=0

for i in range(len(l)):
    if l[i]==num:
        flag=1
        break
        
if flag==1:
    print("Number found at position {}".format(i+1))
else:
    print("Number not found.")
