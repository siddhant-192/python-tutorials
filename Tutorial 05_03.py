#Find the repeated items of a tuple
tup=('apple','banana','mango','apple','guava','watermelon','banana','pineapple','fig','apple','watermelon','dragonfruit','apple')
l=len(tup)
lst=[]
for i in range(l):
    temp=tup[i]
    if temp in lst:
        continue
    else:
        for j in range(i+1,l):
            if tup[j]==tup[i]:
                lst.append(tup[i])
                break
print(lst)
