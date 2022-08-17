#find maximum and minimum value in set
s=set()

n=int(input("Enter number of elements to be added : "))

for i in range(n):
    num=int(input("Enter elements : "))
    s.add(num)
print("Max of the set is ",max(s))
print("Min of the set is ",min(s))
