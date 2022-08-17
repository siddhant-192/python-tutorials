#use set functions
s1={1,2,3,4,5}
s2={4,5,6,7,8}

print("s1 = ",s1)
print("s2 = ",s2)

print("Union is ",set.union(s1,s2))
print("Intersection is ",set.intersection(s1,s2))
print("Difference s1-s2 is ",set.difference(s1,s2))
print("Difference s2-s1 is ",set.difference(s2,s1))
print("Symmetric difference is ",set.symmetric_difference(s1,s2))

s1.clear()
print("s1 = ",s1)

s3={}
print("s3 = ",s3)

s4=set()
print("s4 = ",s4)

del s2
