import numpy as np


arr= np.array(range(0,5))
arr1= np.array(range(5,10))
arr2= np.array([range(0,5),range(5,10)])


print(arr)
print(type(arr))
print(arr1)

print(np.add(arr,arr1))
print(np.subtract(arr,arr1))

print(np.append(arr,arr1))

print("shape",arr.shape)

print(arr2)
print("shape",arr2.shape)
arr3=arr2.reshape(5,2)
print(arr3)

print("Mean : ",np.mean(arr))
print("Median : ",np.median(arr))
print("Median of first 4 no : ",np.median(arr[:4]))
print("Standerd Deviation : ",np.std(arr))
print("Varience",np.var(arr))

