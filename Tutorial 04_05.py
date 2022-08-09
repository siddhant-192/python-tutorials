#Demonstrate list operations

fruits=["Grapes","Apple","Orange"]
print(fruits)

fruits.append("Mango")
print(fruits)

fruits.insert(1,"Blueberry")
print(fruits)

fruits.remove("Grapes")
print(fruits)

del fruits[1]
print(fruits)

del fruits[1:]
print(fruits)

odd=[x for x in range(20) if x%2==1]
print(odd)


num=[x**2 for x in range(20)]
print(num)
