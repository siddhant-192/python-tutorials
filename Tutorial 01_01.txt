#Swap two variables
#Using temp variable
#Using comma operator
#Using bitwise XOR operator


#Part 01
a=100
b=200

temp=a
a=b
b=temp
print(a,b)

#Part 02
a=100
b=200

a,b=b,a
print(a,b)

#Part 03
a=100
b=200

a=a^b
b=a^b
a=a^b
print(a,b)
