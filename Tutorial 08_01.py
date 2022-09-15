import numpy as np
a=np.ones(5)
print(a)
print()

b=np.zeros((4,5))
print(b)
print()

arr=np.random.randint(5,11,size=(3,5))
print(arr)
print()

arr=np.identity(4)
print(arr)
print()
print(np.mean(arr))

arr=np.ones((3,3))
print(arr)
print()
arr=np.pad(arr,pad_width=1,mode='constant',constant_values=0)
print(arr)
