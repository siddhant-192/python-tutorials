#Find out the largest number in the list

l=[10,3,21,45,3,22,33,65,9]

max=l[0]

for i in l:
    if i > max:
        max=i
print("Largest number in list is {}".format(max))
