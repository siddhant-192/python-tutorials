#Read a list of numbers and remove the duplicate numbers from it

l=[12,43,54,54,67,32,12,43,65,8,76,32]

new_l=[]

for i in l:
    if i in new_l:
        continue
    else:
        new_l.append(i)
print(l)
print(new_l)
