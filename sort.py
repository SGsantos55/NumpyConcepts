import numpy as np
arr1=np.array(["santos","gadtaula","thapathali"])
print(np.sort(arr1))
arr3=np.array([[6,7,8,9],[5,4,3,2],[1,2,3,4]])
print("sorted 3 d array is ",np.sort(arr3))
#for sorting in descending order just use -
print("sorted 3 d array in descending order  is ",-np.sort(-arr3))
#alternatively we can do 
print('')
print(np.sort(arr3)[::-1])#for sorting in descending order but this is valid only in 1-d array so it not gonna work here.

