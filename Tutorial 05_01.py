#Demonstrate working with tuples
colors=("White","Blue","Green","Red")

print(colors)
print('-----------------------------')
#name is a variable
name=("Mark")

print(name)
print('-----------------------------')
name=name+("Markus")

print(name)
print('-----------------------------')
#nametuple is a tuple because we put ,
nametuple=("Mark",)
print(nametuple)
print('-----------------------------')
colours=('white','green','red','yellow')
print ("Length of colours is : ",len(colours))
print('-----------------------------')
for n in colours:
    print(n)
print('-----------------------------')
if 'white  ' in colours:
    print("White is present : ")
if 'brown' not in colours:
    print("brown is present : ")
else:
    print("brown is present : ")
print('-----------------------------')
for n in colours:
    if n == 'red':
        print("It is Red")
    else:
        print("Not Red")
print('-----------------------------')
print(colours*3)
