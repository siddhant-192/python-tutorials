#create a set, add members in set and remove one item from the set

s1={1, 2, 3, 4, 5}
print("s1 = ",s1)

s1.add(8)
print("s1 = ",s1)

s1.remove(5)
print("s1 = ",s1)

n=int(input("Enter total : "))

for x in range(n):
    num=int(input("Enter number : "))
    s1.add(num)
print("s1 = ",s1)

print("Length of s1 is ",len(s1))
