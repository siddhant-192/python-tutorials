mydict={'Name' : 'Siddhant' , 'Age' : 19 , 'Gender' : 'Male'}
print(mydict)
mydict['Year']='2nd'
print(mydict)
print(mydict.get("Name"))
print(mydict["Year"])
mydict.clear()
print(mydict)
del mydict
mydict1={'Name' : 'Siddhant' , 'Age' : 19 , 'Gender' : 'Male'}
mydict1.pop("Name")
print(mydict1.popitem())
print(mydict1)
print(len(mydict1))
mydict2 = mydict1.copy
print(mydict2) 
