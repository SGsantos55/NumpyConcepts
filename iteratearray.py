import numpy as np
arr1=np.array([5,7,8,9])
for el in arr1:
    print(el)
    print(end='')

print('')    

arr2=np.array([[3,4,5,6],[0,2,3,1]])
for el in arr2:
    for n in el:
        print(n)
        print(end='')
print('')            
#shortcut
for el in np.nditer(arr2):
    print(el)
