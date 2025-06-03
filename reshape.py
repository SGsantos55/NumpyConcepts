import numpy as np
arr1=np.array([4,5,6,7,8,9,2,1,4,12,0,4])
print(np.shape(arr1))
# converting 1 d array into 3d array
arr2=arr1.reshape(2,2,3)
print(arr2)

#converting 3-d array into 1-d array
arr3=arr2.reshape(-1)
print(arr3)
#slice only from 3-d array
print(arr2[1,1,0:3])
