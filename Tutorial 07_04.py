list = {"Mango" : "10.3" , "Apple" : "8.4" , "Orange" :
"5.5" ,"Grapes" : "8.93"}
print(list)
newdict = {Item:float(Value)*0.86 for (Item,Value) in
list.items()}
print(newdict)
from hashlib import new
from multiprocessing.sharedctypes import Value
list = {"Mango" : "10.3" , "Apple" : "8.4" , "Orange" : "5.5" ,"Grapes" : "8.93"}
print(list)
newdict = {Item:float(Value)*0.5 for (Item,Value) in
list.items()}
print(newdict)
