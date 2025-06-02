import numpy as np
arr1=np.array([4,5,6,7,9])
print(np.shape(arr1))
arr2=np.array([[4,5,6],[9,1,3]])
print(arr2[1:2,0:2])# 9,1
print(arr1[-5:-4])
print(arr1[-4:-2])
print(arr1[-1:-4:-1])#9,7,6


arr3=np.array([[6,7,8,9],[5,4,3,2],[1,2,3,4]]) #its a two dimension array
print(arr3)
print(arr3[2,0:2])#1,2,3 # its a slicing of two dimension array
arr3=np.array([[[6,7,8,9],[5,4,3,2],[1,2,3,4]]])# it's a three dimensional array with only one depth layer
print(arr3[0,1,::-1])# slicing of 3-d array 2,3,4,5
