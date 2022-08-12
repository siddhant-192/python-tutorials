#Create a tuple and find minimum and maximum element in it
numbers=(322,65,34,77,86,55,12,76,2,99,54)
l=len(numbers)
ma=numbers[0]
mi=numbers[0]
for a in numbers:
    if a > ma:
        ma=a;
    if a < mi:
        mi=a
print("Max number is : ",ma)
print("Min number is : ",mi)

print("maximum value=",max(numbers))
print("minimum value=",min(numbers))
