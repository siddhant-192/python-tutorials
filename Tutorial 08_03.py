import numpy as np

arr=np.zeros((8,8))
print(arr)
arr[::2,1::2]=1
print("Even Rows : ")
print(arr)
print()
arr[1::2,::2]=3
print("Odd Rows : ")
print(arr)
