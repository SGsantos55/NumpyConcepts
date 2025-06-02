import numpy as np
arr1=np.array([5,9,2,7,1])
#view is kind of reference variable in cpp. where both arr1 and arr2 point to the same memory location and change in one variable also occur change in another variable.
arr2=arr1.view()
arr3=arr1.copy()
arr2[3]=55

print('arr1 after change at index 3',arr1)
print('arr1 is copied to arr3',arr3)

# # arr2[2]='santosh' will cause error because it's numpy array where in index 2 there is int number not a string.
# but if was list then it is valid