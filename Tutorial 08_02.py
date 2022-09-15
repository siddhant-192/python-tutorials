import numpy as np

arr=np.arange(10,370,12)
print(arr)
print("Number of elements : ",arr.size)

print("Reshaping arr")
arr=arr.reshape(5,6)
print(arr)

print("Print even rows and odd columns : ")
print(arr[0::2,1::2])

print("Subarray excluding borders : ")
print(arr[1:-1,1:-1])
print()
print(arr[:-2,:-3])
